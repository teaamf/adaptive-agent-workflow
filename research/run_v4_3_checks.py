"""Reproduce v4.3 document-maintenance controls in an isolated temporary copy."""
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse
import json
import os
import shutil
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--temp-root', type=Path, required=True)
    parser.add_argument('--skill-validator', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    permitted_temp_root = args.temp_root.resolve(strict=True)
    records = []
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8')
    with TemporaryDirectory(prefix='workflow-v43-', dir=permitted_temp_root) as temp_name:
        temp_root = Path(temp_name).resolve()
        target = temp_root / 'adaptive-agent-workflow'
        # TemporaryDirectory removes its tree on exit; verify its final boundary first.
        if temp_root.parent != permitted_temp_root or target == root or root.is_relative_to(temp_root):
            raise RuntimeError('Unexpected isolated target')
        shutil.copytree(root, target, ignore=shutil.ignore_patterns('__pycache__'))

        def run(label, expected, command=None, message=None):
            cmd = command or [sys.executable, str(target/'tools/documents.py'), 'check']
            result = subprocess.run(cmd, cwd=temp_root, env=env, capture_output=True,
                                    text=True, encoding='utf-8')
            output = (result.stdout + result.stderr).strip()
            passed = result.returncode == expected and (message is None or message in output)
            records.append({'check': label, 'expected_exit': expected,
                            'actual_exit': result.returncode, 'passed': passed,
                            'output': output.replace(str(temp_root), '<isolated-temp>')})
            print(f'{label}: {"PASS" if passed else "FAIL"} (exit {result.returncode})')
            if not passed:
                raise RuntimeError(output)

        run('relocated_clean', 0)
        controls = [
            ('stale_master', 'UI_REVIEW_PLAYBOOK.md',
             lambda s: s+'\nTemporary isolated edit.\n', 'Master prompt differs'),
            ('broken_local_link', 'README.md',
             lambda s: s+'\n[Invalid control](absent-control-file.md)\n', 'missing local file link'),
            ('provider_leakage', 'WORKFLOW_CONFIGURATION.md',
             lambda s: s+'\nclaude\n', 'portability guard matched'),
            ('compact_rule_loss', 'COMPACT_PROMPT.md',
             lambda s: s.replace('Do not weaken a check', 'Removed isolated marker'),
             'lost required rule marker'),
        ]
        for label, filename, mutate, message in controls:
            path = target/filename
            original = path.read_bytes()
            try:
                path.write_text(mutate(original.decode('utf-8')), encoding='utf-8', newline='\n')
                run(label, 1, message=message)
            finally:
                path.write_bytes(original)
            run(label+'_restored', 0)
        for filename in ('WORKFLOW_CONFIGURATION.md', 'UI_REVIEW_PLAYBOOK.md'):
            path = target/filename
            original = path.read_bytes()
            try:
                path.unlink()
                run('missing_'+filename, 1, message='missing or unreadable canonical input')
            finally:
                path.write_bytes(original)
            run('restored_'+filename, 0)
        run('packaged_skill_frontmatter', 0,
            [sys.executable, str(args.skill_validator.resolve()), str(target)], 'Skill is valid!')
        skill_text = (target/'SKILL.md').read_text(encoding='utf-8')
        matched = '\nname: '+target.name+'\n' in skill_text
        records.append({'check': 'deployment_folder_matches_skill_name', 'passed': matched})
        if not matched:
            raise RuntimeError('Deployment folder does not match skill name')
    sizes = {name: {'bytes': len((root/name).read_bytes()),
                    'words': len((root/name).read_text(encoding='utf-8').split())}
             for name in ('COMPACT_PROMPT.md', 'SKILL.md', 'WORKFLOW_CONFIGURATION.md',
                          'UI_REVIEW_PLAYBOOK.md', 'MASTER_PROMPT.md')}
    report = {'date': '2026-11-04', 'version': '4.3',
              'assessment': 'author document-maintenance checks; not agent trials or independent review',
              'setup_failure': 'Initial default temporary location denied a nested write before checks ran; '
                               'rerun used an explicitly writable artifacts directory.',
              'python': sys.version.split()[0], 'checks': records, 'sizes': sizes,
              'all_passed': all(r['passed'] for r in records)}
    (root/'research/v4.3-check-results.json').write_text(json.dumps(report, indent=2)+'\n',
                                                       encoding='utf-8', newline='\n')
    print(f'Recorded {len(records)} checks; all passed')


if __name__ == '__main__':
    main()
