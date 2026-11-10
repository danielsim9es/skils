import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts' / 'scan.py'
SPEC = importlib.util.spec_from_file_location('skils_scan', SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ScannerTests(unittest.TestCase):
    def test_detects_known_indications(self):
        data = MODULE.scan(ROOT / 'tests/fixtures/site-inseguro')
        ids = {item['id'] for item in data['findings']}
        self.assertTrue({'rastreador-encontrado', 'imagem-sem-alt', 'checkbox-pre-marcado', 'promessa-forte', 'div-clicavel', 'campo-cpf', 'consentimento-tacito'} <= ids)
        self.assertEqual(data['files_scanned'], 1)
        for item in data['findings']:
            self.assertEqual(item['status'], 'indicio')
            self.assertIn(':', item['location'])

    def test_clean_fixture_has_no_indications(self):
        data = MODULE.scan(ROOT / 'tests/fixtures/site-seguro')
        self.assertEqual(data['finding_count'], 0)

    def test_ignores_modules_and_dotenv(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'index.html').write_text('<img alt="Banner" src="a.png">', encoding='utf-8')
            (root / '.env').write_text('DATABASE_URL=top-secret', encoding='utf-8')
            (root / 'node_modules').mkdir()
            (root / 'node_modules/a.js').write_text('Math.random()', encoding='utf-8')
            result = MODULE.scan(root)
            self.assertEqual(result['files_scanned'], 1)
            self.assertEqual(result['finding_count'], 0)
            self.assertNotIn('top-secret', json.dumps(result))

    def test_json_cli_output(self):
        result = subprocess.run([sys.executable, str(SCRIPT), str(ROOT / 'tests/fixtures/site-inseguro'), '--format', 'json'], capture_output=True, text=True, check=True)
        payload = json.loads(result.stdout)
        self.assertGreater(payload['finding_count'], 3)

    def test_unknown_path_exits_cleanly(self):
        result = subprocess.run([sys.executable, str(SCRIPT), str(ROOT / 'tests/fixtures/ausente')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('Caminho não encontrado', result.stderr)


if __name__ == '__main__':
    unittest.main()
