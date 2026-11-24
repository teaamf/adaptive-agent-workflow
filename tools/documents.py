"""Maintain the general document package; never executes or certifies a project."""
from pathlib import Path
import argparse
import importlib.util
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
VERSION = '4.4-rc1'
MODULES = ('PROJECT_TEMPLATE.md', 'WORKFLOW.md', 'AGENT_INTERACTION.md', 'COMPOSITION.md', 'PROFILES.md',
           'UI_DESIGN_PROTOCOL.md', 'UI_REVIEW_PLAYBOOK.md', 'HOST_ADAPTERS.md',
           'WORKFLOW_CONFIGURATION.md', 'CONTINUOUS_IMPROVEMENT.md', 'PRACTICAL_PLAYBOOKS.md')
# Documents that instruct an agent or adopter; provenance records (research, validation, merge and
# change history, the advice index) may name historical sources and are not scanned.
OPERATIONAL = MODULES + ('GLOSSARY.md', 'LAUNCH.md', 'COMPACT_PROMPT.md', 'README.md', 'GUIDE.md', 'SKILL.md', 'MIGRATION.md',
                         'evaluation/SCENARIOS.md', 'examples/CONFIGURATIONS.md',
                         'references/ENGINEERING_ADVICE_MAP.md')
# Files that must declare the package version.
VERSIONED = tuple(m for m in MODULES if m != 'PROJECT_TEMPLATE.md') + (
    'GLOSSARY.md', 'LAUNCH.md', 'COMPACT_PROMPT.md', 'README.md', 'SKILL.md', 'MIGRATION.md',
    'examples/CONFIGURATIONS.md')
STALE_VERSION = re.compile(r'\bVersion (?!' + re.escape(VERSION) + r')\d+\.\d')
COMPACT = 'COMPACT_PROMPT.md'
COMPACT_BUDGET_BYTES = 10500  # 4.3 was 7,791; the excess carries the twelve invariants
TIER1 = ('WORKFLOW.md', 'AGENT_INTERACTION.md', 'PROJECT_TEMPLATE.md')
TIER1_BUDGET_BYTES = 39480  # the 4.3 Tier 1 size; 4.4-rc1 must not grow the mandatory core
# The mandatory invariant set is pinned here, so deleting an ID from every tier is still detected.
EXPECTED_INVARIANTS = tuple(f'INV-{n:02d}' for n in range(1, 13))
# Phrases the compact tier must keep in addition to every invariant ID; a drift guard, not a proof.
COMPACT_MARKERS = ('data, not instructions', 'Do not weaken a check', 'Pause and reassess',
                   'untrusted content', 'Role-play is not independent review', 'ACCEPTED_FOR_STATED_SCOPE',
                   'READY_FOR_REQUIRED_REVIEW', 'CHECKPOINTED', 'progress note',
                   'resource use well above the budget', 'or because reviewers are unavailable',
                   'other reliable validation gate', 'recovery evidence', 'domain expertise')
PATTERNS = ROOT/'tools'/'portability_patterns.txt'
# Directories that hold records about the package rather than the package itself.
UNSCANNED_DIRS = {'research', 'releases', 'reports', 'research_notes'}


def assembled():
    parts = [(ROOT/'LAUNCH.md').read_text(encoding='utf-8').rstrip()]
    for name in MODULES:
        body = (ROOT/name).read_text(encoding='utf-8').rstrip()
        parts.append(f'<!-- BEGIN {name} -->\n\n{body}\n\n<!-- END {name} -->')
    return '\n\n---\n\n'.join(parts)+'\n'


def patterns():
    if not PATTERNS.is_file():
        raise ValueError(f'portability pattern file missing: {PATTERNS.name}')
    lines = PATTERNS.read_text(encoding='utf-8').splitlines()
    found = [re.compile(p.strip(), re.I) for p in lines if p.strip() and not p.lstrip().startswith('#')]
    if not found:
        raise ValueError(f'portability pattern file has no patterns: {PATTERNS.name}')
    return found


def invariant_ids():
    text = (ROOT/'WORKFLOW.md').read_text(encoding='utf-8')
    m = re.search(r'^## Mandatory invariants\n(.*?)^## ', text, re.S | re.M)
    if not m:
        return []
    return re.findall(r'\*\*(INV-\d\d)\b', m.group(1))


def heading_exists(path, ref):
    text = path.read_text(encoding='utf-8')
    if not ref:
        return True
    m = re.fullmatch(r'§(\d+)', ref)
    if m:
        return re.search(rf'^## {m.group(1)}\. ', text, re.M) is not None
    m = re.fullmatch(r'([A-Z]\d+)', ref)
    if m:
        return re.search(rf'^## {m.group(1)}\. ', text, re.M) is not None
    return re.search(rf'^## {re.escape(ref)}\s*$', text, re.M) is not None


def glossary_errors():
    errors = []
    path = ROOT/'GLOSSARY.md'
    text = path.read_text(encoding='utf-8')
    m = re.search(r'<!-- table:glossary -->\n(.*?)\n<!-- end -->', text, re.S)
    if not m:
        return ['GLOSSARY.md lacks its glossary table']
    terms = set()
    for row in m.group(1).splitlines()[2:]:
        cells = [c.strip() for c in row.strip().strip('|').split('|')]
        if len(cells) != 3:
            errors.append(f'GLOSSARY.md: malformed row {row!r}')
            continue
        term, _, where = cells
        if term in terms:
            errors.append(f'GLOSSARY.md: term defined twice: {term}')
        terms.add(term)
        name, _, ref = where.partition(' ')
        target = ROOT/name
        if not target.is_file():
            errors.append(f'GLOSSARY.md: {term} points to missing file {name}')
        elif not heading_exists(target, ref.strip()):
            errors.append(f'GLOSSARY.md: {term} points to missing section {where}')
    return errors


def composition_errors():
    spec = importlib.util.spec_from_file_location('composition', ROOT/'tools'/'composition.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.all_checks()


def check():
    errors = []
    try:
        wanted = assembled()
    except (OSError, UnicodeError) as exc:
        print('DOCUMENT CHECK FAILED: missing or unreadable canonical input: '+str(exc))
        return 1
    master = ROOT/'MASTER_PROMPT.md'
    if not master.exists() or master.read_text(encoding='utf-8') != wanted:
        errors.append('Master prompt differs from canonical sources; inspect before assembling')
    try:
        guards = patterns()
    except ValueError as exc:
        guards = []
        errors.append(str(exc))
    for name in OPERATIONAL:
        path = ROOT/name
        if not path.is_file():
            errors.append(f'missing operational file {name}')
            continue
        text = path.read_text(encoding='utf-8')
        for number, line in enumerate(text.splitlines(), 1):
            for guard in guards:
                if guard.search(line):
                    errors.append(f'{name}:{number}: portability guard matched /{guard.pattern}/')
            if name != 'MIGRATION.md' and STALE_VERSION.search(line):
                errors.append(f'{name}:{number}: names a version other than {VERSION}')
        if name in VERSIONED and f'Version {VERSION}' not in text:
            errors.append(f'{name} does not declare Version {VERSION}')
    ids = invariant_ids()
    if tuple(ids) != EXPECTED_INVARIANTS:
        errors.append(f'WORKFLOW.md must define exactly {EXPECTED_INVARIANTS[0]}..{EXPECTED_INVARIANTS[-1]} '
                      f'in order; found {", ".join(ids) or "none"}')
    ids = list(EXPECTED_INVARIANTS)
    tier1 = sum(len((ROOT/n).read_bytes()) for n in TIER1 if (ROOT/n).is_file())
    if tier1 > TIER1_BUDGET_BYTES:
        errors.append(f'Tier 1 core is {tier1} bytes, above its {TIER1_BUDGET_BYTES}-byte ceiling')
    compact = ROOT/COMPACT
    if compact.is_file():
        text = compact.read_text(encoding='utf-8')
        if len(text.encode('utf-8')) > COMPACT_BUDGET_BYTES:
            errors.append(f'{COMPACT} exceeds its {COMPACT_BUDGET_BYTES}-byte budget')
        for marker in COMPACT_MARKERS:
            if marker not in text:
                errors.append(f'{COMPACT} lost required rule marker: {marker!r}')
        for inv in ids:
            if not re.search(rf'\b{inv}\b', text):
                errors.append(f'{COMPACT} lost mandatory invariant {inv}')
        for name in set(re.findall(r'\b([A-Z][A-Z_]+\.md)\b', text)):
            if not (ROOT/name).is_file():
                errors.append(f'{COMPACT} names missing module {name}')
    for p in ROOT.rglob('*.md'):
        if UNSCANNED_DIRS & set(p.relative_to(ROOT).parts):
            continue
        for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
            if '://' in target or target.startswith('#'):
                continue
            name = target.split('#')[0]
            if name and not (p.parent/name).is_file():
                errors.append(f'{p.relative_to(ROOT)}: missing local file link {name}')
    errors += glossary_errors()
    try:
        errors += composition_errors()
    except Exception as exc:  # report, never hide, a broken helper
        errors.append(f'composition helper failed: {exc}')
    if errors:
        print('DOCUMENT CHECK FAILED\n'+'\n'.join(errors))
        return 1
    print(f'DOCUMENT CONSISTENCY PASSED ({VERSION}): master matches {len(MODULES)} modules and launch; '
          f'compact tier within budget carrying {len(ids)} invariant IDs and {len(COMPACT_MARKERS)} markers; '
          f'Tier 1 core {tier1}/{TIER1_BUDGET_BYTES} bytes; versions declared; local links resolve; '
          f'glossary resolves; composition tables, single-dimension presets, quoted defaults and examples consistent; '
          f'{len(guards)} portability guards clear across {len(OPERATIONAL)} operational files. '
          'Not a semantic, behavioral or universal-portability certificate.')
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['assemble', 'check'])
    args = parser.parse_args()
    if args.action == 'assemble':
        (ROOT/'MASTER_PROMPT.md').write_text(assembled(), encoding='utf-8', newline='\n')
        print('Assembled master in '+str(ROOT))
        return 0
    return check()


if __name__ == '__main__':
    sys.exit(main())
