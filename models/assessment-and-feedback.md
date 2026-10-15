---
id: "ai-coach:model:assessment-and-feedback"
type: "model"
version: "0.1.1"
language: "KPS 9.x"
status: "draft"
canonical_name: "Assessment and Feedback"
evidence_status: "provisional"
reviewed: null
basis_kind: "KPS-authored source-grounded explanatory synthesis; not a published unified theory or validated AI intervention"
uses_models: ["ai-coach:model:assessment-triangle"]
uses_concepts: ["ai-coach:concept:formative-assessment", "ai-coach:concept:feedback", "ai-coach:concept:learning-performance-distinction", "ai-coach:concept:metacognitive-calibration"]
references: ["ai-coach:reference:nrc-2001", "ai-coach:reference:sadler-1989", "ai-coach:reference:feedback-2020", "ai-coach:reference:soderstrom-2015"]
source_alignment: [{"reference":"ai-coach:reference:nrc-2001","relation":"synthesis-contribution","locator":"Chapter 2, Purposes of Assessment and Precision and Imprecision, printed pages 37 to 43; Assessment Triangle and vertex relationships, pages 44 to 51","contribution":"Assessment purpose, cognition-observation-interpretation alignment, inference uncertainty, validity, reliability and fairness"},{"reference":"ai-coach:reference:sadler-1989","relation":"synthesis-contribution","locator":"Publisher abstract","contribution":"Quality standards, learner comparison and improvement moves; limited relevance to purely correct/incorrect responses"},{"reference":"ai-coach:reference:feedback-2020","relation":"synthesis-contribution","locator":"Publisher abstract and Introduction","contribution":"Informational account of feedback and heterogeneous effects; no universal feedback treatment"},{"reference":"ai-coach:reference:soderstrom-2015","relation":"synthesis-contribution","locator":"Abstract","contribution":"Distinction between observed performance and durable learning, including retention and transfer"}]
---

# Assessment and Feedback

## Key takeaway

A response becomes useful evidence when it is interpreted against a clear capability and criterion; feedback connects that interpretation to something the learner can understand and revise.

## Summary

This Model explains the Assessment and feedback knowledge domain: what an assessment observes, how conclusions are limited, and how feedback can support another attempt. It integrates named research contributions into a KPS-authored explanation. The connected example is invented and checked, not an observed learner session. No prior assessment terminology is required; the essential distinctions are explained here.

![Assessment and Feedback: capability and criteria align with task conditions. An actual learner response and the criteria inform a bounded interpretation, which informs feedback or clarification and a distinct revision or new attempt. A constructed comparison distinguishes package price from price per kilogram: A costs £5 per kg and B costs £4.50 per kg. Evidence before instruction, with assistance, without answer help, and later or in a new context remains distinct.](../diagrams/assessment-and-feedback-overview.png)

The illustration connects the response, its interpretation and the opportunity to revise. A new attempt supplies another observation; it does not overwrite the original or automatically establish lasting learning. The price comparison is constructed, and all essential relationships and calculations are explained below. The evidence categories can overlap: a later attempt can also be assisted or independent.

Original illustration generated for this Model with the built-in image generation tool; [generation prompt](../diagrams/assessment-and-feedback-overview.prompt.txt). It summarizes our explanatory synthesis rather than reproducing a source figure or reporting learner results.

## Contents

- [The system being explained](#the-system-being-explained)
- [Capability and criteria](#capability-and-criteria)
- [Tasks and observable responses](#tasks-and-observable-responses)
- [Starting knowledge and baseline](#starting-knowledge-and-baseline)
- [Interpretation and competing explanations](#interpretation-and-competing-explanations)
- [Validity reliability and fairness](#validity-reliability-and-fairness)
- [Feedback and revision](#feedback-and-revision)
- [Assistance and evidence conditions](#assistance-and-evidence-conditions)
- [A connected comparison example](#a-connected-comparison-example)
  - [What the task is meant to reveal](#what-the-task-is-meant-to-reveal)
  - [Reading an incomplete response](#reading-an-incomplete-response)
  - [Correction and another observation](#correction-and-another-observation)
- [Interfaces with other domains](#interfaces-with-other-domains)
- [Limits and unresolved coverage](#limits-and-unresolved-coverage)
- [Source alignment](#source-alignment)
- [Evidence status](#evidence-status)

## The system being explained

Assessment is reasoning about capability from what someone says, does or produces. **Feedback** is information about that performance or understanding. **Formative use** means that the information informs learning and improvement; a recorded result can also serve a summative purpose, such as reporting attainment at a checkpoint.

The [Assessment Triangle](assessment-triangle.md) supplies three interdependent elements: cognition specifies the competence of interest, observation concerns evidence-eliciting tasks, and interpretation connects the resulting evidence to conclusions. The triangle is a design relationship, not three compulsory chronological steps.

The following representation extends that foundation to locate feedback and later evidence. It is our synthesis, not a reproduction of a published unified model:

```text
Capability and criteria <---- alignment ----> Task and conditions
           |                                      |
           |                              observed response
           |                                      |
           +----------> bounded interpretation <--+
                                  |
                     relevant feedback or clarification
                                  |
                       learner revision or new attempt
                                  |
                   another observation under stated conditions
```

Arrows mean informational dependence or an opportunity for another observation. They do not guarantee improvement. A disagreement may expose a defective criterion or task rather than a learner error.

## Capability and criteria

A **capability** is what the assessment seeks evidence about. A **criterion** describes which features of a response count toward that claim. In our running example, the capability is explaining a quantity comparison on a common basis. The criterion is not merely choosing the correct package: it also includes the calculation, units and reason for comparing per-unit values.

These distinctions prevent three different outcomes from being collapsed:

| Outcome in the constructed example | What it establishes locally |
|---|---|
| The task was submitted | A response exists |
| The package choice is correct | One response feature matches the key |
| The common-unit reasoning is correct | The response also supports the intended explanation criterion |

The criterion must remain faithful to the goal. Elegant prose is not required to demonstrate unit reasoning unless communication quality is part of the target. Conversely, a fluent paragraph that never establishes a common basis does not meet that reasoning criterion.

## Tasks and observable responses

An observation can be a choice, calculation, explanation, artifact or demonstration. Its usefulness depends on what competing explanations it can distinguish.

In the comparison example, “Which package is cheaper?” is ambiguous: it could mean lower total price or lower price per kilogram. “Which has the lower price per kilogram, and why?” makes the intended comparison explicit. Asking for the reasoning creates evidence unavailable from a bare choice, although the explanation itself may still be copied or mistaken.

Subject truth and assessment fit are separate checks. A mathematically correct answer key can accompany a task that samples the wrong capability. A well-targeted task can have a faulty key. Neither fault is repaired by consistent AI scoring.

## Starting knowledge and baseline

A **baseline** is a starting observation under described conditions. **Self-assessment** is the learner's judgment of their own ability. Both can inform planning, but they are different observations. “I am comfortable with ratios” may suggest a suitable first question; it does not contain a demonstrated ratio comparison.

For our example, a response after seeing the complete calculation cannot be described as an untouched pre-instruction baseline. A hint about converting grams to kilograms also changes what the response reveals about unaided unit selection. Previous instruction is not disqualifying; it is part of the context needed to interpret the observation.

The [Metacognitive Calibration](../concepts/metacognitive-calibration.md) explanation relates judgments to performance criteria. One mismatch between confidence and a response does not establish a stable learner trait. No response leaves the capability unobserved; it does not establish failure.

## Interpretation and competing explanations

An **observation** describes the response. An **interpretation** proposes what it means. A missing unit might reflect incomplete notation, an unclear instruction or a missing understanding of the quantity. Those explanations predict different responses to a clarification.

| Constructed observation | Competing explanations | Information that could distinguish them |
|---|---|---|
| Correct package, no reasoning | Common-unit reasoning, total-price shortcut or guessing | A stated calculation and units |
| Correct division, wrong unit | Notation slip or reversed quantity interpretation | What the numerator and denominator represent |
| Correct reasoning after a hint | Useful support or dependence on that specific cue | A fresh comparison with the actual help recorded |
| Learner challenges the key | Learner misconception, ambiguous goal or erroneous key | Rechecking the task and calculation |

These are authored possibilities, not a diagnostic classifier. A probe that supplies the missing relation can teach it while examining the response; that later response cannot retrospectively prove the relation was available earlier.

## Validity reliability and fairness

**Validity** concerns support for an intended interpretation and use. **Reliability** concerns consistency under comparable measurement conditions. **Fairness** includes relevant access and comparable interpretation rather than irrelevant obstacles. These distinctions follow the NRC account; this introductory Model does not supply psychometric instruments.

In our example:

- Repeatedly scoring “correct” for the same guessed choice could be consistent yet provide weak evidence of reasoning.
- Changing grams to kilograms may expose a conversion demand. An error then does not isolate comparison reasoning unless that demand is considered.
- A screen reader can preserve access to the quantities without supplying the answer. Removing it would change the opportunity to demonstrate the target capability.

A missing subskill and an inaccessible presentation require different responses. A single comparison also samples too little to justify a broad claim such as “understands all proportional reasoning.”

## Feedback and revision

Feedback makes information about a response available; improvement also requires the learner to understand and use it. Sadler's abstract emphasizes recognizing quality, comparing one's work with it and having ways to improve, especially for judgments involving multiple criteria. A numerical correction alone does not reproduce that full account.

For the comparison task, “Wrong” reports a judgment. “You compared the package prices, but the question asks for price per kilogram” identifies a specific mismatch. A worked conversion can then supply missing knowledge; whether the learner can use it is examined in their subsequent work.

The feedback review by Wisniewski and colleagues reports heterogeneous effects and emphasizes informational differences. It does not establish that more feedback, immediate correction or repeated hints are universally better. In our example, a full worked solution may be useful instruction but would obscure an attempt intended to show independent reasoning.

Revision and new evidence also differ. Repairing a displayed calculation shows what the learner can do with that information. Applying the relation to a fresh comparison asks an additional question. Neither observation should overwrite the original response.

## Assistance and evidence conditions

The learning–performance distinction separates an observed response from an inference about lasting capability. Immediate success, later retention and application in a changed context require different observations.

For this Model's examples, the useful conditions include the question, prior answer exposure, actual hints, permitted tools, access accommodations and elapsed time where relevant. A calculator can remove arithmetic demands when the target is interpreting a rate; it would alter the task if unaided computation were the target.

“Independent” therefore needs a stated meaning. It might mean no answer-generating hints while still allowing a screen reader and calculator. Unknown help remains unknown. An AI correction without a suitable source or reproducible check remains an unverified interpretation, even when delivered confidently.

## A connected comparison example

This entire example is constructed. The prices are invented, the calculations are checked and the hypothetical responses are not learning records.

### What the task is meant to reveal

Suppose package A contains 600 g for £3.00 and package B contains 1 kg for £4.50. The question is: **Which has the lower price per kilogram? Explain your calculation and why it permits a comparison.** Assume equal product quality and ignore delivery costs and waste; this is a unit-reasoning task, not shopping advice.

The checking criteria are a common quantity basis, correct calculation, explicit units and a justified conclusion:

| Package | Common quantity | Calculation | Price per kilogram |
|---|---|---|---|
| A | 0.6 kg | £3.00 ÷ 0.6 kg | £5.00/kg |
| B | 1 kg | £4.50 ÷ 1 kg | £4.50/kg |

B has the lower price per kilogram, although A has the lower total package price. Dividing price by mass asks what the same one-kilogram quantity would cost at each rate.

### Reading an incomplete response

Hypothetical first response: “A, because £3 is less than £4.50.”

The observed comparison is between total prices. The common-unit criterion is unmet. It remains possible that the learner misunderstood the question, overlooked the quantities or does not understand unit pricing. “Cannot understand ratios” is a much broader conclusion than this response warrants.

A clarification such as “Are you comparing package price or price for the same mass?” could reveal how the learner read the task. It also directs attention to mass, so an improved response after it would be an assisted revision.

### Correction and another observation

A possible feedback message is: “Your comparison correctly identifies the lower package price. The question asks for price per kilogram. A contains 0.6 kg, so its rate is £3 ÷ 0.6 = £5/kg; B is £4.50/kg. The smaller total price does not make A the lower unit price.” This is authored instructional wording, not a proven optimal feedback script.

If the learner repeats “B is £4.50/kg,” the observation supports using the displayed correction, not an independent solution. A fresh constructed item changes the winning package so that “always choose the larger one” is insufficient:

| Package | Quantity and price | Checked rate |
|---|---|---|
| C | 750 g for £3.00 | £3.00 ÷ 0.75 kg = £4.00/kg |
| D | 1 kg for £4.50 | £4.50/kg |

C now has the lower unit price. A correct independently produced explanation would support this capability on another immediate item. It would not establish later retention, transfer to a different kind of rate or a causal benefit from AI coaching. The answer is visible here for readers; a live independent assessment would need an unrevealed item.

## Interfaces with other domains

| Domain | What assessment receives or contributes |
|---|---|
| Learning and cognition | Supplies hypotheses about understanding; responses constrain those hypotheses without directly revealing a mental state |
| Knowledge representation | Locates the relationship being assessed, such as quantity conversion; a concept map alone does not demonstrate understanding |
| Instructional design | Supplies capability goals and tasks; assessment exposes mismatches between them |
| Instruction and scaffolding | Uses feedback to shape assistance; the assistance supplied changes the interpretation of subsequent work |
| Memory and transfer | Specifies later or changed-context questions; assessment records the resulting evidence rather than inferring it from immediate success |
| Motivation and self-regulation | Receives information for self-monitoring; confidence and willingness remain distinct from task performance |
| Human–AI interaction | Affects available context, source checking and visible assistance; a lost or fabricated reply invalidates the supposed observation |
| Evaluation of AI-assisted learning | Uses bounded learner evidence; identifying the cause of improvement requires additional comparison and design |

The [body-of-knowledge outline](../docs/body-of-knowledge-outline.md#assessment-and-feedback) locates these interfaces. The [formative assessment Practice](../practices/formative-assessment-with-ai.md) conducts a coaching episode; this Model explains the relationships that make its observations and decisions meaningful.

## Limits and unresolved coverage

This is an introductory domain explanation for low-stakes adult learning, not a scoring engine, credential assessment or clinical diagnosis. Detailed rubric design, measurement models, reliability estimation, assessment bias, automated-grading calibration and subject-specific misconceptions need further sources and treatment. Feedback effects also depend on contexts not represented by the constructed arithmetic example.

The integration, diagram, comparison cases and interface descriptions are KPS-authored. They connect source-supported distinctions without claiming that any cited author published or tested the combined Model. An incorrect AI answer key, inaccessible task or unknown assistance can defeat an intended interpretation. No number of locally successful examples establishes general validity.

## Source alignment

All metadata alignments use **synthesis-contribution**: each publication supports an identified part, not the integrated account as a whole.

| Source | Contribution and inspected boundary |
|---|---|
| [NRC assessment report](../references/national-research-council-2001-assessment.md) | Chapter 2 purposes, uncertainty and triangle passages, pp. 37–51: alignment and interpretation quality. School-assessment context; no automated scoring guarantee |
| [Sadler](../references/sadler-1989-formative-assessment.md) | Publisher abstract only: quality, comparison and improvement moves. Limited relevance to purely binary answers; full article not inspected |
| [Wisniewski and colleagues](../references/wisniewski-zierer-hattie-2020-feedback.md) | Abstract and Introduction: informational feedback and heterogeneous effects. No new coding review or universal timing rule |
| [Soderstrom and Bjork](../references/soderstrom-bjork-2015-learning-versus-performance.md) | Abstract: durable learning versus observed performance. No universal delay or mastery threshold |

Supporting explanations preserve their own source boundaries: [Assessment Triangle](assessment-triangle.md), [Formative Assessment](../concepts/formative-assessment.md), [Feedback](../concepts/feedback.md), [Learning–Performance Distinction](../concepts/learning-performance-distinction.md) and [Metacognitive Calibration](../concepts/metacognitive-calibration.md).

## Evidence status

**Provisional.** Sources support bounded components; the synthesis has not received independent expert review or learner validation. Calculations and structural checks do not establish educational effectiveness. No actual learner response, retention result or transfer result is recorded here.
