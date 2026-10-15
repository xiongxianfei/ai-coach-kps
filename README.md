---
language: "KPS 9.x"
package_version: "0.4.0"
status: "draft"
---

# AI Learning Coach KPS

## Key takeaway

Teach a coherent lesson at the adult learner's preferred pace and preserve the evidence of what they actually did.

## Summary

A Practice-first, domain-independent knowledge package for independent adults using conversational AI as a learning coach. One self-contained master Practice coordinates the whole learning programme; five self-contained specialist Practices remain available independently. They are supported by source-aligned academic Concepts, Principles, Models and Methods. AI coaching workflows and prompts are explicitly authored applications, not established theories or tested programs.

## Understand the subject

The [body-of-knowledge outline](docs/body-of-knowledge-outline.md) shows nine connected knowledge domains behind AI coaching, one overall illustration, existing explanations and the topics still missing. Use it to understand what the subject covers. The learning Practices below apply that knowledge to a learner's goal; the outline is not a compulsory learning route.

## Start and stay in the master Practice

[AI-Assisted Learning Orchestration](practices/ai-assisted-learning-orchestration.md) is the primary entry for **overall target → learning stages → coherent lessons → assessment tasks**. Its seven procedural stages contain the planning, instruction, question–response–assessment loop, difficulty investigation, retrieval, revision and resume instructions **inline**. You do not need to open the five specialist files to carry out the master workflow.

**For a new broad subject, start with a brief learner self-assessment and (when appropriate) a small pre-instruction baseline check.** Then build a source-grounded map of the subject's major explanatory areas or subsystems, their boundaries and cross-links; propose a few high-level, revisable capability stages. These are not necessarily one stage per subsystem, and the plan is not a complete calendar of questions.

**Prepare the current coherent lesson:** connected explanation and examples → clarification opportunity → short assessment set → real learner responses → brief checked feedback → next lesson or focused repair. Follow the learner's pace; guided questions remain available when useful. For baseline or retrieval, the question may come before instruction. The coach waits for the reply, distinguishes assisted from independent evidence, and updates the high-level stages only when evidence or learner circumstances warrant it. A daily label is optional; it is not a KPS StageN or a compulsory deadline.

The master contains its own worked example, task card, assessment branches and blank resume record. References provide support and optional depth, not missing instructions. Subject-specific facts still need an inspectable source; a complete procedure does not make an AI an expert.

## Start with a Practice

| Current task | Entry Practice | Output |
|---|---|---|
| Coordinate the full learning journey in one file | [AI-Assisted Learning Orchestration](practices/ai-assisted-learning-orchestration.md) | Overall target, stage plan, coherent lesson, actual responses, bounded assessment and resume record |
| Orient to a subject and plan a learning route | [Concept Mapping and Instructional Sequencing With an AI Coach](practices/concept-mapping-and-instructional-sequencing-with-ai.md) | A panorama, goal map and evidence-revisable stage plan |
| Learn one concept or safe skill | [Self-Regulated Learning With an AI Coach](practices/self-regulated-learning-with-ai.md) | A target, source, original attempts, feedback and a next independent check |
| Understand a recurring task difficulty | [Formative Assessment With an AI Coach](practices/formative-assessment-with-ai.md) | Competing explanations, a probe and a justified instructional decision |
| Retain encountered material | [Retrieval and Distributed Practice With an AI Coach](practices/retrieval-and-distributed-practice-with-ai.md) | Checked questions, saved recall, corrections and a revisable review plan |
| Judge what was actually learned | [Evaluation of AI-Assisted Learning](practices/evaluation-of-ai-assisted-learning.md) | An evidence report separating assistance, retention and application |

Begin with the task that fits. The package does not require reading the full library or completing all six Practices. The master composes the specialist functions inline; the table also permits direct specialist entry. Each stage places actions, explanation and fallback together; stage numbers are a recommended route, not proof of prerequisites.

## Choose a coherent lesson

[Coherent lessons and the wider plan](guides/LEARNING-WORKFLOW.md) connects the goal, lesson capability, essential knowledge and assessment. A few short, complementary questions can be presented together after teaching. Feedback leads directly into the next lesson within the agreed scope, unless a blocking gap needs attention or the learner pauses. Each learning stage ends with a connected summary and one overview picture, saved with actual progress and remaining gaps in a private learning record outside public repositories. The subject panorama and adaptive stage plan provide orientation; a precise small task can still start directly. Lesson scope and interaction pace are adjustable, authored choices rather than universal learning laws.

## First use

1. For a broad goal, record a concise self-assessment and, if useful, a pre-instruction baseline response. Sketch the subject's source-grounded explanatory areas, selected connections and a small high-level stage roadmap. For an already bounded task, start directly without a compulsory survey; prior agreement and actual evidence can be reused.
2. Use the self-contained master for the continuing programme, or enter a specialist directly for a bounded need. Detail **the current lesson and assessment**, not all future days. Reuse agreement on scope and pacing, and state outputs, criteria, answer-help boundaries and when to stop or split. Do not paste private data or trust an uninspected AI bibliography.
3. Preserve your attempt before feedback. Record actual hints and answer exposure, not just what was requested.
4. Give a bounded interpretation and begin the next lesson or needed repair; summarize at stage boundaries. Stop when the learner pauses or the agreed goal is complete. A prompt does not create memory, scheduling, expertise or learning by itself.

## What is included

There are **26 knowledge objects**: seven Concepts, three Principles, six Models, four Methods and six Practices, with **35 procedural stages** across the Practices. Twenty-two Reference records document inspected source scope. Use the [knowledge index](docs/INDEX.md) for Practice stages and academic objects; [claim records](data/claims.json) preserve source premises and application limits.

The Models include two published frameworks, Cognitive Apprenticeship and the Assessment Triangle, and four explicitly authored domain syntheses: [Knowledge Representation](models/knowledge-representation.md), [Instructional Design](models/instructional-design.md), [Instruction and Scaffolding](models/instruction-and-scaffolding.md), and [Assessment and Feedback](models/assessment-and-feedback.md). Each embeds its own overview illustration and connects source-grounded explanations without claiming a published unified theory or a validated AI intervention. The Methods summarize published Retrieval Practice, Self-Explanation and Cognitive Modeling. Concept Map and Concept Mapping use the Novak and Cañas report. The two-level workflow is an authored Practice, not a newly invented academic Model or a validated learning progression. See [the planning record guide](guides/LEARNING-WORKFLOW.md). Distributed practice scheduling is implemented inside a Practice; abstract-only source access was not inflated into a detailed standalone scientific protocol.

## Evidence and outcome boundaries

The full package remains **provisional**. Some definitions are supported by selected full passages, others only by publisher abstracts. No systematic review, independent expert approval, learner study, model evaluation or live coaching trial is claimed. A scientific source does not validate every AI application derived from it.

General learning research and AI-specific studies are distinguished. A structured college physics tutor and a high-school mathematics field experiment do not directly establish effectiveness for every self-directed adult or generic chatbot. [Review](docs/REVIEW.md) records inspection, indirectness, open questions and specific remaining work.

## Architecture and independence

KPS role describes the job of a document, not its subject. Original assistance choices, prompts and local evaluation rules stay in Practices and supporting specifications. Domain Models may integrate inspected source contributions under explicitly declared authorship and limits; original coaching procedures remain in Practices. [ALIGNMENT](docs/SCIENTIFIC-POLICY.md) explicitly adopts a domain version of Core's professional source-alignment policy.

This repository stands alone. It does not require the English Linguistics or Learning and Teaching KPS packages, an Obsidian plugin, an API key or an installed agent. It is knowledge and guidance, not a deployed chatbot. Ordinary relative Markdown links work without a knowledge-graph viewer.

## Repository layout

The root holds the reader entry, agent instructions, licence and attribution, validator and integrity metadata. Authoring and review guidance live in `docs/`; contribution guidance lives in `.github/`. Use [learning workflow](guides/LEARNING-WORKFLOW.md), [private-session records](guides/SESSION-RECORDS.md) and the [worked example](guides/WORKED-EXAMPLE.md) for learner tasks. The [knowledge index](docs/INDEX.md) combines Practice entry points, stage links and academic objects. Canonical names, source alignments and claim records remain in their owning files.

Maintainers use the [scientific and scope policy](docs/SCIENTIFIC-POLICY.md), [validation and compatibility](docs/VALIDATION.md), [reader and diagram guide](docs/READING-AND-DIAGRAMS.md), and [scientific review](docs/REVIEW.md). The existing knowledge types remain in the five original role folders; references, tests and tools remain separately organized.

**Root cleanup changes document locations**. Links to former root-level guide or generated files will need updating in external notes. Stable KPS knowledge IDs, Practice stage anchors, the 10.2.0 Core lock and the 9.1.0 validation semantics are unchanged. See the mapping table in [validation and compatibility](docs/VALIDATION.md) before migrating external links.

## Check locally

Python 3.10 or newer and the standard library are sufficient.

```bash
python3 validate.py .
python3 tools/check_domain.py
python3 tools/build_navigation.py --check
python3 -m unittest discover -s tests -v
```

These commands check structure and declared boundaries, not educational efficacy. See [CHECKS](docs/VALIDATION.md). Blank [session records](data/session-record-template.json) and a [record guide](guides/SESSION-RECORDS.md) are provided for private use. Do not publish completed personal records.

## Versions and rights

Domain package: 0.4.0. Based on KPS Core **10.2.0**, authoring language **9.x**, structural validator **9.1.0**, Practice format **steps-first-v1**. [COMPATIBILITY](docs/VALIDATION.md) and [upstream lock](upstream-lock.json) identify the exact sources; the domain is not version 10.2.0 merely because Core is.

Original content and copied KPS tooling use the retained MIT license. Third-party publications retain their rights and are linked, not mirrored. See [NOTICE](NOTICE.md) and [CONTRIBUTING](.github/CONTRIBUTING.md).
