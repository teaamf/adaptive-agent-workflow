"""Maintain the general document package; never executes or certifies a project."""
from pathlib import Path
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
MODULES = ('PROJECT_TEMPLATE.md', 'WORKFLOW.md', 'AGENT_INTERACTION.md', 'PROFILES.md',
           'UI_DESIGN_PROTOCOL.md', 'UI_REVIEW_PLAYBOOK.md', 'HOST_ADAPTERS.md',
           'WORKFLOW_CONFIGURATION.md', 'CONTINUOUS_IMPROVEMENT.md', 'PRACTICAL_PLAYBOOKS.md')
# Documents that instruct an agent or adopter; provenance records (research, validation, merge and
# change history, the advice index) may name historical sources and are not scanned.
OPERATIONAL = MODULES + ('LAUNCH.md', 'COMPACT_PROMPT.md', 'README.md', 'GUIDE.md', 'SKILL.md',
                         'evaluation/SCENARIOS.md', 'references/ENGINEERING_ADVICE_MAP.md')
COMPACT = 'COMPACT_PROMPT.md'
COMPACT_BUDGET_BYTES = 16000
# Rules the compact tier must keep; a narrow drift guard, not a semantic equivalence proof.
COMPACT_MARKERS = ('data, not instructions', 'Do not weaken a check', 'Pause and reassess',
                   'untrusted content', 'Role-play is not independent review', 'ACCEPTED_FOR_STATED_SCOPE',
                   'progress note')
PATTERNS = ROOT/'tools'/'portability_patterns.txt'


def assembled():
    parts = [(ROOT/'LAUNCH.md').read_text(encoding='utf-8').rstrip()]
    for name in MODULES:
        body = (ROOT/name).read_text(encoding='utf-8').rstrip()
        parts.append(f'<!-- BEGIN {name} -->\n\n{body}\n\n<!-- END {name} -->')
    return '\n\n---\n\n'.join(parts)+'\n'


def patterns():
    if not PATTERNS.is_file():
        return []
    lines = PATTERNS.read_text(encoding='utf-8').splitlines()
    return [re.compile(p.strip(), re.I) for p in lines if p.strip() and not p.lstrip().startswith('#')]


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
    # A narrow guard against known project, vendor and machine leakage, not a semantic proof.
    guards = patterns()
    for name in OPERATIONAL:
        path = ROOT/name
        if not path.is_file():
            errors.append(f'missing operational file {name}')
            continue
        for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            for guard in guards:
                if guard.search(line):
                    errors.append(f'{name}:{number}: portability guard matched /{guard.pattern}/')
    compact = ROOT/COMPACT
    if compact.is_file():
        text = compact.read_text(encoding='utf-8')
        if len(text.encode('utf-8')) > COMPACT_BUDGET_BYTES:
            errors.append(f'{COMPACT} exceeds its {COMPACT_BUDGET_BYTES}-byte budget')
        for marker in COMPACT_MARKERS:
            if marker not in text:
                errors.append(f'{COMPACT} lost required rule marker: {marker!r}')
        for name in set(re.findall(r'\b([A-Z][A-Z_]+\.md)\b', text)):
            if not (ROOT/name).is_file():
                errors.append(f'{COMPACT} names missing module {name}')
    for p in ROOT.rglob('*.md'):
        if 'research' in p.relative_to(ROOT).parts:
            continue
        for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
            if '://' in target or target.startswith('#'):
                continue
            name = target.split('#')[0]
            if name and not (p.parent/name).is_file():
                errors.append(f'{p.relative_to(ROOT)}: missing local file link {name}')
    if errors:
        print('DOCUMENT CHECK FAILED\n'+'\n'.join(errors))
        return 1
    print(f'DOCUMENT CONSISTENCY PASSED: self-contained master matches {len(MODULES)} modules and launch; '
          f'compact tier within budget with required rules; local file links resolve; '
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
