---
language: "KPS 9.x"
package_version: "0.3.0"
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
python3 test_validate.py
python3 tools/check_domain.py
python3 tools/build_navigation.py --check
python3 -m unittest discover -s tests -v
```

## Check boundaries

The upstream suite contains 52 regression tests. Domain checks require valid scholarly source locators, original application labels, adult scope, unchanged upstream copies and retained provisional status. Record tests use synthetic fixtures only; they do not grade a human answer or establish psychometric validity.

## One current task declarations

The optional `next_task` plan entry selects one current proposed task and names its output, checking criterion, assistance boundary and stop/split rule. Its stage ID must exist in the proposal. Optional session-record linkage fields have bounded types and cannot create an observed result. New tests reject unsupported multiple/invalid task declarations and broken plan linkage. These assertions test **format and authorship boundaries**, not whether the task is optimally sized, the criterion is scientifically adequate, or the learner improved.

## Two level plan declarations

The overview extension adds 41 regressions for the optional planning record and Practice integration. They check panorama-to-goal links, explicit propositions, task-specific prerequisites, stable stage IDs, assessment fields, revision rationale and absence of fabricated agreement or mastery. Conceptual cycles are distinct from contradictory required-before stage cycles. These tests do not establish the truth of dependencies or instructional effectiveness.

```bash
python3 tools/check_learning_plan.py data/two-level-learning-plan-template.json
python3 tools/check_learning_plan.py data/two-level-learning-plan-example.json
```

An empty template passes as a template, not as a completed plan. A constructed example is not an observed learner result. Historical execution records retain their original version scope; the overview run is recorded separately in data/overview-validation.json.

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

A passing test does not prove faithful terminology, sufficient evidence, causal effectiveness, model compliance, valid grading, privacy in a third-party product or learner competence. Check logs and versioned records for actual executed commands; intended checks are not results.

## Version and format compatibility

Compatibility of content version, KPS language and validator revision must be documented separately.

## Version declarations

```json
{"version":"0.3.0","based_on_core":"10.2.0","kps_language":"9.x","validated_with":"9.1.0","minimum_validator":"9.1.0","practice_format":"steps-first-v1"}
```

Upstream commit: `9432f1ee86f641d01444038cc81b7efa596b75dc`. File digests and exact reuse are in [upstream-lock.json](../upstream-lock.json). AUTHORING.md, TEMPLATES.md, validate.py, test_validate.py and LICENSE are copied unchanged. Their retained upstream frontmatter dates/version labels describe those upstream documents, not this domain's independent scientific review.

## The one task refinement

Domain release 0.2.1 refines the same five Practice identities and StageN headings without a KPS language change. The optional `next_task` planning entry and optional private session IDs retain compatibility with prior plan and session JSON records; the declaration checkers do not require a new schema version. The upstream contract, validators, templates and license remain identical to Core 10.2.0. New task scoping rules are KPS-authored design guidance, not a source-aligned Principle.

## Practices and links

New Practices are steps-first with consecutive StageN headings and usable actions. The six repeated labels used by old 9.0 packages are not required. An earlier validator can reject the new layout; major-language compatibility alone does not guarantee an old tool understands it.

The local scientific-policy and reading-and-diagrams guides explain this domain's adoption and supporting formats. Core-only tests of retired Core IDs and Core diagram counts are not copied blindly; domain tests exercise the corresponding local commitments.

## Root layout migration for 0 3 0

The update reduces root-level files by consolidating overlapping guides and moving generated views; **it does not delete scientific knowledge objects, source records or validation tooling**. All former filenames remain listed here for external-link migration. No root-level redirect stubs are left behind, because those would defeat the requested cleanup.

| Former root files | New location |
|---|---|
| `ONE-LEARNING-TASK.md`, `LEARNING-PLAN.md` | `guides/LEARNING-WORKFLOW.md` |
| `RECORDS.md` | `guides/SESSION-RECORDS.md` |
| `WORKED-EXAMPLE.md` | `guides/WORKED-EXAMPLE.md` |
| `SCOPE.md`, `ALIGNMENT.md` | `docs/SCIENTIFIC-POLICY.md` |
| `CHECKS.md`, `COMPATIBILITY.md` | `docs/VALIDATION.md` |
| `NAVIGATION.md`, `DIAGRAMS.md` | `docs/READING-AND-DIAGRAMS.md` |
| `REVIEW.md` | `docs/REVIEW.md` |
| `INDEX.md`, `PRACTICE-MAP.md`, `EVIDENCE-MAP.md`, `TERMINOLOGY-MAP.md`, `REVIEW-QUEUE.md`, `knowledge-graph.json` | same names under `generated/` |

Existing URLs pointing to former root paths will not automatically redirect on GitHub. Update external bookmarks and Markdown links deliberately. A copied relative link from an older version may need a new directory prefix; do not blindly replace text without considering the referring file's location. Generated views are rebuilt by `tools/build_navigation.py`. The dependency snapshot is refreshed only after reviewing affected local summaries and their source limits.

The validator, regression suite and licence (`validate.py`, `test_validate.py`, `LICENSE`) remain byte-identical to Core 10.2.0. The copied `AUTHORING.md` and `TEMPLATES.md` retain the same format requirements and examples but have **relative documentation links updated for the new local file paths**. `upstream-lock.json` records both their original Core hashes and the local adapted hashes; no identical-copy claim is made. The package still declares KPS Core 10.2.0, language 9.x, and validator 9.1.0. Automated checks establish structural integrity, not scientific approval.

## Independence

Ordinary reading and validation require no sibling repository, source archive or runtime internet access. Reference inspection may need external access. Future source, domain or Core revisions need separate review; no future release is prevalidated.
