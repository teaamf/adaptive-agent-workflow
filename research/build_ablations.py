"""Build every arm package of the 4.4-rc1 experiment, identically packaged, and identify each by hash.

Arms:
  A1  the 4.3 baseline, unmodified;
  A2  4.4-rc1, unmodified;
  A3  rc1 without the attribution and scope-audit requirements;
  A4  rc1 with scaffolding fixed at `standard` (no capability-based lightening; §0 still applies);
  A5  rc1 in which no assurance level requires a separate reviewer or independent verification.
      Honesty rules that hold in every arm stay (INV-06: role-play is not independent review; how to
      report a review's isolation if one happens).

Each ablation is a deterministic text edit of a full rc1 copy. Every edit must match exactly once, so a
later change to rc1 that breaks an ablation is detected rather than silently producing an unablated arm.
The edited full tree is reassembled and must pass its own `tools/documents.py check`. It is then
packaged by the same rule as every other arm (PACKAGE_EXCLUDE), and the packaged files are searched for
residual text of the removed component (RESIDUALS); any hit fails the build. Ablation arms are evaluation
material, never usable workflow versions. The output directory must be outside the package.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys

# One packaging rule for every arm: what an agent in the trial receives. History, validation records,
# migration notes, scenario lists (which describe trap families) and research records are excluded.
PACKAGE_EXCLUDE = ('research', 'evaluation', '__pycache__', '*.pyc', 'SHA256SUMS', 'RESEARCH_AND_CHANGES.md',
                   'MERGE_DECISIONS.md', 'VALIDATION.md', 'MIGRATION.md')

# (file, old, new): literal replacement that must match exactly once. ('re', file, pattern, new): regex.
ARMS = {
    'A3-no-attribution-scope': [
        ('re', 'WORKFLOW.md', r'- \*\*INV-09 Mechanism\.\*\*[^\n]*\n', ''),
        ('WORKFLOW.md', '| Attribution | Did the claimed mechanism cause the result? | Stated causal claim; revert or ablation; mechanism probe |\n', ''),
        ('WORKFLOW.md', '| Authorization and scope | Were only authorized files, data, tools and external actions used? | Observed changes and actions compared with the contract |\n', ''),
        ('WORKFLOW.md', 'narrow the cause, state the causal claim, make', 'narrow the cause, make'),
        ('WORKFLOW.md', 'an unexpected approach calls for an explanation and attribution evidence, not rejection (INV-09).',
         'an unexpected approach calls for an explanation, not rejection.'),
        ('re', 'COMPACT_PROMPT.md', r'- \*\*INV-09\*\*[^\n]*\n', ''),
        ('LAUNCH.md', 'Accept a result only when its mechanism, scope and checks are sound', 'Accept a result only when its checks are sound'),
        ('COMPACT_PROMPT.md', '**mechanism**, **scope** (only authorized files and actions), ', ''),
        ('COMPACT_PROMPT.md', 'reproduce it, state the cause, fix it;', 'reproduce it, fix it;'),
        ('tools/documents.py', "EXPECTED_INVARIANTS = tuple(f'INV-{n:02d}' for n in range(1, 13))",
         "EXPECTED_INVARIANTS = tuple(f'INV-{n:02d}' for n in range(1, 13) if n != 9)"),
    ],
    'A4-fixed-scaffolding': [
        ('WORKFLOW.md', 'Scaffolding intensity (optional plans, checklists, extra passes) follows task structure, demonstrated capability on the task class, observed progress, uncertainty, consequence and remaining resources (COMPOSITION.md K4). Model identity is only a starting hypothesis.',
         'Scaffolding intensity is fixed at standard: the core protocol as written. §0 still applies to routine work.'),
        ('WORKFLOW.md', ' Capability may lighten procedure, never assurance.', ''),
        ('COMPACT_PROMPT.md', ' Capability may lighten procedure, never assurance.', ''),
        ('re', 'COMPOSITION.md', r'\| auto \(default\) \| Choose from the inputs below[^\n]*\n\| minimal \|[^\n]*\n', ''),
        ('re', 'COMPOSITION.md', r'\| guided \|[^\n]*\n', ''),
        ('re', 'COMPOSITION.md', r'\nSelection inputs for `auto`:\n.*?Approval gates and assurance are never de-escalated this way\.\n', '\n'),
        ('COMPOSITION.md', '| scaffolding | auto, minimal, standard, guided | auto |', '| scaffolding | standard | standard |'),
        ('re', 'COMPOSITION.md', r'\| quick-fix \|[^\n]*\n', ''),
        ('re', 'examples/CONFIGURATIONS.md', r'## 2\. Quick-fix preset.*?(?=## 3\.)', ''),
        ('re', 'examples/CONFIGURATIONS.md', r'## 7\. Co-creation with terse reports and minimal scaffolding.*?(?=## 8\.)', ''),
        ('HOST_ADAPTERS.md', 'Observed capability on the task class is also the starting point for scaffolding intensity (COMPOSITION.md K4): a worker that demonstrably handles the class well may receive less procedure. It never receives less assurance (INV-07). ', ''),
        ('GUIDE.md', ', and minimal procedure never puts non-routine work on the fast path', ''),
        ('SKILL.md', 'a stronger model may lighten procedure but never assurance', 'a stronger model never lowers assurance'),
        ('re', 'COMPOSITION.md', r'\| C-11 \|[^\n]*\n', ''),
    ],
    'A5-no-independent-review': [
        ('WORKFLOW.md', '**Standard:** maker plus fresh-context reviewer; independent tester when distinct coverage is needed',
         '**Standard:** maker with explicit first-party review'),
        ('WORKFLOW.md', '**High consequence:** independent verification, relevant domain expertise',
         '**High consequence:** first-party verification, relevant domain expertise'),
        ('WORKFLOW.md', 'material work usually adds the fresh-context review and an audit of any changed check;',
         'material work usually adds an audit of any changed check;'),
        ('COMPACT_PROMPT.md', '**Standard** (material): add a review in a fresh context.', '**Standard** (material): review your own work explicitly.'),
        ('COMPACT_PROMPT.md', '**High consequence** (consequential): independent verification,', '**High consequence** (consequential): your own verification,'),
        ('COMPACT_PROMPT.md', 'If a required review or capability is missing,', 'If a required capability is missing,'),
        ('GUIDE.md', 'material changes normally receive fresh-context review. Required independence remains required if the host cannot provide it.',
         'material changes receive explicit first-party review.'),
        ('SKILL.md', ' First-party work cannot satisfy a required independent review.', ''),
        ('UI_REVIEW_PLAYBOOK.md', ' Obtain any required independent review before acceptance.', ''),
        ('COMPOSITION.md', 'Requested independent review → required: blocked (ReviewerUnavailable: no separate session on this host).\n', ''),
        ('tools/composition.py', "needs_review = eff['assurance'] in ('standard', 'high')", 'needs_review = False'),
        ('re', 'examples/CONFIGURATIONS.md', r'## 3\. Lightweight assurance requested.*?(?=## 4\.)', ''),
    ],
}
# Residual text of the removed component; a case-insensitive hit in the packaged arm fails the build.
RESIDUALS = {
    'A3-no-attribution-scope': [r'INV-09', r'attribution', r'mechanism, scope', r'its mechanism', r'mechanism probe', r'authorization and scope',
                                r'scope audit', r'claimed mechanism', r'state the causal claim', r'state the cause'],
    'A4-fixed-scaffolding': [r'scaffolding=minimal', r'scaffolding: minimal', r'\| minimal \|', r'\| guided \|',
                             r'quick-fix', r'demonstrably handles', r'lighten procedure', r'Selection inputs'],
    'A5-no-independent-review': [r'fresh-context reviewer', r'add a review in a fresh context',
                                 r'adds the fresh-context review', r'normally receive fresh-context review',
                                 r'independent verification', r'cannot satisfy a required independent review',
                                 r'Obtain any required independent review', r'independent_review: required'],
}
TEXT_SUFFIXES = {'.md', '.py', '.txt'}


def manifest(root):
    lines = []
    for path in sorted((p for p in root.rglob('*') if p.is_file()), key=lambda p: p.relative_to(root).as_posix()):
        lines.append(f'{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(root).as_posix()}')
    return hashlib.sha256('\n'.join(lines).encode('utf-8')).hexdigest(), len(lines), lines


def run(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace')


def apply(arm, tree, edits):
    for edit in edits:
        if edit[0] == 're':
            _, name, pattern, new = edit
            path = tree/name
            text, count = re.subn(pattern, new, path.read_text(encoding='utf-8'), flags=re.S)
        else:
            name, old, new = edit
            path = tree/name
            text = path.read_text(encoding='utf-8')
            count = text.count(old)
            text = text.replace(old, new)
        if count != 1:
            raise SystemExit(f'{arm}: expected one match in {name}, found {count}: {str(edit[-2])[:70]!r}')
        path.write_text(text, encoding='utf-8', newline='\n')
    for name in ('WORKFLOW.md', 'COMPACT_PROMPT.md', 'COMPOSITION.md'):
        path = tree/name
        text = path.read_text(encoding='utf-8')
        path.write_text(text.replace('Version 4.4-rc1', f'Version 4.4-rc1 ablation {arm.split("-")[0]}', 1), encoding='utf-8',
                        newline='\n')


def check_tree(arm, tree, regenerate):
    py = [sys.executable, '-I', '-X', 'utf8', '-B']
    if regenerate:
        result = run(py+[str(tree/'tools/composition.py'), 'write-examples'], tree)
        if result.returncode:
            raise SystemExit(f'{arm}: write-examples failed\n{result.stdout}{result.stderr}')
        run(py+[str(tree/'tools/documents.py'), 'assemble'], tree)
    result = run(py+[str(tree/'tools/documents.py'), 'check'], tree)
    if result.returncode:
        raise SystemExit(f'{arm}: its own documents.py check failed\n{result.stdout}{result.stderr}')
    return result.stdout.strip().splitlines()[-1][:120]


def package(full, target):
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(full, target, ignore=shutil.ignore_patterns(*PACKAGE_EXCLUDE))


def residual_hits(arm, target):
    hits = []
    for pattern in RESIDUALS.get(arm, []):
        rx = re.compile(pattern, re.I)
        for path in target.rglob('*'):
            if path.is_file() and path.suffix in TEXT_SUFFIXES:
                for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
                    if rx.search(line):
                        hits.append(f'{path.relative_to(target).as_posix()}:{number}: /{pattern}/')
    return hits


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--baseline', type=Path, help='4.3 baseline folder (default: ../../releases/4.3-baseline)')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    baseline = (args.baseline or root.parent.parent/'releases'/'4.3-baseline').resolve(strict=True)
    out = args.out.resolve()
    if out == root or root in out.parents or out == baseline or baseline in out.parents:
        parser.error('--out must be outside both packages')
    out.mkdir(parents=True, exist_ok=True)
    work = out/'_full'
    if work.exists():
        shutil.rmtree(work)
    summary = {'packaging_rule': {'excluded': list(PACKAGE_EXCLUDE)},
               'rc1_source_manifest': manifest(root)[0], 'baseline_source_manifest': manifest(baseline)[0], 'arms': {}}
    sources = {'A1-baseline-4.3': (baseline, None), 'A2-rc1': (root, None)}
    sources.update({arm: (root, edits) for arm, edits in ARMS.items()})
    for arm, (source, edits) in sources.items():
        full = work/arm
        shutil.copytree(source, full, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        if edits:
            apply(arm, full, edits)
        check = check_tree(arm, full, regenerate=bool(edits))
        target = out/arm
        package(full, target)
        hits = residual_hits(arm, target)
        if hits:
            raise SystemExit(f'{arm}: residual text of the removed component\n' + '\n'.join(hits))
        tree_hash, files, lines = manifest(target)
        summary['arms'][arm] = {'package_manifest_sha256': tree_hash, 'files': files, 'own_check': check,
                                'residual_patterns_clear': len(RESIDUALS.get(arm, [])), 'file_manifest': lines}
        print(f'{arm}: package {tree_hash} ({files} files); residual patterns clear: {len(RESIDUALS.get(arm, []))}')
    shutil.rmtree(work)
    (out/'arms.json').write_text(json.dumps(summary, indent=2)+'\n', encoding='utf-8', newline='\n')
    print(f'Recorded arm identities in {out/"arms.json"}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
