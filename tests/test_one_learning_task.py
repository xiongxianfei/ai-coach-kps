"""One-task authoring and record-linkage checks; no claim of learning efficacy."""
import copy
import json
from pathlib import Path
import unittest
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.check_learning_plan import inspect_plan
from tools.check_record import inspect_record

class NextTaskDeclarationTests(unittest.TestCase):
    def sample(self):return json.loads((ROOT/'data/two-level-learning-plan-example.json').read_text())
    def test_constructed_example_has_one_task(self):
        x=self.sample();r=inspect_plan(x);self.assertTrue(r['ok'],r['errors'])
        self.assertEqual(1,r['counts']['next_tasks'])
    def test_existing_plan_without_field_remains_valid(self):
        x=self.sample();del x['next_task'];r=inspect_plan(x)
        self.assertTrue(r['ok'],r['errors']);self.assertEqual(0,r['counts']['next_tasks'])
    def test_unknown_stage_rejected(self):
        x=self.sample();x['next_task']['stage_id']='unknown';r=inspect_plan(x)
        self.assertFalse(r['ok']);self.assertIn('next_task: stage_id',str(r['errors']))
    def test_empty_output_rejected(self):
        x=self.sample();x['next_task']['observable_output']='';r=inspect_plan(x)
        self.assertFalse(r['ok']);self.assertIn('next_task.observable_output',str(r['errors']))
    def test_unbounded_payload_rejected(self):
        x=self.sample();x['next_task']=[x['next_task'],copy.deepcopy(x['next_task'])]
        r=inspect_plan(x);self.assertFalse(r['ok']);self.assertIn('next_task: expected object',str(r['errors']))
    def test_invented_results_not_supported(self):
        x=self.sample();x['next_task']['mastered']=True
        r=inspect_plan(x);self.assertFalse(r['ok']);self.assertIn('unsupported field mastered',str(r['errors']))
    def test_blank_template_cannot_assert_selection(self):
        x=json.loads((ROOT/'data/two-level-learning-plan-template.json').read_text())
        x['next_task']=self.sample()['next_task'];r=inspect_plan(x)
        self.assertFalse(r['ok']);self.assertIn('blank template',str(r['errors']))
    def test_read_only(self):
        x=self.sample();before=copy.deepcopy(x);inspect_plan(x);self.assertEqual(before,x)

class SessionTaskLinkTests(unittest.TestCase):
    def blank(self):return json.loads((ROOT/'data/session-record-template.json').read_text())
    def test_old_session_without_optional_fields(self):
        r=self.blank()
        for key in ('learning_task_id','plan_id','plan_version','learning_stage_id'):r.pop(key)
        self.assertTrue(inspect_record(r)['ok'])
    def test_standalone_task_identifier(self):
        r=self.blank();r['learning_task_id']='day1-sample';self.assertTrue(inspect_record(r)['ok'])
    def test_valid_linked_planned_record(self):
        r=self.blank();r.update(plan_id='my-plan',plan_version=1,learning_stage_id='normalize',learning_task_id='day1-units')
        self.assertTrue(inspect_record(r)['ok'])
    def test_missing_parent_plan_rejected(self):
        r=self.blank();r['learning_stage_id']='normalize'
        self.assertFalse(inspect_record(r)['ok'])
    def test_invalid_version_rejected(self):
        r=self.blank();r.update(plan_id='my-plan',plan_version=True)
        self.assertFalse(inspect_record(r)['ok'])
    def test_unknown_external_link_not_verified(self):
        r=self.blank();r.update(plan_id='unverified',plan_version=2,learning_stage_id='not-checked')
        self.assertTrue(inspect_record(r)['ok'])  # checker cannot inspect private plan file
    def test_no_mastery_or_observed_claim(self):
        r=self.blank();r['learning_task_id']='day1-units';out=inspect_record(r)
        self.assertTrue(out['ok']);self.assertEqual(0,out['counts']['observed'])
        self.assertNotIn('mastery',out)
