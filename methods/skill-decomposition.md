---
id: "ai-coach:method:skill-decomposition"
type: "method"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "Skill Decomposition"
evidence_status: "provisional"
reviewed: null
basis_kind: "KPS-authored reusable adaptation of component-skill analysis and integration guidance"
references: ["ai-coach:reference:ambrose-2010-component-skills"]
source_alignment: [{"reference": "ai-coach:reference:ambrose-2010-component-skills", "relation": "published-procedure-summary", "locator": "How Learning Works, chapter 4, printed pages 112 to 117: component skills, diagnosis, isolated practice and integration"}]
name: "skill-decomposition"
home: "1-plan"
also: ["4-test-and-fix", "5-coach-and-reflect"]
use_when: "A goal is too broad to choose practice or a recurring difficulty has no clear bottleneck"
ai_role: "Task analyst; propose component demands and distinguish evidence from hypotheses"
time: "15-20 min suggested; stop when one useful target is identified"
---

# Skill Decomposition

## Key takeaway

Map the demands of a whole task, check candidate bottlenecks and choose focused practice with a return to integration.

## Summary

Use actual work to select a practice target; a generated component list does not identify the learner's weakest skill.

## Purpose and rationale

Turn a broad skill into actionable practice. Separate knowledge, execution and coordination so a successful isolated step is not mistaken for successful whole-task performance.

## Inputs

- Target capability, representative whole task and success criteria.
- Credible subject guidance or an example checked by a competent performer.
- Existing attempts or baseline results, if available; a baseline is not compulsory.
- Relevant constraints, permitted support and an adjustable session budget.

## Steps

Run these steps as the AI; the learner supplies any requested performance.

1. **Locate the whole task.** Restate what successful performance looks like. Ask for missing context or an example and wait if it changes the analysis. Reuse existing evidence.
2. **Decompose.** Trace required knowledge, decisions, actions and coordination. Check dependencies against subject guidance; flag assumptions. Stop splitting when components are observable and useful for teaching, not at an arbitrary number of sub-skills.
3. **Inspect evidence.** For each component, mark demonstrated under stated support, difficulty observed or untested. Attach the relevant work. Never infer weakness from a self-rating or an AI-generated tree alone.
4. **Probe only if needed.** If competing explanations would lead to different practice, prepare a small task and checked criterion. Present it, wait for the response, then preserve the work and actual assistance before interpreting it. If missing evidence would not change the choice, proceed provisionally without another test.
5. **Select a target.** Explain which consequential, addressable demand the evidence points to and what remains uncertain. When isolated components succeed but the whole task fails, inspect coordination before assigning more isolated drills. Invite correction when the interpretation is uncertain; wait for a necessary clarification.
6. **Design the return.** Propose focused practice plus a new whole-task check with explicit criteria. Stop with one next action. If later component gains do not carry into the whole task, revise the decomposition or guidance.

## Prompt

```text
Help decompose [target capability] using [representative task and success
criteria], [subject source or checked example] and [existing work, if any].
Identify the knowledge, decisions, execution and coordination required.
Distinguish checked dependencies from assumptions. For each component, show
actual evidence and assistance or mark it untested. Do not invent my weakest
skill. If an unresolved distinction would change practice, present one checked
probe and wait for my response before judging it. Otherwise use existing evidence.
Recommend one consequential target, explain uncertainty, and provide both a
focused exercise and a whole-task return check. Keep the analysis revisable;
do not turn every component into a compulsory module. Return the component
table and one next action. Do not claim to have saved a record without doing so.
```

## Output and validation

Return `component | observable criterion | evidence and support | uncertainty | proposed practice`, then the chosen target and whole-task check. Check that every weakness claim has evidence and that focused success could be tested in the original capability.

**Constructed example:** For package-price comparison, inspect conversion (750 g to 0.75 kg), rate formation (price divided by quantity), calculation and comparison on common units. If conversion and supplied divisions succeed but the learner compares £/g with £/kg, focus on writing both rate units before judging. Return to a fresh complete comparison. More division exercises would not directly target the observed mismatch; this example reports no learner outcome.

## Common failures and limits

- **Ranking untested components:** retain unknowns and collect evidence only when useful.
- **Splitting too finely:** stop at distinctions that change instruction.
- **Treating every dependency as mandatory:** check the actual task and permitted tools.
- **Drilling parts without integration:** include a whole-task return criterion.
- **AI guesses about physical technique:** obtain observable evidence and qualified guidance where required.

## Next

Use [Baseline Check](baseline-check.md) for a consequential evidence gap or [Deliberate Practice Loop](deliberate-practice-loop.md) for a supported target. Use [Concept Mapping](concept-mapping.md) when the question concerns relationships among ideas rather than performance demands.

## Source alignment

[Ambrose and colleagues](../references/ambrose-et-al-2010-component-skills.md), chapter 4, pages 112-117, supports component analysis, focused practice and integration. Evidence labels, the AI procedure, prompt and example are authored adaptations; no unique universal decomposition is established.

## Evidence status

**Provisional.** No independent review, learner trial or exhaustive task-analysis protocol is claimed. The prompt does not guarantee AI behavior.
