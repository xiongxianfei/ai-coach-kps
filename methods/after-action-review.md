---
id: "ai-coach:method:after-action-review"
type: "method"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
canonical_name: "After Action Review"
evidence_status: "provisional"
reviewed: null
basis_kind: "KPS-authored reusable adaptation of a published team after-action review procedure to individual learning"
references: ["ai-coach:reference:salem-schatz-2010-after-action-review"]
source_alignment: [{"reference": "ai-coach:reference:salem-schatz-2010-after-action-review", "relation": "published-procedure-summary", "locator": "Guide to the After Action Review, version 1.1, printed page 1, Overview: four questions and AAR features"}]
name: "after-action-review"
home: "5-coach-and-reflect"
also: ["4-test-and-fix"]
use_when: "A completed attempt or project episode could inform a better next action"
ai_role: "Review facilitator; reconstruct evidence and challenge unsupported causal explanations"
time: "10-15 min suggested; focus on one meaningful episode"
---

# After Action Review

## Key takeaway

Review intention and actual events, distinguish evidence from explanations, and select an adjustment with a follow-up check.

## Summary

Facilitate a review of a completed episode using the learner's real record; keep useful actions and uncertain causes visible.

## Purpose and rationale

Decide what to retain or change after an attempt. The outcome alone does not identify which action caused it; compare the process with the original intention before proposing changes.

## Inputs

- One completed episode and its original goal, criterion and conditions.
- Actual work, feedback, help and relevant events; label recollections separately.
- Current constraints and an adjustable review budget.

## Steps

Run these steps as the AI; never supply missing events or the learner's account.

1. **Recover intention.** Restate the original goal from the record. If absent, ask what was intended and wait. Label a reconstructed intention; do not silently rewrite it to fit the result.
2. **Reconstruct events.** Summarize the actual work, support and deviations. Ask for missing facts only when they affect the review and wait for answers. Mark unresolved gaps unknown.
3. **Compare.** Apply the original criterion. Identify supported successes and difficulties without forcing one of each. Keep assisted completion distinct from independent performance.
4. **Investigate explanations.** Present plausible causes as hypotheses, including task design and feedback quality. Ask which evidence supports or challenges them; wait when the learner's account is necessary. Avoid attributing motives from a short record.
5. **Choose a change.** Propose a feasible adjustment, an action worth retaining and a way to judge the next attempt where evidence supports them. Let the learner choose; wait for a decision unless already supplied. Retaining the approach or collecting better evidence is an acceptable outcome.
6. **Close.** Return the dated review and next check. Stop when the decision is usable or the learner pauses. Provide a private copyable record; save only to an authorized private destination through an available tool, and report its actual result.

## Prompt

```text
Facilitate an after-action review of [completed episode] using [original goal,
criteria, actual work and events] within [time budget]. Recover what was intended
and what actually happened, distinguishing records from recollection and unknowns.
Ask about consequential gaps and wait for my answers; never invent missing events.
Compare the result with the original criterion and record actual assistance.
Identify supported successes and difficulties, then examine competing explanations
without treating them as proven causes or inferring motives. Help me choose one
feasible adjustment or a justified decision to retain the approach, plus a future
observation that could test it. Wait for my choice if I have not already made it.
Return a dated private review and next action; report saving only after a confirmed
write. Do not present the review as proof of learning or intervention effectiveness.
```

## Output and validation

Return `original intention | actual events and evidence | interpretation and uncertainty | retain or change | next check`. Distinguish the AI's recommendation from the learner's decision. Check that observations are traceable, proposed causes are labeled and the next action can be evaluated.

**Constructed example:** A learner intended to choose unit-price calculations independently, but the record shows AI-supplied division setups before each correct answer. Report successful calculation with support; independent setup remains unassessed. Possible causes include unclear help boundaries or extra AI assistance, not necessarily learner dependence. Retain unit checking and, if the learner chooses, withhold setups on the next fresh task. A requested demonstration remains a legitimate instructional choice. This review does not prove that its adjustment will improve performance.

## Common failures and limits

- **Changing the goal after seeing results:** preserve the original and record any later revision separately.
- **Inventing a neat narrative:** distinguish observations, recollections, hypotheses and unknowns.
- **Blame or empty praise:** examine work against criteria and include task or feedback problems.
- **A long list of lessons without action:** select a feasible change and a checking occasion.
- **Claiming a cause from one episode:** retain competing explanations and bounded conclusions.

## Next

Use [Deliberate Practice Loop](deliberate-practice-loop.md) for a supported performance target or [GROW Coaching](grow-coaching.md) when choosing a feasible action is the obstacle. A weekly review can aggregate episodes and revise priorities; it need not repeat this procedure for every session.

## Source alignment

[Salem-Schatz and colleagues](../references/salem-schatz-et-al-2010-after-action-review.md), Overview, printed page 1, supplies the review questions and team-review features. Individual use, causal checks, AI procedure, prompt and example are authored adaptations; no team-to-AI effectiveness equivalence is established.

## Evidence status

**Provisional.** No actual review outcome, independent appraisal or causal improvement claim is reported. Prompt wording cannot ensure model compliance.
