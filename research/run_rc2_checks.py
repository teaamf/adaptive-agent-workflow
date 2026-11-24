"""Run 4.4-rc2 document-maintenance controls in an isolated temporary copy.

Each control mutates the copy, expects tools/documents.py check to fail with a specific message, then
restores the file and expects a clean pass. Results are written to a run-stamped file in --out, never
into the tested package, and every record is kept even when a control fails. These are
document-maintenance checks, not agent trials or independent review.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
from datetime import datetime, timezone
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

IGNORE = shutil.ignore_patterns('__pycache__', '*.pyc')


def manifest(root):
    """SHA-256 over the sorted per-file hashes of a tree: identifies exactly what was tested."""
    lines = []
    files = [p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
    for path in sorted(files, key=lambda p: p.relative_to(root).as_posix()):  # code-point order, any OS
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f'{digest}  {path.relative_to(root).as_posix()}')
    return hashlib.sha256('\n'.join(lines).encode('utf-8')).hexdigest(), len(lines)


def frontmatter_errors(skill_text, folder_name):
    m = re.match(r'---\n(.*?)\n---\n', skill_text, re.S)
    if not m:
        return ['SKILL.md has no frontmatter']
    fields = dict(line.split(':', 1) for line in m.group(1).splitlines() if ':' in line)
    fields = {k.strip(): v.strip() for k, v in fields.items()}
    errors = []
    allowed = {'name', 'description', 'license', 'allowed-tools', 'metadata', 'compatibility'}
    if set(fields) - allowed:
        errors.append(f'unexpected frontmatter fields {sorted(set(fields) - allowed)}')
    if fields.get('name') != folder_name:
        errors.append(f'name {fields.get("name")!r} does not match folder {folder_name!r}')
    if not 0 < len(fields.get('description', '')) <= 1024:
        errors.append('description missing or longer than 1024 characters')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--temp-root', type=Path, required=True, help='writable directory for the isolated copy')
    parser.add_argument('--out', type=Path, required=True, help='directory for the run-stamped result file')
    parser.add_argument('--skill-validator', type=Path, help='optional external skill validator to run as well')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    temp_parent = args.temp_root.resolve(strict=True)
    out_dir = args.out.resolve()
    if out_dir == root or root in out_dir.parents:
        parser.error('--out must be outside the tested package so results never overwrite it')
    out_dir.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc)
    records = []
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8')
    source_hash, source_files = manifest(root)
    with TemporaryDirectory(prefix='workflow-rc2-', dir=temp_parent) as temp_name:
        temp_root = Path(temp_name).resolve()
        target = temp_root/'adaptive-agent-workflow'
        if temp_root.parent != temp_parent or target == root or root.is_relative_to(temp_root):
            raise RuntimeError('Unexpected isolated target')
        shutil.copytree(root, target, ignore=IGNORE)
        tested_hash, tested_files = manifest(target)

        def run(label, expected, message=None, command=None):
            cmd = command or [sys.executable, '-I', '-X', 'utf8', str(target/'tools/documents.py'), 'check']
            result = subprocess.run(cmd, cwd=temp_root, env=env, capture_output=True, text=True, encoding='utf-8', errors='replace')
            output = ((result.stdout or '') + (result.stderr or '')).strip()
            passed = result.returncode == expected and (message is None or message in output)
            records.append({'check': label, 'expected_exit': expected, 'expected_message': message,
                            'actual_exit': result.returncode, 'passed': passed,
                            'output': output.replace(str(temp_root), '<isolated-temp>')})
            print(f'{label}: {"PASS" if passed else "FAIL"} (exit {result.returncode})')

        def mutate(label, filename, change, message):
            # filename/change may also be parallel lists, for controls that must change several files at once.
            names = filename if isinstance(filename, list) else [filename]
            changes = change if isinstance(change, list) else [change]
            originals = {}
            try:
                for name, edit in zip(names, changes):
                    path = target/name
                    originals[name] = path.read_bytes() if path.exists() else None
                    if edit is None:
                        path.unlink()
                        continue
                    old = originals[name].decode('utf-8')
                    new = edit(old)
                    if new == old:
                        raise RuntimeError(f'control {label} did not change {name}')
                    path.write_text(new, encoding='utf-8', newline='\n')
                run(label, 1, message)
            finally:
                for name, original in originals.items():
                    if original is not None:
                        (target/name).write_bytes(original)
            run(label+'_restored', 0)

        run('relocated_clean', 0)
        controls = [
            ('stale_master', 'UI_REVIEW_PLAYBOOK.md', lambda s: s+'\nTemporary isolated edit.\n', 'Master prompt differs'),
            ('broken_local_link', 'README.md', lambda s: s+'\n[Invalid control](absent-control-file.md)\n',
             'missing local file link'),
            ('provider_leakage', 'WORKFLOW_CONFIGURATION.md', lambda s: s+'\nclaude\n', 'portability guard matched'),
            ('compact_marker_loss', 'COMPACT_PROMPT.md',
             lambda s: s.replace('Do not weaken a check', 'Removed isolated marker'), 'lost required rule marker'),
            ('compact_invariant_loss', 'COMPACT_PROMPT.md', lambda s: s.replace('**INV-07**', '**Ratchet**'),
             'lost mandatory invariant INV-07'),
            ('compact_over_budget', 'COMPACT_PROMPT.md', lambda s: s+'\n'+'x'*11000+'\n', 'exceeds its 10500-byte budget'),
            ('tier1_over_ceiling', 'PROJECT_TEMPLATE.md', lambda s: s+'\n'+'x'*400+'\n', 'Tier 1 core is'),
            ('stale_version', 'PROFILES.md', lambda s: s.replace('Version 4.4-rc2.', 'Version 4.3.', 1),
             'names a version other than 4.4-rc2'),
            ('missing_patterns', 'tools/portability_patterns.txt', None, 'portability pattern file missing'),
            ('empty_patterns', 'tools/portability_patterns.txt', lambda s: '# comments only\n', 'has no patterns'),
            ('incompatible_preset', 'COMPOSITION.md',
             lambda s: s.replace('| unattended | attended=no |', '| unattended | attended=no; learning=on; analyse=autonomous |'),
             'violates C-01'),
            ('undefined_preset_value', 'COMPOSITION.md',
             lambda s: s.replace('| quick-fix | scaffolding=minimal |', '| quick-fix | scaffolding=extreme |'),
             'preset quick-fix: invalid scaffolding=extreme'),
            ('preset_coupling', 'COMPOSITION.md',
             lambda s: s.replace('| careful-change | assurance=high |', '| careful-change | assurance=high; cadence=each-decision |'),
             'preset careful-change couples dimensions'),
            ('scaffolding_clamp_warning_removed', 'COMPOSITION.md',
             lambda s: re.sub(r'\| C-11 \|[^\n]*\n', '', s), 'example 2: recorded result differs from resolution'),
            ('quoted_default_drift', 'COMPOSITION.md',
             lambda s: s.replace('| stagnation_window | integer | 2 |', '| stagnation_window | integer | 3 |'),
             'does not quote the K5 default stagnation_window=3'),
            ('core_invariant_deleted_everywhere', ['WORKFLOW.md', 'COMPACT_PROMPT.md'],
             [lambda s: re.sub(r'- \*\*INV-12 [^\n]*\n', '', s), lambda s: re.sub(r'- \*\*INV-12\*\*[^\n]*\n', '', s)],
             'must define exactly INV-01..INV-12'),
            ('example_drift', 'examples/CONFIGURATIONS.md',
             lambda s: s.replace('assurance: high  [floor (consequential)]', 'assurance: lightweight  [floor (consequential)]', 1),
             'recorded result differs from resolution'),
            ('glossary_dangling', 'GLOSSARY.md', lambda s: s.replace('| Claim | Entity | WORKFLOW.md §9 |', '| Claim | Entity | WORKFLOW.md §99 |'),
             'points to missing section'),
            ('missing_composition', 'COMPOSITION.md', None, 'missing or unreadable canonical input'),
        ]
        for label, filename, change, message in controls:
            mutate(label, filename, change, message)
        if args.skill_validator:
            run('external_skill_validator', 0, None,
                [sys.executable, str(args.skill_validator.resolve()), str(target)])
        problems = frontmatter_errors((target/'SKILL.md').read_text(encoding='utf-8'), target.name)
        records.append({'check': 'skill_frontmatter_and_folder_name', 'passed': not problems, 'output': problems})
        print(f'skill_frontmatter_and_folder_name: {"PASS" if not problems else "FAIL"}')
        restored_hash, _ = manifest(target)
        records.append({'check': 'isolated_copy_restored_exactly', 'passed': restored_hash == tested_hash})
    finished = datetime.now(timezone.utc)
    report = {
        'version': '4.4-rc2',
        'assessment': 'document-maintenance controls on an isolated copy; not agent trials or independent review',
        'started_utc': started.isoformat(timespec='seconds'), 'finished_utc': finished.isoformat(timespec='seconds'),
        'python': sys.version.split()[0], 'platform': sys.platform,
        'source_manifest_sha256': source_hash, 'source_files': source_files,
        'tested_manifest_sha256': tested_hash, 'tested_files': tested_files,
        'external_skill_validator': 'run' if args.skill_validator else 'not run',
        'checks': records, 'all_passed': all(r['passed'] for r in records),
    }
    out = out_dir/f'rc2-checks-{started.strftime("%Y%m%dT%H%M%SZ")}.json'
    out.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8', newline='\n')
    print(f'Recorded {len(records)} checks in {out}; all passed: {report["all_passed"]}')
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
