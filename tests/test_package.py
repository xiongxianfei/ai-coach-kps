"""Pinned-file integrity and blank-record checks; not tests of scientific truth."""
from pathlib import Path
import hashlib
import json
import unittest
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))

class PackageIntegrityTests(unittest.TestCase):
    def test_06_original_tooling_and_license_preserved(self):
        lock=json.loads((ROOT/'upstream-lock.json').read_text())
        for name in ('validate.py','LICENSE'):
            self.assertEqual('unchanged copy',lock['files'][name]['reuse'])
            self.assertEqual(lock['files'][name]['sha256'],hashlib.sha256((ROOT/name).read_bytes()).hexdigest())
    def test_07_core_document_link_adaptations_disclosed(self):
        lock=json.loads((ROOT/'upstream-lock.json').read_text())
        for name in ('AUTHORING.md','TEMPLATES.md'):
            self.assertIn('link',lock['files'][name]['reuse'])
            self.assertIn('upstream_sha256',lock['files'][name])
            self.assertEqual(lock['files'][name]['sha256'],hashlib.sha256((ROOT/name).read_bytes()).hexdigest())
            self.assertNotEqual(lock['files'][name]['sha256'],lock['files'][name]['upstream_sha256'])
    def test_11_learning_records_remain_private_and_blank(self):
        record=json.loads((ROOT/'data/session-record-template.json').read_text())
        self.assertEqual('blank_template',record['record_kind'])
        self.assertEqual('planned',record['attempts'][0]['state'])

if __name__=='__main__': unittest.main(verbosity=2)
