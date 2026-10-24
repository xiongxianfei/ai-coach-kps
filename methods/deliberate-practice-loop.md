---
id: "ai-coach:method:deliberate-practice-loop"
type: "method"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "Deliberate Practice Loop"
evidence_status: "provisional"
reviewed: null
basis_kind: "KPS-authored reusable adaptation of deliberate-practice training conditions; AI-only use is not established expert-guided deliberate practice"
references: ["ai-coach:reference:ericsson-1993-deliberate-practice"]
source_alignment: [{"reference": "ai-coach:reference:ericsson-1993-deliberate-practice", "relation": "published-procedure-summary", "locator": "The Role of Deliberate Practice in the Acquisition of Expert Performance, printed pages 367 to 368: Characteristics of Deliberate Practice and comparison with other activities"}]
name: "deliberate-practice-loop"
home: "5-coach-and-reflect"
also: ["4-test-and-fix"]
use_when: "Actual performance shows a specific weakness and reliable feedback can guide adjustment"
ai_role: "Practice assistant; organize attempts and checked feedback without claiming expert coaching"
time: "15-20 min suggested; stop sooner if practice becomes uninformative"
---

# Deliberate Practice Loop

## Key takeaway

Collect a focused attempt, give checked feedback, adjust and retry, then examine independent and integrated performance separately.

## Summary

Run practice against a specific criterion; describe AI-only support as an adaptation of deliberate-practice conditions, not established expert-guided training.

## Purpose and rationale

Improve a consequential component through actionable feedback. Keeping the criterion explicit makes each adjustment inspectable; repeated corrections alone do not establish independent performance or transfer.

## Inputs

- A specific target supported by actual work and its relation to the whole skill.
- A task the learner can understand, a checked criterion and reliable feedback.
- Agreed support, stopping conditions and an adjustable time budget.
- Competent domain guidance where task selection or physical observation requires it.

## Steps

Run these steps as the AI. The learner performs the task; you must not invent an attempt or improvement.

1. **Set the target.** Identify one consequential discrepancy from the record and the intended improvement. If the target is unclear, ask for relevant work and wait, or use decomposition before prescribing drills.
2. **Prepare.** Verify the task and criterion. Explain instructions and agree on support and the stopping boundary. Track accuracy and relevant quality; do not reward speed at their expense. If correctness cannot be checked, obtain better guidance before starting repetitions.
3. **Attempt.** Present the task and wait for the actual response. Preserve original work and actual assistance before showing a correction. If the learner requests a demonstration, provide it and label the changed conditions.
4. **Give feedback.** Compare with the criterion, identify the important discrepancy and explain a specific adjustment. Verify the correction; praise or a score alone is insufficient. Ask for clarification when the work does not reveal the issue and wait before judging.
5. **Retry.** Present a similar task using the adjustment and wait. Keep the retry separate from the original. If the same difficulty persists, inspect prerequisites, instructions and feedback; change guidance rather than merely adding repetitions.
6. **Check independence and integration.** When useful, give a fresh case with agreed answer help removed, retaining access supports; wait before feedback. Then return to a meaningful whole task. Mark these as separate observations or as planned if not performed. If only the repeated item improves, keep the conclusion narrow.
7. **Stop and record.** Pause on request, discomfort, deteriorating attention, unreliable feedback or an exhausted budget. Return the attempt record and one next decision. Save privately only through an authorized, confirmed write; otherwise provide copyable output.

## Prompt

```text
Guide focused practice for [specific target] using [actual evidence], [checked
criterion or source], [permitted support] and [time budget and stop conditions].
Check that the task is understandable and feedback can be verified. Give one
attempt and wait for my real work before showing a solution. Preserve the original
response and help received. Explain one specific correction, then present a
similar retry and wait again. If difficulty persists, inspect the task,
prerequisites and feedback instead of assigning endless repetitions. When useful,
check a fresh case with agreed support reduced and return to the whole task;
do not invent those results if we stop earlier. Respect requests for a full
explanation or a pause. Return attempts, support, checked feedback, adjustments
and one next action. Treat AI-only use as focused practice adapted from deliberate
practice, not expert coaching. Report saving only after a confirmed private write.
```

## Output and validation

Return `target and criterion | original attempt | actual assistance | checked feedback | adjustment | retry | independent or whole-task check`. Mark unperformed checks planned. Verify that any improvement claim identifies the actual task and conditions; time spent or one before-and-after change does not establish its cause or later retention.

**Constructed example:** For `3x + 6 = 21`, a response of `3x = 21` omits subtracting 6 on the right. Preserve it, then explain equal operations on both sides: `3x = 15`, `x = 5`; substitution gives `3 × 5 + 6 = 21`. A retry asks for the first transformation of `4y + 3 = 19`, expecting `4y = 16`. Copied transformations are assisted. A later fresh equation checks independent execution; a word problem checks constructing and using the equation. These are illustrative tasks, not observed progress.

## Common failures and limits

- **No verified criterion:** obtain a source or competent feedback before repeating.
- **More repetitions without an adjustment:** inspect what prevented useful feedback.
- **Corrected work counted as independent:** retain original and assisted attempts separately.
- **Isolated success treated as whole-skill mastery:** return to an integrated task and preserve unknowns.
- **AI presented as an expert coach:** state its limits, especially for unobserved physical technique. No universal hours or expertise threshold is prescribed.

## Next

Use [Skill Decomposition](skill-decomposition.md) if the target needs revision, [Spaced Repetition](spaced-repetition.md) for delayed revisits, or [After Action Review](after-action-review.md) when the episode's process needs reflection. Continue only while the next attempt serves a useful decision.

## Source alignment

[Ericsson and colleagues](../references/ericsson-et-al-1993-deliberate-practice.md), pages 367-368, supplies suitable tasks, informative feedback, repeated attempts and individualized teacher-designed training. The named loop, stopping rules, AI prompt and example are authored adaptations; a chatbot is not evidence of competent domain guidance.

## Evidence status

**Provisional.** No independent review, learner trial or equivalence between AI assistance and expert coaching is claimed. Prompt instructions cannot guarantee model behavior.
