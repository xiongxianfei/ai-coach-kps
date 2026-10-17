---
id: "ai-coach:method:worked-example-instruction"
type: "method"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "Worked Example Instruction"
evidence_status: "provisional"
reviewed: null
basis_kind: "source-aligned procedure with authored examples and explicit chat pacing adaptation"
references: ["ai-coach:reference:pashler-2007-organizing-instruction"]
source_alignment: [{"reference": "ai-coach:reference:pashler-2007-organizing-instruction", "relation": "published-procedure-summary", "locator": "Recommendation 2, printed pages 9 to 11: evidence, implementation and roadblocks"}]
---

# Worked Example Instruction

## Key takeaway

Let a learner inspect a solved task, then attempt a related task; adjust example support as their understanding develops.

## Summary

A worked example includes a problem and its solution path, rather than only a final answer. The inspected IES guidance recommends alternating worked solutions with problems learners solve, with support adapted to expertise. A demonstration can explain relationships as well as calculations. Our examples and chat application are authored choices.

## Inputs and prerequisites

A target problem type, necessary terms, an accurate solution, and a related task with checked criteria. A learner who does not understand the notation may need an explanation before the example is useful. Keep the solution to an independent check unavailable until the learner attempts it.

## Rationale

The solved case makes an approach available for study; the related attempt reveals what the learner can use. Reading a convincing solution and producing one are different observations. More annotation is not automatically better: the IES guide describes variation in the useful amount of explanation and supports reducing example assistance as expertise develops.

## Procedure

1. Select a representative problem and show a correct solution path with the support appropriate to the learner.
2. Have the learner attempt a related problem. Compare the actual work with the relevant relationships, not only the final result.
3. Use the attempt to choose another example, a clarification or less supported problem solving. When useful, supply part of a solution and let the learner complete it; reduce support as evidence warrants.

Repeated use alternates examples and attempts. If a lesson instead presents its demonstrations together and then a grouped question set, identify that as a pacing adaptation. It is not the same sequence as the guide's interleaving recommendation, and that recommendation does not establish the adaptation's effectiveness.

## Worked application

**Constructed case:** The learner understands equality and basic arithmetic but needs to learn a two-step equation.

Problem: Find `x` when `3x + 6 = 21`.

| Step | Result | Relevant reason |
|---|---|---|
| Subtract 6 from both sides | `3x = 15` | Doing the same subtraction preserves equality and removes the added term. |
| Divide both sides by 3 | `x = 5` | Three equal quantities total 15, so each is 5. |
| Substitute into the original equation | `3 × 5 + 6 = 21` | The proposed value satisfies the original relationship. |

Then ask the learner to solve `4y + 3 = 19`, showing enough work to check the operations. The evaluator's solution is `4y = 16`, then `y = 4`; substitution gives 19. In live delivery, keep that solution behind the attempt.

If the learner subtracts 3 on only one side, clarify preservation of equality and compare the two sides. If they understand the operations but make an arithmetic slip, correct that slip without reteaching the whole procedure. A later completion problem could supply `5z = 20` after an initial subtraction and ask for the remaining steps. Successful use of that support does not prove independent solution selection.

The example uses positive coefficients and addition. It does not by itself teach every linear equation, including zero coefficients or variables on both sides. Change the case when the next learning objective requires that extension.

## Cognitive modeling and self explanation

[Cognitive modeling](cognitive-modeling.md) adds an inspectable account of why a demonstrator chooses a step or checks a condition. A worked solution can contain those decisions, but the two descriptions emphasize different things. [Self-explanation](self-explanation.md) asks the learner to supply an explanation of a step. Neither requires a long commentary on every operation.

## Output and validation

Retain the demonstration and the learner's actual related attempt, noting any supplied steps or answers. Check mathematical or subject correctness independently of fluency. If the learner only reproduces the original example, a fresh case is still needed to examine application. Later retention and changed-context use require their own evidence.

## Limits

The IES recommendation draws especially on mathematics, science and technology tasks. Its evidence rating is moderate, as assessed by that guide. Neither identical benefits across subjects nor an optimum example-to-question ratio for chatbot lessons follows. For a learner already able to solve the task, repeated complete demonstrations may be unnecessary.

## Source alignment

[Pashler and colleagues, Organizing Instruction and Study](../references/pashler-2007-organizing-instruction.md), Recommendation 2, printed pages 9–11, supplies alternating worked examples and problems, expertise-sensitive support and fading. The equations, response decisions and grouped-delivery caveat here apply that guidance; underlying studies were not independently reappraised.

## Evidence status

**Provisional.** Published guidance is not independent review of this explanation or validation of AI-generated solutions. All examples are constructed; no learning results are reported.
