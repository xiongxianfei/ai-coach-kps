---
id: "ai-coach:method:spaced-repetition"
type: "method"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "Spaced Repetition"
evidence_status: "provisional"
reviewed: null
basis_kind: "KPS-authored reusable adaptation combining delayed review and retrieval with feedback; not an optimized scheduling algorithm"
references: ["ai-coach:reference:pashler-2007-organizing-instruction"]
uses_principles: ["ai-coach:principle:spacing-effect", "ai-coach:principle:testing-effect"]
source_alignment: [{"reference": "ai-coach:reference:pashler-2007-organizing-instruction", "relation": "published-procedure-summary", "locator": "Recommendation 1, printed pages 5 to 7; Recommendation 5b, printed page 21, opening recommendation"}]
---

# Spaced Repetition

## Key takeaway

Revisit important learned material on separated occasions, preserve recall before correction and revise future reviews using actual performance and the intended retention horizon.

## Summary

This Method operationalizes spaced review through retrieval and checked feedback. The IES guide supplies delayed revisiting and recall with correction; the scheduling decisions here are authored adaptations. The [Spacing Effect](../principles/spacing-effect.md) concerns timing, while [Retrieval Practice](retrieval-practice.md) concerns what the learner does during a review. Neither specifies an individualized scheduling algorithm.

## Use when and prerequisites

Use this for material already encountered that must remain available later and is not sufficiently revisited through ordinary use. Identify the future use, relevant content, checked prompts and answers, and a practical place to keep the review record. If the learner never understood the relation, teach it before interpreting a failure to retrieve it.

## Rationale and procedure

The IES guide recommends returning to important content after delays and using recall quizzes with correct-answer feedback. Its classroom recommendations include reviews weeks or months later. That basis supports separated review, not one mandatory calendar for every adult or topic.

The following decisions make the approach usable without specialized software:

1. Select a manageable set of facts, relationships or procedures relevant to the goal. Phrase each prompt so its answer can be checked; avoid ambiguous fragments whose correctness depends on hidden context.
2. Choose a later review occasion and record why it fits the intended use and available time. Include existing meaningful practice when planning workload rather than adding duplicate reviews automatically.
3. At the review, attempt retrieval before viewing the answer. Preserve the response and record actual elapsed time, hints and answer exposure. Then inspect the checked answer, explain consequential differences and correct the record.
4. Decide what happens next. After a successful independent response, consider a longer gap if it fits the goal. After a failure, repair the knowledge or prompt and arrange an earlier check than previously planned. These are revisable heuristics, not proven optimal interval rules.
5. Retire, combine or reduce low-value items as the goal changes. Include a later application task when the goal requires using knowledge; remembering a card does not establish that capability.

Repeated difficulty can indicate a bad question, missing understanding or excessive workload. Investigate those possibilities before merely shortening every interval.

## Worked application

**Constructed scheduling example:** A learner wants to retain the distinction between a package price and a unit price for use over the next month. After instruction, they schedule a review two days later and another a week after that. These dates are convenient trial choices, not an optimum derived from the source.

One prompt asks for the price per kilogram of a 750 g package costing £3 and the meaning of the result. The checked answer is £4/kg. The learner's response must be saved before revealing it. If the numerator and denominator are reversed, revisit what each quantity counts and make a new check sooner. If the response is independent and justified, retain the planned later occasion or lengthen the gap within the retention goal.

Use a different package comparison later to inspect application. Record each actual date; a missed review stays missed. Resume from the available evidence instead of manufacturing a successful streak or assuming all knowledge was lost.

## Output and validation

Keep the prompt and answer basis, original recall, correction, actual assistance, elapsed interval and next planned review. Judge the method by what is available after a delay under the intended conditions, not by the number of cards completed. Compare records cautiously when questions or support change. One successful review does not establish durable retention.

## AI role and limits

AI can draft prompts, help verify answers and propose a schedule from the supplied record. It cannot observe unreported reviews or create reminders, persistent memory or background scheduling merely through instructions. The learner retrieves; a source, executable check or competent reviewer supplies the verification basis.

[Interleaved Practice](interleaved-practice.md) changes which task types occur together. Spacing changes when material returns; the two can be combined. A short fixed countdown or repeated rereading should not be presented as evidence of independent recall.

## Source alignment

[Pashler and colleagues](../references/pashler-2007-organizing-instruction.md), Recommendation 1, pages 5–7, and the opening of Recommendation 5b, page 21, support the procedural basis. The schedule, interval-adjustment heuristics and example are authored and untested. No particular software algorithm is adopted.

## Evidence status

**Provisional.** Published learning findings do not validate this scheduling implementation or establish outcomes for independent adult AI coaching.
