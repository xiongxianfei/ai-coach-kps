---
id: "ai-coach:practice:formative-assessment-with-ai"
type: "practice"
version: "0.3.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "Formative Assessment With an AI Coach"
primary_audience: "independent adult learners"
evidence_status: "provisional"
reviewed: null
basis_kind: "KPS-specific application synthesis; AI adaptations and local criteria are authored, not a tested intervention"
practice_format: "steps-first-v1"
stage_order: "recommended; prerequisites and evidence govern entry"
stage_titles: ["Stage1 Locate the discrepancy and check the task", "Stage2 Compare explanations with a discriminating probe", "Stage3 Provide actionable feedback or modeling", "Stage4 Observe a revision and a comparable task", "Stage5 Choose the next instructional decision"]
references: ["ai-coach:reference:sadler-1989", "ai-coach:reference:feedback-2020", "ai-coach:reference:nrc-2001", "ai-coach:reference:collins-1991"]
uses_concepts: ["ai-coach:concept:formative-assessment", "ai-coach:concept:feedback", "ai-coach:concept:instructional-scaffolding"]
uses_principles: []
uses_models: ["ai-coach:model:assessment-triangle"]
uses_methods: ["ai-coach:method:cognitive-modeling", "ai-coach:method:self-explanation"]
uses_practices: ["ai-coach:practice:concept-mapping-and-instructional-sequencing-with-ai"]
---

# Formative Assessment With an AI Coach

## Key takeaway

Investigate a specific learning obstacle through evidence and choose an instructional response without diagnosing the learner.

## Summary

Use this Practice when an explanation, response or artifact does not yet meet a stated criterion. It produces competing explanations, a small discriminating probe, feedback the learner can act on, and a checked next attempt. Sadler's formative-assessment account informs quality judgment; its application to simple right/wrong probes is explicitly a local extension. The five stages are a recommended order; the source, task and learner consent are prerequisites.

## Entry and boundaries

This Practice is for educational obstacles in a bounded adult learning task. It is not psychological, clinical or disability diagnosis. Learner agreement, an inspectable response and a trustworthy criterion are prerequisites. The learner controls pacing and may refuse an assessment. The AI provides proposed interpretations; it is not an infallible judge.

## One obstacle and one discriminating probe

Enter with **one observed discrepancy**, its task, a credible criterion and actual assistance information. Check whether the task or reference is wrong before inferring a learner difficulty. Choose a small probe whose answers would lead to different instructional decisions; ask it before presenting multiple new explanations. Return one concrete next learning task or an explicit reason to pause, not a global learner diagnosis. Use [the lesson and task guide](../guides/learning-workflow.md) when the instructional response needs to be scoped further.

This targeted investigation does not make one question the default size of a lesson. When the learner is answering a grouped set, review the available answers together and address shared confusion once. Use a separate probe only when its result would change the next teaching action. If the explanation or demonstration was insufficient, repair that content instead of repeatedly requesting self-ratings. Keep any corrective exercise connected to the original lesson and return to the relevant application before claiming transfer.

## Stage map

1. [Stage1 Locate the discrepancy and check the task](#stage1-locate-the-discrepancy-and-check-the-task)
2. [Stage2 Compare explanations with a discriminating probe](#stage2-compare-explanations-with-a-discriminating-probe)
3. [Stage3 Provide actionable feedback or modeling](#stage3-provide-actionable-feedback-or-modeling)
4. [Stage4 Observe a revision and a comparable task](#stage4-observe-a-revision-and-a-comparable-task)
5. [Stage5 Choose the next instructional decision](#stage5-choose-the-next-instructional-decision)

## Stage1 Locate the discrepancy and check the task

1. Preserve the exact response and the task it answered, including sources, hints and prior exposure. Write the criterion in observable terms rather than saying only "not understood."
2. Ask the learner what they were trying to do. Separate their report from an inference about an internal misconception.
3. Inspect the task, reference and AI feedback first. An incorrect answer key, ambiguous phrase or inaccessible format can produce an apparent learning problem.
4. Choose one discrepancy to investigate. If the target is high-stakes, the criterion uncertain, or the learner wants to stop, end with the limit rather than continuing a speculative diagnosis.

**Constructed example**: a learner selects the lower total price when asked for the lower price per equal quantity. Possible issues include the meaning of "per," unit conversion, calculation or a misread instruction. None is established by the final choice alone.

## Stage2 Compare explanations with a discriminating probe

1. Write at least two plausible explanations when the evidence permits them. Include task/source error or insufficient evidence rather than forcing a learner deficit.
2. Choose **one** short probe whose possible responses would change the next instructional action. The question should isolate a relation, not simply repeat the original task more loudly.
3. State which answer-generating help is withheld for the probe and retain access supports. Save the response before interpreting it.
4. Mark the hypothesis unresolved if both explanations predict the same response. Do not infer a stable learning style, mental disorder, intelligence or motivation from one answer.

| Candidate explanation in the constructed comparison | Useful probe | Possible next step |
|---|---|---|
| Unit basis is unclear | Ask what "per 100 g" denotes without calculating | Explain the unit relation |
| Conversion is unclear | Ask whether 0.75 kg and 750 g represent the same quantity | Review the conversion |
| Arithmetic procedure is unclear | Supply a common unit and ask for the next operation | Model that operation |
| Original wording was misread | Ask the learner to restate the goal | Repair wording, not alleged ability |

These branches are authored task-design hypotheses. They are not a validated diagnostic instrument. Prefer a knowledgeable human when an interpretation has consequences beyond choosing the next low-stakes learning task.

## Stage3 Provide actionable feedback or modeling

1. Relate the feedback to the criterion and one inspectable feature of the original response. Avoid unsupported praise or personal labels.
2. Choose an appropriate next move within the learner's existing agreement, preserving their ability to request a hint, simpler explanation or verified worked example. Do not require a new choice at every turn. Direct instruction is legitimate when questioning alone is unproductive; prepare the missing explanation and demonstrate the relevant relationship before requesting another attempt.
3. If the AI supplies a worked example, verify the relation before presenting it as a model. Ask for an external explanation of the solution, not for private chain-of-thought or a claim about internal model cognition.
4. Have the learner attempt the relevant step and explain the criterion they used. Preserve every supplied cue in the assistance record.

**Example prompt**

```text
Use the criterion and original response below. Identify one discrepancy,
state the evidence for it and one alternative explanation. Carry out a useful
next teaching action within our agreed pacing. Do not infer a personal trait.
If the source or correction is uncertain, say so. Present any needed questions
together after the explanation, and wait for my actual response.
```

The learner's response and the content check determine whether the feedback was useful. A polite acknowledgment is not evidence of correction.

Preserve ambiguous replies without upgrading them: “yes” to a prompt offering several possibilities does not identify which occurred, and “better” reports perceived change without verifying accuracy or its cause. Ask a short clarification only when needed for the decision. Otherwise retain the uncertainty and continue useful instruction. These examples describe interpretation limits, not additional questions to ask after every response.

## Stage4 Observe a revision and a comparable task

1. Keep the original answer and the assisted revision as separate records. Ask the learner to state what changed and why, without demanding unnecessary verbosity.
2. Choose a comparable item for which the crucial relation remains but the answer has not just been shown. Declare assistance and access conditions before the response.
3. Check both the product and the reasoning features relevant to the criterion. For multicriterion work, report which dimensions improved and which remain uncertain rather than collapsing them into an unexplained score.
4. Revisit the hypothesis when the expected improvement is absent. Repeated correction failure may reflect a bad explanation, unsuitable probe, fatigue or source error; it does not prove a learner defect.

A correct analogous calculation supports a limited next decision. It does not show that all tasks in the topic are understood or that the learning will persist.

## Stage5 Choose the next instructional decision

1. Summarize the discrepancy, evidence inspected, support given and new observation in a private note.
2. Choose **one next bounded action** among continuing with less answer help, teaching a prerequisite, using another representation, obtaining human feedback, or pausing. State the reason and any uncertainty.
3. Set a later independent check when retention matters and label it planned until it occurs. Preserve access accommodations in that plan.
4. Retain unresolved alternatives and discard an unsupported hypothesis rather than preserving it as a learner profile. Invite the learner to correct the record.

Completion means a justified instructional decision, not a clinical diagnosis or verified psychological measurement. No change should be attributed to the AI intervention from this short sequence alone.

With a [two-level learning plan](concept-mapping-and-instructional-sequencing-with-ai.md), identify the specific map relation, prerequisite hypothesis or stage that this evidence concerns. A faulty map edge requires content correction; it is not a learner deficit. Record whether the change is source-based, performance-based or a learner priority, then revise the affected part rather than restarting the entire subject.

## Completion and limits

A useful output is a stated decision with supporting and conflicting evidence. Sadler's published framework particularly concerns quality judgments across multiple criteria; our unit-cost decision table extends the evidence-to-action idea to a simple learning task without claiming source equivalence. The protocol itself is KPS-authored and unvalidated.

## Private observation format

```text
Task and criterion: [fill]
Original response and assistance: [fill]
Competing explanations: [fill]
Discriminating probe and observed response: [fill]
Feedback and learner revision: [fill]
Follow-up task and actual help: [fill]
Interpretation, limits and next decision: [fill]
```

Unfilled fields remain unknown. Use [learning notes](../guides/learning-notes.md) before turning an observation into a learning claim.

## Academic basis and adaptation

Research identifies constructs and bounded findings; the stage sequence, prompts, assistance categories and decision criteria above are **KPS-authored application choices**. They have not been independently tested as one AI coaching intervention.

- [D. Royce Sadler](../references/sadler-1989-formative-assessment.md) — Abstract. Read the local record for the inspected extent and applicability limits.
- [Benedikt Wisniewski, Klaus Zierer and John Hattie](../references/wisniewski-zierer-hattie-2020-feedback.md) — Abstract and Introduction. Read the local record for the inspected extent and applicability limits.
- [National Research Council; James W. Pellegrino, Naomi Chudowsky and Robert Glaser, editors](../references/national-research-council-2001-assessment.md) — Chapter 2: Assessment as a Process of Reasoning from Evidence; The Assessment Triangle; relationships among the three vertices. Read the local record for the inspected extent and applicability limits.
- [Allan Collins, John Seely Brown and Ann Holum](../references/collins-brown-holum-1991-cognitive-apprenticeship.md) — Method items 1 to 6; framework summary and concluding discussion. Read the local record for the inspected extent and applicability limits.

## Supporting knowledge

- [Formative assessment](../concepts/formative-assessment.md) — concept supporting the local explanation, not a substitute for the steps.
- [Feedback](../concepts/feedback.md) — concept supporting the local explanation, not a substitute for the steps.
- [Instructional scaffolding](../concepts/instructional-scaffolding.md) — concept supporting the local explanation, not a substitute for the steps.
- [Assessment triangle](../models/assessment-triangle.md) — model supporting the local explanation, not a substitute for the steps.
- [Cognitive modeling](../methods/cognitive-modeling.md) — method supporting the local explanation, not a substitute for the steps.
- [Self explanation](../methods/self-explanation.md) — method supporting the local explanation, not a substitute for the steps.

## Evidence status

**Provisional.** This Practice is a proposed synthesis for independent adult learners. No learner recordings, scores, retained gains, independent reviewer approval or coaching effectiveness have been invented. Source access is documented individually; general learning research and AI-specific evidence are not interchangeable.

## Current practice summary

Actual use: **not recorded**.  
Observed response and assistance: **not recorded**.  
Verified outcome: **not established**.  
Unresolved issue and next check: **to be chosen during actual use**.

This blank record is intentional. Keep completed personal records and private material outside the public repository. Publication tests do not populate it.
