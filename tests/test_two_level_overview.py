"""Authored planning-contract tests, not evidence of learning efficacy."""
from pathlib import Path
import copy
import json
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import validate
from tools.check_learning_plan import inspect_plan

P='practices/concept-mapping-and-instructional-sequencing-with-ai.md'
PID='ai-coach:practice:concept-mapping-and-instructional-sequencing-with-ai'

class PlanRecordTests(unittest.TestCase):
    def example(self):return json.loads((ROOT/'data/two-level-learning-plan-example.json').read_text())
    def template(self):return json.loads((ROOT/'data/two-level-learning-plan-template.json').read_text())
    def invalid(self,p,fragment):
        result=inspect_plan(p)
        self.assertFalse(result['ok'],result)
        self.assertTrue(any(fragment in e for e in result['errors']),result)
    def test_blank_template_has_no_observation_or_mastery(self):
        p=self.template();out=inspect_plan(p)
        self.assertTrue(out['ok']);self.assertEqual(out['counts']['stages'],0)
        self.assertEqual('not_recorded',p['learner_agreement'])
        self.assertNotIn('mastery',out);self.assertTrue(out['warnings'])
    def test_constructed_example(self):self.assertTrue(inspect_plan(self.example())['ok'])
    def test_template_cannot_be_claimed_complete(self):
        p=self.template();p['record_kind']='proposed_plan';self.invalid(p,'expected nonempty text')
    def test_panorama_missing(self):
        p=self.example();p['panorama']['regions']=[];self.invalid(p,'panorama.regions: cannot be empty')
    def test_goal_not_located(self):
        p=self.example();p['goal']['panorama_region_ids']=[];self.invalid(p,'goal.panorama_region_ids: cannot be empty')
    def test_map_only_labels(self):
        p=self.example();p['goal_map']['relations']=[];self.invalid(p,'at least one proposition')
    def test_missing_focus_question(self):
        p=self.example();p['goal_map']['focus_question']='';self.invalid(p,'focus_question')
    def test_missing_relation_label(self):
        p=self.example();p['goal_map']['relations'][0]['relation']='';self.invalid(p,'expected nonempty text')
    def test_concept_must_link_to_panorama(self):
        p=self.example();p['goal_map']['concepts'][0]['panorama_region_ids']=['absent'];self.invalid(p,'unknown id')
    def test_relation_endpoint(self):
        p=self.example();p['goal_map']['relations'][0]['target']='absent';self.invalid(p,'unknown target')
    def test_conceptual_cycle_is_not_a_prerequisite_cycle(self):
        p=self.example();r=copy.deepcopy(p['goal_map']['relations'][0]);r.update(source='quantity',target='conversion',relation='is represented equivalently through')
        p['goal_map']['relations'].append(r)
        self.assertTrue(inspect_plan(p)['ok'])
    def test_stage_required_before_cycle(self):
        p=self.example();p['learning_stages'][0].update(requires_stage_ids=['integrate'],dependency_rationale='Constructed contradictory order')
        self.invalid(p,'circular required-before')
    def test_stage_unknown_predecessor(self):
        p=self.example();p['learning_stages'][2]['requires_stage_ids']=['absent'];self.invalid(p,'unknown id')
    def test_predecessor_must_be_earlier(self):
        p=self.example();p['learning_stages'][2]['order']=1;p['learning_stages'][0]['order']=3;self.invalid(p,'not earlier')
    def test_order_boolean_is_not_integer(self):
        p=self.example();p['learning_stages'][0]['order']=True;self.invalid(p,'positive integer')
    def test_duplicate_stage_id(self):
        p=self.example();p['learning_stages'][1]['id']='normalize';self.invalid(p,'duplicate id')
    def test_reordering_preserves_ids(self):
        p=self.example();before={x['id'] for x in p['learning_stages']}
        p['learning_stages'][0]['order']=2;p['learning_stages'][1]['order']=1
        self.assertTrue(inspect_plan(p)['ok']);self.assertEqual(before,{x['id'] for x in p['learning_stages']})
    def test_prerequisite_requires_probe(self):
        p=self.example();p['prerequisite_hypotheses'][0]['probe']='';self.invalid(p,'prerequisite.probe')
    def test_supported_hypothesis_needs_evidence(self):
        p=self.example();p['prerequisite_hypotheses'][0]['status']='supported';self.invalid(p,'evidence_refs: cannot be empty')
    def test_rejected_hypothesis_not_used(self):
        p=self.example();p['prerequisite_hypotheses'][0]['status']='rejected';self.invalid(p,'rejected prerequisite')
    def test_stage_dependency_needs_own_rationale(self):
        p=self.example();p['learning_stages'][2]['dependency_rationale']=None;self.invalid(p,'dependency_rationale')
    def test_check_requires_criterion(self):
        p=self.example();p['learning_stages'][0]['check']['criterion']='';self.invalid(p,'check.criterion')
    def test_adaptation_trigger_required(self):
        p=self.example();p['learning_stages'][0]['adaptation_trigger']='';self.invalid(p,'adaptation_trigger')
    def test_agreement_not_fabricated(self):
        p=self.example();p['learner_agreement']='agreed';self.invalid(p,'agreement_evidence')
    def test_unknown_source_cannot_support_claim(self):
        p=self.example();p['panorama']['regions'][0]['source_status']='source_supported';self.invalid(p,'inspected source')
    def test_no_automatic_mastery_field(self):
        p=self.example();p['mastery']='complete';self.invalid(p,'unsupported field mastery')
    def revision(self,basis):
        p=self.example();p['version']=2;p['revision_log']=[{'from_version':1,'to_version':2,'change':'Constructed reduction of scope','reason':'Example only','basis':basis,'evidence_refs':[],'affected_stage_ids':['normalize']}];return p
    def test_performance_revision_requires_observation_reference(self):self.invalid(self.revision('performance_evidence'),'evidence_refs: cannot be empty')
    def test_learner_choice_need_not_invent_performance(self):self.assertTrue(inspect_plan(self.revision('learner_choice'))['ok'])
    def test_revision_version_increases(self):
        p=self.revision('learner_choice');p['revision_log'][0]['to_version']=1;self.invalid(p,'version must increase')
    def test_history_can_keep_retired_stage_id(self):
        p=self.revision('source_review');p['revision_log'][0]['affected_stage_ids']=['retired-stage'];self.assertTrue(inspect_plan(p)['ok'])
    def test_checker_does_not_mutate(self):
        p=self.example();before=copy.deepcopy(p);inspect_plan(p);self.assertEqual(before,p)
    def test_malformed_inputs_fail_cleanly(self):
        for x in (None,[],False,'text',{}):
            with self.subTest(x=x):self.assertFalse(inspect_plan(x)['ok'])
        for key in ('record_kind','learner_agreement'):
            p=self.example();p[key]=[];self.assertFalse(inspect_plan(p)['ok'])
        p=self.example();p['learning_stages']=[None];self.assertFalse(inspect_plan(p)['ok'])
    def test_state_is_not_a_learning_outcome(self):
        p=self.example();p['record_kind']='validated_progression';self.invalid(p,'invalid record_kind')

class PracticeIntegrationTests(unittest.TestCase):
    def test_planning_is_first_entry(self):
        s=(ROOT/'README.md').read_text()
        self.assertLess(s.index('concept-mapping-and-instructional-sequencing-with-ai.md'),s.index('self-regulated-learning-with-ai.md'))
    def test_four_existing_practices_link_planning(self):
        for f in ('self-regulated-learning-with-ai','formative-assessment-with-ai','retrieval-and-distributed-practice-with-ai','evaluation-of-ai-assisted-learning'):
            doc=validate.parse(ROOT/'practices'/f'{f}.md')
            self.assertIn(PID,doc.meta.get('uses_practices',[]));self.assertIn('concept-mapping-and-instructional-sequencing-with-ai.md',doc.links)
    def test_existing_stage_anchors_retained(self):
        doc=validate.parse(ROOT/'practices/self-regulated-learning-with-ai.md')
        self.assertEqual(['Stage1 Define a learning goal and constraints','Stage2 Establish a source and a starting response','Stage3 Agree on assistance and begin instruction','Stage4 Attempt explain and revise with feedback','Stage5 Check performance with less assistance','Stage6 Plan retention transfer and a learner owned record'],doc.meta['stage_titles'])
    def test_no_recursive_composition(self):
        self.assertNotIn(PID,validate.parse(ROOT/'practices/self-regulated-learning-with-ai.md').meta.get('composes',[]))
    def test_planning_remains_authored_and_provisional(self):
        doc=validate.parse(ROOT/P)
        self.assertIn('KPS',doc.meta['basis_kind']);self.assertEqual('provisional',doc.meta['evidence_status']);self.assertIsNone(doc.meta['reviewed']);self.assertEqual(6,len(doc.meta['stage_titles']))
    def test_no_new_fake_model(self):
        self.assertEqual(['assessment-triangle.md','cognitive-apprenticeship.md'],sorted(p.name for p in (ROOT/'models').glob('*.md')))
    def test_terminology_and_sources(self):
        for path in ('concepts/concept-map.md','methods/concept-mapping.md'):
            doc=validate.parse(ROOT/path)
            self.assertTrue(doc.meta['source_alignment'][0]['locator'])
        text=(ROOT/P).read_text()
        self.assertIn('provisional instructional sequence',text)
        self.assertIn('national-research-council-2007-learning-progressions.md',text)
    def test_private_plan_is_not_mandatory(self):
        text=(ROOT/'guides/LEARNING-WORKFLOW.md').read_text()
        self.assertIn('A plain private table is sufficient',text)
        self.assertIn('does not write',text)

if __name__=='__main__':unittest.main(verbosity=2)
