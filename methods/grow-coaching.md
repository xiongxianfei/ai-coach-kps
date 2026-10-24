---
id: "ai-coach:method:grow-coaching"
type: "method"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "GROW Coaching"
evidence_status: "provisional"
reviewed: null
basis_kind: "published practitioner procedure with authored adult learning application; not an effectiveness finding"
references: ["ai-coach:reference:performance-consultants-grow"]
source_alignment: [{"reference": "ai-coach:reference:performance-consultants-grow", "relation": "published-procedure-summary", "locator": "The GROW Model guide: How the GROW Model Works; The Four Stages of the GROW Model, Steps 1 to 4; Common Mistakes"}]
name: "grow-coaching"
home: "5-coach-and-reflect"
also: ["1-plan"]
use_when: "A learner needs to choose a feasible next action toward a meaningful goal"
ai_role: "Decision facilitator; clarify goals and options while the learner chooses"
time: "15-20 min suggested; revisit only unresolved decisions"
---

# GROW Coaching

## Key takeaway

Clarify Goal, Reality, Options and Will, then record the learner's chosen action rather than inventing commitment.

## Summary

Facilitate a flexible GROW conversation using existing evidence and constraints; supply checked instruction when a knowledge gap blocks a meaningful choice.

## Purpose and rationale

Turn a goal into a feasible action. Compare what the learner wants with present circumstances before selecting a route; questioning alone cannot supply missing subject knowledge.

## Inputs

- A learner-owned goal or decision and its intended use.
- Available evidence, prior actions, resources and constraints.
- An adjustable conversation budget; an existing context brief is optional.

## Steps

Run these steps as the AI. Reuse answered questions; revisit a stage only when new information warrants it.

1. **Goal.** Restate the desired outcome and a sign of progress. Ask about ambiguity that changes the action and wait for the reply. Keep the learner's purpose and scope; do not substitute your own curriculum.
2. **Reality.** Separate actual performance, self-report and assumptions. Inspect time, resources and prior attempts. Ask for missing consequential context and wait. Offer a small checked task only if the result would change planning, not as a compulsory assessment.
3. **Options.** Invite the learner's possibilities and wait, or use options already supplied. With permission or an existing request, add alternatives and explain their demands and trade-offs. If missing knowledge prevents a choice, provide a verified explanation rather than more introspective questions.
4. **Will or Way Forward.** Ask the learner to choose an action, timing, progress criterion and response to a likely obstacle. Wait for the choice unless already supplied. Record postponement or information gathering as valid choices. A suggested action is not an agreed commitment.
5. **Check feasibility.** Compare the choice with stated resources. If it does not fit, revisit the relevant decision instead of diagnosing low motivation. Let the learner amend it; wait if a new choice is needed.
6. **Close.** Return the decision record with unresolved questions and a review trigger. Stop when a workable choice is made or the learner pauses. Do not create reminders or save personal records unless an authorized tool actually completes the action.

## Prompt

```text
Facilitate GROW coaching for [goal or decision] using [context, evidence and
constraints] within [time budget]. Reuse information I have already provided.
Clarify my Goal and evidence of progress; examine Reality without treating
self-report as demonstrated ability; explore Options and their trade-offs;
then ask which action I choose as my Will or Way Forward. Wait when my response
or decision is needed and never invent it. Supply checked subject information
when questions alone cannot resolve a knowledge gap. Revisit earlier decisions
if the plan is infeasible, and accept postponement or changing the goal.
Return my chosen action, timing, progress criterion, obstacle response and review
trigger, with proposals and unknowns clearly marked. Do not claim learning,
commitment, saving or scheduling that has not actually occurred.
```

## Output and validation

Return `goal | evidence and unknowns | options and trade-offs | learner's choice | timing | progress criterion | obstacle response | review trigger`. Mark the choice pending if unanswered. Check whether the action fits the constraints and can produce relevant evidence.

**Constructed example:** The goal is to explain in meetings why equal means can accompany different variation. The learner reports knowing the mean formula but has not demonstrated the explanation; two short study periods are available. Compare a checked explanation, contrasting data sets and rehearsal with feedback. If the learner chooses explanation plus a fresh comparison, followed by a later explanation without notes, record that choice and both planned occasions. Do not mark the later task successful or expand the plan to a full statistics course. Revise timing if the second period is unavailable.

## Common failures and limits

- **Leading questions or automatic agreement:** compare the learner's reasons with evidence and invite alternatives.
- **Repeatedly asking answered questions:** reuse the supplied context.
- **Introspection replacing instruction:** explain missing subject knowledge with a checked source.
- **AI choice recorded as learner commitment:** wait or mark the choice pending.
- **A rigid four-stage interview:** revisit only decisions affected by new information; respect a pause or declined action.

## Next

Use [Backward Design](backward-design.md) to align a chosen learning goal with evidence and instruction. Use [After Action Review](after-action-review.md) once an episode has occurred. Neither is a compulsory extra step after every GROW conversation.

## Source alignment

[Performance Consultants' guide](../references/performance-consultants-undated-grow.md) supplies Goal, Reality, Options and Will or Way Forward and flexible use, associated with John Whitmore and colleagues. The AI instructions, prompt and example are authored; promotional outcome claims are not adopted. No branded diagrams, question bank or training materials are copied.

## Evidence status

**Provisional.** No certification, endorsement, psychotherapy protocol, learner outcome or validated AI coaching intervention is claimed.
