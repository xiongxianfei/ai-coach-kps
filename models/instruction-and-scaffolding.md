---
id: "ai-coach:model:instruction-and-scaffolding"
type: "model"
version: "0.5.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "Instruction and Scaffolding"
evidence_status: "provisional"
reviewed: null
basis_kind: "KPS-authored source-grounded explanatory synthesis; not a published unified theory or validated AI intervention"
uses_models: ["ai-coach:model:cognitive-apprenticeship", "ai-coach:model:instructional-design", "ai-coach:model:assessment-and-feedback"]
uses_concepts: ["ai-coach:concept:instructional-scaffolding"]
uses_methods: ["ai-coach:method:cognitive-modeling", "ai-coach:method:self-explanation"]
references: ["ai-coach:reference:collins-1991","ai-coach:reference:pashler-2007-organizing-instruction","ai-coach:reference:richards-2022-morphology","ai-coach:reference:cmu-eberly-assessment-alignment"]
source_alignment: [{"reference":"ai-coach:reference:collins-1991","relation":"synthesis-contribution","locator":"Framework Content, Method items 1 to 6, and Sequencing","contribution":"Knowledge and strategies, observable demonstration, articulation, task support, fading and meaningful whole-task context"},{"reference":"ai-coach:reference:pashler-2007-organizing-instruction","relation":"synthesis-contribution","locator":"Official WWC recommendation overview, recommendations 2, 3, 4 and 7 and their short descriptions","contribution":"Alternating worked examples with problems, connecting representations and eliciting explanatory responses; overview scope only"},{"reference":"ai-coach:reference:richards-2022-morphology","relation":"synthesis-contribution","locator":"Lecture 3 PDF text, numbered pages 16 to 18","contribution":"Subject basis for the unlockable contrast; no teaching-effectiveness contribution"},{"reference":"ai-coach:reference:cmu-eberly-assessment-alignment","relation":"synthesis-contribution","locator":"Opening alignment discussion and table of learning objectives, assessment activities and measurement","contribution":"Alignment of intended learning and assessment activity; basis for distinguishing thinking from response format, not a validated question menu"}]
---

# Instruction and Scaffolding

## Key takeaway

Explain enough connected knowledge for the learner to understand what happens, how, why and when; make the relevant reasoning visible, then give the learner an opportunity to use it. Adjust support from the actual response.

## Summary

This Model explains how knowledge, demonstrations, questions and assistance relate within a lesson. It covers connected explanations, worked examples, question types and response formats, learner articulation, guided and independent activity, scaffolding and responses to misunderstanding. A constructed lesson on equal sharing connects these topics; a short morphology contrast connects structure with meaning. The account is an introductory KPS synthesis of selected source contributions; its lesson organization and examples are authored applications. No prior teaching terminology is required.

![Instruction and Scaffolding connects an explanation to learner activity and an actual response, which informs subsequent support. Eight tokens shared among four equal groups gives two tokens per group. Demonstration, targeted hints and attempts without answer help are possible support conditions, not compulsory stages.](../diagrams/instruction-and-scaffolding-overview.png)

The arrows express opportunities and informational relationships, not guaranteed learning. The token example is constructed. A response only exists when the learner supplies one; the image does not report an observed session. Original illustration generated with the built-in image generation tool; [generation prompt](../diagrams/instruction-and-scaffolding-overview.prompt.txt).

## Contents

- [What instruction makes available](#what-instruction-makes-available)
- [Building a connected explanation](#building-a-connected-explanation)
- [Demonstration and representations](#demonstration-and-representations)
  - [Connecting structure to meaning](#connecting-structure-to-meaning)
- [Lesson scope and interaction pace](#lesson-scope-and-interaction-pace)
- [Questioning and learner explanation](#questioning-and-learner-explanation)
  - [Thinking requested](#thinking-requested)
  - [Answer formats](#answer-formats)
  - [Question purposes](#question-purposes)
  - [Learner explanations and evidence](#learner-explanations-and-evidence)
- [Scaffolding and changing responsibility](#scaffolding-and-changing-responsibility)
- [Interpreting misunderstanding](#interpreting-misunderstanding)
- [A worked lesson on equal sharing](#a-worked-lesson-on-equal-sharing)
  - [Purpose and essential knowledge](#purpose-and-essential-knowledge)
  - [Worked reasoning and its boundary](#worked-reasoning-and-its-boundary)
  - [A learner task and possible next decisions](#a-learner-task-and-possible-next-decisions)
- [Interfaces with other domains](#interfaces-with-other-domains)
- [Limits and unresolved coverage](#limits-and-unresolved-coverage)
- [Source alignment](#source-alignment)
- [Evidence status](#evidence-status)

## What instruction makes available

**Instruction** arranges explanations and activity intended to help someone learn. **Scaffolding** supplies support for a task the learner cannot yet manage fully. The important distinction is between what the explanation makes available and what the learner actually does with it.

Our representation connects four responsibilities:

```text
Subject knowledge and the lesson capability constrain the explanation.
Explanation and demonstration make relevant relationships inspectable.
The learner's activity produces a response under actual support conditions.
Interpretation of that response informs further explanation or assistance.
```

This is a representation of instructional relationships, not a compulsory script. A baseline or retrieval attempt can precede an explanation. A learner may also ask for a complete demonstration rather than attempt a problem immediately. No response should be inferred from the fact that content was displayed.

Cognitive Apprenticeship brings knowledge and strategies together with modeling, coaching, support and articulation. Its modeling account makes relevant task decisions available for inspection; its scaffolding account adjusts help and transfers responsibility as the learner takes over. These contributions inform this Model, without prescribing our lesson format. [Source record](../references/collins-brown-holum-1991-cognitive-apprenticeship.md).

## Building a connected explanation

A **connected explanation** relates the ideas needed to answer the lesson's central question. In an equal-sharing lesson, naming division is insufficient: the explanation must connect the total, the number of groups and the amount in each group. Conversely, an entire history of arithmetic adds little to that particular question.

The following are content responsibilities in our synthesis, not mandatory headings or a fixed order:

| Responsibility | What it contributes | Example in the lesson below |
|---|---|---|
| Purpose and context | Establishes the question and why the idea matters | How can eight tokens be shared equally among four groups? |
| Essential concepts | Gives unfamiliar terms usable meanings | Total, number of groups, amount per group |
| Relationships and mechanisms | Connects the parts and explains why the result follows | Number of groups × amount per group reconstructs the total |
| Worked reasoning | Exposes the decisions and checks in an example | Divide eight by four; check four groups of two |
| Distinctions and boundaries | Prevents a nearby but different claim from being substituted | Four groups differs from four tokens per group |

The appropriate explanation depends on the subject. A physical mechanism may need a causal account. A mathematical relationship may need a derivation. A linguistic distinction may need contrasting examples and conditions of use. A procedure needs reasons for important choices and checks. Forcing every subject into a causal story can introduce claims the evidence does not support.

Self-contained teaching introduces the terms and background needed now, while reusing what the learner already understands. Its scope is a coherent relationship or meaningful problem. Shortening until the learner must guess the missing connection defeats that purpose; adding every related topic can obscure it. An unclear response may justify expanding one relationship rather than repeating a longer version of everything.

## Demonstration and representations

A **worked example** includes a solution and the reasoning that makes it intelligible. A demonstration makes a relevant action inspectable. For the sharing example, “8 / 4 = 2” shows the calculation; four groups of two and a reconstruction of the total explain what it means. The supplied reasoning must be checked, even when fluent. An AI explanation is an authored account of a solution, not access to hidden model cognition.

The IES overview recommends alternating worked solutions and problem solving, connecting graphics with verbal accounts, connecting concrete and abstract representations, and asking explanatory questions. These are bounded design resources; they do not establish a universal sequence, optimal explanation length or benefit from any added picture. [Overview and inspection limits](../references/pashler-2007-organizing-instruction.md).

Representations contribute when their correspondence is explicit. Eight drawn tokens correspond to the numerator; the four group boundaries correspond to the divisor; the two tokens inside each group correspond to the quotient. If the drawing instead shows four groups of three, it contradicts the equation. A label saying “division” cannot repair that error.

A contrasting example can reveal a boundary. Keeping eight tokens but reducing the number of equal groups to two changes the amount in each group to four. This makes the divisor's role visible. Simply changing the color of the tokens would not test that relationship.

### Connecting structure to meaning

For a structural distinction, a complete explanation connects the parts, their contributions, the meaning of the combination and a case where the distinction matters. Notation can summarize these connections, but reproducing a diagram or grouping does not by itself explain them. Meaning, examples and notation can be introduced in the order that makes the relationship accessible; no fixed sequence or learner type follows from this guidance.

The following illustration uses the analysis of *unlockable* in [Richards's lecture, pages 16–18](../references/richards-2022-morphology.md). A base is the unit an affix attaches to at a particular step; brackets show that grouping. The door situations are authored examples, not learner records.

| Structure | Contributions and resulting meaning | Concrete case |
|---|---|---|
| `[[un + lock] + able]` | Reversive *un-* forms the verb *unlock*; *-able* then gives **can be unlocked** | A locked door can be opened with its working key |
| `[un + [lock + able]]` | *-able* forms the adjective *lockable*; negative *un-* gives **cannot be locked** | A broken mechanism prevents a door from being locked |

The first case can still involve a door that can be locked. It therefore need not satisfy the second reading. The contrast makes the different claims visible; it does not present them as logical opposites. The word's written sequence is unchanged, while the grouping changes which contribution applies to which base.

The teaching point is the correspondence among representation, interpretation and situation. Repeating the brackets with more labels leaves that correspondence unexplained if the meanings are still missing. Explaining each contribution and comparing a concrete case addresses the relationship directly. This is an authored instructional application of a bounded linguistic analysis, not evidence that every context favors both readings equally or that this teaching order is universally best.

## Lesson scope and interaction pace

A coherent explanation can connect several concepts before a response is requested. Breaking it after every definition changes the interaction but does not necessarily expose a new reasoning demand. Explanation length and question frequency are separate design choices: a complete explanation is complete relative to the lesson capability, not encyclopedic coverage of the subject.

Two arrangements remain available. A connected explanation followed by a short question set keeps the relationships in view before assessment. Guided interaction introduces a meaningful part and uses a response to inform subsequent support. The latter can be useful when a procedure depends on earlier decisions, a prerequisite is uncertain, or the learner asks for stepwise help. Neither arrangement is a fixed learner type or a universal best sequence.

Cognitive Apprenticeship supplies whole-task context and adjustable support; the IES overview includes alternating worked examples with problems. Neither source establishes that all teaching must precede all questions, or that every small idea needs an immediate check. The lesson pacing choice and default delivery cycle belong to the master Practice.

A question set can reveal relationships across answers. Correct definitions alongside a mistaken application suggest a different gap from uniformly missing terminology. Feedback can therefore address the common misunderstanding while retaining the evidence for each answer. An unanswered item remains unobserved; it is not filled from another answer or treated as failure automatically.

## Questioning and learner explanation

Questions can elicit different kinds of work: naming, calculating, explaining a reason, predicting a change, comparing cases or finding a boundary. Their usefulness depends on what the lesson is trying to develop. A brief comparison or prediction may expose the relevant distinction without a long explanation. More elaborate reasoning is useful when it resolves a material uncertainty; it is not a necessary response format for every check. “What is the answer?” may reveal a quotient; “Why is four the divisor?” addresses its interpretation.

### Thinking requested

A question can be described by the thinking it requests, the format of the answer and its purpose in the lesson. These dimensions interact but are not interchangeable. The [Eberly Center guidance](../references/cmu-eberly-assessment-alignment.md) relates objectives to assessment activities and summarizes revised Bloom categories: remember, understand, apply, analyze, evaluate and create. The following KPS menu makes common questioning choices concrete; it is not that taxonomy reproduced, a new validated classification or a mandatory progression.

The examples use the already introduced relationship between total tokens, equal groups and amount per group. They are constructed prompts, not a question set to administer in full or records of learner answers.

| Type | Illustrative prompt |
|---|---|
| Recall | From the earlier lesson, what does the divisor count when sharing a total equally? |
| Identify or classify | In “twelve tokens in three groups,” which quantity counts groups? |
| Interpret | What does “four tokens per group” tell us? |
| Compare | How does “four tokens” differ from “four tokens per group”? |
| Explain or justify | Why do we divide the total by the number of equal groups? |
| Apply | Share fifteen tokens equally among five groups. What amount does each receive? |
| Predict | Keep twelve tokens but increase the equal groups from three to six. What changes about each share? |
| Diagnose and correct | A solution ends “twelve tokens divided among three groups gives four groups.” What needs correcting? |
| Evaluate evidence | Does knowing the average is four tokens prove that every group received four? |
| Explore a boundary | When would total divided by group count fail to describe each group's actual share? |
| Generate or design | Give two different total-and-group-count pairs that produce the same amount per equal group. |
| Reflect | Which part of this explanation is still unclear, and what would help? |

Types can overlap: diagnosing a wrong unit may involve interpretation and explanation. A label does not determine the work actually required; prior knowledge, novelty, number of connected ideas and supplied support change the demand. Reflection elicits the learner's account of understanding or effort; that account is useful evidence about their experience, not a direct demonstration of the target capability. No lesson needs every type, and recalling a relevant prerequisite can be useful even during an advanced task.

### Answer formats

Possible formats include yes/no or multiple choice, matching or sorting, ordering steps, filling a gap, completing a worked step, a short phrase, a calculation, a brief explanation, an annotated diagram, a practical demonstration or a created artifact. A format describes how the response is expressed; it does not automatically establish the thinking used or the question's difficulty.

For example, dividing twelve tokens among three equal groups can be posed as a choice among numerical answers, a written calculation, or arranging tokens into groups. These formats offer different cues and observations. A correct choice alone can leave the reason for division unobserved; a demonstration may make the distribution visible but still require clarification of its interpretation. More writing does not automatically provide better evidence. Conversely, shortening an argument until its justification disappears can remove the very capability being assessed.

Thinking demand, response effort and support therefore need separate attention. Offered options can cue recognition, and a completed diagram can reveal part of the answer. Those conditions matter when interpreting a response; they are not inherently inappropriate during teaching. Familiar wording or an accessible response mode can reduce incidental effort without supplying the target reasoning.

### Question purposes

The same kind of question may locate a starting point, develop understanding through guided activity, practise application, revisit earlier knowledge, integrate relationships or invite reflection. Purpose changes the appropriate support and the interpretation of the result. A question whose answer has just been demonstrated may support learning, but it cannot establish an unexposed baseline. A planned review is not observed retention until an actual later response exists under recorded conditions.

A question about previously taught group meaning could request recall, accept a brief phrase, and serve retrieval practice. A question asking the learner to justify division could request explanation, accept speech or writing, and serve guided learning or assessment depending on the help provided. Neither combination determines the lesson's next action on its own. The coaching Practice owns selection and adaptation from the goal, available evidence and learner preferences; this classification describes the options.

### Learner explanations and evidence

When the intended capability includes meaning, correct notation and an adequate interpretation are separate response features. An accurate grouping can leave its significance unobserved. An explanation of what it means, or a justified choice of a contrasting situation, can supply the missing evidence. If the relationship is then taught, the subsequent answer is a response after clarification; it does not retroactively supply independent understanding in the original attempt. An already adequate explanation needs no redundant extra question.

**Learner self-explanation** is reasoning generated by the learner about the material. Reading a supplied explanation and producing one are different activities. The existing [Self-Explanation Method](../methods/self-explanation.md) retains its particular source and applicability limits. Here, a request for explanation is an opportunity to observe reasoning, not a guarantee that the reasoning is correct.

An answer-revealing prompt changes that opportunity. “There are four groups, so we divide by four; why?” has already supplied the key relationship. The response may still be useful during instruction, but its conditions differ from an unaided explanation. A fresh item is useful when independent application matters; changing numbers alone does not establish broad transfer.

The coaching Practice distinguishes three purposes: new learning permits explanation before application; a baseline observes current understanding before teaching the answer; retrieval asks for previously encountered knowledge before re-exposure. These are operational choices whose evidence conditions must remain visible.

## Scaffolding and changing responsibility

Support can change the work left for the learner. In the sharing example, an empty group diagram supports organizing the quantities; a completed diagram supplies the distribution; a full worked solution supplies both distribution and interpretation. Each can be appropriate for a different purpose, but the resulting responses support different conclusions.

**Fading** means reducing task support as responsibility shifts to the learner. It is not removing help after a fixed number of turns. If the learner can distribute the tokens but cannot interpret the units, removing the diagram and offering more arithmetic drills may miss the problem. A focused explanation of “tokens per group” addresses a different demand.

Guided activity and an attempt without answer help are conditions, not ranks assigned to a person. The learner can request more explanation or stop. Access accommodations, such as a screen reader, remain available; they are not automatically answer-generating scaffolds to fade. A calculator may be appropriate when the goal is interpretation rather than manual calculation.

## Interpreting misunderstanding

A discrepancy is evidence to investigate, not a stable learner trait. A missing unit may reflect an omitted label, an unclear question or uncertainty about which quantity is being calculated. The response alone may not distinguish these explanations.

Instruction and assessment meet at this point. Assessment identifies the discrepancy against a checked criterion and considers alternative interpretations. Instruction supplies an explanation or support directed at the relevant relationship. The [Assessment and Feedback Model](assessment-and-feedback.md) develops the inference and feedback boundaries.

In the example, “four tokens per group” could follow from swapping the roles of the numbers. A reconstruction check exposes the contradiction: four groups of four would require sixteen tokens. This explains why the proposed result does not fit the stated situation. It does not establish why a particular person made the error. The task wording, illustration and answer key must also be checked.

## A worked lesson on equal sharing

This is a constructed illustration of the Model, not an observed learner session. The [master Practice](../practices/ai-assisted-learning-orchestration.md#stage4-teach-question-and-preserve-the-learner-response) owns the live delivery actions and response-wait boundary.

### Purpose and essential knowledge

Within a stage about interpreting rates, this lesson develops the capability to **explain an amount per group and justify the divisor**. Its starting assumption is that the learner can count and interpret simple multiplication; calculator use can support arithmetic. If that background is uncertain, the lesson design remains provisional.

The explanation begins with a question: how much does each group receive when a total is shared equally? The total counts all the tokens. The number of groups counts the recipients. “Per group” describes the amount assigned to one group. These are three related quantities, not three names for the same number.

### Worked reasoning and its boundary

Eight tokens are shared equally among four groups. Putting one token in each group uses four tokens. A second round uses the remaining four. Each group therefore has two tokens:

```text
Group A: ● ●   Group B: ● ●   Group C: ● ●   Group D: ● ●
8 tokens / 4 groups = 2 tokens per group
4 groups × 2 tokens per group = 8 tokens
```

The divisor is four because four counts the groups across which the total is shared. Multiplying the result by the number of groups reconstructs the original total. The numerical result and its units express the relationship together.

Equal sharing is essential to this interpretation. If the groups receive 1, 1, 2 and 4 tokens, the average is still two tokens per group, but not every group receives two. The calculation of an average and the claim about each individual group are different. This boundary prevents the rule from being extended beyond the stated conditions.

### A learner task and possible next decisions

The learner-facing task is: **Twelve tokens are shared equally among three groups. What is the amount in each group, and why is the divisor three?** The response should include a quotient, units and an explanation connecting the divisor to the number of groups. A calculator is permitted; answer-generating help must be recorded.

In live use, the coach waits here. No actual reply or assessment is recorded in this example. The author key is `12 / 3 = 4 tokens per group`, checked by `3 × 4 = 12`. Because the complete document discloses the key, a reader who has seen it needs a fresh item for an unexposed attempt.

| Hypothetical response or condition | What remains uncertain | Possible next decision in the Practice |
|---|---|---|
| “4” only | Units and the reason for division are absent | Ask for the meaning of four in this situation |
| “3 tokens per group” | The roles of total, groups and quotient may be confused | Clarify what three counts and use reconstruction to examine the answer |
| Correct explanation after a supplied distribution | Independent construction has not been observed | Preserve the help; use another item without that answer support if needed |
| Correct explanation without answer help | The current task supports the intended relationship | Choose another relevant application or close the lesson; later retention remains unobserved |
| No reply | No learner evidence exists | Wait, clarify or record a pause |

These are conditional follow-up alternatives, not a required sequence. The single task illustrates a narrow capability; it does not require all lessons to have that scope or forbid presenting complementary questions together. At a lesson close, the meaningful record is what was explained, what the learner actually produced, under what help, and one next action. Feedback can connect directly to teaching the next lesson within the existing learning agreement; a new permission turn is not inherent in the instructional relationship. An unresolved prerequisite can instead make a focused repair the appropriate continuation. The master Practice owns these delivery choices and the stage-summary procedure. There is no automatic stage-completion claim or requirement to finish the lesson in one day.

## Interfaces with other domains

[Instructional Design](instructional-design.md) selects a lesson capability, content scope and useful task. [Knowledge Representation](knowledge-representation.md) explains how relationships remain consistent across words, diagrams and symbols. Assessment interprets the actual response. Motivation and self-regulation concerns learner choice and persistence; memory and transfer concerns later availability and changed-context use. Human–AI interaction concerns turn-taking, access and the reliability of generated content. Evaluation asks whether the approach helped under appropriate comparisons.

## Limits and unresolved coverage

The six outline topics have introductory coverage, not a complete theory of instruction. The source base does not establish ideal explanation length, hint timing, automatic fading, domain-specific misconception repair or the effectiveness of this adult AI lesson. Deeper evidence about worked examples, multimedia learning, tutoring dialogue and accessibility remains to be inspected. Physical skills may need demonstrations and observation beyond text. The lesson and visual are original examples, and arithmetic correctness does not validate their teaching effects.

## Source alignment

- [Collins, Brown and Holum](../references/collins-brown-holum-1991-cognitive-apprenticeship.md): framework Content, Method and Sequencing supply the named instructional relationships. The six methods are not six compulsory lesson stages. No underlying experiments were reanalyzed.
- [Pashler and colleagues](../references/pashler-2007-organizing-instruction.md): the official overview of recommendations 2, 3, 4 and 7 supports the selected example, representation and questioning considerations. The full guide and primary studies are outside this inspection.
- [Richards](../references/richards-2022-morphology.md): PDF text on pages 16–18 supplies the subject analysis for the morphology contrast, not evidence for a teaching method. The concrete cases and coaching implications are authored here.

- [Eberly Center](../references/cmu-eberly-assessment-alignment.md): the opening discussion and objective/activity table support distinguishing intended thinking from assessment format. Our overlapping question menu, reflection entry and token prompts are authored explanatory choices, not a validated taxonomy or an efficacy claim.

The explanation responsibilities, connecting representation, lesson and conditional decisions are KPS-authored integration. None of these sources publishes this complete Model or validates its AI implementation.

## Evidence status

Provisional source-grounded explanatory synthesis. No real learner response, independent scientific review, educational-effect estimate or validated coaching intervention is claimed.
