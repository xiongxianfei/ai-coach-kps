---
language: "KPS 9.x"
package_version: "0.4.0"
status: "draft"
reviewed: null
---

# AI Coach Body of Knowledge Outline

This outline describes the knowledge needed to help independent adults understand, practise, retain and apply a subject with conversational AI. It supports readers who want to understand coaching decisions and authors who need to see what the library still lacks.

## Key takeaway

Understand the connected knowledge areas behind coaching, then use a learning Practice to apply them to a learner's goal.

## Summary

Nine areas organize the subject by explanatory responsibility. Each section names the topics to cover, aligns existing explanations with those topics and makes gaps visible. This is a project coverage outline, not a universal taxonomy, a validated curriculum or a claim that nine independent mechanisms explain all learning. Numbering supports navigation and does not prescribe a study order.

## Overview

![Nine AI Coach knowledge areas: Learning and cognition; Knowledge representation; Instructional design; Instruction and scaffolding; Assessment and feedback; Memory and transfer; Motivation and self-regulation; Human–AI interaction; Evaluation of AI-assisted learning. Selected connections show representation informing design, assessment adjusting instruction, and retention and transfer supplying evaluation outcomes.](../diagrams/body-of-knowledge-overview.png)

The areas answer different questions about the same learning situation. Knowledge representation informs instructional design; assessment and feedback can adjust instruction and scaffolding; memory and transfer supplies outcomes for evaluation. These are selected connections, not a complete causal model or a sequence of compulsory stages. The text below contains the essential content independently of the image.

Original AI-generated illustration, produced for this project with the built-in image generation tool. No third-party figure was copied. The [generation prompt](../diagrams/body-of-knowledge-overview.prompt.txt) records the intended labels and relationships; the illustration makes no measured-effect claim.

## Overall outline

| Area | Responsibility | Main coverage |
|---|---|---|
| [Learning and cognition](#learning-and-cognition) | Explain how understanding and skill develop | Prior knowledge; attention; working memory; cognitive load; mental representations; conceptual change; expertise; context |
| [Knowledge representation](#knowledge-representation) | Represent what a subject contains and how its ideas connect | Boundaries; concepts and propositions; explanatory subsystems; concept maps; multiple representations; source grounding |
| [Instructional design](#instructional-design) | Translate a capability goal into a justified learning design | Objectives; task analysis; prerequisites; sequencing; task difficulty; alignment; adaptation |
| [Instruction and scaffolding](#instruction-and-scaffolding) | Explain how assistance supports increasingly independent activity | Explanations; worked examples; modeling; questioning; self-explanation; scaffolding and fading; guided and independent practice |
| [Assessment and feedback](#assessment-and-feedback) | Interpret responses and inform improvement | Baselines; evidence and criteria; assessment quality; error interpretation; feedback; assistance conditions |
| [Memory and transfer](#memory-and-transfer) | Explain availability and use of learning over time and contexts | Encoding and forgetting; retrieval; spacing; interleaving; retention; transfer |
| [Motivation and self-regulation](#motivation-and-self-regulation) | Explain how learners direct and sustain learning | Goals and values; self-efficacy; agency; planning and monitoring; calibration; reflection; emotion and social support |
| [Human–AI interaction](#human-ai-interaction) | Explain the possibilities and limits of learning through an AI interface | Dialogue; grounding and verification; context and tools; reliance; accessibility; privacy and control |
| [Evaluation of AI-assisted learning](#evaluation-of-ai-assisted-learning) | Judge the quality and effects of the coaching approach | Outcomes; comparisons; confounding; generalizability; usability; unintended effects |

## Scope and boundaries

The unit of interest is an adult learner using a conversational AI with suitable subject material. The outline includes knowledge about learning, instruction, evidence and the interaction medium. Language, culture, prior experience, disability and access conditions cut across the areas; they are not fixed learner types.

Subject facts remain owned by the relevant subject library. English phonology, for example, is content that a coach may help someone learn; the AI Coach library explains how to select, support and interpret that learning activity. Model training, deployment infrastructure, clinical diagnosis, credentialing and institutional policy administration are outside the present scope. Relevant interface limits and privacy responsibilities remain in scope.

A knowledge area groups explanatory questions. A subsystem Model would need to explain a coherent set of entities, relationships, mechanisms and interfaces. This outline does not assert that every area is already such a subsystem. The existing Cognitive Apprenticeship and Assessment Triangle files retain their published identities and can contribute to more than one area. New Models must satisfy the [source-alignment policy](SCIENTIFIC-POLICY.md); an empty coverage row is not a reason to invent a theory.

## Reading coverage

The table entries describe document coverage, not learner achievement or scientific approval. **Partial** means a local explanation covers a named subset; **source only** means a relevant source record exists but a local explanation is missing; **gap** means the topic needs a suitable inspected basis and an explanation. No entire area is marked complete. Source access may be limited even when a local explanation exists.

The tables link explanatory knowledge and sources. Authored coaching Practices are applications and do not count as academic coverage merely because they mention a topic. Topics can appear at several interfaces without requiring duplicate canonical definitions or one file per row.

## Learning and cognition

This area asks how a learner develops a usable understanding or skill. It concerns the processes and representations involved in learning; instructional design concerns how to arrange opportunities to learn. Memory is introduced here as a cognitive process and developed under Memory and transfer for retention and later use.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Prior knowledge and understanding | How existing knowledge relates to interpretation, integration and mistaken assumptions | Partial: [Concept Map](../concepts/concept-map.md) represents relationships; a mechanism-level account of prior knowledge is missing |
| Attention and working memory | Selection of information, temporary maintenance and task demands | Source only: [How People Learn II overview](../references/nasem-2018-how-people-learn-ii.md) locates the relevant chapters; detailed passages still need inspection |
| Cognitive load | Demands created by the task, its presentation and the learner's available knowledge | Gap: inspect appropriate cognitive-load theory and boundary evidence before recommending task-size rules |
| Mental representations and conceptual change | How concepts, explanations and procedures are represented, challenged and revised | Gap: an external concept map is not itself a model of the learner's internal representation |
| Expertise and skill development | Differences in organized knowledge, strategies and increasingly independent performance | Partial: [Cognitive Apprenticeship](../models/cognitive-apprenticeship.md) describes expert content and supported participation; a fuller account of expertise is missing |
| Context and individual variation | Learning across situations, cultures, languages and adult circumstances | Source only: [How People Learn II overview](../references/nasem-2018-how-people-learn-ii.md); domain applicability and adult variation need local explanation |

## Knowledge representation

This area asks what belongs in the subject and what relationships make it understandable. Its output is a representation of knowledge. Instructional design separately decides which relationships matter for a learner's route; a conceptual connection does not establish a prerequisite.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Subject boundaries and explanatory areas | Scope, omissions, responsibilities and useful overlap between areas | Gap: current outlines are authored coverage choices; no standalone scholarly account of domain analysis is included |
| Concepts and propositions | Terms, meanings and labeled relationships that express a claim | Partial: [Concept Map](../concepts/concept-map.md) defines the representation and its limits |
| Explanatory subsystems and interfaces | What each system explains and how its variables or outputs connect to another | Gap: selecting appropriate domain systems needs inspected subject sources; the coach must not invent a universal partition |
| Concept mapping | Focus questions, hierarchy, cross-links and revision | Partial: [Concept Mapping](../methods/concept-mapping.md) gives the operation; map accuracy remains a separate check |
| Multiple representations | Relationships between verbal, graphical, concrete and abstract accounts | Source only: [IES recommendation overview](../references/pashler-2007-organizing-instruction.md); detailed conditions need inspection |
| Source grounding and uncertainty | Provenance, inspected scope, conflicting accounts and revisable claims | Gap: repository policies specify authoring behavior; broader knowledge about source evaluation is not yet explained |

## Instructional design

This area asks how a goal becomes a coherent set of learning opportunities. It concerns proposed capabilities, tasks and their relationships. Instruction and scaffolding concerns the help offered during those tasks; assessment examines what responses support concluding.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Capability objectives and alignment | Observable capabilities and matching content, activities and criteria | Partial: [Assessment Triangle](../models/assessment-triangle.md) aligns competence, observation and interpretation; instructional-design coverage is incomplete |
| Task analysis | Component demands, integration and meaningful units of work | Gap: no standalone account; one task at a time is currently an authored workflow choice |
| Prerequisites and corequisites | Required preparation, helpful background and capabilities learned together | Gap: a map edge alone does not justify a required-before relation |
| Sequencing and learning progressions | Complexity, diversity and evidence for proposed routes | Partial: [Cognitive Apprenticeship](../models/cognitive-apprenticeship.md); [learning-progressions source](../references/national-research-council-2007-learning-progressions.md) bounds terminology |
| Task difficulty and practice selection | How demand changes with knowledge, support and the target capability | Partial: [Instructional Scaffolding](../concepts/instructional-scaffolding.md) covers support; difficulty selection needs deeper treatment |
| Adaptive instructional decisions | Reasons to revisit, bypass, split, combine or reorder work | Gap: local adaptation rules exist in Practices but are not an established adaptive-instruction model |

## Instruction and scaffolding

This area asks how explanations, demonstrations and support help a learner engage with a task. It connects instructional design to the learner's actual activity. An accurate AI explanation is an instructional input, not evidence that the learner can produce or apply it.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Explanations and worked examples | Essential terms, mechanisms, decision rationale, examples and limits | Partial: [Cognitive Modeling](../methods/cognitive-modeling.md); [IES overview](../references/pashler-2007-organizing-instruction.md) supplies further reading, not a complete worked-example theory |
| Demonstration and articulation | Making relevant decisions inspectable and eliciting the learner's account | Partial: [Cognitive Apprenticeship](../models/cognitive-apprenticeship.md) and [Cognitive Modeling](../methods/cognitive-modeling.md) |
| Questioning and self-explanation | Questions that elicit relationships and learner-generated explanations | Partial: [Self-Explanation](../methods/self-explanation.md) and [Self-Explanation Effect](../principles/self-explanation-effect.md); broader questioning strategies remain open |
| Scaffolding and fading | Support for unavailable capabilities and conditions for reducing it | Partial: [Instructional Scaffolding](../concepts/instructional-scaffolding.md); access accommodations are distinct from answer assistance |
| Guided and independent practice | What the learner performs, what help supplies and how responsibility changes | Partial: [Cognitive Apprenticeship](../models/cognitive-apprenticeship.md); AI-specific help selection remains an authored application |
| Responding to misunderstanding | Distinguishing an unclear task, missing knowledge and a mistaken relationship | Partial: [Formative Assessment](../concepts/formative-assessment.md) and [Feedback](../concepts/feedback.md); subject-specific repair needs subject expertise |

## Assessment and feedback

This area asks what an observed response warrants concluding and how information about it supports improvement. Assessment relates capability, observation and interpretation; feedback supplies information that may inform another attempt. Evaluation of AI-assisted learning asks the broader question of whether the coaching approach helped.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Starting knowledge and baseline | Self-report, direct observation, prior exposure and pre-instruction conditions | Partial: [Metacognitive Calibration](../concepts/metacognitive-calibration.md) distinguishes judgments and criteria; baseline design needs fuller coverage |
| Capability and evidence | Tasks that elicit relevant observations and justified interpretation | Partial: [Assessment Triangle](../models/assessment-triangle.md) |
| Criteria and assessment quality | Meaningful criteria, validity, reliability, fairness and uncertainty | Partial: [Assessment Triangle](../models/assessment-triangle.md) introduces inference limits; detailed measurement concepts are missing |
| Formative interpretation | Using evidence to choose instruction and investigating competing explanations | Partial: [Formative Assessment](../concepts/formative-assessment.md); the source scope does not establish clinical diagnosis |
| Feedback and revision | Information about the work, actionable discrepancies and subsequent use | Partial: [Feedback](../concepts/feedback.md); timing and task-dependent effects need fuller treatment |
| Assistance and evidence conditions | Original versus corrected answers, hints, answer exposure and access supports | Partial: [Learning–Performance Distinction](../concepts/learning-performance-distinction.md); live recording rules remain Practice design |

## Memory and transfer

This area asks whether learning remains available and can be used when time, cues or context change. It concerns learning processes and practice conditions. Assessment provides observations of those outcomes; evaluation considers what caused them and how far conclusions extend.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Encoding and forgetting | How information becomes retrievable and why later access can fail | Source only: [How People Learn II overview](../references/nasem-2018-how-people-learn-ii.md); detailed memory mechanisms remain missing |
| Retrieval practice | Reconstructing encountered knowledge and separating recall from correction | Partial: [Retrieval Practice](../methods/retrieval-practice.md) and [Testing Effect](../principles/testing-effect.md), including comparison limits |
| Spacing | Temporal distribution, retention goals and actual intervals | Partial: [Spacing Effect](../principles/spacing-effect.md); no individualized scheduling algorithm is established |
| Interleaving and practice variation | Changing categories, examples or contexts, separately from spacing | Source only for alternating examples and problems: [IES overview](../references/pashler-2007-organizing-instruction.md); category-interleaving claims need their own evidence |
| Retention and performance | Immediate success, later availability and the conditions of observation | Partial: [Learning–Performance Distinction](../concepts/learning-performance-distinction.md) |
| Transfer | Applying a relationship to a changed representation, context or reasoning demand | Partial: [Learning–Performance Distinction](../concepts/learning-performance-distinction.md) supplies the distinction; mechanisms and conditions for transfer remain missing |

## Motivation and self regulation

This area asks how learners choose, monitor and sustain learning. It includes motivational, cognitive, behavioral and affective dimensions. The learner's confidence is a judgment to examine, not a substitute for demonstrated capability; the coach's proposed plan is not the learner's own regulation.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Goals and values | Purpose, interest, perceived value and competing demands | Partial: [Self-Regulated Learning](../concepts/self-regulated-learning.md) names the broad dimensions; mechanisms need fuller explanation |
| Self-efficacy and motivation | Beliefs about capability, persistence and context | Source only: [How People Learn II overview](../references/nasem-2018-how-people-learn-ii.md) identifies relevant sections; detailed source inspection remains necessary |
| Agency and choice | Learner control, assistance preferences and responsibility | Partial context: [Self-Regulated Learning](../concepts/self-regulated-learning.md); consent and autonomy commitments also have a normative basis |
| Planning and monitoring | Selecting strategies, observing progress and controlling study | Partial: [Self-Regulated Learning](../concepts/self-regulated-learning.md), without claiming a complete named phase model |
| Metacognitive calibration | Comparing judgments with performance under stated conditions | Partial: [Metacognitive Calibration](../concepts/metacognitive-calibration.md); measurement methods remain open |
| Reflection and strategy revision | Interpreting an attempt and changing how one learns | Partial: [Cognitive Apprenticeship](../models/cognitive-apprenticeship.md) and [Self-Regulated Learning](../concepts/self-regulated-learning.md) |
| Emotion and social support | Frustration, effort, belonging, collaboration and help-seeking | Partial: the sociology dimension of [Cognitive Apprenticeship](../models/cognitive-apprenticeship.md); broader explanation remains missing |

## Human AI interaction

This area asks how the interaction medium changes what a learner and coach can do and know. It covers the interface, reliability and human control. It does not assume that a prompt installs persistent memory, verifies a source or guarantees compliance. Its privacy and agency commitments include normative choices as well as empirical questions.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Dialogue and turn-taking | Questions, clarification, actual replies and repair of misunderstandings | Gap: authored dialogue rules exist, but no standalone account of tutoring dialogue is included |
| Grounding and verification | Subject sources, provenance, erroneous content and checked feedback | Partial: [Cognitive Modeling](../methods/cognitive-modeling.md) states the verified-demonstration condition; AI reliability mechanisms need explanation |
| Context and tool limits | Supplied context, persistent state, external tools and resumption | Gap: behavior depends on the actual system; repository prompts do not implement those capabilities |
| Reliance and cognitive offloading | What work the learner performs versus delegates, and when reliance is warranted | Source only: [Bastani and colleagues](../references/bastani-2025-generative-ai-guardrails.md) supplies a bounded study context; a general mechanism account is missing |
| Accessibility and inclusion | Language, representation, accommodations and barriers to participation | Source only: [How People Learn II overview](../references/nasem-2018-how-people-learn-ii.md) identifies universal design and access topics; practical guidance needs further inspection |
| Privacy and human control | Disclosure, consent, retained records, goal ownership and stopping | Source only: [UNESCO guidance overview](../references/unesco-2023-generative-ai-guidance.md); no legal compliance or platform privacy guarantee is implied |

## Evaluation of AI assisted learning

This area asks whether a coaching approach produces useful learning under specified conditions. It uses assessment evidence but adds questions about comparison, cause, context and unintended effects. A usable interface or correct AI answer is a different outcome from learner understanding or retention.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Outcome definition | Understanding, independent application, retention and transfer versus satisfaction or task completion | Partial: [Learning–Performance Distinction](../concepts/learning-performance-distinction.md) and [Assessment Triangle](../models/assessment-triangle.md) |
| Comparison and causal inference | Baselines, comparison conditions, selection, exposure and alternative explanations | Source only: [Kestin and colleagues](../references/kestin-2025-ai-tutoring.md) and [Bastani and colleagues](../references/bastani-2025-generative-ai-guardrails.md); a general evaluation explanation is missing |
| Timing and assistance | Immediate versus later outcomes and performance with versus without AI support | Partial: [Learning–Performance Distinction](../concepts/learning-performance-distinction.md) |
| Generalizability | Population, subject, setting, tutor design and evidence beyond the tested case | Source only: existing [AI tutoring](../references/kestin-2025-ai-tutoring.md) and [guardrails](../references/bastani-2025-generative-ai-guardrails.md) records document limits; a broader treatment remains missing |
| Usability and access | Whether people can understand, operate and resume the coaching process | Gap: no observed adult usability or accessibility evaluation exists for this package |
| Unintended effects and tradeoffs | Dependence, incorrect feedback, time demands, exclusion and privacy costs | Source only for selected concerns: [UNESCO overview](../references/unesco-2023-generative-ai-guidance.md) and [guardrails study](../references/bastani-2025-generative-ai-guardrails.md); no comprehensive risk assessment is claimed |

## Connections between areas

These relationships explain why the areas belong together. They are authored orientation statements, not measured causal coefficients or prerequisites.

| Connection | Meaning and boundary |
|---|---|
| Knowledge representation informs Instructional design | A map identifies relationships worth learning; design still needs a goal and evidence before imposing an order |
| Learning and cognition informs Instruction and scaffolding | An account of prior knowledge and task demands helps explain why support might be useful; it does not prescribe a universal hint schedule |
| Assessment and feedback adjusts Instruction and scaffolding | An observed discrepancy can motivate a different explanation or support; the task and correction must first be checked |
| Motivation and self-regulation informs Instructional design | Learner goals, constraints and choices shape the route; a route is not a fixed psychological profile |
| Memory and transfer supplies outcomes for Evaluation of AI-assisted learning | Later and changed-context responses extend what can be examined beyond immediate completion; they alone do not establish causation |
| Human–AI interaction constrains Assessment and feedback | Hidden answer help, lost context or incorrect AI feedback changes what an observation supports concluding |
| Evaluation of AI-assisted learning informs Instructional design | Results under stated conditions can motivate revisions; evidence from one implementation does not validate every coaching prompt |

For a constructed example, suppose a learner wants to explain a unit-price comparison. Knowledge representation connects quantity, units and rates. Design selects a meaningful comparison. Instruction may demonstrate one example; assessment examines the learner's own explanation of a fresh one. Memory and transfer asks about later use with different packaging. Self-regulation concerns the learner's goals and study choices. Human–AI interaction concerns what help was actually supplied. Evaluation asks whether a particular coaching approach improved relevant outcomes. This is an illustration of responsibilities, not an observed learning session.

## Source basis and inspection limits

The nine-area arrangement is a KPS editorial synthesis. The following sources inform coverage and distinctions; none establishes this exact partition or a universally best coaching sequence. Topics marked as gaps are questions to develop, not unsupported explanations disguised as established theory.

| Source | Contribution to the outline | Inspected basis and limit |
|---|---|---|
| [How People Learn II](../references/nasem-2018-how-people-learn-ii.md) | Breadth across cognition, knowledge, motivation, context and technology | Official contents and introductory report guide; topic-location support, not full chapter or study review |
| [IES instruction and study guide](../references/pashler-2007-organizing-instruction.md) | Examples, representations, questioning, retention and study judgments | Official recommendation overview and displayed evidence levels; full guide and underlying studies not inspected in this addition |
| [Novak and Cañas](../references/novak-canas-2008-concept-maps.md) | Relationships, focus questions and revisable maps | Existing Introduction and construction-section inspection; no proof of universal prerequisite order |
| [Collins and colleagues](../references/collins-brown-holum-1991-cognitive-apprenticeship.md) | Instruction, support, sequencing and social context | Existing framework-section inspection; no validation of an AI implementation |
| [NRC assessment framework](../references/national-research-council-2001-assessment.md) | Capability, observation and interpretation | Existing Chapter 2 scope; not a ready-made scoring algorithm |
| [Panadero](../references/panadero-2017-self-regulated-learning.md) | Self-regulation spans more than metacognition | Existing abstract and introduction scope; original models not independently inspected |
| [Learning and performance](../references/soderstrom-bjork-2015-learning-versus-performance.md) | Distinguishing present performance from durable learning | Existing abstract-only scope; no universal retention threshold |
| [UNESCO GenAI guidance](../references/unesco-2023-generative-ai-guidance.md) | Human control, privacy and educational suitability | Official publication overview only; policy guidance is not effectiveness evidence |

## Relation to coaching and further development

The [master coaching Practice](../practices/ai-assisted-learning-orchestration.md) applies knowledge from several areas in each session. Its learner assessment, subject orientation, capability roadmap, task selection, teaching and adaptation are operational decisions. They are not the divisions of this body of knowledge and do not require a learner to study the entire outline first.

Current explanations are strongest as bounded entry points to concept mapping, guided instruction, assessment, retrieval and self-regulation. The broadest explanation gaps are cognition, instructional design and human–AI interaction. Inspect appropriate source passages and improve a useful connected explanation before creating more files. Preserve the distinction between source-supported meaning, authored coaching choices and actual learner evidence.

The outline and illustration can be revised as coverage improves. Additional topic illustrations are optional. [The knowledge index](INDEX.md) remains the generated catalog by KPS role; this outline remains the reader's subject coverage view.
