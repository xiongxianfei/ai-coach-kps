---
language: "KPS 9.x"
package_version: "0.1.0"
status: "draft"
---

# Content and authoring compatibility

## Key takeaway

Core content version, authoring language and structural checker version have different meanings.

## Summary

This domain is based on pinned KPS Core 10.2.0, follows the KPS 9.x authoring language and uses the unchanged 9.1.0 checker. It has its own 0.1.0 content version and no required sibling-package dependency.

## Version declarations

```json
{"version":"0.1.0","based_on_core":"10.2.0","kps_language":"9.x","validated_with":"9.1.0","minimum_validator":"9.1.0","practice_format":"steps-first-v1"}
```

Upstream commit: `9432f1ee86f641d01444038cc81b7efa596b75dc`. File digests and exact reuse are in [upstream-lock.json](upstream-lock.json). AUTHORING.md, TEMPLATES.md, validate.py, test_validate.py and LICENSE are copied unchanged. Their retained upstream frontmatter dates/version labels describe those upstream documents, not this domain's independent scientific review.

## Practices and links

New Practices are steps-first with consecutive StageN headings and usable actions. The six repeated labels used by old 9.0 packages are not required. An earlier validator can reject the new layout; major-language compatibility alone does not guarantee an old tool understands it.

The local ALIGNMENT and DIAGRAMS documents explain this domain's adoption and supporting formats. Core-only tests of retired Core IDs and Core diagram counts are not copied blindly; domain tests exercise the corresponding local commitments.

## Independence

Ordinary reading and validation require no sibling repository, source archive or runtime internet access. Reference inspection may need external access. Future source, domain or Core revisions need separate review; no future release is prevalidated.
