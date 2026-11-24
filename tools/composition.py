"""Check and resolve workflow configurations from the tables in COMPOSITION.md.

Optional helper. It reads the single authoritative tables in COMPOSITION.md, checks that they are
consistent, resolves example configuration blocks into requested/effective values with reason codes, and
checks that its own resolver treats participation, cadence/format and scaffolding independently. It
says nothing about how an agent interprets the settings, observes no agent run and enforces nothing.
"""
from pathlib import Path
import argparse
import difflib
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT/'COMPOSITION.md'
WORKFLOW = ROOT/'WORKFLOW.md'
EXAMPLES = ROOT/'examples'/'CONFIGURATIONS.md'
STAGES = ('acquire', 'analyse', 'decide', 'execute')
STAGE_KEYS = STAGES + ('learning',)
# Extra names for mandatory invariants; the invariant titles in WORKFLOW.md are added at load time.
# Requests to set any of them are refused, never applied.
INVARIANT_ALIASES = {'security_gate', 'claims_within_evidence', 'unavailable_gates', 'gate_applicability',
                     'evidence_integrity', 'human_override'}
ORDERED = {'assurance': ('lightweight', 'standard', 'high'), 'planning': ('direct', 'outline', 'full')}
NUMBER_WORDS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'}
# WORKFLOW §11 sentence fragments that quote the K5 defaults; the number word precedes each fragment.
QUOTED_DEFAULTS = {'retries_transient': 'retries of a suspected transient condition',
                   'repair_attempts': 'repair attempts per hypothesis',
                   'stagnation_window': 'attempts without new evidence',
                   'attempt_ceiling': 'attempts in total on one problem'}
FLOOR = {'routine': 'lightweight', 'material': 'standard', 'consequential': 'high'}
ASSURANCE_RANK = {'lightweight': 0, 'standard': 1, 'high': 2}
PLAN_FOR = {'routine': 'direct', 'material': 'outline', 'consequential': 'full'}
PLAN_RANK = {'direct': 0, 'outline': 1, 'full': 2}
# Stricter alternative applied when an error rule fires.
FIXES = {'C-01': ('analyse', 'assist'), 'C-02': ('decide', 'human'), 'C-03': ('execute', 'assist'),
         'C-04': ('action_log', 'on'), 'C-05': ('action_log', 'on'), 'C-06': ('attempt_ceiling', '12')}
CONTEXT_DEFAULTS = {'consequence': 'material', 'host_independent_review': 'yes',
                    'host_parallel_workers': 'yes', 'coupled': 'no'}


class SpecError(Exception):
    pass


def tables(text):
    found = {}
    for name, body in re.findall(r'<!-- table:(\w+) -->\n(.*?)\n<!-- end -->', text, re.S):
        rows = [r.strip() for r in body.strip().splitlines() if r.strip().startswith('|')]
        if len(rows) < 3:
            raise SpecError(f'table {name} has no rows')
        cells = lambda r: [c.strip() for c in r.strip('|').split('|')]
        head = cells(rows[0])
        found[name] = [dict(zip(head, cells(r))) for r in rows[2:]]
    return found


def invariant_names(path=WORKFLOW):
    """Slugs of the invariant titles, e.g. 'INV-05 Oracle integrity.' -> 'oracle_integrity'."""
    text = path.read_text(encoding='utf-8') if path.is_file() else ''
    titles = re.findall(r'\*\*INV-\d\d ([^.*]+)\.\*\*', text)
    return {re.sub(r'\W+', '_', t.strip().lower()).strip('_') for t in titles} | INVARIANT_ALIASES


def load(spec=SPEC):
    t = tables(spec.read_text(encoding='utf-8'))
    for need in ('participation', 'precedence', 'reasons', 'compatibility', 'presets', 'defaults',
                 'dimensions'):
        if need not in t:
            raise SpecError(f'COMPOSITION.md lacks table {need}')
    keys = {}
    for row in t['defaults']:
        values = [v.strip() for v in row['Values'].split(',')]
        keys[row['Key']] = {'values': values, 'default': row['Default']}
    participation = {row['Preset']: {k: row[k] for k in STAGE_KEYS} for row in t['participation']}
    presets = {}
    for row in t['presets']:
        values = {}
        if row['Values'] != '(defaults)':
            for item in row['Values'].split(';'):
                k, _, v = item.strip().partition('=')
                values[k.strip()] = v.strip()
        presets[row['Preset']] = values
    rules = []
    for row in t['compatibility']:
        clauses = []
        for clause in row['Condition'].split('&'):
            clause = clause.strip()
            m = re.fullmatch(r'(\w+) in \{([^}]*)\}', clause)
            g = re.fullmatch(r'(\w+) > (\w+)', clause)
            if g:
                clauses.append((g.group(1), ('>', g.group(2))))
            elif m:
                clauses.append((m.group(1), {v.strip() for v in m.group(2).split(',')}))
            else:
                k, _, v = clause.partition('=')
                clauses.append((k.strip(), {v.strip()}))
        rules.append({'id': row['ID'], 'severity': row['Severity'], 'clauses': clauses,
                      'reason': row['Reason']})
    reasons = {row['Code'] for row in t['reasons']}
    ranks = [row['Rank'] for row in t['precedence']]
    dimensions = {row['Dimension']: [k.strip() for k in row['Keys'].split(',')] for row in t['dimensions']}
    return {'keys': keys, 'participation': participation, 'presets': presets, 'rules': rules,
            'reasons': reasons, 'ranks': ranks, 'dimensions': dimensions, 'protected': invariant_names()}


def holds(eff, clause):
    k, vs = clause
    if isinstance(vs, tuple) and vs[0] == '>':
        a, b = eff.get(k, ''), eff.get(vs[1], '')
        return a.isdigit() and b.isdigit() and int(a) > int(b)
    return eff.get(k) in vs


def valid(spec, key, value):
    allowed = spec['keys'][key]['values']
    if allowed == ['integer']:
        return value.isdigit()
    if allowed == ['text']:
        return True
    if 'integer' in allowed and value.isdigit():
        return True
    return value in allowed


def check_spec(spec):
    errors = []
    if spec['ranks'] != [str(i) for i in range(1, len(spec['ranks'])+1)]:
        errors.append('precedence ranks are not 1..n in order')
    for name, stages in spec['participation'].items():
        if name not in spec['keys']['participation']['values']:
            errors.append(f'participation preset {name} missing from defaults values')
        for k, v in stages.items():
            if not valid(spec, k, v):
                errors.append(f'participation preset {name}: invalid {k}={v}')
    for value in spec['keys']['participation']['values']:
        if value not in spec['participation']:
            errors.append(f'participation value {value} has no preset row')
    for name, values in spec['presets'].items():
        for k, v in values.items():
            if k not in spec['keys']:
                errors.append(f'preset {name}: unknown key {k}')
            elif not valid(spec, k, v):
                errors.append(f'preset {name}: invalid {k}={v}')
    for rule in spec['rules']:
        if rule['severity'] not in ('error', 'warn'):
            errors.append(f'rule {rule["id"]}: severity must be error or warn')
        if rule['severity'] == 'error' and rule['id'] not in FIXES:
            errors.append(f'rule {rule["id"]}: error rule has no stricter alternative in the helper')
        for k, vs in rule['clauses']:
            if k not in spec['keys']:
                errors.append(f'rule {rule["id"]}: unknown key {k}')
            if isinstance(vs, tuple):
                if vs[1] not in spec['keys']:
                    errors.append(f'rule {rule["id"]}: unknown key {vs[1]}')
                continue
            for v in vs:
                if not valid(spec, k, v):
                    errors.append(f'rule {rule["id"]}: invalid value {k}={v}')
    owner = {}
    for dim, keys in spec['dimensions'].items():
        for k in keys:
            if k not in spec['keys']:
                errors.append(f'dimension {dim}: unknown key {k}')
            if k in owner:
                errors.append(f'key {k} belongs to dimensions {owner[k]} and {dim}')
            owner[k] = dim
    for k in spec['keys']:
        if k not in owner:
            errors.append(f'key {k} belongs to no dimension')
    for name, values in spec['presets'].items():
        dims = sorted({owner.get(k, '?') for k in values})
        if len(dims) > 1:
            errors.append(f'preset {name} couples dimensions {", ".join(dims)}')
    used = {'PolicyClamp', 'MandatoryInvariant', 'HostLacksCapability', 'ReviewerUnavailable',
            'IncompatibleCombination', 'UnknownKey', 'InvalidValue'}
    for code in used - spec['reasons']:
        errors.append(f'reason code {code} used by the helper is not defined')
    for name in spec['presets']:
        for consequence in FLOOR:
            result = resolve(spec, {'preset': name}, {'consequence': consequence})
            bad = [d for d in result['divergences'] if d['code'] == 'IncompatibleCombination']
            if bad:
                errors.append(f'preset {name} violates {bad[0]["detail"]} under {consequence} work')
            unknown = [d for d in result['divergences'] if d['code'] in ('UnknownKey', 'MandatoryInvariant')]
            if unknown:
                errors.append(f'preset {name}: {unknown[0]["detail"]}')
    return errors


def parse_block(text):
    requested, context = {}, {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        k, sep, v = line.partition(':')
        if not sep:
            continue
        k, v = k.strip().lower(), v.strip()
        (context if k.startswith('@') else requested)[k.lstrip('@')] = v
    return requested, context


def resolve(spec, requested, context=None):
    ctx = dict(CONTEXT_DEFAULTS, **(context or {}))
    eff, src, divergences, warnings = {}, {}, [], []

    def setv(k, v, source):
        eff[k], src[k] = v, source

    def diverge(key, asked, got, code, detail):
        divergences.append({'key': key, 'requested': asked, 'effective': got, 'code': code,
                            'detail': detail})

    for k, meta in spec['keys'].items():
        if meta['default'] != 'from participation':
            setv(k, meta['default'], 'default')

    def apply_participation(name, source):
        for k, v in spec['participation'][name].items():
            setv(k, v, source)

    apply_participation(eff['participation'], 'default (participation)')
    # rc2 fix KD-01: key names are case-insensitive (WORKFLOW_CONFIGURATION), also when resolve() is called
    # directly rather than through parse_block. Two spellings of one key keep the later one, with a warning.
    folded = {}
    for k, v in requested.items():
        key = str(k).strip().lower()
        if key in folded:
            warnings.append(f'{key} given twice (key names ignore case); the later value is used')
        folded[key] = v
    requested = folded
    preset = requested.get('preset')
    if preset is not None:
        if preset not in spec['presets']:
            diverge('preset', preset, '(none)', 'UnknownKey', f'unknown preset {preset}')
        else:
            values = spec['presets'][preset]
            if values.get('participation') in spec['participation']:
                setv('participation', values['participation'], f'preset {preset}')
                apply_participation(values['participation'], f'preset {preset} (participation)')
            for k, v in values.items():
                if k != 'participation':
                    setv(k, v, f'preset {preset}')
    explicit = {}
    for k, v in requested.items():
        k = k.lower()
        if k != 'preset':
            text = spec['keys'].get(k, {}).get('values') == ['text']
            explicit[k] = v if text else v.lower()
    # rc2 fix KD-02: participation, valid or corrected to its closest value, is resolved before every other
    # explicit key, so an explicit stage setting such as execute: human always overrides the participation
    # preset, whatever the order of the keys and whether or not the participation value was misspelt.
    if 'participation' in explicit:
        v = explicit['participation']
        if v in spec['participation']:
            setv('participation', v, 'task')
            apply_participation(v, 'task (participation)')
        else:
            close = difflib.get_close_matches(v, list(spec['participation']), n=2, cutoff=0.6)
            got = close[0] if len(close) == 1 else eff['participation']
            diverge('participation', v, got, 'InvalidValue', f'{v} is not a value of participation')
            if len(close) == 1:
                setv('participation', got, 'task (closest valid value)')
                apply_participation(got, 'task (participation)')
    for k, v in explicit.items():
        if k == 'participation':
            continue
        if k in spec['protected'] or k.upper().startswith('INV-'):
            diverge(k, v, '(invariant)', 'MandatoryInvariant', f'{k} is a mandatory invariant')
            continue
        if k not in spec['keys']:
            diverge(k, v, '(ignored)', 'UnknownKey', f'{k} is not a configurable key')
            continue
        if not valid(spec, k, v):
            choices = [c for c in spec['keys'][k]['values'] if c not in ('integer', 'text')]
            close = difflib.get_close_matches(v, choices, n=2, cutoff=0.6)
            got = close[0] if len(close) == 1 else eff.get(k)
            if k in ORDERED and got in ORDERED[k] and eff.get(k) in ORDERED[k]:
                got = max(got, eff[k], key=ORDERED[k].index)
            diverge(k, v, got, 'InvalidValue', f'{v} is not a value of {k}')
            setv(k, got, 'task (closest valid value)' if len(close) == 1 else src.get(k, 'default'))
            continue
        setv(k, v, 'task')

    consequence = ctx['consequence']
    floor = FLOOR[consequence]
    asked = eff['assurance']
    if asked == 'auto':
        setv('assurance', floor, f'floor ({consequence})')
    elif ASSURANCE_RANK[asked] < ASSURANCE_RANK[floor]:
        diverge('assurance', asked, floor, 'PolicyClamp', f'{consequence} work has a {floor} floor')
        setv('assurance', floor, f'floor ({consequence})')
    needs_review = eff['assurance'] in ('standard', 'high')
    if not needs_review:
        setv('independent_review', 'optional', 'assurance')
    elif ctx['host_independent_review'] == 'yes':
        setv('independent_review', 'required', 'assurance')
    else:
        setv('independent_review', 'required: blocked', 'host capability')
        diverge('independent_review', 'required', 'required: blocked', 'ReviewerUnavailable',
                'no separate session; acceptance waits as READY_FOR_REQUIRED_REVIEW')

    derived_plan = PLAN_FOR[consequence]
    if eff['planning'] == 'auto':
        setv('planning', derived_plan, f'rule ({consequence})')
    elif PLAN_RANK[eff['planning']] < PLAN_RANK[derived_plan]:
        diverge('planning', eff['planning'], derived_plan, 'PolicyClamp',
                f'{consequence} work needs planning of at least {derived_plan}')
        setv('planning', derived_plan, f'rule ({consequence})')

    if eff['topology'] == 'auto':
        setv('topology', 'single', 'rule (smallest eligible team)')
    if eff['topology'].startswith('parallel') and ctx['host_parallel_workers'] != 'yes':
        diverge('topology', eff['topology'], 'single', 'HostLacksCapability', 'no parallel workers on this host')
        setv('topology', 'single', 'host capability')
    if eff['topology'] == 'parallel-write' and ctx['coupled'] == 'yes':
        diverge('topology', 'parallel-write', 'single', 'PolicyClamp', 'tightly coupled artifact')
        setv('topology', 'single', 'rule (coupled artifact)')
    if eff['tier'] == 'auto':
        setv('tier', 'by host capacity', 'rule')
    fast = consequence == 'routine' and eff['assurance'] == 'lightweight'
    setv('path', 'fast' if fast else 'full', f'rule ({consequence}, assurance {eff["assurance"]})')

    for rule in spec['rules']:
        if all(holds(eff, c) for c in rule['clauses']):
            if rule['severity'] == 'error':
                key, value = FIXES[rule['id']]
                diverge(key, eff[key], value, 'IncompatibleCombination', f'{rule["id"]}: {rule["reason"]}')
                setv(key, value, f'rule {rule["id"]}')
            else:
                warnings.append(f'{rule["id"]}: {rule["reason"]}')
    notice = []
    label = eff['participation']
    if label in spec['participation'] and any(eff[k] != v for k, v in spec['participation'][label].items()):
        label = f'custom (from {label})'
    raised = ASSURANCE_RANK[eff['assurance']] > ASSURANCE_RANK[floor]
    if divergences or warnings or raised or consequence == 'consequential':
        notice.append(f'Configuration: {label} participation, {eff["cadence"]}/{eff["format"]}, '
                      f'scaffolding {eff["scaffolding"]}, assurance {eff["assurance"]}.')
        for d in divergences:
            notice.append(f'{d["key"]}: requested {d["requested"]} -> {d["effective"]} ({d["code"]}: {d["detail"]}).')
        notice.extend(f'Warning {w}.' for w in warnings)
        if raised:
            notice.append(f'Assurance {eff["assurance"]} is above the {floor} floor for {consequence} work: '
                          f'{"full path, " if consequence == "routine" else ""}review {eff["independent_review"]}.')
    return {'effective': eff, 'source': src, 'divergences': divergences, 'warnings': warnings,
            'notice': notice[:5] if len(notice) <= 5 else notice[:4]+[f'... {len(notice)-4} more in the record']}


def render(result):
    lines = [f'{k}: {v}  [{result["source"][k]}]' for k, v in sorted(result['effective'].items())]
    lines += [f'DIVERGENCE {d["key"]}: {d["requested"]} -> {d["effective"]} ({d["code"]})' for d in result['divergences']]
    lines += [f'WARNING {w}' for w in result['warnings']]
    lines += [f'NOTICE {n}' for n in result['notice']] or ['NOTICE (none)']
    return '\n'.join(lines)


def independence(spec):
    """Change each new setting alone and confirm the resolver changes nothing outside its own keys.

    This is a property of this helper's resolver only, not of the documents' meaning."""
    errors = []
    owned = {'participation': set(('participation',) + STAGE_KEYS), 'cadence': {'cadence'},
             'format': {'format'}, 'scaffolding': {'scaffolding'}}
    for consequence in FLOOR:
        for review in ('yes', 'no'):
            ctx = {'consequence': consequence, 'host_independent_review': review}
            base = resolve(spec, {}, ctx)['effective']
            for key, own in owned.items():
                for value in spec['keys'][key]['values']:
                    changed = resolve(spec, {key: value}, ctx)['effective']
                    diff = {k for k in set(base) | set(changed) if base.get(k) != changed.get(k)}
                    if diff - own:
                        errors.append(f'{key}={value} under {consequence}/review={review} also changed '
                                      f'{sorted(diff - own)}')
    return errors


def quoted_defaults_errors(spec, path=WORKFLOW):
    """WORKFLOW §11 quotes the K5 numeric defaults; the two must agree."""
    errors = []
    text = path.read_text(encoding='utf-8') if path.is_file() else ''
    for key, fragment in QUOTED_DEFAULTS.items():
        default = spec['keys'].get(key, {}).get('default', '')
        word = NUMBER_WORDS.get(int(default)) if default.isdigit() else None
        if word is None:
            errors.append(f'K5 default for {key} is not a small integer')
        elif not re.search(rf'\b{word} {re.escape(fragment)}', text):
            errors.append(f'WORKFLOW.md §11 does not quote the K5 default {key}={default} ("{word} {fragment}")')
    return errors


def example_blocks(path=EXAMPLES):
    text = path.read_text(encoding='utf-8')
    return re.findall(r'```workflow-config\n(.*?)```\n+```text\n(.*?)```', text, re.S)


def check_examples(spec, path=EXAMPLES):
    errors = []
    if not path.is_file():
        return [f'missing {path.relative_to(ROOT)}']
    blocks = example_blocks(path)
    if not blocks:
        errors.append('no example configuration blocks found')
    for i, (block, expected) in enumerate(blocks, 1):
        requested, context = parse_block(block)
        actual = render(resolve(spec, requested, context))
        if actual.strip() != expected.strip():
            errors.append(f'example {i}: recorded result differs from resolution')
    return errors


def write_examples(spec, path=EXAMPLES):
    text = path.read_text(encoding='utf-8')

    def fill(m):
        requested, context = parse_block(m.group(1))
        return f'```workflow-config\n{m.group(1)}```\n\n```text\n{render(resolve(spec, requested, context))}\n```'
    new = re.sub(r'```workflow-config\n(.*?)```\n+```text\n.*?```', fill, text, flags=re.S)
    path.write_text(new, encoding='utf-8', newline='\n')


def all_checks():
    try:
        spec = load()
    except (OSError, SpecError) as exc:
        return [f'composition specification unreadable: {exc}']
    return check_spec(spec) + independence(spec) + quoted_defaults_errors(spec) + check_examples(spec)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('check')
    sub.add_parser('independence')
    r = sub.add_parser('resolve')
    r.add_argument('file', type=Path, help='file containing key: value lines (@key for context)')
    sub.add_parser('write-examples')
    args = parser.parse_args()
    spec = load()
    if args.action == 'check':
        errors = all_checks()
        print('\n'.join(errors) if errors else 'COMPOSITION CONSISTENT: tables, single-dimension presets, '
              'resolver independence, quoted defaults and examples')
        return 1 if errors else 0
    if args.action == 'independence':
        errors = independence(spec)
        print('\n'.join(errors) if errors else 'RESOLVER INDEPENDENT: in this helper, participation, cadence, '
              'format and scaffolding change only their own keys (a helper property, not a semantic one)')
        return 1 if errors else 0
    if args.action == 'resolve':
        requested, context = parse_block(args.file.read_text(encoding='utf-8'))
        print(render(resolve(spec, requested, context)))
        return 0
    write_examples(spec)
    print('Rewrote recorded example results')
    return 0


if __name__ == '__main__':
    sys.exit(main())
