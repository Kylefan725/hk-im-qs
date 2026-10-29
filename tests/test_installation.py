"""Regression checks for the single-skill package and non-destructive installation."""
from __future__ import annotations

import contextlib
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))

import install_skills  # noqa: E402
from validate_repository import PLAYBOOKS, SKILL_PATH, validate  # noqa: E402


class SingleSkillInstallationTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix='hk-im-qs-install-test-')
        self.addCleanup(temporary.cleanup)
        self.scratch = Path(temporary.name)
        self.target = self.scratch/'active-skills'

    def install(self, *options: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(ROOT/'scripts/install_skills.py'),
             '--target', str(self.target), *options],
            text=True, capture_output=True, check=False,
        )

    def add_unrelated_entry(self) -> Path:
        self.target.mkdir()
        sentinel = self.target/'unrelated-skill.txt'
        sentinel.write_text('preserve me', encoding='utf-8')
        return sentinel

    def fixture_repository(self) -> Path:
        root = self.scratch/'repository'
        root.mkdir()
        for name in ('skills', 'scripts', 'docs'):
            shutil.copytree(ROOT/name, root/name,
                            ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        for name in ('README.md', 'README.zh-HK.md', 'LICENSE'):
            shutil.copyfile(ROOT/name, root/name)
        self.assertEqual(validate(root), [], 'The source package must validate first.')
        return root

    def test_dry_run_creates_nothing(self) -> None:
        result = self.install('--dry-run')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('no files written', result.stdout)
        self.assertFalse(self.target.exists())

    def test_copy_installs_one_complete_skill_and_preserves_unrelated_entry(self) -> None:
        sentinel = self.add_unrelated_entry()
        result = self.install('--mode', 'copy')
        self.assertEqual(result.returncode, 0, result.stderr)
        entry = self.target/'hk-im-qs'
        self.assertFalse(entry.is_symlink())
        self.assertEqual([p.relative_to(self.target) for p in self.target.rglob('SKILL.md')],
                         [Path('hk-im-qs/SKILL.md')])
        source_files = {p.relative_to(ROOT/SKILL_PATH) for p in (ROOT/SKILL_PATH).rglob('*')
                        if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
        installed_files = {p.relative_to(entry) for p in entry.rglob('*') if p.is_file()}
        self.assertEqual(installed_files, source_files)
        for name in PLAYBOOKS:
            self.assertTrue((entry/'playbooks'/f'{name}.md').is_file())
        self.assertTrue((entry/'references/source-register.json').is_file())
        self.assertEqual(sentinel.read_text(), 'preserve me')

    def test_symlink_installs_one_complete_skill_and_preserves_unrelated_entry(self) -> None:
        sentinel = self.add_unrelated_entry()
        result = self.install('--mode', 'symlink')
        self.assertEqual(result.returncode, 0, result.stderr)
        entry = self.target/'hk-im-qs'
        self.assertTrue(entry.is_symlink())
        self.assertEqual(entry.resolve(), (ROOT/SKILL_PATH).resolve())
        for name in PLAYBOOKS:
            self.assertTrue((entry/'playbooks'/f'{name}.md').is_file())
        self.assertTrue((entry/'references/source-register.json').is_file())
        self.assertEqual({p.name for p in self.target.iterdir()},
                         {'hk-im-qs', 'unrelated-skill.txt'})
        self.assertEqual(sentinel.read_text(), 'preserve me')

    def test_existing_destination_is_not_overwritten(self) -> None:
        sentinel = self.add_unrelated_entry()
        entry = self.target/'hk-im-qs'
        entry.mkdir()
        existing = entry/'local-notes.md'
        existing.write_text('local edits', encoding='utf-8')
        result = self.install('--mode', 'copy')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('existing skill destinations', result.stderr)
        self.assertEqual(existing.read_text(), 'local edits')
        self.assertEqual({p.name for p in entry.iterdir()}, {'local-notes.md'})
        self.assertEqual(sentinel.read_text(), 'preserve me')

    def test_legacy_entries_including_broken_symlinks_block_all_writes(self) -> None:
        sentinel = self.add_unrelated_entry()
        legacy = self.target/'hkqs-general'
        legacy.mkdir()
        original = legacy/'SKILL.md'
        original.write_text('user-modified legacy skill', encoding='utf-8')
        broken = self.target/'hkqs-ground-investigation'
        broken.symlink_to(self.scratch/'missing-old-checkout', target_is_directory=True)
        previous_router = self.target/'hkqs-mode'
        previous_router.symlink_to(self.scratch/'missing-router-checkout', target_is_directory=True)
        result = self.install('--mode', 'copy')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('hkqs-general', result.stderr)
        self.assertIn('hkqs-ground-investigation', result.stderr)
        self.assertIn('hkqs-mode', result.stderr)
        self.assertIn('Archive these entries outside every active skills directory', result.stderr)
        self.assertFalse((self.target/'hk-im-qs').exists())
        self.assertTrue(broken.is_symlink())
        self.assertTrue(previous_router.is_symlink())
        self.assertEqual(original.read_text(), 'user-modified legacy skill')
        self.assertEqual(sentinel.read_text(), 'preserve me')

    def test_failed_copy_rolls_back_only_its_new_entry(self) -> None:
        sentinel = self.add_unrelated_entry()

        def partial_copy(source: Path, destination: Path, **options: object) -> None:
            (destination/'partial-file').write_text('partial', encoding='utf-8')
            raise OSError('simulated copy failure')

        argv = ['install_skills.py', '--target', str(self.target), '--mode', 'copy']
        with mock.patch.object(sys, 'argv', argv), \
                mock.patch.object(install_skills.shutil, 'copytree', side_effect=partial_copy), \
                contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            result = install_skills.main()
        self.assertEqual(result, 1)
        self.assertFalse((self.target/'hk-im-qs').exists())
        self.assertEqual({p.name for p in self.target.iterdir()}, {'unrelated-skill.txt'})
        self.assertEqual(sentinel.read_text(), 'preserve me')

    def test_validator_rejects_a_nested_second_entry_skill(self) -> None:
        root = self.fixture_repository()
        unexpected = root/SKILL_PATH/'playbooks/extra/SKILL.md'
        unexpected.parent.mkdir()
        unexpected.write_text('---\nname: extra\ndescription: Stray entry.\n---\n', encoding='utf-8')
        errors = validate(root)
        self.assertTrue(any('Exactly one entry skill required' in error for error in errors), errors)

    def test_validator_rejects_a_broken_playbook_link(self) -> None:
        root = self.fixture_repository()
        entry = root/SKILL_PATH/'SKILL.md'
        content = entry.read_text(encoding='utf-8')
        self.assertIn('playbooks/review-tender.md', content)
        entry.write_text(content.replace('playbooks/review-tender.md',
                                         'playbooks/missing-playbook.md'), encoding='utf-8')
        errors = validate(root)
        self.assertTrue(any('broken local link playbooks/missing-playbook.md' in error
                            for error in errors), errors)


if __name__ == '__main__':
    unittest.main()
