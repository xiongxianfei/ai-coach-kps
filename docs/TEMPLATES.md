---
package_version: "10.0.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---


# Reusable authoring templates

## Key takeaway
These are non-normative examples implementing the [authoring contract](AUTHORING.md).

A template supports the job of the knowledge type; it does not prove correctness or require every field to become a file.

## Summary
All objects need identity, meaning, locally sufficient content, scope and support. Copy only the useful fields, replacing placeholders with real content. The examples below are fenced templates, not live published knowledge. Reference records support the five knowledge types rather than becoming a sixth type.

## Common metadata
```yaml
---
id: "domain:method:meaningful-identity"
type: "method"
version: "1.0.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
uses_principles: []
uses_models: []
references: []
---
```
For the optional dependency-free checker, write metadata values in JSON-compatible YAML as shown. General Markdown content does not depend on that checker.

## Common opening
```markdown
# Meaningful title

## Key takeaway
One useful sentence stating the object itself.

## Summary
What it means, why it matters, how it is used and its main limit.
```

## Concept content
Definition; necessary distinctions; recognizable example and non-example; why it matters; boundaries and evidence; optional deeper links. Do not force procedures into a vocabulary note.

## Principle content
Declarative Statement; explanatory mechanism or relationship; evidence-supported premises; explicit derivation; independently useful applications; limits; possible challenge. Do not disguise a selected instruction as a universal truth. Scientific and domain levels can be metadata; formal or design reasoning must be labelled rather than invented as experiment.

## Model content
Purpose; necessary terms; actual representation; relationships; assumptions; implications; how to evaluate; evidence and limitations. Summarize necessary dependencies inline instead of linking away the explanation.

## Method content
Objective; inputs and prerequisites; rationale; numbered procedure; expected effect; observations and counter-signals; limits or stop conditions; example; deeper evidence. A new comparison procedure is a proposal until used; examples do not establish effectiveness.

## Practice content

Use the [authoring contract](AUTHORING.md#practice-responsibilities) for required responsibilities and format. The following is a minimal starting point, not a required sequence of supporting headings. Add the common identity metadata with `type: "practice"` and `practice_format: "steps-first-v1"`; the package must declare a minimum compatible checker of 9.1.0 or later.

```markdown
> **Template guidance — remove before use**
>
> Adapt the stage names, number, order and detail to the task. Keep actions,
> essential reasoning, observations and next decisions locally usable.
> Combine these responsibilities where natural; add support only where useful.
> Explain how users judge results and adapt the approach. Include previous
> outcomes when supported, and distinguish proposed from demonstrated improvements.

# Practice name

## Key takeaway

The central action or decision this Practice helps the reader make.

## Summary

The intended outcome, scope and necessary starting conditions.

## Stage map

1. [Stage1 Meaningful action](#stage1-meaningful-action)

## Stage1 Meaningful action

1. Describe an action with the context and reason needed to carry it out.
2. Explain how to interpret its result and choose the next action or finish.

## Current practice summary

Actual application and observations: not recorded.
```

Replace the placeholders and update links as stages are added or renamed. The two numbered lines illustrate combining responsibilities; they are not a two-step requirement. A decision table may be clearer for a branching task. No separate rationale, worked-example, diagram, prompt or record section is compulsory. Keep important limits and source support beside the relevant claim or action.

Draft the target Practice early and refine its actions with the supporting knowledge. For a learning Practice, an output may be an explanation or analysis; state what makes it adequate and what evidence is still missing. Reuse existing explanations without copying their whole documents. Practice composition remains optional and must not create circular containment.

The existing [master coaching Practice](../practices/ai-assisted-learning-orchestration.md) supplies inline decisions, while the [worked examples](../guides/WORKED-EXAMPLE.md) illustrate possible applications. Their topics, stage counts and presentation choices are not additions to the contract. Review a representative task with links hidden: can the reader begin, act, interpret a normal or uncertain result and choose what follows? Record an author walkthrough separately from an independent learner trial.

## Reference content
Publication identity, creators, publication or update year and its basis, external URL or DOI, actual access date and extent, located claims, evidence family, limitations and non-claims. Use creator-year-short-title filenames, or `undated` when a date was not established. The record must summarize what the source contributes without requiring immediate external access; it is not a copy of the publication.

## Review before publication
Hide links and attempt the intended use; restore links and check the summary remains faithful. Check claim-source fit, headings and fragments, then run the package checker. [Authoring](AUTHORING.md), [Navigation](READING-AND-DIAGRAMS.md) and [Compatibility](VALIDATION.md) provide the complete local maintenance instructions.

## Core source alignment example

```yaml
source_alignment: [{"reference":"kps:r:skos","relation":"definition-paraphrase","locator":"Sections 3 and 5"}]
```

Record the actual source and locator, its meaning and boundary, and any qualification. This declaration is not a formal equivalence mapping. KPS-specific authoring routines belong in Practices rather than new generic Methods. The five role labels remain our local organization.
