---
id: "ai-coach:method:interleaved-practice"
type: "method"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "Interleaved Practice"
evidence_status: "provisional"
reviewed: null
basis_kind: "source-aligned mixed-problem procedure with authored adult application and error-analysis decisions"
references: ["ai-coach:reference:rohrer-2015-interleaved-practice"]
source_alignment: [{"reference": "ai-coach:reference:rohrer-2015-interleaved-practice", "relation": "published-procedure-summary", "locator": "ERIC-hosted advance article, PDF pages 1 to 3 on strategy selection and spacing; PDF pages 4 to 5, Method and Procedure"}]
name: "interleaved-practice"
home: "4-test-and-fix"
also: []
use_when: "The learner needs to select among approaches already introduced"
ai_role: "Practice designer and assessor; separate approach-selection errors from execution errors"
time: "15-20 min suggested; adapt the set to the learner"
---

# Interleaved Practice

## Key takeaway

Mix taught problem types, wait for the learner's choice and solution, then check selection separately from execution.

## Summary

Run a checked mixed set without giving away the required strategy; return to instruction when a type is unfamiliar.

## Purpose and rationale

Practise choosing an approach from the problem itself. A block of one type can disclose the strategy in advance; a mixed set removes that shortcut. The inspected mathematics study also changed spacing, so it does not isolate a pure discrimination effect.

## Inputs

- Target capability and previously introduced problem types worth distinguishing.
- Checked problems, acceptable approaches and answer criteria.
- Agreed resources, delivery preference and adjustable time budget.

## Steps

Run these steps as the AI; do not select the learner's strategy before their attempt.

1. **Check readiness.** Establish which types were taught using the supplied record. Ask for missing context and wait if necessary. Teach an unfamiliar type before interpreting its difficulty as failed discrimination.
2. **Build the set.** Mix relevant types and verify every answer, including valid alternatives. Remove category headings or other labels that disclose the method, but retain information needed to solve the problem. Avoid a predictable alternating pattern that becomes another cue; no fixed mixture ratio is required.
3. **Collect attempts.** Present one problem, or a short set if preferred. Ask for the intended approach and enough work to inspect it. Wait for the actual response. Keep solutions hidden and record help or exposure before judging performance.
4. **Check two decisions.** First compare the selected approach with the problem's demands, then check execution. Explain the distinguishing feature after a selection error; repair calculation or implementation after an execution error. If the response does not reveal the cause, ask a brief clarification and wait rather than inventing one.
5. **Adapt.** Give a checked explanation or focused example when a type was not understood. Continue with fresh mixed cases if useful; record which parts were assisted. Pause on request, when the budget ends or when enough evidence supports the next decision.
6. **Summarize.** Return the record and one next action. Propose a later independent mixed check if needed; do not count corrected practice as evidence that the learner can select independently later.

## Prompt

```text
Run interleaved practice for [capability] across [previously taught types],
using [checked source or problem bank], [permitted resources] and [time budget].
Verify problems and acceptable solutions before presenting them. Mix types
without headings or predictable ordering that reveals the strategy. Use
[one problem at a time / a short set]. Ask me to choose an approach and show
enough work, then wait for my actual response before giving solutions.
Preserve original choices, work and any help. Distinguish strategy-selection
errors from execution errors; clarify uncertain causes instead of guessing.
Teach an unfamiliar type before testing it again. Stop at the agreed boundary
or my request, and return the evidence table, uncertainty and one next action.
Do not invent responses, later retention or a saved record.
```

## Output and validation

Return `problem | chosen approach | original work | actual help | selection assessment | execution assessment | correction`. Verify that independent-selection claims concern fresh problems without revealing cues; a corrected worksheet is not sufficient.

**Constructed example, evaluator key withheld during delivery:** Mix a fee rising from £40 to £50 (percentage increase: 25%), £80 to £92 (pounds added: £12), and £60 to £45 (percentage decrease: 25%). “£10” for the first prompt may indicate the wrong requested quantity; incorrect arithmetic after setting up `10 / 40` suggests a different difficulty. Inspect the work before choosing feedback. Use later cases in a less predictable order, including repeated types where useful. These are illustrations, not study materials or learner results.

## Common failures and limits

- **Mixing unrelated material randomly:** choose types whose distinction matters to the goal.
- **Giving a formula before the response:** record assistance; independent selection is unobserved.
- **Strict alternation or category headings:** remove unintended cues.
- **Treating every wrong answer alike:** inspect selection and execution separately.
- **Demanding unaided success on untaught content:** provide instruction and label the changed conditions.

## Next

Use a fresh mixed check when independent choice matters. Use [Spaced Repetition](spaced-repetition.md) to arrange revisits, or [Worked Example Instruction](worked-example-instruction.md) to supply a missing demonstration. Mixing categories and alternating examples with problems are different operations.

## Source alignment

[Rohrer and colleagues](../references/rohrer-et-al-2015-interleaved-practice.md), advance article PDF pages 1-5, supplies the rationale and assignment procedure in school mathematics. The adult example, error categories, AI delivery and prompt are authored adaptations; no universal benefit is inferred.

## Evidence status

**Provisional.** No learner trial or validated AI implementation is claimed. The prompt cannot guarantee faithful delivery.
