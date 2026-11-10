from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CatalogTests(unittest.TestCase):
    def test_seven_agent_skills_have_unique_metadata(self):
        skill_files = sorted((ROOT / 'skills').glob('*/SKILL.md'))
        self.assertEqual(len(skill_files), 7)
        names = set()
        for file in skill_files:
            content = file.read_text(encoding='utf-8')
            self.assertTrue(content.startswith('---\n'), file.name)
            match = re.match(r'---\n(.*?)\n---\n', content, flags=re.DOTALL)
            self.assertIsNotNone(match, file)
            name = re.search(r'^name:\s*(\S+)', match.group(1), flags=re.MULTILINE)
            description = re.search(r'^description:\s*(.+)', match.group(1), flags=re.MULTILINE)
            self.assertIsNotNone(name, file)
            self.assertIsNotNone(description, file)
            self.assertEqual(name.group(1), file.parent.name)
            self.assertGreater(len(description.group(1)), 40)
            self.assertNotIn(name.group(1), names)
            names.add(name.group(1))


if __name__ == '__main__':
    unittest.main()
