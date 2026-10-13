---
language: "KPS 9.x"
package_version: "0.2.0"
status: "draft"
---

# Validation and its limits

## Key takeaway

Structural integrity and evidence-declaration checks do not certify learning or coaching effectiveness.

## Summary

The unchanged KPS 9.1.0 checker validates the package format. Domain tests separately inspect source alignment, Practice coverage, record declarations and generated navigation. Actual execution results are reported outside claims of scientific review.

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
