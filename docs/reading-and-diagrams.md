---
language: "KPS 9.x"
package_version: "0.4.0"
status: "draft"
---

# Reading navigation and diagrams

## Key takeaway

Use direct local links and simple explanation aids without requiring a special viewer or image quota.

## Summary

This guide combines the navigation profile and the selective visual-explanation policy. Tables and text remain appropriate where an image would not resolve ambiguity.

## Navigation and reading

These conventions help readers move between independently complete documents; a link is not a replacement for necessary guidance.

## Reading routes

The [knowledge index](index.md) combines Practice entry points, stage links and academic objects by role. Canonical naming and source alignments remain in each object; [claim records](../data/claims.json) preserve source support and application limits. Reference inspection limits and the owning knowledge documents identify remaining inspection and explanation gaps.

The [body-of-knowledge outline](body-of-knowledge-outline.md) organizes coverage by knowledge domain, with topic-aligned explanations and gaps. It complements the generated index and does not prescribe a learning sequence.

## Link procedure

1. Prefer a relative file link for an entire object.
2. For a stage, include the full lowercase heading fragment, such as #stage1-define-a-learning-goal-and-constraints.
3. After renaming a heading, update the stage map, metadata and incoming links together.
4. Test the actual reader when rendering matters; structural validation is not a click test in every Markdown application.

The generated graph is a dependency view, not a model of human cognition or a compulsory reading sequence. No plugin or iframe is required.

## Selective visual explanations

Diagrams are used when they clarify a relationship, not to satisfy an illustration quota.

## Master reading route

The master Practice contains a text hierarchy, task card, conditional assessment table and complete resume format. These are inline representations, not links to a missing application. Read the relevant procedural stage after resuming; there is no requirement to reread the whole document or render a graph.

## Current audit

The five specialist Practices and the master use point-of-use decision and evidence tables. Their branch conditions and next actions are readable without graphics. Cognitive Apprenticeship is represented as a four-dimension table, not a newly invented six-stage cycle. The Assessment Triangle has a text triad with explicit noncausal edge meaning. The source and reference declarations remain in the owning Models.

These relationships are sufficiently compact for text, so no D2/SVG assets are claimed or required. This is a selective-format decision consistent with the Core contract's allowance for simple text diagrams and tables; it is not a claim that visual instruction is ineffective.

The overview Practice adds a compact text flow and local tables. Conceptual connections, selected-goal links, stage requirements and feedback decisions are explained separately. The text layout does not imply that knowledge forms a prerequisite tree.

The body-of-knowledge outline owns one overall PNG illustration and its generation prompt in `diagrams/`. It shows nine knowledge domains and three selected connections, with the same content available as text in the outline. It is an original AI-generated orientation aid, not a metadata dependency graph or evidence of visual-learning effectiveness. Additional subtopic illustrations are optional and chosen for reader need.

Each developed domain Model owns one overall summary illustration, embedded after its introduction and before Contents, with meaningful alternative text and a short explanation. Develop the Model's explanation first, then illustrate its key ideas and relationships. Store the PNG and prompt together under `diagrams/` using the domain name. The outline links to the Model rather than duplicating its image. Additional detail illustrations remain optional.

The [Assessment and Feedback Model](../models/assessment-and-feedback.md) owns `assessment-and-feedback-overview.png` and its matching prompt. It illustrates criteria, task conditions, the actual response, bounded interpretation, feedback and a distinct new observation, alongside the Model's constructed unit-price comparison. The [Knowledge Representation](../models/knowledge-representation.md), [Instructional Design](../models/instructional-design.md), and [Instruction and Scaffolding](../models/instruction-and-scaffolding.md) Models also embed their own PNG summaries with matching prompts. The instruction illustration connects explanation, activity, actual response and adjusted support, with a constructed equal-sharing example. The remaining domain summaries will accompany their Models as those explanations are developed; an outline gap is not a completed Model to illustrate.

## Future image procedure

1. Identify an actual ambiguity the diagram would resolve and document its owner and scope.
2. Use D2 for a useful editable diagram and keep the generated SVG alongside it; retain attribution and labels for synthetic examples. For an AI-generated overview illustration, keep its prompt beside the image and describe provenance in the owning document.
3. For D2 outputs, register owner, reason and files in diagrams.json and include actual pinned-render checks before claiming freshness. A generated PNG is visually inspected against its owning text; it has no D2 freshness claim and does not require a new renderer or registry.
4. Inspect the rendered result for legibility and preserve the text explanation. Do not hand-edit generated SVG or imply an effect-size chart is measured when its data are invented.

No D2 renderer check is applicable because no D2 artifact is included. Each PNG must be inspected for accurate labels, relationships, examples and legibility against its owning text when changed. Keep essential meaning in text and avoid duplicate full-size image links.
