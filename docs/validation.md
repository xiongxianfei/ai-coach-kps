---
language: "KPS 9.x"
package_version: "0.4.0"
status: "draft"
---

# Validation and compatibility

## Key takeaway

Verify structure and provenance without mistaking successful checks for scientific or learning outcomes.

## Summary

This guide combines runnable publication checks, declaration boundaries, KPS Core version compatibility, and root-migration procedures. Tests verify limited mechanical properties; they cannot evaluate educational effectiveness.

## Run and interpret the checks

Execute the declared checks, inspect failures, and distinguish structural integrity from educational outcome evaluation.

## Commands

```bash
python3 validate.py .
python3 tools/check_domain.py
python3 tools/build_navigation.py --check
python3 -m unittest discover -s tests -v
```

## Master orchestration checks

The 0.4.0 update adds a self-contained master and preserves all five original specialist files. New domain tests check the declared composition, hierarchy, response-wait boundary, inline specialist responsibilities, evidence distinctions, unchanged record schemas, preserved root layout and source-review limits. The response-wait mutation check remains. Tests that required numbered actions or banned supporting stage links have been removed; those properties do not establish usability. Text and metadata checks do not establish usability or educational effectiveness; report author walkthroughs and change-specific check results in the PR.

Record actual local and archive check results in the change PR. The ordinary validation commands above include the new tests. The master uses existing optional session and plan records; their checkers are unchanged.

## Check boundaries

The full shared validator suite is maintained in Core; this domain checks the pinned copy and validates its actual files. Domain checks require valid scholarly source locators, original application labels, adult scope, declared upstream provenance and retained provisional status. Record tests use synthetic fixtures only; they do not grade a human answer or establish psychometric validity.

The local source-alignment profile also admits explanatory domain Models using `synthesis-contribution`. Each contribution needs an inspected locator and a description of what the source supports; the Model must identify KPS synthesis authorship. Focused declaration regressions reject missing authorship, missing contributions and use of that relation outside Models. The former exact two-Model inventory assertion was removed because it did not test source faithfulness. That Model policy did not change the validator; its later local adaptations are recorded below. Checks still cannot validate the synthesis scientifically.

## One current task declarations

The optional `next_task` plan entry selects one current proposed task and names its output, checking criterion, assistance boundary and stop/split rule. Its stage ID must exist in the proposal. Optional session-record linkage fields have bounded types and cannot create an observed result. New tests reject unsupported multiple/invalid task declarations and broken plan linkage. The single record can describe a related question set in its existing text fields; it does not impose a one-question lesson. These assertions test **format and authorship boundaries**, not whether the task is optimally sized, the criterion is scientifically adequate, or the learner improved.

## Two level plan declarations

The overview extension adds 41 regressions for the optional planning record and Practice integration. They check panorama-to-goal links, explicit propositions, task-specific prerequisites, stable stage IDs, assessment fields, revision rationale and absence of fabricated agreement or mastery. Conceptual cycles are distinct from contradictory required-before stage cycles. These tests do not establish the truth of dependencies or instructional effectiveness.

```bash
python3 tools/check_learning_plan.py data/two-level-learning-plan-template.json
python3 tools/check_learning_plan.py data/two-level-learning-plan-example.json
```

An empty template passes as a template, not as a completed plan. A constructed example is not an observed learner result. References retain source-inspection scope. Record dependent-summary review and executed checks in the change PR; old execution logs remain available in Git history.

## Summary review

When a dependency changes, inspect affected local summaries and their source limits. Then, and only then, run:

```bash
python3 tools/build_navigation.py
python3 validate.py . --accept-reviewed-summaries
python3 validate.py .
```

Ordinary CI never accepts fingerprints automatically. The initial baseline follows AI-assisted authoring review, not independent scientific review.

## Archive and CI

A downloadable archive can include a checksum manifest and must be checked after fresh extraction. A Git source tree should not contain a stale archive manifest. The permanent CI is read-only, uses a commit-pinned checkout action and no AI API credentials. Temporary authoring-transfer workflows must not be present in the final PR.

## Not established

A passing test does not prove faithful terminology, sufficient evidence, causal effectiveness, model compliance, valid grading, privacy in a third-party product or learner competence. Check the change PR and CI logs for actual executed commands; intended checks are not results.

## Version and format compatibility

Compatibility of content version, KPS language and validator revision must be documented separately.

## Version declarations

```json
{"version":"0.4.0","based_on_core":"10.2.0","kps_language":"9.x","validated_with":"9.1.0","minimum_validator":"9.1.0","practice_format":"steps-first-v1"}
```

Upstream commit: `9432f1ee86f641d01444038cc81b7efa596b75dc`. File digests and exact reuse are in [upstream-lock.json](../upstream-lock.json). LICENSE remains an unchanged copy. The Core 9.1.0 validator has the explicit local adaptations described below; its upstream commit and original checksum remain pinned. docs/authoring.md and docs/templates.md adapt local links; docs/authoring.md also adapts the local test command and review-record destinations. The original regression suite is retained in Core at the pinned commit. Their retained upstream frontmatter dates/version labels describe those upstream documents, not this domain's independent scientific review.

## The one task refinement

Domain release 0.2.1 refines the same five Practice identities and StageN headings without a KPS language change. The optional `next_task` planning entry and optional private session IDs retain compatibility with prior plan and session JSON records; the declaration checkers do not require a new schema version. That task refinement retained the Core 10.2.0 validator behavior; subsequent local adaptations are recorded below and in the upstream lock. New task scoping rules are KPS-authored design guidance, not a source-aligned Principle.

## Documentation filename migration

Ordinary documentation now uses lowercase kebab-case. This filename-only migration preserves each document's responsibility and its heading anchors. Update external bookmarks and private notes using these paths; no duplicate files or redirects are retained.

| Former path | Current path |
|---|---|
| `docs/AUTHORING.md` | [Authoring](authoring.md) |
| `docs/INDEX.md` | [Knowledge index](index.md) |
| `docs/READING-AND-DIAGRAMS.md` | [Reading and diagrams](reading-and-diagrams.md) |
| `docs/SCIENTIFIC-POLICY.md` | [Scientific policy](scientific-policy.md) |
| `docs/TEMPLATES.md` | [Templates](templates.md) |
| `docs/VALIDATION.md` | [Validation](validation.md) |

`docs/body-of-knowledge-outline.md` is unchanged. Navigation generation writes `docs/index.md`; original upstream filenames and checksums remain in `upstream-lock.json`, whose local paths and digests describe the renamed copies. That filename migration did not change validator behavior.

## Practices and links

New Practices are steps-first with consecutive StageN headings and usable actions. The six repeated labels used by old 9.0 packages are not required. An earlier validator can reject the new layout; major-language compatibility alone does not guarantee an old tool understands it.

The authoring contract and Practice template also adopt the clarified separation of required content, required format and optional presentation, including contextual method selection, relevant trade-offs and reasons to reconsider a choice. Method guidance also permits documentation for one intended Practice and explains source investigation, sufficient depth and flexible presentation. These authoring changes did not alter the Core pin, record schemas or stable Practice stages. The separate removal of the validator's stage-format heuristic is documented below. The original upstream checksums remain in the lock alongside the current local file digests.

The local authoring, template and scientific-policy guidance also adopts open selection from learning needs and permits source-grounded reusable Method adaptations with explicit changes and limits. This is a documentation-policy adoption, not a Core upgrade: the validator, allowed alignment relations, record schemas and original upstream checksums remain unchanged. The current adapted authoring/template digests are recorded separately in the lock.

The local scientific-policy and reading-and-diagrams guides explain this domain's adoption and supporting formats. Core-only tests of retired Core IDs and Core diagram counts are not copied blindly; domain tests exercise the corresponding local commitments.

## Root layout migration for 0 3 0

The update reduces root-level files by consolidating overlapping guides and moving generated views; **it does not delete scientific knowledge objects, source records or validation tooling**. All former filenames remain listed here for external-link migration. No root-level redirect stubs are left behind, because those would defeat the requested cleanup.

| Former root files | New location |
|---|---|
| `ONE-LEARNING-TASK.md`, `LEARNING-PLAN.md`, `guides/LEARNING-WORKFLOW.md` | `guides/learning-workflow.md` |
| `RECORDS.md`, `guides/SESSION-RECORDS.md` | `guides/learning-notes.md` |
| `WORKED-EXAMPLE.md` | `guides/WORKED-EXAMPLE.md` |
| `SCOPE.md`, `ALIGNMENT.md` | `docs/scientific-policy.md` |
| `CHECKS.md`, `COMPATIBILITY.md` | `docs/validation.md` |
| `NAVIGATION.md`, `DIAGRAMS.md` | `docs/reading-and-diagrams.md` |
| `REVIEW.md`, `docs/REVIEW.md` | Removed; source evidence remains in References, knowledge gaps in owning documents, and change-specific review in PRs |
| `INDEX.md`, `generated/INDEX.md`, Practice and terminology maps | [Combined knowledge index](index.md) |
| Evidence map | Canonical [claim records](../data/claims.json) |
| Review queue | Reference inspection limits and gaps in the owning knowledge documents |
| `knowledge-graph.json` | Removed; no consumer requires the export |
| `AUTHORING.md`, `TEMPLATES.md` | `docs/authoring.md`, `docs/templates.md` |
| `CONTRIBUTING.md` | `.github/CONTRIBUTING.md` |

Existing URLs pointing to former root paths will not automatically redirect on GitHub. Update external bookmarks and Markdown links deliberately. A copied relative link from an older version may need a new directory prefix; do not blindly replace text without considering the referring file's location. Generated views are rebuilt by `tools/build_navigation.py`. The dependency snapshot is refreshed only after reviewing affected local summaries and their source limits.

The licence (`LICENSE`) remains byte-identical to Core 10.2.0. The validator derives from that release, with a local template exception: the two copyable private-note scaffolds at `templates/learning-notes/learning-notes.md` and `templates/learning-notes/stages/01-stage-name.md` need no Key takeaway or Summary headings. They still receive language, title, heading and local-link checks. The exception applies only to those exact paths without knowledge type or identity; ordinary documents and knowledge objects retain their summary requirements. These private-note scaffolds are not new KPS knowledge roles. The upstream and locally adapted validator hashes are both recorded in `upstream-lock.json`. The copied regression suite was subsequently removed under the test allowlist. The copied `docs/authoring.md` and `docs/templates.md` retain the same format requirements and examples but have **relative documentation links updated for the local file paths, the authoring test command adapted to the domain suite, and review-record destinations adapted to References, owning knowledge documents and PRs**. `upstream-lock.json` records both their original Core hashes and the local adapted hashes; no identical-copy claim is made. The package still declares KPS Core 10.2.0, language 9.x, and validator 9.1.0. Automated checks establish structural integrity, not scientific approval.

## Stage usability and the local validator adaptation

The pinned Core 9.1.0 copy now also backports the removal of `has_local_actions` and its `stage-actions` error from [Core PR 17](https://github.com/xiongxianfei/knowledge-practice-system/pull/17). This is a deliberate, narrow adaptation, not an upgrade to Core 9.2.1: original upstream commit, version and checksum remain recorded alongside the current local digest in `upstream-lock.json`. The existing private-note exception remains; Model-opening behavior and all other validator checks stay at the local pinned baseline.

Core owns the shared checker change and removes its formatting-heuristic tests. AI Coach removes the additional tests requiring numbered actions and prohibiting Markdown links inside stages. Metadata, link targets, stage navigation, response-wait and other existing checks remain. Passing them establishes neither locally sufficient instructions nor reader capability.

Review a representative task with links hidden: can the reader act, interpret the result and choose the next action without guessing essential information? Record concrete locations, gaps, consequences, fixes and remaining limits in the PR description, identifying an author walkthrough separately from an actual reader trial. If no material gap is found, report the examined task and limit. Do not create a review file or completeness score. A link-only or unhelpful stage remains an editorial problem even when mechanically valid.

## Independence

Ordinary reading and validation require no sibling repository, source archive or runtime internet access. Reference inspection may need external access. Future source, domain or Core revisions need separate review; no future release is prevalidated.

## Maintenance tool audit

Reading and applying a Practice requires no scripts. The existing tools have bounded maintenance jobs:

| Tool | Purpose retained |
|---|---|
| `validate.py` | KPS structure, links and dependency checks on this package |
| `tools/check_domain.py` | Source-alignment declarations, evidence boundaries and role constraints |
| `tools/build_navigation.py` | Keep the combined knowledge index and source register aligned with canonical Markdown |
| `tools/check_record.py` | Detect inconsistent declarations in a private session record without inferring mastery |
| `tools/check_learning_plan.py` | Detect missing or inconsistent plan fields and references without asserting prerequisite truth |
| `tests/` | Exercise those contracts, examples and their failure cases |

Retain the pinned local checker and allowlisted domain tests for independent use; Core owns shared validator regressions. Fixed-layout, fixed-count, release-version and redundant prose assertions were removed. Updating the pin is a separate compatibility decision. No new synchronization or publication script is required.

`.gitattributes` keeps text in LF format. This preserves the exact bytes used by dependency fingerprints and the upstream-file checks. A line-ending conversion is not evidence of changed knowledge; restore intended line endings before reviewing checksum failures.

## Test allowlist

Retain pinned-file integrity, actual package source and evidence declarations, generated-view freshness, and learning-plan/session-record behavior. Exercise accepted records, rejected inconsistent declarations and read-only behavior. The full shared validator suite stays in Core at the `upstream_regression_suite` revision recorded in the lock. Old root inventories, file counts, release numbers and duplicate phrase assertions are retired. A new test must identify a concrete failure within one of these responsibilities.
