---
language: "KPS 9.x"
package_version: "0.4.0"
status: "draft"
reviewed: null
---

# AI Coach Body of Knowledge Outline

This outline describes the knowledge needed to help independent adults understand, practise, retain and apply a subject with conversational AI. It supports readers who want to understand coaching decisions and authors who need to see what the library still lacks.

## Key takeaway

Understand the connected knowledge domains behind coaching, then use a learning Practice to apply them to a learner's goal.

## Summary

Nine domains organize the subject by explanatory responsibility. Each section names the topics to cover, aligns existing explanations with those topics and makes gaps visible. This is a project coverage outline, not a universal taxonomy, a validated curriculum or a claim that nine independent mechanisms explain all learning. The outline provides navigation and does not prescribe a study order.

## Overview

![Nine AI Coach knowledge domains: Learning and cognition; Memory and transfer; Motivation and self-regulation; Knowledge representation; Instructional design; Instruction and scaffolding; Assessment and feedback; Human–AI interaction; Evaluation of AI-assisted learning. Selected connections show representation informing design, assessment adjusting instruction, and retention and transfer supplying evaluation outcomes.](../diagrams/body-of-knowledge-overview.png)

The domains answer different questions about the same learning situation. Knowledge representation informs instructional design; assessment and feedback can adjust instruction and scaffolding; memory and transfer supplies outcomes for evaluation. These are selected connections, not a complete causal model or a sequence of compulsory stages. The text below contains the essential content independently of the image.

Original AI-generated illustration, produced for this project with the built-in image generation tool. No third-party figure was copied. The [generation prompt](../diagrams/body-of-knowledge-overview.prompt.txt) records the intended labels and relationships; the illustration makes no measured-effect claim.

## Overall outline

| Domain | Responsibility | Main coverage |
|---|---|---|
| [Learning and cognition](#learning-and-cognition) | Explain how understanding and skill develop | Prior knowledge; attention; working memory; cognitive load; mental representations; conceptual change; expertise; context |
| [Memory and transfer](#memory-and-transfer) | Explain availability and use of learning over time and contexts | Encoding and forgetting; retrieval; spacing; interleaving; retention; transfer |
| [Motivation and self-regulation](#motivation-and-self-regulation) | Explain how learners direct and sustain learning | Goals and values; self-efficacy; agency; planning and monitoring; calibration; reflection; emotion and social support |
| [Knowledge representation](#knowledge-representation) | Represent what a subject contains and how its ideas connect | Boundaries; concepts and propositions; explanatory subsystems; concept maps; multiple representations; source grounding |
| [Instructional design](#instructional-design) | Translate a capability goal into a justified learning design | Objectives; task analysis; prerequisites; sequencing; task difficulty; alignment; adaptation |
| [Instruction and scaffolding](#instruction-and-scaffolding) | Explain how assistance supports increasingly independent activity | Explanations; worked examples; modeling; questioning; self-explanation; scaffolding and fading; guided and independent practice |
| [Assessment and feedback](#assessment-and-feedback) | Interpret responses and inform improvement | Baselines; evidence and criteria; assessment quality; error interpretation; feedback; assistance conditions |
| [Human–AI interaction](#human-ai-interaction) | Explain the possibilities and limits of learning through an AI interface | Dialogue; grounding and verification; context and tools; reliance; accessibility; privacy and control |
| [Evaluation of AI-assisted learning](#evaluation-of-ai-assisted-learning) | Judge the quality and effects of the coaching approach | Outcomes; comparisons; confounding; generalizability; usability; unintended effects |

The reading order moves from the learner to represented knowledge, instructional design and support, evidence, and the AI medium and its evaluation. It is an explanatory order, not a prerequisite chain or the coaching process. The [six-step Practice overview](../practices/ai-assisted-learning-orchestration.md#default-planning-handoff) shows how these domains contribute to actual coaching decisions.

## Scope and boundaries

The unit of interest is an adult learner using a conversational AI with suitable subject material. The outline includes knowledge about learning, instruction, evidence and the interaction medium. Language, culture, prior experience, disability and access conditions cut across the domains; they are not fixed learner types.

Subject facts remain owned by the relevant subject library. English phonology, for example, is content that a coach may help someone learn; the AI Coach library explains how to select, support and interpret that learning activity. Model training, deployment infrastructure, clinical diagnosis, credentialing and institutional policy administration are outside the present scope. Relevant interface limits and privacy responsibilities remain in scope.

A knowledge domain groups coherent explanatory questions. Here, “domain” and the earlier “area” name the same nine divisions; neither implies an independently functioning component. Each domain can develop one self-contained Model of its essential concepts, mechanisms, examples, boundaries and interfaces. The existing Cognitive Apprenticeship and Assessment Triangle files retain their published identities as supporting frameworks. Source-grounded explanatory syntheses are explicitly distinguished from published frameworks under the [source-alignment policy](scientific-policy.md#domain-models-and-published-frameworks). Missing coverage is developed as explanation, not filled with empty Model files.

## Reading coverage

The table entries describe document coverage, not learner achievement or scientific approval. **Partial** means a local explanation covers a named subset; **source only** means a relevant source record exists but a local explanation is missing; **gap** means the topic needs a suitable inspected basis and an explanation. No entire domain is marked complete. Source access may be limited even when a local explanation exists.

The tables link explanatory knowledge and sources. Authored coaching Practices are applications and do not count as academic coverage merely because they mention a topic. Topics can appear at several interfaces without requiring duplicate canonical definitions or one file per row.

## Learning and cognition

This domain asks how a learner develops a usable understanding or skill. It concerns the processes and representations involved in learning; instructional design concerns how to arrange opportunities to learn. Memory is introduced here as a cognitive process and developed under Memory and transfer for retention and later use.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Prior knowledge and understanding | How existing knowledge relates to interpretation, integration and mistaken assumptions | Partial: [Concept Map](../concepts/concept-map.md) represents relationships; a mechanism-level account of prior knowledge is missing |
| Attention and working memory | Selection of information, temporary maintenance and task demands | Source only: [How People Learn II overview](../references/nasem-2018-how-people-learn-ii.md) locates the relevant chapters; detailed passages still need inspection |
| Cognitive load | Demands created by the task, its presentation and the learner's available knowledge | Gap: inspect appropriate cognitive-load theory and boundary evidence before recommending task-size rules |
| Mental representations and conceptual change | How concepts, explanations and procedures are represented, challenged and revised | Gap: an external concept map is not itself a model of the learner's internal representation |
| Expertise and skill development | Differences in organized knowledge, strategies and increasingly independent performance | Partial: [Cognitive Apprenticeship](../models/cognitive-apprenticeship.md) describes expert content and supported participation; a fuller account of expertise is missing |
| Context and individual variation | Learning across situations, cultures, languages and adult circumstances | Source only: [How People Learn II overview](../references/nasem-2018-how-people-learn-ii.md); domain applicability and adult variation need local explanation |

## Memory and transfer

This domain asks whether learning remains available and can be used when time, cues or context change. It concerns learning processes and practice conditions. Assessment provides observations of those outcomes; evaluation considers what caused them and how far conclusions extend.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Encoding and forgetting | How information becomes retrievable and why later access can fail | Source only: [How People Learn II overview](../references/nasem-2018-how-people-learn-ii.md); detailed memory mechanisms remain missing |
| Retrieval practice | Reconstructing encountered knowledge and separating recall from correction | Partial: [Retrieval Practice](../methods/retrieval-practice.md) and [Testing Effect](../principles/testing-effect.md), including comparison limits |
| Spacing | Temporal distribution, retention goals and actual intervals | Partial: [Spacing Effect](../principles/spacing-effect.md); no individualized scheduling algorithm is established |
| Interleaving and practice variation | Changing categories, examples or contexts, separately from spacing | Source only for alternating examples and problems: [IES overview](../references/pashler-2007-organizing-instruction.md); category-interleaving claims need their own evidence |
| Retention and performance | Immediate success, later availability and the conditions of observation | Partial: [Learning–Performance Distinction](../concepts/learning-performance-distinction.md) |
| Transfer | Applying a relationship to a changed representation, context or reasoning demand | Partial: [Learning–Performance Distinction](../concepts/learning-performance-distinction.md) supplies the distinction; mechanisms and conditions for transfer remain missing |

## Motivation and self regulation

This domain asks how learners choose, monitor and sustain learning. It includes motivational, cognitive, behavioral and affective dimensions. The learner's confidence is a judgment to examine, not a substitute for demonstrated capability; the coach's proposed plan is not the learner's own regulation.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Goals and values | Purpose, interest, perceived value and competing demands | Partial: [Self-Regulated Learning](../concepts/self-regulated-learning.md) names the broad dimensions; mechanisms need fuller explanation |
| Self-efficacy and motivation | Beliefs about capability, persistence and context | Source only: [How People Learn II overview](../references/nasem-2018-how-people-learn-ii.md) identifies relevant sections; detailed source inspection remains necessary |
| Agency and choice | Learner control, assistance preferences and responsibility | Partial context: [Self-Regulated Learning](../concepts/self-regulated-learning.md); consent and autonomy commitments also have a normative basis |
| Planning and monitoring | Selecting strategies, observing progress and controlling study | Partial: [Self-Regulated Learning](../concepts/self-regulated-learning.md), without claiming a complete named phase model |
| Metacognitive calibration | Comparing judgments with performance under stated conditions | Partial: [Metacognitive Calibration](../concepts/metacognitive-calibration.md); measurement methods remain open |
| Reflection and strategy revision | Interpreting an attempt and changing how one learns | Partial: [Cognitive Apprenticeship](../models/cognitive-apprenticeship.md) and [Self-Regulated Learning](../concepts/self-regulated-learning.md) |
| Emotion and social support | Frustration, effort, belonging, collaboration and help-seeking | Partial: the sociology dimension of [Cognitive Apprenticeship](../models/cognitive-apprenticeship.md); broader explanation remains missing |

## Knowledge representation

This domain asks what belongs in the subject and what relationships make it understandable. Its output is a representation of knowledge. Instructional design separately decides which relationships matter for a learner's route; a conceptual connection does not establish a prerequisite.

The [Knowledge Representation Model](../models/knowledge-representation.md) connects the topics below in one introductory explanation with a worked comparison and its own illustration.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Subject boundaries and knowledge domains | Scope, omissions, responsibilities and useful overlap between domains | [Scope and explanatory responsibility](../models/knowledge-representation.md#scope-and-explanatory-responsibility) introduces focus and omissions; formal domain-analysis methods remain open |
| Concepts and propositions | Terms, meanings and labeled relationships that express a claim | [Concepts propositions and relationships](../models/knowledge-representation.md#concepts-propositions-and-relationships) explains meanings and typed links; [Concept Map](../concepts/concept-map.md) retains the published terminology |
| Explanatory subsystems and interfaces | What each system explains and how its variables or outputs connect to another | [Domains subsystems and interfaces](../models/knowledge-representation.md#domains-subsystems-and-interfaces) explains responsibilities and exchanged quantities; specific subjects still require disciplinary sources |
| Concept mapping | Focus questions, hierarchy, cross-links and revision | [Outlines maps and learning routes](../models/knowledge-representation.md#outlines-maps-and-learning-routes) distinguishes outputs; [Concept Mapping](../methods/concept-mapping.md) supplies the construction procedure |
| Multiple representations | Relationships between verbal, graphical, concrete and abstract accounts | [Connected representations](../models/knowledge-representation.md#connected-representations) and the worked comparison explain meaning across forms; detailed learning mechanisms remain open |
| Source grounding and uncertainty | Provenance, inspected scope, conflicting accounts and revisable claims | [Sources uncertainty and revision](../models/knowledge-representation.md#sources-uncertainty-and-revision) gives introductory distinctions; comprehensive evidence appraisal remains open |

## Instructional design

This domain asks how a goal becomes a coherent set of learning opportunities. It concerns proposed capabilities, tasks and their relationships. Instruction and scaffolding concerns the help offered during those tasks; assessment examines what responses support concluding.

The [Instructional Design Model](../models/instructional-design.md) connects the topics below through a capability goal, task demands, support and evidence, with its own illustration.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Capability objectives and alignment | Observable capabilities, stages and lessons, matching content, activities and criteria | [Capability objectives and alignment](../models/instructional-design.md#capability-objectives-and-alignment) connects goals, activities and evidence; [lesson scope](../models/instructional-design.md#choosing-lesson-content-and-scope) and [coverage to lessons](../models/instructional-design.md#from-subject-coverage-to-lessons) explain the learning units; broader design frameworks remain open |
| Task analysis | Component demands, integration and meaningful units of work | [Task analysis and meaningful integration](../models/instructional-design.md#task-analysis-and-meaningful-integration) explains a local decomposition; formal analysis methods need deeper coverage |
| Prerequisites and corequisites | Required preparation, helpful background and capabilities learned together | [Prerequisites and corequisites](../models/instructional-design.md#prerequisites-and-corequisites) explains task-dependent relations; no universal prerequisite graph is established |
| Sequencing and learning progressions | Complexity, diversity and evidence for proposed routes | [Sequencing and learning progressions](../models/instructional-design.md#sequencing-and-learning-progressions) distinguishes a provisional route from a researched progression; subject-specific sequence evidence remains open |
| Task difficulty and practice selection | How demand changes with knowledge, support and the target capability | [Task demand support and practice](../models/instructional-design.md#task-demand-support-and-practice) explains changing demands and help; no optimized difficulty or schedule is supplied |
| Adaptive instructional decisions | Reasons to revisit, bypass, split, combine or reorder work | [Adaptation from evidence](../models/instructional-design.md#adaptation-from-evidence) and the connected design example explain conditional changes; actual coaching decisions remain authored Practice content |

## Instruction and scaffolding

This domain asks how explanations, demonstrations and support help a learner engage with a task. It connects instructional design to the learner's actual activity. An accurate AI explanation is an instructional input, not evidence that the learner can produce or apply it.

The [Instruction and Scaffolding Model](../models/instruction-and-scaffolding.md) explains these relationships through a worked lesson and an embedded illustration. Its [lesson scope and pacing](../models/instruction-and-scaffolding.md#lesson-scope-and-interaction-pace) section distinguishes connected teaching from the timing of questions. It provides introductory coverage with remaining source and depth limits.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Explanations and worked examples | Essential terms, mechanisms, decision rationale, examples and limits | [Building a connected explanation](../models/instruction-and-scaffolding.md#building-a-connected-explanation) and [the worked lesson](../models/instruction-and-scaffolding.md#a-worked-lesson-on-equal-sharing) connect purpose, terms, reasoning and boundaries; detailed worked-example evidence remains open |
| Demonstration and articulation | Making relevant decisions inspectable and eliciting the learner's account | [Demonstration and representations](../models/instruction-and-scaffolding.md#demonstration-and-representations) and [questioning](../models/instruction-and-scaffolding.md#questioning-and-learner-explanation) distinguish supplied reasoning from the learner's account; [Cognitive Modeling](../methods/cognitive-modeling.md) retains the published operation |
| Questioning and self-explanation | Questions that elicit relationships and learner-generated explanations | [Questioning and learner explanation](../models/instruction-and-scaffolding.md#questioning-and-learner-explanation) explains purposes and answer exposure; [Self-Explanation](../methods/self-explanation.md) retains its source scope; broader tutoring-dialogue evidence remains open |
| Scaffolding and fading | Support for unavailable capabilities and conditions for reducing it | [Scaffolding and changing responsibility](../models/instruction-and-scaffolding.md#scaffolding-and-changing-responsibility) explains adjustable help and access accommodations; no fixed fading schedule is established |
| Guided and independent practice | What the learner performs, what help supplies and how responsibility changes | [Scaffolding and changing responsibility](../models/instruction-and-scaffolding.md#scaffolding-and-changing-responsibility) and [the learner task](../models/instruction-and-scaffolding.md#a-learner-task-and-possible-next-decisions) distinguish assistance conditions; AI-specific choices remain authored applications |
| Responding to misunderstanding | Distinguishing an unclear task, missing knowledge and a mistaken relationship | [Interpreting misunderstanding](../models/instruction-and-scaffolding.md#interpreting-misunderstanding) connects discrepancies to explanation and support; subject-specific misconception repair remains open |

## Assessment and feedback

This domain asks what an observed response warrants concluding and how information about it supports improvement. Assessment relates capability, observation and interpretation; feedback supplies information that may inform another attempt. Evaluation of AI-assisted learning asks the broader question of whether the coaching approach helped.

The [Assessment and Feedback Model](../models/assessment-and-feedback.md) is the self-contained domain explanation. It integrates source contributions and a constructed comparison example while preserving the Assessment Triangle as a named framework. This is introductory coverage, not a complete measurement theory or a validated coaching intervention.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Starting knowledge and baseline | Self-report, direct observation, prior exposure and pre-instruction conditions | [Starting knowledge and baseline](../models/assessment-and-feedback.md#starting-knowledge-and-baseline) distinguishes the evidence; detailed baseline instrument design remains open |
| Capability and evidence | Tasks that elicit relevant observations and justified interpretation | [Capability and criteria](../models/assessment-and-feedback.md#capability-and-criteria), [tasks and responses](../models/assessment-and-feedback.md#tasks-and-observable-responses), and [Assessment Triangle](../models/assessment-triangle.md) supply introductory coverage |
| Criteria and assessment quality | Meaningful criteria, validity, reliability, fairness and uncertainty | [Validity reliability and fairness](../models/assessment-and-feedback.md#validity-reliability-and-fairness) explains distinctions; psychometric estimation, rubric design and bias analysis need deeper coverage |
| Formative interpretation | Using evidence to choose instruction and investigating competing explanations | [Interpretation and competing explanations](../models/assessment-and-feedback.md#interpretation-and-competing-explanations) connects the distinctions to an example; subject-specific misconception accounts remain outside this general Model |
| Feedback and revision | Information about the work, actionable discrepancies and subsequent use | [Feedback and revision](../models/assessment-and-feedback.md#feedback-and-revision) explains the relationship; timing and context-dependent effects still need fuller treatment |
| Assistance and evidence conditions | Original versus corrected answers, hints, answer exposure and access supports | [Assistance and evidence conditions](../models/assessment-and-feedback.md#assistance-and-evidence-conditions) and the [connected comparison example](../models/assessment-and-feedback.md#a-connected-comparison-example); no universal mastery threshold is supplied |

## Human AI interaction

This domain asks how the interaction medium changes what a learner and coach can do and know. It covers the interface, reliability and human control. It does not assume that a prompt installs persistent memory, verifies a source or guarantees compliance. Its privacy and agency commitments include normative choices as well as empirical questions.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Dialogue and turn-taking | Questions, clarification, actual replies and repair of misunderstandings | Gap: authored dialogue rules exist, but no standalone account of tutoring dialogue is included |
| Grounding and verification | Subject sources, provenance, erroneous content and checked feedback | Partial: [Cognitive Modeling](../methods/cognitive-modeling.md) states the verified-demonstration condition; AI reliability mechanisms need explanation |
| Context and tool limits | Supplied context, persistent state, external tools and resumption | Gap: behavior depends on the actual system; repository prompts do not implement those capabilities |
| Reliance and cognitive offloading | What work the learner performs versus delegates, and when reliance is warranted | Source only: [Bastani and colleagues](../references/bastani-2025-generative-ai-guardrails.md) supplies a bounded study context; a general mechanism account is missing |
| Accessibility and inclusion | Language, representation, accommodations and barriers to participation | Source only: [How People Learn II overview](../references/nasem-2018-how-people-learn-ii.md) identifies universal design and access topics; practical guidance needs further inspection |
| Privacy and human control | Disclosure, consent, retained records, goal ownership and stopping | Source only: [UNESCO guidance overview](../references/unesco-2023-generative-ai-guidance.md); no legal compliance or platform privacy guarantee is implied |

## Evaluation of AI assisted learning

This domain asks whether a coaching approach produces useful learning under specified conditions. It uses assessment evidence but adds questions about comparison, cause, context and unintended effects. A usable interface or correct AI answer is a different outcome from learner understanding or retention.

| Topic | What the explanation needs to cover | Existing explanation and gap |
|---|---|---|
| Outcome definition | Understanding, independent application, retention and transfer versus satisfaction or task completion | Partial: [Learning–Performance Distinction](../concepts/learning-performance-distinction.md) and [Assessment Triangle](../models/assessment-triangle.md) |
| Comparison and causal inference | Baselines, comparison conditions, selection, exposure and alternative explanations | Source only: [Kestin and colleagues](../references/kestin-2025-ai-tutoring.md) and [Bastani and colleagues](../references/bastani-2025-generative-ai-guardrails.md); a general evaluation explanation is missing |
| Timing and assistance | Immediate versus later outcomes and performance with versus without AI support | Partial: [Learning–Performance Distinction](../concepts/learning-performance-distinction.md) |
| Generalizability | Population, subject, setting, tutor design and evidence beyond the tested case | Source only: existing [AI tutoring](../references/kestin-2025-ai-tutoring.md) and [guardrails](../references/bastani-2025-generative-ai-guardrails.md) records document limits; a broader treatment remains missing |
| Usability and access | Whether people can understand, operate and resume the coaching process | Gap: no observed adult usability or accessibility evaluation exists for this package |
| Unintended effects and tradeoffs | Dependence, incorrect feedback, time demands, exclusion and privacy costs | Source only for selected concerns: [UNESCO overview](../references/unesco-2023-generative-ai-guidance.md) and [guardrails study](../references/bastani-2025-generative-ai-guardrails.md); no comprehensive risk assessment is claimed |

## Connections between domains

These relationships explain why the domains belong together. They are authored orientation statements, not measured causal coefficients or prerequisites.

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

The nine-domain arrangement is a KPS editorial synthesis. The following sources inform coverage and distinctions; none establishes this exact partition or a universally best coaching sequence. Topics marked as gaps are questions to develop, not unsupported explanations disguised as established theory.

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

The [master coaching Practice](../practices/ai-assisted-learning-orchestration.md) applies knowledge from several domains in each session. Its learner assessment, subject orientation, capability roadmap, task selection, teaching and adaptation are operational decisions. They are not the divisions of this body of knowledge and do not require a learner to study the entire outline first.

Knowledge representation, Instructional design, Instruction and scaffolding, and Assessment and feedback now have integrated introductory domain Models, each with an embedded overview illustration. Their topic tables retain unresolved depth and evidence limits. Other current explanations provide bounded entry points to guided instruction, retrieval and self-regulation. The broadest explanation gaps include cognition, memory and transfer, motivation, human–AI interaction and evaluation. Inspect appropriate source passages and improve a useful connected explanation before creating more files. Preserve the distinction between source-supported meaning, authored coaching choices and actual learner evidence.

The outline and illustration can be revised as coverage improves. Additional topic illustrations are optional. [The knowledge index](index.md) remains the generated catalog by KPS role; this outline remains the reader's subject coverage view.
