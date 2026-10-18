---
id: "ai-coach:method:cognitive-modeling"
type: "method"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "Cognitive Modeling"
evidence_status: "provisional"
reviewed: null
basis_kind: "source-aligned explanation; AI application is separately authored in Practices"
references: ["ai-coach:reference:collins-1991"]
source_alignment: [{"reference": "ai-coach:reference:collins-1991", "relation": "published-procedure-summary", "locator": "Method item 1: Modeling"}]
uses_models: ["ai-coach:model:cognitive-apprenticeship"]
---

# Cognitive Modeling

## Key takeaway

Make a knowledgeable task demonstration and its explanatory decisions available for a learner to inspect.

## Summary

Modeling here refers to the instructional method within Cognitive Apprenticeship, not mathematical model fitting or access to an AI system's internal cognition.

## Inputs and prerequisites

A task, a demonstrator or verified worked solution, and decisions worth explaining. Fluent AI output alone does not establish that the demonstration is correct.

## Rationale

A learner can inspect how an example is approached rather than only seeing its final answer.

## Procedure

1. Select a task that makes the target decisions visible.
2. Demonstrate the task and explain the relevant choices, checks and constraints.
3. Invite the learner to articulate those choices and compare another attempt.

## Worked decisions and their limits

A [worked example](worked-example-instruction.md) shows a task and its solution path. Cognitive modeling makes relevant choices and checks explicit within a demonstration. For `3x + 6 = 21`, a solution can show `3x = 15`, then `x = 5`. The modeling adds: remove the added 6 by subtracting it from both sides to preserve equality; then divide by 3; finally substitute 5 into the original equation to check it. The explanation exposes a usable decision rule rather than asking the learner to imitate unexplained symbols.

Select the decisions the learner needs. Narrating every trivial action can obscure the important choice. Check the demonstrated operations and the stated reason before teaching them. If the learner can already justify the steps, another task may be more useful than repeating the demonstration. This equation and these support choices are authored illustrations of modeling, not observations reported in the source publication.

A learner explaining the step is performing self-explanation; the demonstrator explaining its choice is modeling. Both can occur around the same example. An AI-generated explanatory account is a teaching artifact, not a transcript of hidden internal cognition.

## Output and validation

An inspectable demonstration with relevant explanatory decisions. A worked arithmetic example can expose the unit choice and calculation. Such an example is a teaching artifact, not a measured account of the demonstrator's hidden reasoning.

## Limits

This procedural summary preserves the source's knowledgeable-instruction condition. Any use of a fallible AI demonstrator requires independent content checks described in the Practice.

## Source alignment

- [Allan Collins, John Seely Brown and Ann Holum](../references/collins-brown-holum-1991-cognitive-apprenticeship.md) — Method item 1: Modeling. Relation: **published-procedure-summary**. Inspection scope and nonclaims are in the record.

## Evidence status

**Provisional.** Source alignment records scholarly meaning and bounded support; it is not independent review of this paraphrase, an institutional endorsement, or validation of an AI implementation. Illustrations are constructed, not observed learner outcomes.
