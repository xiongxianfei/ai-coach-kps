---
id: "ai-coach:method:learning-from-erroneous-examples"
type: "method"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "Learning from Erroneous Examples"
evidence_status: "provisional"
reviewed: null
basis_kind: "KPS-authored reusable adaptation of published erroneous worked-example instruction; changes and untested limits stated"
references: ["ai-coach:reference:booth-2013-examples"]
source_alignment: [{"reference": "ai-coach:reference:booth-2013-examples", "relation": "published-procedure-summary", "locator": "Section 3.1.2 Intervention pp. 26–27; General discussion pp. 31–32"}]
---

# Learning from Erroneous Examples

## Key takeaway

Use a checked flawed solution to examine why a step fails, then construct and check a valid correction.

## Summary

This reusable adaptation develops reasoning about errors through a worked example. It distinguishes recognizing a wrong result, explaining the faulty step and producing a justified repair. It is one approach to error diagnosis, not a definition of every diagnostic task or a universal teaching sequence.

## Rationale and published basis

Booth and colleagues studied school algebra with guided practice. Example steps were labelled correct or incorrect. Learners used menu-supported explanations of what the step did and why it was valid or invalid; hints and feedback were available. Reported conceptual benefits did not imply superiority on all procedural measures. [Intervention and discussion](../references/booth-et-al-2013-example-problems.md).

Here the reusable adaptation permits a brief explanation, annotation or supported choice, followed by an explicit repair and a separate application where useful. It does not replicate the tutor interface or experimental conditions. Asking a learner to find an unmarked error adds a demand beyond explaining an already identified one. The rationale for this adaptation is to make the learner's correction inspectable; its effectiveness in this form remains untested.

## Inputs and prerequisites

Begin with a particular relationship the learner needs: for example, maintaining equality when transforming an equation. Prepare the valid solution and check that the displayed error really violates the stated conditions. A merely unfamiliar but valid alternative is not an error. Distinguish an invalid operation from a valid operation that is inefficient for the current goal.

Use a short example with enough surrounding work to locate the issue. If the learner does not yet know the relevant rule, teach it with a correct example first. An error hunt cannot supply missing foundational knowledge. The proposed mechanism is that contrasting a flawed step with the relevant condition makes the reason for choosing a valid operation explicit; locating the wrong line alone leaves that reason unobserved.

## Procedure for examining and repairing reasoning

The following is the authored reusable procedure:

1. Present the task and flawed work. State that it contains an error; highlight the step when locating it is not the learning goal. Keep the checked correction available for feedback, without displaying it as the learner's answer.
2. Ask what the step changed and why that change fails under the task's rules. Accept a bounded explanation or annotation. If necessary, offer a specific contrast or identify the affected rule, recording the help.
3. Ask for a valid replacement and a check of the result. Compare the reasoning with the prepared solution, allowing other valid approaches. Explain the missing relationship when the learner cannot yet repair it.
4. When independent application matters, use a different case and record whether the learner needed further help. Omit extra work when adequate evidence already exists; a repaired example alone should not be reported as general mastery.

The initial explanation and repair requests can be presented together. Feedback waits for actual responses. Avoid disclosing the full correction before an intended independent attempt, but provide it when instruction is needed or requested.

## Worked example of preserving equality

This invented example assumes the learner has learned that applying the same addition or subtraction to both sides preserves equality.

Problem: solve `2x + 6 = 14`.

Displayed flawed work:

```text
2x + 6 = 14
2x     = 14   ← incorrect: subtracting 6 changed only the left side
x      = 7
```

For a supported explanation task, leave the marked comment visible and ask why that change is invalid and how to repair it. For a separate localization task, remove the comment but state that an error exists; do not interpret the two conditions as equivalent evidence.

The checked correction is:

```text
2x + 6 - 6 = 14 - 6
2x         = 8
x          = 4
Check: 2 × 4 + 6 = 14
```

The essential reason is maintaining the same value on both sides. Saying “the answer is four” supplies a result; explaining the two-sided subtraction supplies its justification. Substitution also exposes the original failure: `2 × 7 + 6 = 20`, which is not fourteen.

For contrast, adding six to both sides gives `2x + 12 = 20`. That preserves equality even though it does not immediately isolate `2x`. Do not mark it invalid merely because it differs from the prepared solution.

A possible later case is `3y + 5 = 17`, whose checked solution is `y = 4`. Keep that answer out of a live independent task. Correctly repairing the first problem does not establish that this new one was attempted or solved.

## Output checks and interpretation

A wrong answer can reflect a misread symbol, calculation slip, misunderstood rule or ambiguous prompt. Ask for only the missing evidence needed to distinguish consequential possibilities. If the learner can explain equality but subtracts incorrectly, targeted arithmetic feedback may suffice. If they cannot explain why both sides change, revisit equality with a checked demonstration. Repeated guessing is a reason to change support, not proof of low ability.

The [coaching Practice](../practices/ai-assisted-learning-orchestration.md#stage3-select-one-current-learning-task) chooses the task, assistance, feedback and next lesson. This document supplies a reusable explanation, not a mandatory additional assessment stage.

## Limits

Unlabelled errors can confuse readers or become remembered as correct examples; keep the intended flaw and eventual correction explicit. Source evidence concerns a supported algebra setting, not independent adult AI use, and the tested intervention retained support for correct knowledge. A language or security example needs its own checked subject basis and explicit adaptation. Correct diagnosis of supplied work is not evidence that the learner can perform the whole task unaided. The optimal amount of guidance cannot be inferred from the method name.

## Source alignment

[Booth and colleagues, 2013](../references/booth-et-al-2013-example-problems.md), section 3.1.2, supplies the published operation of explaining labelled steps with support. The discussion bounds the findings and the continuing need for correct instruction. Open responses, explicit repair, the invented equation and conditional follow-up are KPS-authored adaptations, not an exact published script or additional demonstrated effects.

## Evidence status

**Provisional.** Located passages and the constructed arithmetic have been inspected. No actual learner result, efficacy test of this adaptation, complete literature review or independent scientific approval is claimed.
