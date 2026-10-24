---
id: "ai-coach:method:spaced-repetition"
type: "method"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "Spaced Repetition"
evidence_status: "provisional"
reviewed: null
basis_kind: "KPS-authored reusable adaptation combining delayed review and retrieval with feedback; not an optimized scheduling algorithm"
references: ["ai-coach:reference:pashler-2007-organizing-instruction"]
uses_principles: ["ai-coach:principle:spacing-effect", "ai-coach:principle:testing-effect"]
source_alignment: [{"reference": "ai-coach:reference:pashler-2007-organizing-instruction", "relation": "published-procedure-summary", "locator": "Recommendation 1, printed pages 5 to 7; Recommendation 5b, printed page 21, opening recommendation"}]
name: "spaced-repetition"
home: "4-test-and-fix"
also: ["5-coach-and-reflect"]
use_when: "Previously learned material needs to remain available after a delay"
ai_role: "Review facilitator; prepare checked prompts and propose revisits from actual recall"
time: "10-15 min per review suggested; intervals depend on the retention goal"
---

# Spaced Repetition

## Key takeaway

Collect recall on separated occasions, check it before revising the schedule and keep planned reviews distinct from completed ones.

## Summary

Guide one review at a time using actual responses and an explicit retention horizon; do not invent an optimal calendar or automatic reminders.

## Purpose and rationale

Keep important learned material available later. [Spacing](../principles/spacing-effect.md) concerns when material returns; [retrieval](retrieval-practice.md) concerns recalling it before seeing the answer. This procedure combines them with checked feedback.

## Inputs

- Previously encountered material, intended future use and retention horizon.
- Checked prompts and answers, or a source from which to prepare them.
- Actual review dates, responses and intervening study where known.
- Available time; an optional private record or calendar destination.

## Steps

Run these steps as the AI, using only reviews and capabilities actually available.

1. **Choose material.** Identify a manageable set relevant to future use. Reuse existing items and ordinary practice rather than creating duplicate reviews. If understanding was never established, offer checked instruction first.
2. **Prepare a review.** Verify each prompt and criterion. Keep the answer separate from delivery; record any exposure during preparation. Ask only for missing information needed to set conditions or timing, and wait when a reply is required.
3. **Retrieve.** Present a checked question without its answer and wait for the learner's actual response. Preserve it and record actual hints, resources and elapsed time since relevant study; leave unknown timing unknown.
4. **Correct.** Compare with the criterion, explain the important difference and retain the correction separately. If help was supplied before completion, label the attempt assisted. Repair an ambiguous prompt rather than attributing its failure to memory.
5. **Reschedule.** Propose a later occasion with a reason. Consider a longer gap after successful independent recall, or repair followed by an earlier check after difficulty. These are adjustable heuristics, not optimized interval rules. Include a delayed application task when using knowledge matters.
6. **Close and record.** Return the review record and next date or trigger. Reduce low-value items when the goal or workload changes. Save privately or create a reminder only through an available, authorized tool and verify its result; otherwise provide copyable details and state that no save or reminder occurred.

## Prompt

```text
Guide spaced review of [learned material] for use by [retention horizon].
Use [checked source or items], [actual prior review record, if available] and
[time budget]. Ask for essential missing context, then verify the next prompt
and its answer. Present the question without the answer and wait for my work.
Keep original recall, actual help and correction separate. Record actual delays
or unknown timing; do not treat a missed review as a failed memory test.
Explain corrections, then propose a next review with a reason. Treat longer or
shorter gaps as revisable choices, not optimal rules. If understanding is missing,
teach it rather than repeating unsupported retrieval. Return a dated record and
next occasion; do not claim persistent memory, saving or scheduling without a
confirmed authorized tool result. Pause when I stop or the agreed set is complete.
```

## Output and validation

Return `item and source | actual date and delay | original recall | help | correction | next occasion and reason`. Distinguish planned entries from observed attempts. Check whether the evidence actually comes after a known delay; completion counts or corrected cards alone do not establish retention.

**Constructed example:** After instruction, a learner plans a unit-price review two days later and another a week after that. Those are trial choices. A 750 g package costing £3 has a checked price of £4/kg. Reversing the ratio calls for repairing its meaning and considering an earlier check; independent, justified recall may support keeping or lengthening the gap. A different package comparison can later examine application. A missed appointment stays missed, not failed.

## Common failures and limits

- **Rereading counted as recall:** record answer exposure and seek a later independent response if needed.
- **Failure triggers endless cards:** inspect understanding, wording and workload first.
- **One fixed calendar for every topic:** revise timing against the goal and actual evidence.
- **Unknown delays treated as retention:** preserve uncertainty.
- **Fictional reminders or saves:** report only confirmed actions; keep personal records outside public repositories.

## Next

Continue at the next review occasion. Use [Interleaved Practice](interleaved-practice.md) when choosing among problem types matters; it changes the mixture, not just timing. Schedule a separate application check when recall alone does not sample the goal.

## Source alignment

[Pashler and colleagues](../references/pashler-2007-organizing-instruction.md), Recommendation 1, pages 5-7, and the opening of 5b, page 21, supplies delayed review and recall with correction. Timing choices, the AI procedure, prompt and example are authored and untested; no software algorithm is adopted.

## Evidence status

**Provisional.** Published findings do not validate this scheduling implementation or guarantee that an AI follows the prompt.
