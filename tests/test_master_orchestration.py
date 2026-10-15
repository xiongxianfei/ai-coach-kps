"""Editorial contract tests; neither learner trials nor tests of scientific efficacy."""
from pathlib import Path
from fractions import Fraction
import copy
import json
import re
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import validate
from tools import build_navigation, check_domain

MASTER = 'practices/ai-assisted-learning-orchestration.md'
MASTER_ID = 'ai-coach:practice:ai-assisted-learning-orchestration'
SPECIALISTS = {
    'concept-mapping-and-instructional-sequencing-with-ai': 6,
    'self-regulated-learning-with-ai': 6,
    'formative-assessment-with-ai': 5,
    'retrieval-and-distributed-practice-with-ai': 5,
    'evaluation-of-ai-assisted-learning': 6,
}
STAGES = [
    'Stage1 Establish the overall target and learning agreement',
    'Stage2 Orient to the subject and propose learning stages',
    'Stage3 Select one current learning task',
    'Stage4 Teach question and preserve the learner response',
    'Stage5 Assess the response and adapt assistance',
    'Stage6 Evaluate stage evidence and revise the programme',
    'Stage7 Retrieve review and resume or close',
]


def section(text, heading):
    """Extract a top-level section without requiring another knowledge file."""
    match = re.search(r'^## ' + re.escape(heading) + r'\n(.*?)(?=^## |\Z)',
                      text, flags=re.M | re.S)
    return match.group(1) if match else ''


def inline_contract_errors(text):
    """Mechanical early-warning checks, not a measure of self-containment quality."""
    errors = []
    for heading in STAGES:
        body = section(text, heading)
        visible = re.sub(r'```[^\n]*\n.*?```', '', body, flags=re.S)
        if not re.search(r'^\d+\. \S', visible, flags=re.M):
            errors.append('missing-inline-actions:' + heading)
        if re.search(r'\]\([^)]*\.md(?:#[^)]*)?\)', body):
            errors.append('stage-link-dependency:' + heading)
    if "wait for the learner's response" not in section(text, STAGES[3]).lower():
        errors.append('missing-response-wait')
    if 'overall target' not in section(text, 'Keep the levels distinct').lower():
        errors.append('missing-hierarchy')
    return errors


class MasterContentTests(unittest.TestCase):
    def text(self): return (ROOT / MASTER).read_text(encoding='utf-8')
    def doc(self): return validate.parse(ROOT / MASTER)
    def test_primary_practice_is_master(self):
        pub = json.loads((ROOT/'publication.json').read_text())
        self.assertEqual(MASTER_ID, pub['primary_practice'])
        self.assertEqual('master', self.doc().meta['orchestration_role'])
    def test_seven_steps_first_stages(self):
        self.assertEqual(STAGES, self.doc().meta['stage_titles'])
        self.assertEqual('steps-first-v1', self.doc().meta['practice_format'])
    def test_actions_available_without_specialist_files(self):
        self.assertEqual([], inline_contract_errors(self.text()))
    def test_link_only_stage_is_detected(self):
        text = self.text(); body = section(text, STAGES[1])
        text = text.replace(body, '\n[Use planning](other-practice.md)\n', 1)
        errors = inline_contract_errors(text)
        self.assertTrue(any(e.startswith('missing-inline-actions') for e in errors))
        self.assertTrue(any(e.startswith('stage-link-dependency') for e in errors))
    def test_removed_wait_is_detected(self):
        text = self.text().replace("wait for the learner's response", 'proceed automatically')
        self.assertIn('missing-response-wait', inline_contract_errors(text))
    def test_hierarchy_distinguishes_calendar_and_procedure(self):
        s = section(self.text(), 'Keep the levels distinct')
        for term in ['Overall target','Learning stage','Current task','Attempt and assessment',
                     'StageN','Day','plan_id','learning_stage_id','learning_task_id','attempt_id']:
            # Calendar meaning is expressed as “One day” rather than an extra layer.
            if term == 'Day': term = 'day'
            self.assertIn(term, s)
    def test_two_level_orientation_and_prerequisite_limits_inline(self):
        s = section(self.text(), STAGES[1])
        for term in ['panorama','concept map','prerequisite','hypothesis','stable ID','criterion']:
            self.assertIn(term, s)
    def test_one_task_card_is_inline(self):
        s = section(self.text(), STAGES[2])
        for term in ['Parent','Current task','Knowledge/input','Response','Criterion','Conditions','Stop or split']:
            self.assertIn(term, s)
    def test_real_reply_not_simulated(self):
        s = section(self.text(), STAGES[3])
        self.assertIn('wait for the learner', s)
        self.assertIn('Do not generate both sides', s)
        self.assertIn('NOT RECORDED', s)
    def test_explanation_allowed_and_assistance_preserved(self):
        s = section(self.text(), STAGES[3])
        self.assertIn('full explanation', s)
        self.assertIn('Do not treat the resulting assisted answer as independent evidence', s)
        self.assertIn('actual', self.text().lower())
    def test_knowledge_first_not_mandatory_for_retrieval(self):
        s = section(self.text(), STAGES[3])
        self.assertIn('In retrieval', s)
        self.assertIn('withhold the solution', s)
    def test_worked_example_is_not_clean_unexposed_test(self):
        s = section(self.text(), STAGES[3])
        self.assertIn('has now seen the answer', s)
        self.assertIn('fresh', s)
        self.assertEqual(Fraction(4), Fraction(12,3))
        self.assertEqual(Fraction(2), Fraction(8,4))
    def test_feedback_has_criterion_and_verification(self):
        s = section(self.text(), STAGES[4])
        for term in ['criterion','verification','unverified','original answer','new attempt']:
            self.assertIn(term, s)
    def test_formative_investigation_is_inline(self):
        s = section(self.text(), STAGES[4])
        self.assertIn('plausible explanations', s)
        self.assertIn('distinguish them', s)
        self.assertIn('Do not infer intelligence', s)
    def test_missing_response_not_failure(self):
        s = section(self.text(), STAGES[4])
        self.assertIn('No reply yet', s)
        self.assertIn('A score or demonstrated failure', s)
    def test_task_stage_target_decisions_are_separate(self):
        s = section(self.text(), STAGES[5])
        self.assertIn('Evidence for one decision does not automatically justify the others', s)
        self.assertIn('Advancing provisionally', s)
        self.assertIn('does not isolate an AI treatment effect', s)
    def test_revision_and_pause_are_not_erasure(self):
        s = section(self.text(), STAGES[5])
        self.assertIn('keep the old plan version', s)
        self.assertIn('not reused', s)
        self.assertIn('does not erase', s)
    def test_retrieval_and_timing_are_inline(self):
        s = section(self.text(), STAGES[6])
        for term in ['put the answer aside','actual interval','No fixed review schedule','missed appointment']:
            self.assertIn(term, s)
    def test_resume_without_ai_memory(self):
        s = section(self.text(), STAGES[6])
        for term in ['resume record','persistent AI memory','not automatically Stage1','calendar']:
            self.assertIn(term, s)
    def test_plain_text_template_is_sufficient(self):
        s = section(self.text(), STAGES[6])
        self.assertIn('Plain text is sufficient', s)
        self.assertIn('Original response / attempt ID / time / actual help: NOT RECORDED', s)
        self.assertIn('No new application or record file is required', s)
    def test_instruction_respects_adult_agency(self):
        s = section(self.text(), 'Entry and learner control')
        for term in ['pause or stop','request direct explanation','private','rules']:
            self.assertIn(term, s)
    def test_scholarship_does_not_validate_whole_workflow(self):
        s = section(self.text(), 'Academic basis and source limits')
        self.assertIn('no cited publication tests this complete programme', s)
        self.assertIn('not a renamed Zimmerman model', s)
    def test_actual_use_summary_is_blank(self):
        s = section(self.text(), 'Current practice summary')
        self.assertEqual(3, s.count('not recorded'))
        self.assertIn('not established', s)
        self.assertIsNone(self.doc().meta['reviewed'])
    def test_optional_links_are_after_operational_stages(self):
        text = self.text()
        self.assertGreater(text.index('## Optional specialist reading'), text.index('## Stage7'))
        self.assertIn('none must be opened', text.lower())
    def test_master_composes_exact_five_specialists(self):
        expected = {'ai-coach:practice:'+p for p in SPECIALISTS}
        self.assertEqual(expected, set(self.doc().meta['composes']))
    def test_children_do_not_contain_master(self):
        for name, n in SPECIALISTS.items():
            d = validate.parse(ROOT/'practices'/f'{name}.md')
            self.assertEqual(n, len(d.meta['stage_titles']))
            self.assertNotIn(MASTER_ID, d.meta.get('composes', []))
    def test_reader_navigation_prioritizes_master(self):
        text = (ROOT/'README.md').read_text()
        self.assertLess(text.index(MASTER), text.index('practices/concept-mapping-'))
        generated = build_navigation.generate(ROOT)
        self.assertIn('Self-contained master entry', generated['docs/INDEX.md'])
        docs, _ = build_navigation.collect(ROOT)
        self.assertEqual(MASTER, docs[0][0])
    def test_specialists_retain_independent_entry(self):
        s = (ROOT/'README.md').read_text()
        for name in SPECIALISTS:self.assertIn('practices/'+name+'.md', s)
        self.assertIn('direct specialist entry', s)
    def test_prior_record_templates_are_still_valid_and_blank(self):
        from tools.check_record import inspect_record
        from tools.check_learning_plan import inspect_plan
        r = json.loads((ROOT/'data/session-record-template.json').read_text())
        p = json.loads((ROOT/'data/two-level-learning-plan-template.json').read_text())
        self.assertTrue(inspect_record(r)['ok'])
        self.assertTrue(inspect_plan(p)['ok'])
        self.assertIsNone(r['attempts'][0]['original_response'])
        self.assertNotIn('programme_mastery', r)
    def test_claim_receivers_include_master_without_new_efficacy_claim(self):
        claims = json.loads((ROOT/'data/claims.json').read_text())
        self.assertEqual(16, len(claims))
        self.assertEqual(8, sum(MASTER_ID in c['practices'] for c in claims))



    def test_adaptive_route_is_visible_and_not_fixed_curriculum(self):
        text = self.text()
        summary = section(text, 'Summary')
        handoff = section(text, 'Default planning handoff')
        self.assertIn('self-assessment and an optional pre-instruction diagnostic', summary)
        for phrase in ('Assess the learner', 'Map the subject',
                       'Propose learning stages', 'Teach and assess', '6. Adapt',
                       'Do not pre-generate', 'high-level'):
            self.assertIn(phrase, handoff)

    def test_pre_instruction_diagnostic_and_self_report_are_distinguished(self):
        entry = section(self.text(), STAGES[0])
        for phrase in ('brief self-assessment', 'pre-instruction baseline response',
                       'original reply', 'prior exposure', 'not failed',
                       'self-report', 'not demonstrated competence'):
            self.assertIn(phrase, entry.lower() if phrase == 'self-report' else entry)

    def test_subject_areas_have_purpose_boundary_and_relationship(self):
        s = section(self.text(), STAGES[1])
        for phrase in ('subject subsystem map', 'what question it explains',
                       'important boundary', 'cross-area relationships or overlaps',
                       'actually inspected disciplinary sources',
                       'provisional'):
            self.assertIn(phrase, s)
        self.assertIn('not an arbitrary number of chapters', s)

    def test_learning_stages_are_not_identical_to_subject_areas(self):
        s = section(self.text(), STAGES[1])
        for phrase in ('a compulsory stage', 'several subsystems',
                       'high-level set of learning stages',
                       'Do not pre-generate the detailed daily tasks',
                       'instructional hypothesis'):
            self.assertIn(phrase, s)
        self.assertIn('Constructed English orientation', s)

    def test_current_activity_has_boundary_and_criterion(self):
        s = section(self.text(), STAGES[2])
        self.assertIn('defer generating future daily questions', s)
        self.assertIn('Do not silently switch tasks', s)
        self.assertIn('criterion', s)

    def test_task_result_drives_next_action_not_automatic_roadmap_rewrite(self):
        s = section(self.text(), STAGES[5])
        for phrase in ('Adaptive planning triggers', 'Independently checked task response',
                       'Repeated, well-identified conceptual gap',
                       'Ambiguous item', 'old plan version',
                       'Do not rewrite the roadmap after every answer'):
            self.assertIn(phrase, s)

    def test_opening_prompt_enforces_planning_and_reply_boundaries(self):
        s = section(self.text(), 'Opening prompt and one turn contract')
        for phrase in ('self-assessment', 'pre-instruction baseline',
                       'subsystem', 'high-level',
                       'Do not pre-generate', 'WAIT for my real response',
                       'preserve old versions'):
            self.assertIn(phrase, s)


class MasterDeclarationMutationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)/'package'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git','__pycache__','*.pyc'))
    def tearDown(self): self.temp.cleanup()
    def test_missing_primary_is_rejected(self):
        p = self.root/'publication.json';x = json.loads(p.read_text());x.pop('primary_practice')
        p.write_text(json.dumps(x))
        self.assertIn('primary-practice', check_domain.inspect(self.root))
    def test_nonpractice_primary_is_rejected(self):
        p = self.root/'publication.json';x = json.loads(p.read_text());x['primary_practice']='ai-coach:concept:feedback'
        p.write_text(json.dumps(x))
        self.assertIn('primary-practice', check_domain.inspect(self.root))
    def test_invented_composed_target_is_rejected_by_upstream(self):
        p=self.root/MASTER;s=p.read_text().replace('"ai-coach:practice:formative-assessment-with-ai"','"unknown:practice:invented"')
        p.write_text(s)
        result=validate.validate(self.root)
        self.assertFalse(result['ok'])
        self.assertIn('unresolved-id', [e['code'] for e in result['errors']])
    def test_recursive_master_composition_is_rejected(self):
        p=self.root/'practices/formative-assessment-with-ai.md';s=p.read_text()
        s=s.replace('type: "practice"', 'type: "practice"\ncomposes: ["'+MASTER_ID+'"]',1)
        p.write_text(s)
        result=validate.validate(self.root)
        self.assertFalse(result['ok'])
        self.assertIn('composition-cycle', [e['code'] for e in result['errors']])

if __name__=='__main__':unittest.main(verbosity=2)
