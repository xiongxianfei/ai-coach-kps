---
language: "KPS 9.x"
package_version: "0.2.1"
status: "draft"
---

# Two Level Learning Plan Records

## Key takeaway

Keep subject orientation, goal-specific conceptual structure, instructional hypotheses and actual learning evidence distinct.

## Summary

This is an optional local record format supporting the [planning Practice](practices/concept-mapping-and-instructional-sequencing-with-ai.md). It is not a scientific model, an obligatory software system, a validated learning progression or a mastery instrument. A plain private table is sufficient. The JSON version and checker make selected inconsistencies visible without deciding whether content is true or instruction effective.

## Begin with the three artifacts

| Artifact | Minimum useful information | Does not establish |
|---|---|---|
| Subject panorama | Boundary, major regions, purposes, selected relations, source limits and omissions | Complete disciplinary coverage or understanding |
| Goal concept map | One focus question, selected concepts, explicit propositions and links back to the panorama | Which concept must be learned first |
| Adaptive stage plan | Capability, concepts, activity, proposed prerequisites, allowed assistance, check, criterion and revision trigger | An observed learning outcome or universal progression |

The prerequisite register is a set of task-sensitive hypotheses, not a fourth knowledge level. Label a relation as required for this task, helpful, or corequisite only with a rationale and a way to probe it. Even a supported declaration must state the evidence and scope; the checker cannot verify it.

## Use the optional template

1. Copy [the blank template](data/two-level-learning-plan-template.json) outside the public repository. Use `record_kind: template` while fields are intentionally empty; a template pass does not mean a usable plan exists.
2. Inspect [the constructed example](data/two-level-learning-plan-example.json). It demonstrates syntax and hypothetical design only. No source review, learner agreement or performance is invented by the example.
3. Fill the panorama before zooming to the goal map. Existing checked panoramas can be reused; keep the versions and scope visible. Select `proposed_plan` when the records contain a usable proposal, or `constructed_example` for explicitly invented demonstration data.
4. Use stable region, concept and learning-stage IDs. `order` is a replaceable display position, not the stage identity or proof of developmental necessity. A stage ID such as `normalize` remains unchanged when reordered. This differs from the repository Practice's navigable StageN headings.
5. Keep the learner's actual response in a separate [session record](RECORDS.md). Refer to it privately in the prerequisite evidence or revision history rather than copying it into the public knowledge base.

## Choose one current task

A learning plan can contain several provisional stages while presenting **one next task** for immediate work. Use the optional `next_task` object to specify an `id`, `stage_id`, `task`, `observable_output`, `criterion`, `allowed_resources`, `assistance_boundary` and `stop_rule`. This is a proposed activity, not a learner response or a validated progression. `null` means no next task is selected yet; prior plans without this optional field remain readable by the checker. The ID references a stable learning-stage ID, not the navigable `StageN` headings of a KPS Practice. A day label is optional and never a performance claim.

Choose the smallest *meaningful* evidence-producing action, not the smallest dictionary fragment. If important relationships need to be applied together, the next task may be integrative. A ready learner may bypass redundant preliminary episodes with supporting evidence. See [the one-task guide](ONE-LEARNING-TASK.md); retain the original map, plan and revision history rather than overwriting earlier decisions.

## Field interpretation

`sources` records citations, locators and inspected/uninspected/constructed status. Source references on nodes or propositions support the content declaration, not learner competence. `source_supported` requires a declared inspected source; a source declaration does not prove that inspection occurred.

`panorama.regions` supplies the broad view, while `goal.panorama_region_ids` and `goal_map.concepts[].panorama_region_ids` preserve the zoom relationship. `goal_map.relations` stores source concept, linking phrase and target concept. Nodes alone are not the intended concept map. Source-supported, unverified and constructed propositions remain distinguishable.

`prerequisite_hypotheses` names concepts, kind, proposed/supported/rejected status, rationale, probe and evidence references. Unsupported hypotheses may remain proposed. Rejected prerequisites cannot remain in a stage's prerequisite list. Evidence references are descriptions of private records, not files the checker uploads or opens.

`learning_stages` provides target capability, concepts, activities, allowed instructional help, a separately specified check and an adaptation trigger. `next_task` selects at most one current proposed task from those stages; it never stores an observed answer. `requires_stage_ids` is reserved for a chosen required-before ordering of learning episodes. It needs its own rationale and may be revised; conceptual map edges are never converted automatically to stage dependencies. Related concepts may form cycles, but contradictory strict stage ordering must be repaired or combined into a corequisite episode.

`learner_agreement` remains `not_recorded` until actual agreement exists. `agreed` needs `agreement_evidence`; neither the assistant nor a test should fabricate it. `revision_log` states versions, affected stage IDs, the change and reason. A source correction or learner choice can justify a revision without inventing a performance result; a performance-based revision requires an actual observation reference. Retired or split stage IDs stay in the history instead of being repurposed.

## Adaptation from evidence

| Observation or choice | Planning response |
|---|---|
| Prior capability is demonstrated appropriately | Consider omitting redundant teaching; retain the observation |
| A relationship cannot be explained or used | Add a relational example or integration task |
| An answer is correct only after help | Record assistance and plan a new independent check |
| A required-before hypothesis is contradicted | Revise that hypothesis and the stages that relied on it |
| A source or map claim is erroneous | Correct the representation before interpreting learner performance |
| Goal, workload or interest changes | Re-scope or defer with learner agreement, not an invented failure |

A learner can pause, request a direct explanation or decline a check. There is no universally required number of regions, concepts, stages, attempts or minutes. Later retention and changed-context checks remain planned until actually performed.

## Read only checks

```bash
python3 tools/check_learning_plan.py data/two-level-learning-plan-template.json
python3 tools/check_learning_plan.py data/two-level-learning-plan-example.json
```

The checker validates the declared format, links between levels, proposition fields, references, prerequisites, stage ordering and revision declarations. It accepts conceptual cycles but rejects contradictory required-before stage cycles. It does not write, generate stages, fetch sources, inspect private referenced records, infer a learner state, schedule sessions or classify mastery. A successful check is structural only.

## Scientific and privacy boundaries

The source-aligned [Concept Map](concepts/concept-map.md) and [Concept Mapping](methods/concept-mapping.md) objects explain the scholarly representation and procedure. This record schema and the two-level coaching sequence are authored design choices. Preserve source limitations and keep private content outside public version control. These examples are constructed; no real learning results are stored here.
