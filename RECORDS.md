---
language: "KPS 9.x"
package_version: "0.1.0"
status: "draft"
---

# Learning observation records

## Key takeaway

Keep the original response, assistance, timing and verification separate from interpretation.

## Summary

The JSON record is a local reporting convention for private use, not a validated measurement model. Its checker detects inconsistent declarations and reports counts without producing mastery decisions.

## Start a private record

1. Copy data/session-record-template.json outside the public repository.
2. Specify the goal, task and criterion. Keep identifiers local and avoid unnecessary personal information.
3. Create a separate attempt when help or feedback changes the conditions. Never overwrite the original response with the revision.
4. Leave unobserved events and unknown fields blank. Do not turn a missing response into a numerical failure.
5. Run python3 tools/check_record.py /path/to/private-record.json to inspect declarations. Do not upload the private file to an AI service unless appropriate.

## Assistance and verification

answer_help records actual answer assistance as none, hint, partial_solution, full_solution or unknown. access_accommodations is separate. Independent means no answer-generating help during the attempt under the declared resources, not absence of all technology or prior learning. The same item can have been seen before; that affects interpretation and is reported separately.

verification_basis can be none, ai_only, source_checked, deterministic_check or human_review. A checked flag requires a locator describing the actual verification basis; the schema does not prove that inspection occurred. An AI-only judgment remains unverified. Criterion judgments may be meets, does_not_meet, uncertain or not_evaluated; they are not universal grades.

## Timing and changed context

Use actual timestamps and elapsed days when known. A future plan is not a delayed observation. The checker reports unknown timing rather than inventing it. A context_change description identifies what differs; it does not prove far transfer or general competence.

## Outputs and limits

The report counts planned, missing, observed and unchecked attempts. It never calculates a learning-effect size or declares mastery. Data validation does not verify truth, prevent all re-identification or establish a causal effect. The supplied template has no observed learner response, and tests contain constructed records, not user data.
