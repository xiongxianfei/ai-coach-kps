---
language: "KPS 9.x"
package_version: "0.4.0"
status: "draft"
---

# Learning records

## Key takeaway

Keep the starting point, current assessment and supporting stage evidence distinct, so the learner can understand progress and resume the next lesson.

## Summary

This guide describes private learning notes for a small goal or a programme with many stages. The overview carries the current position; the initial assessment preserves starting evidence; stage records connect knowledge, actual responses, feedback and summaries. Plain Markdown is sufficient. The existing optional JSON record describes attempts and its checker detects inconsistent declarations; neither layout is a validated measurement model or an automatic mastery system.

## Programme continuity

The [master Practice](../practices/ai-assisted-learning-orchestration.md) includes a complete plain-text resume record, so JSON and separate files are optional. Existing `plan_id`, `plan_version`, `learning_stage_id` and `learning_task_id` connect an attempt to the programme when those records exist. No new required schema fields are introduced. Keep the overall target, stage decisions and task attempts distinct, and never fill a learner response merely to complete a template.

## Stage summaries and private storage

Keep completed learning records outside every public repository. For a small goal, one `learning-record.md` with separate sections is enough. When many stages make that file difficult to read, keep the overview short and move stage detail into separate files. One possible layout beneath a learner-chosen private directory is:

```text
learning-records/
  singing/
    learning-record.md
    initial-assessment.md
    stages/
      voice-production.md
      pitch-relationships.md
    images/
      voice-production-overview.png
```

These are illustrative paths, not files created by this guide. Use descriptive lowercase filenames. Create a stage file when work begins or existing notes need splitting; future stages can remain roadmap rows. A domain organizes subject knowledge, while a stage develops a learner capability: one stage can draw on several domains and revisit a domain used earlier.

| Record | Responsibility |
|---|---|
| `learning-record.md` | Goal and preferences, a short stage roadmap, dated current assessment with evidence links, and the next lesson or pending question |
| `initial-assessment.md` | Starting goal and conditions, self-report, baseline tasks and actual replies, assistance, interpretation and unknowns |
| `stages/*.md` | Stage capability and relevant domains; useful lesson explanations, meaningful answers, feedback, assistance and a stage summary |
| `images/` | Pictures embedded beside the stage explanations they support, with source or generation provenance retained |

These responsibilities can be sections of one file; they do not require a fixed template, score or new schema. A roadmap can be a short table of stage name, capability, current position and link when a file exists. Keep stable stage IDs and semantic filenames when reordering the route. If splitting or renaming a stage file, preserve original observations and update incoming evidence links and relative image paths. Existing separate records can be linked instead of copied. No file per lesson or mandatory history folder is needed.

## Initial and current assessment

The **initial assessment** preserves the starting evidence under the original goal and conditions. Distinguish a learner's self-report from an observed answer, and record actual assistance, answer exposure, the checking criterion and verification basis. Missing baseline evidence stays not assessed. Do not reconstruct an earlier answer from what the learner can explain after instruction.

The **current assessment** in the overview is a dated interpretation of available evidence, organized by relevant capabilities rather than whole-domain scores. For each useful conclusion, state what is supported, link to the actual observation and help conditions, and name the important uncertainty or next step. A compact table can compare starting evidence, current evidence and remaining gaps, but prose is equally valid. Not assessed, assisted success, independent immediate performance, delayed retention and practical application must remain distinguishable.

Update the current assessment at a stage boundary or when meaningful evidence changes the next decision, not after every conversational turn. Keep previous consequential judgments and their reasons in the relevant stage notes while the overview shows the latest position. If an earlier judgment or answer key was wrong, add a dated correction explaining why and update the current conclusion; preserve the original response and mark the earlier interpretation as superseded rather than silently rewriting the evidence. If the goal or criterion changes, record the new scope and avoid comparing unlike assessments as if they measured the same capability.

For example, in a hypothetical record, a correct response after a hint supports assisted performance. A later correct application without answer help can support a new, bounded current conclusion; it does not turn the first response into an independent baseline. Neither observation supplies delayed retention unless the timing and relevant conditions were actually observed. This example contains no learner results.

## Useful notes within a stage

Name the stage's capability and link to the relevant knowledge domains or Models. Keep lessons inside the stage file initially. Separate the connected explanation supplied during teaching from the evidence produced by the learner:

- Summarize useful mechanisms, examples and boundaries in enough detail to understand the lesson later; link to canonical explanations instead of copying entire Models.
- Preserve meaningful original answers with their question or task, criterion, actual help and feedback. A faithful excerpt or clearly labeled summary is acceptable when it preserves the reasoning needed to assess the response. Retain exact wording when interpretation depends on it. Do not save every conversational turn by default.
- Record an assisted correction or later attempt separately. An explanation supplied by the coach is teaching, not a learner response.

At the stage boundary, add a connected synthesis and one checked overview picture, what the actual evidence supports, remaining gaps and the next stage's purpose. Mark a pause or provisional transition explicitly. The summary is not a replacement for its supporting observations or a mastery certificate. Additional pictures are optional.

In a stage file such as `stages/voice-production.md`, embed the image with `![Voice production overview](../images/voice-production-overview.png)`. In a single root-level record, the relative path is `images/voice-production-overview.png`. Check the actual image exists and keep its essential meaning in text. Reuse a suitable subject illustration or create one with available tools, retaining provenance. If an image or private saving destination is unavailable, supply the text in the conversation and state the limitation; do not claim an asset or saved record exists.

## Feed useful gaps back into knowledge

A recurring question or unclear explanation can identify a reusable improvement. Note the missing distinction, mechanism, example or boundary, then check it against suitable sources before changing the owning subject file. Coaching-process improvements belong in AI Coach. A learner's difficulty motivates inspection; it does not establish a scientific claim or prove that the document is wrong.

When an authorized knowledge update is complete, link the note to the improved explanation. Preserve the original learning evidence and distinguish the later explanation from what was available at the time. Keep personal answers and assessments private; promoting a reusable explanation does not authorize publishing the learner record.

## Start a private record

A plain private note is sufficient. If structured JSON is useful instead, use the existing optional record:

1. Copy data/session-record-template.json outside the public repository.
2. Specify the goal, task and criterion. Keep identifiers local and avoid unnecessary personal information.
3. Create a separate attempt when help or feedback changes the conditions. Never overwrite the original response with the revision.
4. Leave unobserved events and unknown fields blank. Do not turn a missing response into a numerical failure.
5. Run python3 tools/check_record.py /path/to/private-record.json to inspect declarations. Do not upload the private file to an AI service unless appropriate.

For a multi-episode goal, keep the [planning record](learning-workflow.md) logically separate from observations, as sections in the same private Markdown file or separate existing records. Reference a plan version and stable learning-stage ID in your private note. The plan holds intended activities; this session record holds actual responses and assistance. Neither a plan edit nor a checked map link changes the original performance record.

## Link a single task to its plan when available

The optional `learning_task_id` identifies the bounded task currently being attempted, whether or not a formal plan exists. Optional `plan_id`, `plan_version` and `learning_stage_id` can relate this private observation to the corresponding plan version and stable learning-stage ID. If a stage link is supplied, a plan ID and version are required; these are declarations, **not** proof that the referenced plan or task actually exists. Omit the fields or leave them `null` for standalone learning tasks. A learner may produce several attempts for one task, each preserving its real help and conditions.

Use the [lesson and task guide](learning-workflow.md) to select an immediate observable output and criterion. The checker validates identifier shapes and observation declarations, but cannot inspect or certify an external private plan or infer mastery from one success.

## Assistance and verification

answer_help records actual answer assistance as none, hint, partial_solution, full_solution or unknown. access_accommodations is separate. Independent means no answer-generating help during the attempt under the declared resources, not absence of all technology or prior learning. The same item can have been seen before; that affects interpretation and is reported separately.

verification_basis can be none, ai_only, source_checked, deterministic_check or human_review. A checked flag requires a locator describing the actual verification basis; the schema does not prove that inspection occurred. An AI-only judgment remains unverified. Criterion judgments may be meets, does_not_meet, uncertain or not_evaluated; they are not universal grades.

## Timing and changed context

Use actual timestamps and elapsed days when known. A future plan is not a delayed observation. The checker reports unknown timing rather than inventing it. A context_change description identifies what differs; it does not prove far transfer or general competence.

## Outputs and limits

The report counts planned, missing, observed and unchecked attempts. It never calculates a learning-effect size or declares mastery. Data validation does not verify truth, prevent all re-identification or establish a causal effect. The supplied template has no observed learner response, and tests contain constructed records, not user data.
