---
id: "ai-coach:model:knowledge-representation"
type: "model"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "Knowledge Representation"
evidence_status: "provisional"
reviewed: null
basis_kind: "KPS-authored source-grounded explanatory synthesis; not a published unified theory or validated AI intervention"
uses_concepts: ["ai-coach:concept:concept-map"]
references: ["ai-coach:reference:novak-canas-2008", "ai-coach:reference:pashler-2007-organizing-instruction"]
source_alignment: [{"reference":"ai-coach:reference:novak-canas-2008","relation":"synthesis-contribution","locator":"Introduction and Constructing Good Concept Maps","contribution":"Concepts, labeled propositions, focus questions, hierarchy, cross-links and revision"},{"reference":"ai-coach:reference:pashler-2007-organizing-instruction","relation":"synthesis-contribution","locator":"Official recommendation overview, recommendations 3 and 4","contribution":"Connecting graphical with verbal and abstract with concrete representations; overview-level support only"}]
---

# Knowledge Representation

## Key takeaway

A useful representation makes the subject's important relationships explicit while preserving their meaning, scope and uncertainty. Its organization helps someone reason about a question; it does not by itself establish a teaching order or show what a learner knows.

## Summary

This Model explains the external representations used to organize knowledge for learning: outlines, concepts, propositions, diagrams, examples and their connections. It draws on concept mapping and guidance about connecting representations, with an original unit-price example. No prior mapping terminology is required. The account is a KPS-authored synthesis, not a formal ontology, a model of internal cognition or a complete theory of knowledge representation in artificial intelligence.

![Knowledge Representation connects a focus question, concepts and boundaries, labeled relationships, and complementary representations. The constructed example relates price and mass to unit price. A subject outline shows coverage, a concept map shows relationships, and a learning route proposes an order.](../diagrams/knowledge-representation-overview.png)

The illustration separates three outputs that can look similar but answer different questions. Its calculation is £3 divided by 0.6 kg, giving £5/kg. The image table scales the same rate from 0.6 kg at £3 to 1 kg at £5; its second row is not package B from the comparison below. The map does not establish that the reader can perform or explain that calculation. Original illustration generated with the built-in image generation tool; [generation prompt](../diagrams/knowledge-representation-overview.prompt.txt).

## Contents

- [Scope and explanatory responsibility](#scope-and-explanatory-responsibility)
- [Concepts propositions and relationships](#concepts-propositions-and-relationships)
- [Domains subsystems and interfaces](#domains-subsystems-and-interfaces)
- [Outlines maps and learning routes](#outlines-maps-and-learning-routes)
- [Connected representations](#connected-representations)
- [A connected comparison example](#a-connected-comparison-example)
- [Sources uncertainty and revision](#sources-uncertainty-and-revision)
- [Interfaces with other domains](#interfaces-with-other-domains)
- [Limits and unresolved coverage](#limits-and-unresolved-coverage)
- [Source alignment](#source-alignment)
- [Evidence status](#evidence-status)

## Scope and explanatory responsibility

An external knowledge representation selects something about a subject and expresses it in words, symbols, pictures or another inspectable form. Selection is unavoidable: a shopping comparison can represent price and mass without representing packaging chemistry. The question determines which omissions matter.

Here the focus question is **how to compare prices when package quantities differ**. It includes quantity, units, division and the meaning of a rate. It excludes preferences about taste, nutrition and storage. Consequently, the answer can identify lower price per kilogram without establishing the best purchase for a particular person.

The explanatory relationship used throughout this Model is:

```text
Question and scope select relevant concepts and relationships.
Relationships expressed as claims connect the concepts.
Representations and examples make those claims inspectable.
Sources and counterexamples constrain what the claims warrant.
```

This is our organizing account, not a causal theory of how every learner acquires knowledge. A representation can be internally consistent yet factually wrong, or correct yet unsuitable for the learner's current question.

## Concepts propositions and relationships

A **concept** names a general idea, such as mass or unit price. A **proposition** expresses a claim by connecting concepts: “unit price expresses price per unit quantity.” In Novak and Cañas's account, labeled links carry the meaning of a concept map; hierarchy and cross-links organize those propositions around a focus question. The construction process includes revision. See the [inspected report record](../references/novak-canas-2008-concept-maps.md).

Different links answer different questions. In our example:

| Relationship | Example | What the relationship does not establish |
|---|---|---|
| Classification | Price per kilogram is a unit price | Which calculation the learner can perform |
| Quantitative definition | Price divided by mass gives price per unit mass | Whether mass is the appropriate purchase criterion |
| Equivalence | 600 g and 0.6 kg express the same mass | That their numerical values are interchangeable without conversion |
| Comparison | £4.50/kg is less than £5/kg | That the larger package has the lower total cost |
| Proposed prerequisite | This task requires interpreting kilograms | That every rate lesson must begin with a separate conversion lesson |

An unlabeled line cannot distinguish these meanings. An arrow also needs a direction and interpretation: “mass determines unit price” would omit price as another input. “Price and mass determine unit price” is more precise under the stated positive-mass condition. A picture of two connected boxes does not repair an incomplete claim.

## Domains subsystems and interfaces

A **domain** groups related explanatory questions. A **subsystem** is useful when the subject supports an account of interacting parts with identifiable responsibilities. Neither term requires an exclusive partition of all knowledge. The grouping must earn its place by explaining something and preserving a useful distinction.

For the constructed comparison, measurement explains what the quantities and units denote; rate reasoning explains the quotient; decision criteria explain which comparison answers the purchase question. Their interface is concrete: the rate calculation consumes a price and a mass expressed in a declared unit, and produces a quantity with units such as pounds per kilogram. The purchase decision interprets that output under a criterion.

These are analytical concerns for this example, not a proposed universal decomposition of mathematics. For another subject, established disciplinary sources should determine the candidates. A coach's ability to invent plausible names does not establish that they are accepted divisions. A topic can cross several domains; explicit interfaces often explain this overlap better than creating another category.

## Outlines maps and learning routes

| Representation | Question answered | Example and boundary |
|---|---|---|
| Body of knowledge outline | What needs to be covered? | Quantities, units and rates belong in coverage; listing them supplies no mechanism |
| Concept map | How do selected ideas relate? | Equivalent units preserve the represented mass; an edge needs an explicit claim |
| Explanatory Model | How does a connected part work? | A rate relates two quantities; equations, assumptions and examples explain its use |
| Learning route | What capabilities might this learner develop next? | Interpreting a rate may come before a harder comparison; the order is a design proposal |
| Learner response | What did the learner actually produce? | An explanation of why conversion is needed provides evidence under its conditions |

The distinctions matter when a coach reads a polished map. The map may have been generated entirely by AI. Its completeness therefore says nothing by itself about the learner's understanding. Conversely, a learner may reason accurately without using the author's preferred layout. Assessment needs the actual response and an appropriate criterion.

## Connected representations

A verbal explanation, equation and table can express overlapping aspects of the same relationship. The IES overview recommends connecting graphical and verbal presentations, and concrete and abstract representations. It does not establish that adding any picture improves any lesson. [Source and inspection limits](../references/pashler-2007-organizing-instruction.md).

In our example, the package label gives a concrete pair of quantities, the table aligns units, and the equation states how to calculate the rate. Translation is useful only if meaning survives. Changing “£3 for 600 g” into “£3/kg” loses the denominator and changes the claim. A decorative package picture without legible quantities supplies no missing relationship.

The representations also omit different information. An equation may hide why the calculation is relevant; prose can explain the criterion but leave the arithmetic ambiguous. Their connection is substantive when the reader can point to the same price, mass and unit rate in each.

## A connected comparison example

Assume comparable products, positive masses, no extra fees and a criterion of lowest price per kilogram. These invented values illustrate the representation; they are not shopping advice or learner data.

| Package | Price | Mass as labeled | Mass in kilograms | Unit price |
|---|---|---|---|---|
| A | £3.00 | 600 g | 0.6 kg | £3.00 / 0.6 kg = £5/kg |
| B | £4.50 | 1 kg | 1 kg | £4.50 / 1 kg = £4.50/kg |

The quantity is preserved by conversion: 600 g × (1 kg / 1000 g) = 0.6 kg. Dividing price by that mass expresses how much one kilogram would cost at the same rate. With the common denominator unit, 4.50 is less than 5, so B has the lower unit price. A still requires less total money for one package. Both statements can be true because they answer different questions.

The connected explanation is therefore:

```text
Package labels provide price and mass.
Unit conversion preserves mass while changing its numerical expression.
Price / mass gives a unit price.
A common unit makes the two numerical rates comparable.
The chosen criterion makes the lower rate relevant to the decision.
```

If the criterion changes to “spend at most £3 today,” B no longer satisfies it. That change does not refute the rate calculation; it changes the decision boundary. If the learner divides 3 by 600 and compares the result directly with 4.50, the issue is mixed rate units: pounds per gram versus pounds per kilogram. A correct representation exposes the distinction instead of merely labeling the final choice wrong.

## Sources uncertainty and revision

Three judgments remain separate: whether a proposition is supported, whether it is relevant to this scope, and whether a learner understands it. Our arithmetic can be checked directly. A claim about a disciplinary boundary needs subject sources. A claim about effective teaching needs evidence about learning under relevant conditions.

Provenance connects a claim to the passage or calculation that supports it. It also records limits: a table of contents identifies a topic, but does not supply its explanation. Where sources disagree, the disagreement may concern definitions, assumptions or evidence. Recording the competing claim and its conditions is more informative than silently selecting whichever fits a diagram.

The practical representation can change without claiming that the underlying subject changed. For example, adding a budget criterion expands this comparison's scope; correcting a mixed-unit equation repairs an error. The reasons differ and should remain intelligible. These are KPS authoring distinctions, not a comprehensive theory of source evaluation.

## Interfaces with other domains

[Instructional Design](instructional-design.md) uses represented relationships to propose capabilities and tasks, but adds learner evidence and constraints. Instruction and scaffolding uses examples and representations to explain those relationships. [Assessment and Feedback](assessment-and-feedback.md) interprets the learner's use of them. Learning and cognition concerns internal understanding, which cannot be read directly from a supplied diagram. Human–AI interaction concerns whether sources were accessible and whether the AI generated or merely repeated the representation.

## Limits and unresolved coverage

This introductory account covers the six outline topics at unequal depth. It does not supply a formal domain-analysis method, an ontology language, a theory of internal mental representation, or a comprehensive account of evidence appraisal. Detailed mechanisms and conditions for learning with multiple representations need further source inspection. The example validates its own arithmetic, not the instructional effectiveness of these maps. No fixed number of domains, concepts or links is implied.

## Source alignment

- [Novak and Cañas](../references/novak-canas-2008-concept-maps.md): Introduction and Constructing Good Concept Maps support the map vocabulary and focus-question approach. Their full theoretical claims and cited studies were not reviewed here.
- [IES instruction overview](../references/pashler-2007-organizing-instruction.md): recommendations 3 and 4 support connecting representations. The overview does not substitute for the full guide or underlying studies.

The distinction among outlines, Models, routes and evidence, the domain interfaces, and the unit-price example are authored integration. Neither source publishes this entire Model or validates its AI application.

## Evidence status

Provisional source-grounded explanatory synthesis. No independent scientific review, observed learner outcome or validated AI intervention is claimed.
