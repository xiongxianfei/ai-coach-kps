"""Pinned-file integrity and blank-record checks; not tests of scientific truth."""
from pathlib import Path
import hashlib
import json
import unittest
import sys
import tempfile
import shutil
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import validate

class PackageIntegrityTests(unittest.TestCase):
    def test_06_original_license_and_disclosed_validator_adaptation(self):
        lock=json.loads((ROOT/'upstream-lock.json').read_text())
        self.assertEqual('unchanged copy',lock['files']['LICENSE']['reuse'])
        entry=lock['files']['validate.py']
        self.assertIn('locally adapted',entry['reuse'])
        self.assertEqual('18e7e9a7eb86ace86a1f8fa31f7772b182b488ab0a5ab10c3fce2a2ea4e70f50',entry['upstream_sha256'])
        self.assertNotEqual(entry['sha256'],entry['upstream_sha256'])
        for name in ('validate.py','LICENSE'):
            self.assertEqual(lock['files'][name]['sha256'],hashlib.sha256((ROOT/name).read_bytes()).hexdigest())
    def test_07_core_document_link_adaptations_disclosed(self):
        lock=json.loads((ROOT/'upstream-lock.json').read_text())
        for name in ('docs/authoring.md','docs/templates.md'):
            self.assertIn('link',lock['files'][name]['reuse'])
            self.assertIn('upstream_sha256',lock['files'][name])
            self.assertEqual(lock['files'][name]['sha256'],hashlib.sha256((ROOT/name).read_bytes()).hexdigest())
            self.assertNotEqual(lock['files'][name]['sha256'],lock['files'][name]['upstream_sha256'])
    def test_11_learning_records_remain_private_and_blank(self):
        record=json.loads((ROOT/'data/session-record-template.json').read_text())
        self.assertEqual('blank_template',record['record_kind'])
        self.assertEqual('planned',record['attempts'][0]['state'])

class LearningNoteTemplateTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        shutil.copytree(ROOT/'templates',self.root/'templates')

    def template_errors(self):
        return [e for e in validate.validate(self.root)['errors']
                if e['file'].startswith('templates/')]

    def test_copyable_templates_keep_working_links_without_knowledge_summaries(self):
        self.assertEqual([],self.template_errors())

    def test_summary_exception_does_not_extend_to_other_documents_or_objects(self):
        text='---\nlanguage: "KPS 9.x"\n---\n\n# Other document\n'
        (self.root/'templates/other.md').write_text(text)
        path=self.root/'templates/learning-notes/learning-notes.md'
        path.write_text(path.read_text().replace('language:', 'type: "model"\nlanguage:'))
        errors=self.template_errors()
        for name in ('templates/other.md','templates/learning-notes/learning-notes.md'):
            self.assertTrue(any(e['file']==name and e['code']=='local-summary' for e in errors),errors)

    def test_template_title_and_link_checks_remain_active(self):
        path=self.root/'templates/learning-notes/learning-notes.md'
        path.write_text(path.read_text().replace('# Learning notes','Learning notes').replace('stages/01-stage-name.md','stages/missing.md'))
        errors=self.template_errors()
        self.assertTrue(any(e['code']=='h1' for e in errors),errors)
        self.assertTrue(any('missing.md' in e['detail'] for e in errors),errors)

if __name__=='__main__': unittest.main(verbosity=2)
