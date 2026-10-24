---
id: "ai-coach:method:baseline-check"
type: "method"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "Baseline Check"
evidence_status: "provisional"
reviewed: null
basis_kind: "KPS-authored reusable adaptation of performance-based prior knowledge assessment; not a standardized diagnostic instrument"
references: ["ai-coach:reference:cmu-eberly-prior-knowledge"]
source_alignment: [{"reference": "ai-coach:reference:cmu-eberly-prior-knowledge", "relation": "published-procedure-summary", "locator": "Performance-Based Prior Knowledge Assessments, three introductory paragraphs; How to Assess Students' Prior Knowledge, direct and indirect measures"}]
name: "baseline-check"
home: "1-plan"
also: ["5-coach-and-reflect"]
use_when: "Starting a skill or improvement effort when evidence would change the next lesson"
ai_role: "Instructional assessor; prepare checked tasks and compare predictions with observed performance"
time: "15-20 min suggested; narrow the scope if needed"
uses_concepts: ["ai-coach:concept:metacognitive-calibration"]
---

# Baseline Check

## Key takeaway

Record the learner's prediction before testing, then choose a starting point from checked performance and explicit unknowns.

## Summary

Run a bounded assessment using the same criteria for predicted and observed performance; keep assistance, corrections and untested skills separate.

## Purpose and rationale

Find a useful starting point for instruction. Recording predictions first preserves the learner's initial judgment; comparing matched criteria makes a confidence discrepancy interpretable without inventing a general ability score.

## Inputs

- Target capability and intended use; a prior plan or context brief is optional.
- Relevant experience, constraints, allowed resources and the learner's time budget.
- A checked subject source, answer key or rubric. If absent, obtain one before scoring.
- An optional private record destination outside public repositories.

## Steps

Run these steps as the AI; wait for real learner responses.

1. **Scope.** Restate the target and agree on resources and time. Ask for missing essentials and wait. Reuse adequate prior evidence; do not require a diagnostic just to complete a template.
2. **Prepare.** Choose representative tasks, often 3-5 if they fit the budget, and check their answers or rubric. Include integration when the target requires it. Keep solutions hidden; replace exposed items or record the exposure.
3. **Predict first.** Show criteria without solutions. Ask which the learner expects to meet independently, partly or not yet, with a reason; allow “unsure.” Wait and preserve predictions before testing. Define any numerical scale before use.
4. **Test.** Present a task and wait. Preserve the original response and actual help. Retain access supports; if the learner requests instruction, provide it and label the attempt assisted. Defer feedback that would reveal a later task's answer.
5. **Assess.** Compare the work with checked criteria. Keep errors, assistance, missing responses and uncertain judgments distinct. Repair invalid tasks rather than assigning a failure.
6. **Compare.** Contrast predictions and observations on matching criteria and conditions. Use qualitative discrepancies unless a common numerical scale is defined. Report supported strengths and the largest observed difficulty among sampled areas; leave untested skills unknown.
7. **Decide.** Recommend one next focus with evidence and uncertainty. Stop when further testing would not change the choice, the budget ends or the learner pauses; mark incomplete coverage.
8. **Record.** Return dated, copyable output. Save only to an authorized private destination through an available tool and verify the write; otherwise say it has not been saved. Preserve this baseline when later results arrive.

## Prompt

```text
Run a baseline check for [target and intended use]. Budget: [15-20 minutes or
my preference]. Context and existing evidence: [optional]. Permitted resources:
[resources]. Verification source or rubric: [source, or help me obtain one].

Clarify missing essentials, then prepare representative tasks with checked
criteria. Before testing, show the criteria without solutions and ask me to
predict my performance on each under the agreed conditions. Wait for my reply.
Give tasks one at a time and wait for my actual work; never supply my responses.
Preserve predictions and original answers. Record any hints or answer exposure;
defer feedback that would reveal a later answer. Compare work with checked
criteria, leaving unsupported judgments provisional and untested skills unknown.
Compare predictions and evidence on matching criteria, without subtracting
unrelated scales or diagnosing a trait. Stop at the budget or when enough
evidence supports a starting decision. Return a dated table, coverage limits
and one next focus. Provide a private copyable record; claim a save only after
a confirmed authorized write. Do not require a context brief to start.
```

## Output and validation

Return the target, date, resources, task and source identifiers, preserved predictions and responses, then:

| Criterion | Prediction before test | Observed evidence | Actual assistance | Result and confidence discrepancy |
|---|---|---|---|---|
| [criterion] | [prediction and reason] | [response or untested] | [actual help] | [bounded comparison or unknown] |

Finish with one next-focus sentence and the evidence needed to revisit it. Check that every conclusion is supported by an actual response and that predictions and results refer to the same criterion.

**Constructed example, not a learner record:** To compare a 750 g package costing £3 with a 1 kg package costing £5, the evaluator checks 0.75 kg and £4/kg versus £5/kg. If conversion was predicted independent and performed independently, that criterion agrees. If selecting a rate was predicted independent but required a supplied division setup, record the mismatch and assistance; independent rate selection remains unestablished. Correct conversion with wrong division suggests a different next lesson from comparing unlike units. Do not reveal this example's key during a fresh baseline, and do not generalize its result to untested skills.

## Common failures and limits

- **Ratings collected after testing:** label them retrospective; do not overwrite predictions.
- **Tasks too easy, too hard or unrepresentative:** revise the sample; a short check is not a full skill ranking.
- **Hints or visible solutions:** retain the response as assisted, not an untouched baseline.
- **Unverified AI scores or mismatched scales:** check the criterion or report uncertainty; do not invent a numeric gap.
- **No record or invented save:** return the copyable record and actual storage status. Never default to a public repository's `logs/`.

## Next

Teach a demonstrated prerequisite gap directly. Use [Skill Decomposition](skill-decomposition.md) if the bottleneck is unclear, or [Deliberate Practice Loop](deliberate-practice-loop.md) for a supported target. Recheck after relevant practice or at a meaningful milestone using comparable conditions and fresh tasks; 4-8 weeks is an optional planning choice, not a validated interval.

## Source alignment

[Eberly Center guidance](../references/cmu-eberly-undated-prior-knowledge.md) supplies the performance-assessment basis. [Metacognitive Calibration](../concepts/metacognitive-calibration.md) explains judgment versus criterion; its abstract-level source does not validate a scale. Prediction-first delivery, the prompt, timing, recording rules and example are authored adaptations, not a standardized diagnostic instrument.

## Evidence status

**Provisional.** No reliability study, independent review or learner trial is claimed. Prompt instructions do not guarantee AI behavior.
