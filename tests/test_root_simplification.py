"""Root layout checks for the v0.3.0 domain package; not tests of scientific truth."""
from pathlib import Path
import hashlib
import json
import unittest
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import validate
from tools import build_navigation

ROOT_FILES={'.gitignore','AGENTS.md','AUTHORING.md','CHANGELOG.md',
            'CONTRIBUTING.md','LICENSE','NOTICE.md','README.md','TEMPLATES.md',
            'publication.json','summary-dependencies.json','test_validate.py',
            'upstream-lock.json','validate.py'}
RETIRED={'ONE-LEARNING-TASK.md','LEARNING-PLAN.md','RECORDS.md','WORKED-EXAMPLE.md',
         'SCOPE.md','ALIGNMENT.md','CHECKS.md','COMPATIBILITY.md','NAVIGATION.md',
         'DIAGRAMS.md','REVIEW.md','INDEX.md','PRACTICE-MAP.md','EVIDENCE-MAP.md',
         'TERMINOLOGY-MAP.md','REVIEW-QUEUE.md','knowledge-graph.json'}
GENERATED={'INDEX.md','PRACTICE-MAP.md','EVIDENCE-MAP.md','TERMINOLOGY-MAP.md',
           'REVIEW-QUEUE.md','knowledge-graph.json'}

class RootSimplificationTests(unittest.TestCase):
    def test_01_root_has_only_required_files(self):
        root={p.name for p in ROOT.iterdir() if p.is_file() and p.name!='MANIFEST.sha256'}
        self.assertEqual(ROOT_FILES,root)
    def test_02_old_root_paths_are_gone(self):
        self.assertTrue(RETIRED.isdisjoint(ROOT_FILES))
        self.assertTrue(all(not (ROOT/x).exists() for x in RETIRED))
    def test_03_generated_views_are_together(self):
        self.assertEqual(GENERATED,{p.name for p in (ROOT/'generated').iterdir()})
        for path,text in build_navigation.generate(ROOT).items():
            self.assertEqual(text,(ROOT/path).read_text(),path)
    def test_04_scientific_library_is_intact(self):
        counts={'concepts':7,'principles':3,'models':2,'methods':4,'practices':5}
        for role,n in counts.items():self.assertEqual(n,len(list((ROOT/role).glob('*.md'))))
        self.assertEqual(17,sum(1 for p in (ROOT/'references').glob('*.md')
                                if validate.parse(p).meta.get('type')=='reference'))
    def test_05_practice_stage_identity_is_preserved(self):
        self.assertEqual(28,sum(len(validate.parse(p).meta['stage_titles']) for p in
                                (ROOT/'practices').glob('*.md')))
    def test_06_original_tooling_and_license_preserved(self):
        lock=json.loads((ROOT/'upstream-lock.json').read_text())
        self.assertEqual('10.2.0',lock['core_version'])
        for name in ('validate.py','test_validate.py','LICENSE'):
            self.assertEqual('unchanged copy',lock['files'][name]['reuse'])
            self.assertEqual(lock['files'][name]['sha256'],hashlib.sha256((ROOT/name).read_bytes()).hexdigest())
    def test_07_core_document_link_adaptations_disclosed(self):
        lock=json.loads((ROOT/'upstream-lock.json').read_text())
        for name in ('AUTHORING.md','TEMPLATES.md'):
            self.assertIn('link',lock['files'][name]['reuse'])
            self.assertIn('upstream_sha256',lock['files'][name])
            self.assertEqual(lock['files'][name]['sha256'],hashlib.sha256((ROOT/name).read_bytes()).hexdigest())
            self.assertNotEqual(lock['files'][name]['sha256'],lock['files'][name]['upstream_sha256'])
    def test_08_scientific_and_scope_sections_remain(self):
        s=(ROOT/'docs/SCIENTIFIC-POLICY.md').read_text()
        for heading in ('## Admission by role','## Alignment records','## Included work',
                        '## Roles and consent','## Research scope'):self.assertIn(heading,s)
    def test_09_checks_and_compatibility_remain(self):
        s=(ROOT/'docs/VALIDATION.md').read_text()
        for heading in ('## Commands','## Check boundaries','## Version declarations',
                        '## Root layout migration for 0 3 0'):self.assertIn(heading,s)
    def test_10_learning_workflow_retains_both_jobs(self):
        s=(ROOT/'guides/LEARNING-WORKFLOW.md').read_text()
        self.assertIn('## Find the next task',s)
        self.assertIn('## Begin with the three artifacts',s)
        self.assertIn('A plain private table is sufficient',s)
        self.assertIn('not a learner response',s)
    def test_11_learning_records_remain_private_and_blank(self):
        s=(ROOT/'guides/SESSION-RECORDS.md').read_text()
        self.assertIn('Keep the original response',s)
        self.assertIn('not a validated measurement model',s)
        record=json.loads((ROOT/'data/session-record-template.json').read_text())
        self.assertEqual('blank_template',record['record_kind'])
        self.assertEqual('planned',record['attempts'][0]['state'])
    def test_12_generated_link_paths_are_rebased(self):
        index=(ROOT/'generated/INDEX.md').read_text()
        self.assertIn('(../practices/',index)
        e=(ROOT/'generated/EVIDENCE-MAP.md').read_text()
        self.assertIn('(../references/',e)
        self.assertIn('(../data/claims.json)',e)
    def test_13_root_migration_explicit_about_external_links(self):
        s=(ROOT/'docs/VALIDATION.md').read_text()
        for old in RETIRED:self.assertIn('`'+old+'`',s)
        self.assertIn('will not automatically redirect',s)
    def test_14_pinned_core_and_version_identified(self):
        p=json.loads((ROOT/'publication.json').read_text())
        self.assertEqual('0.3.0',p['version'])
        self.assertEqual('10.2.0',p['based_on_core'])
        self.assertEqual('9.1.0',p['minimum_validator'])
        self.assertEqual('steps-first-v1',p['practice_format'])
    def test_15_reader_can_find_original_five_practices(self):
        s=(ROOT/'README.md').read_text()
        for path in sorted((ROOT/'practices').glob('*.md')):
            self.assertIn('practices/'+path.name,s)
        self.assertIn('guides/LEARNING-WORKFLOW.md',s)
        self.assertIn('generated/INDEX.md',s)
    def test_16_only_one_summary_and_heading_in_merged_docs(self):
        for name in ('docs/SCIENTIFIC-POLICY.md','docs/VALIDATION.md',
                     'docs/READING-AND-DIAGRAMS.md','guides/LEARNING-WORKFLOW.md'):
            d=validate.parse(ROOT/name)
            self.assertEqual(1,sum(level==1 for level,_ in d.headings))
            self.assertEqual(1,sum(title=='Summary' for _,title in d.headings))
            self.assertEqual(1,sum(title=='Key takeaway' for _,title in d.headings))
    def test_17_no_unsupported_learning_outcome_promoted(self):
        self.assertFalse(json.loads((ROOT/'publication.json').read_text())['independent_review'])
        self.assertIn('not recorded',(ROOT/'practices/self-regulated-learning-with-ai.md').read_text())
    def test_18_source_review_is_separate_from_ci_validation(self):
        review=(ROOT/'docs/REVIEW.md').read_text()
        checks=(ROOT/'docs/VALIDATION.md').read_text()
        self.assertIn('## Conflicting and indirect evidence',review)
        self.assertIn('structural',checks.lower())
    def test_19_references_register_points_to_review(self):
        s=(ROOT/'references/README.md').read_text()
        self.assertIn('docs/REVIEW.md',s)

if __name__=='__main__': unittest.main(verbosity=2)
