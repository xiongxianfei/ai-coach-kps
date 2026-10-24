---
id: "ai-coach:method:deliberate-practice-loop"
type: "method"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "Deliberate Practice Loop"
evidence_status: "provisional"
reviewed: null
basis_kind: "KPS-authored reusable adaptation of deliberate-practice training conditions; AI-only use is not established expert-guided deliberate practice"
references: ["ai-coach:reference:ericsson-1993-deliberate-practice"]
source_alignment: [{"reference": "ai-coach:reference:ericsson-1993-deliberate-practice", "relation": "published-procedure-summary", "locator": "The Role of Deliberate Practice in the Acquisition of Expert Performance, printed pages 367 to 368: Characteristics of Deliberate Practice and comparison with other activities"}]
---

# Deliberate Practice Loop

## Key takeaway

Work on a specific performance target through an attempt, informative feedback and an adjusted retry, then check whether the improvement survives reduced support and return to the whole task.

## Summary

This loop adapts training conditions described by Ericsson, Krampe and Tesch-Römer: tasks matched to existing knowledge, informative feedback and repeated opportunities to improve. Their account places individualized teacher-designed training within established domains of expertise. A generic chatbot does not supply that expertise merely by proposing exercises. Without competent domain guidance, describe the activity as focused practice adapted from these conditions, not as verified deliberate practice in the original sense.

## Use when and prerequisites

Use the loop when actual work reveals a specific, consequential weakness and a credible criterion can guide correction. Identify the component, a suitable task, the performance standard and a trustworthy feedback source. A qualified coach may be necessary to observe physical technique or select an appropriate progression. If neither correctness nor improvement can be judged, obtain better guidance before repeating the task.

## Rationale and procedure

A narrow target makes feedback actionable: it identifies a discrepancy that the next attempt can address. Keeping the criterion stable while recording changes in support helps distinguish a successful correction from a new independent performance. This is the local rationale for the loop, not a claim that every task can be improved through repetition.

1. Select a narrow target from evidence. Keep its connection to the whole performance explicit; [Skill Decomposition](skill-decomposition.md) can help when that relationship is unclear.
2. Prepare an attempt that the learner can understand with the available instruction. Define what would count as a useful improvement, including accuracy and relevant quality rather than speed alone.
3. Perform and preserve the attempt. Record the support actually received before evaluating it.
4. Compare with the criterion and provide specific, checked feedback. Identify a change in strategy or execution that addresses the discrepancy; praise or a score alone does not specify what to adjust.
5. Retry the same or a closely related task with that change. If the error persists, inspect the explanation, prerequisite, task and feedback rather than simply increasing repetitions.
6. Check a fresh case with the intended level of independence, then return the component to a meaningful whole task. Stop, rest or change approach when attention, discomfort, learner preference or lack of reliable feedback makes further repetitions unhelpful.

The stopping rules, assistance record, fresh-case check and whole-task return are authored decisions. They prevent a corrected response from being counted as a broader capability without examining it.

## Worked application

**Constructed example:** A learner can subtract numbers but sometimes changes only one side of an equation. The chosen target is preserving equality while isolating the unknown, rather than completing an entire algebra course.

For `3x + 6 = 21`, the learner writes `3x = 21`. The criterion requires applying the same operation to both sides. Feedback identifies the missing subtraction on the right: `3x = 15`, then `x = 5`; substitution checks `3 × 5 + 6 = 21`. Preserve the original error before showing this correction.

A retry asks for the first transformation of `4y + 3 = 19`. The evaluator expects `4y = 16`. If the learner copies a supplied transformation, label the retry assisted. A subsequent fresh equation without the reminder can inspect independent execution. Finally, return to a word problem where the learner must first construct the equation; success on supplied equations alone does not establish that broader skill.

These are authored examples of feedback and checking, not a tested training programme or actual learner progress. Repeated failure after explanation calls for reconsidering the task or guidance, not an automatic judgment about effort.

## Output and validation

Retain the target and criterion, attempts, actual assistance, feedback basis, adjustments and result of any independent or integrated check. Improvement should be visible in the relevant performance, not inferred from time spent. If only the repeated example improves, keep the claim narrow. Later retention needs a later observation; one before-and-after change does not identify the cause.

## AI role and limits

AI can help draft comparable tasks, organize feedback and maintain a record supplied in the conversation. Verify generated solutions and task equivalence. AI-only feedback cannot establish expert-designed progression or unobserved physical execution. The learner remains the performer and may request a demonstration, change support or stop.

[Spaced Repetition](spaced-repetition.md) primarily arranges delayed revisits; this loop targets a current performance discrepancy. [After Action Review](after-action-review.md) examines the completed episode and can inform the next target. No universal practice duration, expertise threshold or guaranteed outcome is prescribed here.

## Source alignment

[Ericsson and colleagues](../references/ericsson-et-al-1993-deliberate-practice.md), pages 367–368, supplies the bounded training conditions and teacher-guidance context. The named loop, arithmetic example and AI adaptation are authored. The wider theory of expertise is not adjudicated by this procedural account.

## Evidence status

**Provisional.** No independent expert review, learner trial or demonstrated equivalence between AI assistance and expert coaching is claimed.
