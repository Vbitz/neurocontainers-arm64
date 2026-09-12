"""Exercise dispatch validation against the pinned fork's real recipe resolver."""

import contextlib
import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('arm64', ROOT / 'scripts/arm64.py')
arm64 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(arm64)


@contextlib.contextmanager
def recipe_checkout():
    previous = Path.cwd()
    os.chdir(ROOT / 'neurocontainers')
    try:
        yield
    finally:
        os.chdir(previous)


class DispatchValidationTests(unittest.TestCase):
    def test_real_arm64_recipe_resolves_and_records_revision(self):
        with recipe_checkout(), tempfile.TemporaryDirectory() as temp:
            info = arm64.prepare('workshopdemo', 'arm64', Path(temp))
            self.assertEqual(info['architecture'], 'aarch64')
            self.assertEqual(info['container'], 'workshopdemo_arm64')
            self.assertRegex(info['source_sha'], r'^[0-9a-f]{40}$')
            self.assertTrue((Path(temp) / 'metadata.json').is_file())

    def test_rejects_paths_and_multiple_recipes(self):
        for recipe in ('../workshopdemo', 'a,b', '--help', 'a\nb'):
            with self.subTest(recipe=recipe), self.assertRaises(ValueError):
                arm64.prepare(recipe, 'arm64', Path('/unused'))

    def test_rejects_x86_variant_before_building(self):
        with recipe_checkout(), tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(RuntimeError, 'does not declare variant'):
                arm64.prepare('workshopdemo', 'x86_64', Path(temp))

    def test_rejects_stale_or_empty_fulltest(self):
        original = Path.read_text
        for suite in (
            'name: workshopdemo\nversion: stale\ntests: [{name: hello}]',
            'name: workshopdemo\nversion: 1.0.0\ntests: []',
        ):
            def read(path, *args, **kwargs):
                if path.name == 'fulltest.yaml':
                    return suite
                return original(path, *args, **kwargs)

            with recipe_checkout(), tempfile.TemporaryDirectory() as temp:
                with patch.object(Path, 'read_text', read), self.assertRaises(ValueError):
                    arm64.prepare('workshopdemo', 'arm64', Path(temp))


if __name__ == '__main__':
    unittest.main()
