"""Publication and constructed-record regressions, not tests of human learning."""
from pathlib import Path
import copy
from fractions import Fraction
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import validate as v
from tools import check_domain, build_navigation, check_record

class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)/'domain'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__','.pytest_cache','*.pyc'))
    def tearDown(self):self.temp.cleanup()
    def mutate(self,name,func):
        p=self.root/name;m,b=v.split_frontmatter(p.read_text());func(m)
        p.write_text('---\n'+'\n'.join(k+': '+json.dumps(x,ensure_ascii=False) for k,x in m.items())+'\n---\n\n'+b)
    def has_error(self,prefix):self.assertTrue(any(e.startswith(prefix) for e in check_domain.inspect(self.root)),check_domain.inspect(self.root))
    def test_package_alignment(self):self.assertEqual([],check_domain.inspect(self.root))
    def test_missing_source_alignment(self):
        self.mutate('concepts/feedback.md',lambda m:m.pop('source_alignment'));self.has_error('missing-alignment')
    def test_missing_locator(self):
        self.mutate('concepts/feedback.md',lambda m:m['source_alignment'][0].update(locator=''));self.has_error('alignment-locator')
    def test_unknown_reference(self):
        self.mutate('concepts/feedback.md',lambda m:m['source_alignment'][0].update(reference='unknown'));self.has_error('alignment-target')
    def test_reference_must_be_dependency(self):
        self.mutate('concepts/feedback.md',lambda m:m.update(references=[]));self.has_error('alignment-dependency')
    def test_wrong_alignment_relation(self):
        self.mutate('models/assessment-triangle.md',lambda m:m['source_alignment'][0].update(relation='endorsed-by-source'));self.has_error('alignment-relation')
    def test_no_unsupported_review(self):
        self.mutate('principles/testing-effect.md',lambda m:m.update(reviewed='2026-10-12',status='active'));self.has_error('unsupported-promotion')
    def test_application_authorship(self):
        self.mutate('practices/self-regulated-learning-with-ai.md',lambda m:m.update(basis_kind='experimentally established intervention'));self.has_error('application-authorship')
    def test_adult_scope(self):
        self.mutate('practices/self-regulated-learning-with-ai.md',lambda m:m.update(primary_audience='all children'));self.has_error('audience')
    def test_steps_first(self):
        self.mutate('practices/self-regulated-learning-with-ai.md',lambda m:m.update(practice_format='legacy'));self.has_error('practice-format')
    def test_blank_current_record(self):
        p=self.root/'practices/formative-assessment-with-ai.md';p.write_text(p.read_text().replace('not recorded','proven successful'));self.has_error('fabricated-practice-record')
    def test_reference_access(self):
        self.mutate('references/pieschl-2009-metacognitive-calibration.md',lambda m:m.update(access_extent=''));self.has_error('reference-field')
    def test_original_author_correct(self):
        d=v.parse(self.root/'references/pieschl-2009-metacognitive-calibration.md');self.assertEqual('Stephanie Pieschl',d.meta['creator'])
    def test_upstream_unchanged(self):
        p=self.root/'validate.py';p.write_text(p.read_text()+'\n# changed\n');self.has_error('upstream-digest')
    def test_no_writer_ci(self):
        p=self.root/'.github/workflows/checks.yml';p.write_text(p.read_text().replace('contents: read','contents: write'));self.has_error('unsafe-permanent-ci')
    def test_no_automatic_summary_refresh(self):
        p=self.root/'.github/workflows/checks.yml';p.write_text(p.read_text()+'\n# --accept-reviewed-summaries\n');self.has_error('unsafe-permanent-ci')
    def test_no_temporary_payload(self):
        (self.root/'.coach-build').mkdir();self.has_error('temporary-payload')
    def test_claim_locator_required(self):
        p=self.root/'data/claims.json';d=json.loads(p.read_text());d[0]['locator']='';p.write_text(json.dumps(d));self.has_error('claim-field')
    def test_claim_link_to_practice(self):
        p=self.root/'data/claims.json';d=json.loads(p.read_text());d[0]['practices']=['unknown'];p.write_text(json.dumps(d));self.has_error('claim-practice')
    def test_navigation_matches(self):
        for name,text in build_navigation.generate(self.root).items():self.assertEqual(text,(self.root/name).read_text(),name)
    def test_practice_and_library_counts(self):
        docs,refs=build_navigation.collect(self.root)
        self.assertEqual(18,len(docs));self.assertEqual(15,len(refs))
        practices=[d for _,d in docs if d.meta['type']=='practice']
        self.assertEqual(4,len(practices));self.assertEqual(22,sum(len(d.meta['stage_titles']) for d in practices))
    def test_no_uninspected_named_model(self):
        paths=[p.name for p in (self.root/'models').glob('*.md')]
        self.assertEqual(['assessment-triangle.md','cognitive-apprenticeship.md'],sorted(paths))
    def test_example_arithmetic(self):
        a=Fraction(6,750)*100;b=Fraction(720,100)/1000*100
        self.assertEqual(Fraction(4,5),a);self.assertEqual(Fraction(18,25),b);self.assertLess(b,a)

class RecordTests(unittest.TestCase):
    def template(self):return json.loads((ROOT/'data/session-record-template.json').read_text())
    def observed(self):
        r=self.template();r.update(record_kind='constructed_example',task='Compare a constructed quantity.',criterion='Use the declared common-unit calculation.')
        r['attempts'][0].update(state='observed',attempted_at='2026-10-12T12:00:00+00:00',original_response='Synthetic response, not actual learner data.',answer_help='none',answer_visible_during_attempt=False,claimed_independent=True,same_item_seen_before=False)
        return r
    def test_template_is_unobserved(self):
        x=check_record.inspect_record(self.template());self.assertTrue(x['ok']);self.assertEqual(0,x['counts']['observed'])
    def test_observed_declarations(self):self.assertTrue(check_record.inspect_record(self.observed())['ok'])
    def test_missing_response_is_not_result(self):
        r=self.observed();r['attempts'][0]['original_response']=None;self.assertFalse(check_record.inspect_record(r)['ok'])
    def test_planned_cannot_have_score(self):
        r=self.template();r['attempts'][0]['criterion_judgment']='meets';self.assertFalse(check_record.inspect_record(r)['ok'])
    def test_hint_not_independent(self):
        r=self.observed();r['attempts'][0]['answer_help']='hint';self.assertFalse(check_record.inspect_record(r)['ok'])
    def test_unknown_help_not_independent(self):
        r=self.observed();r['attempts'][0]['answer_help']='unknown';self.assertFalse(check_record.inspect_record(r)['ok'])
    def test_answer_visible_not_independent(self):
        r=self.observed();r['attempts'][0]['answer_visible_during_attempt']=True;self.assertFalse(check_record.inspect_record(r)['ok'])
    def test_access_support_allowed(self):
        r=self.observed();r['attempts'][0]['access_accommodations']=['screen reader'];self.assertTrue(check_record.inspect_record(r)['ok'])
    def test_prior_study_does_not_preclude_recall(self):
        r=self.observed();r['attempts'][0]['same_item_seen_before']=True;self.assertTrue(check_record.inspect_record(r)['ok'])
    def test_ai_only_is_not_verified(self):
        r=self.observed();r['attempts'][0].update(verified=True,verification_basis='ai_only',verification_locator='AI response',criterion_judgment='meets');self.assertFalse(check_record.inspect_record(r)['ok'])
    def test_ai_judgment_can_stay_unverified(self):
        r=self.observed();r['attempts'][0].update(verification_basis='ai_only',criterion_judgment='meets');x=check_record.inspect_record(r);self.assertTrue(x['ok']);self.assertTrue(x['warnings'])
    def test_source_check_requires_locator(self):
        r=self.observed();r['attempts'][0].update(verified=True,verification_basis='source_checked',criterion_judgment='meets');self.assertFalse(check_record.inspect_record(r)['ok'])
    def test_declared_verification_not_truth_proof(self):
        r=self.observed();r['attempts'][0].update(verified=True,verification_basis='deterministic_check',verification_locator='Synthetic arithmetic assertion in tests',criterion_judgment='meets');self.assertTrue(check_record.inspect_record(r)['ok'])
    def test_delay_unknown_is_not_delayed_proof(self):
        r=self.observed();r['attempts'][0].update(phase='delayed_check',delay_days=None);x=check_record.inspect_record(r);self.assertTrue(x['ok']);self.assertTrue(any('delay unknown' in w for w in x['warnings']))
    def test_immediate_not_delayed(self):
        r=self.observed();r['attempts'][0].update(phase='delayed_check',delay_days=0);self.assertFalse(check_record.inspect_record(r)['ok'])
    def test_transfer_requires_description_for_interpretation(self):
        r=self.observed();r['attempts'][0]['phase']='transfer_check';x=check_record.inspect_record(r);self.assertTrue(x['ok']);self.assertTrue(any('context change' in w for w in x['warnings']))
    def test_no_automatic_mastery(self):
        r=self.observed();r['mastery_decision']='mastered';self.assertFalse(check_record.inspect_record(r)['ok'])
    def test_timestamp_required(self):
        r=self.observed();r['attempts'][0]['attempted_at']='tomorrow';self.assertFalse(check_record.inspect_record(r)['ok'])
    def test_unattempted_remains_missing(self):
        r=self.template();r['attempts'][0]['state']='not_attempted';x=check_record.inspect_record(r);self.assertTrue(x['ok']);self.assertEqual(0,x['counts']['observed'])
    def test_no_mutation_of_original(self):
        r=self.observed();before=copy.deepcopy(r);check_record.inspect_record(r);self.assertEqual(before,r)
    def test_boolean_not_numeric_delay(self):
        r=self.observed();r['attempts'][0]['delay_days']=True;self.assertFalse(check_record.inspect_record(r)['ok'])
    def test_invalid_record_fails_cleanly(self):self.assertFalse(check_record.inspect_record([])['ok'])

if __name__=='__main__':unittest.main(verbosity=2)
