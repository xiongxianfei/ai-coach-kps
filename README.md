---
language: "KPS 9.x"
package_version: "0.1.0"
status: "draft"
---

# AI Learning Coach KPS

## Key takeaway

Start with a bounded adult learning task and preserve the evidence of what the learner actually did.

## Summary

A Practice-first, domain-independent knowledge package for independent adults using conversational AI as a learning coach. Four locally usable Practices are supported by source-aligned academic Concepts, Principles, Models and Methods. AI coaching workflows and prompts are explicitly authored applications, not established theories or tested programs.

## Start with a Practice

| Current task | Entry Practice | Output |
|---|---|---|
| Learn one concept or safe skill | [Self-Regulated Learning With an AI Coach](practices/self-regulated-learning-with-ai.md) | A target, source, original attempts, feedback and a next independent check |
| Understand a recurring task difficulty | [Formative Assessment With an AI Coach](practices/formative-assessment-with-ai.md) | Competing explanations, a probe and a justified instructional decision |
| Retain encountered material | [Retrieval and Distributed Practice With an AI Coach](practices/retrieval-and-distributed-practice-with-ai.md) | Checked questions, saved recall, corrections and a revisable review plan |
| Judge what was actually learned | [Evaluation of AI-Assisted Learning](practices/evaluation-of-ai-assisted-learning.md) | An evidence report separating assistance, retention and application |

Begin with the task that fits. The package does not require reading the full library or completing all four Practices. Each stage places actions, explanation and fallback together; stage numbers are a recommended route, not proof of prerequisites.

## First use

1. Select a low-stakes capability, a source you can inspect and a response that would demonstrate the target.
2. Open the first Practice and adapt its short opening prompt to your situation. Do not paste private data or trust an uninspected AI bibliography.
3. Preserve your attempt before feedback. Record actual hints and answer exposure, not just what was requested.
4. End with a bounded interpretation and next action. A prompt does not create memory, scheduling, expertise or learning by itself.

## What is included

There are **18 knowledge objects**: six Concepts, three Principles, two Models, three Methods and four Practices, with **22 stages** across the Practices. Fifteen Reference records document inspected source scope. Read [INDEX](INDEX.md), [Practice coverage](PRACTICE-MAP.md), [terminology](TERMINOLOGY-MAP.md) and [evidence map](EVIDENCE-MAP.md).

The Models are actual published frameworks: Cognitive Apprenticeship and the Assessment Triangle. The Methods summarize published Retrieval Practice, Self-Explanation and Cognitive Modeling. Distributed practice scheduling is implemented inside a Practice; abstract-only source access was not inflated into a detailed standalone scientific protocol.

## Evidence and outcome boundaries

The full package remains **provisional**. Some definitions are supported by selected full passages, others only by publisher abstracts. No systematic review, independent expert approval, learner study, model evaluation or live coaching trial is claimed. A scientific source does not validate every AI application derived from it.

General learning research and AI-specific studies are distinguished. A structured college physics tutor and a high-school mathematics field experiment do not directly establish effectiveness for every self-directed adult or generic chatbot. [REVIEW](REVIEW.md) records inspection, indirectness and open questions. [REVIEW-QUEUE](REVIEW-QUEUE.md) makes remaining work explicit.

## Architecture and independence

KPS role describes the job of a document, not its subject. Original assistance choices, prompts and local evaluation rules stay in Practices and supporting specifications. No new AI coaching theory is invented as a standalone Model. [ALIGNMENT](ALIGNMENT.md) explicitly adopts a domain version of Core's professional source-alignment policy.

This repository stands alone. It does not require the English Linguistics or Learning and Teaching KPS packages, an Obsidian plugin, an API key or an installed agent. It is knowledge and guidance, not a deployed chatbot. Ordinary relative Markdown links work without a knowledge-graph viewer.

## Check locally

Python 3.10 or newer and the standard library are sufficient.

```bash
python3 validate.py .
python3 test_validate.py
python3 tools/check_domain.py
python3 tools/build_navigation.py --check
python3 -m unittest discover -s tests -v
```

These commands check structure and declared boundaries, not educational efficacy. See [CHECKS](CHECKS.md). Blank [session records](data/session-record-template.json) and a [record guide](RECORDS.md) are provided for private use. Do not publish completed personal records.

## Versions and rights

Domain package: 0.1.0. Based on KPS Core **10.2.0**, authoring language **9.x**, structural validator **9.1.0**, Practice format **steps-first-v1**. [COMPATIBILITY](COMPATIBILITY.md) and [upstream lock](upstream-lock.json) identify the exact sources; the domain is not version 10.2.0 merely because Core is.

Original content and copied KPS tooling use the retained MIT license. Third-party publications retain their rights and are linked, not mirrored. See [NOTICE](NOTICE.md) and [CONTRIBUTING](CONTRIBUTING.md).
