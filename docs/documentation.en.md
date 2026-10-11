---
title: "文档采用配置 (English)"
status: current
owner: maintainer
updated: "2026-10-11"
---

# 文档采用配置 (English)

[中文](documentation.md)

Standard source anzihenry/software-engineering `952e840752741431c027097b5c242b7bc7fa3be5`; maintainer maps to anzihenry. [documentation-check.json](documentation-check.json), [harness-adoption.json](harness-adoption.json). Task facts live only in this trial PR. A trusted maintainer publishes the independent immutable envelope, corroborating real validate/lifecycle-policy. Unchanged CANARY.md is a tracked legacy asset, owned by maintainer and due 2026-11-01. No production candidate or deployment.

## Adoption scope and checks

This trial uses Python 3.14 and Ruff 0.16.7 with no production dependencies. Actual commands have one source in [adoption configuration](harness-adoption.json): format/lint inspect synthetic.py and test_synthetic.py; build uses py_compile; tests use unittest; documentation invokes the pinned knowledge checkout documentation_check.py check against the main baseline. The caller explicitly substitutes configured placeholders. Local outputs are in the [original verification report](../verification.txt).

The [validate workflow](../.github/workflows/validate.yml) runs dependency installation, format, static checks, build, tests and pinned documentation validation on PRs. The [lifecycle-policy workflow](../.github/workflows/lifecycle-policy.yml) checks the current PR record. Both are existing required GitHub Actions checks, App ID 15368. Only after actual verification may a trusted maintainer publish the independent review status; enforcement requires authorized ruleset addition and readback. This trial PR retains server check URLs, full head/base/merge and the immutable review URL; task state lives only in the PR.

## Original assets and provenance

The [Agent runtime entry](../AGENTS.en.md) and Chinese entry route pinned harness rules and project commands without redefining formal standards. The [original installer guide](github-lifecycle-automation.md) is the unchanged Chinese harness asset at the pinned commit; the [original PR input template](../.github/PULL_REQUEST_TEMPLATE.md) is its unchanged English machine input. Both are installed byte-for-byte by the governance installer, registered as raw with hashes; they are not represented as translated formal project guides. This bilingual page explains their trial use and scope. The installer distributes governance, without first-layer standards/skills. Formal project knowledge is inventoried in documentation-check.json documents.

## Revalidation and migration

The maintainer revalidates each delivery and any changes to entrypoints, commands, knowledge pin, ownership, platform permissions or rules. External references are the pinned harness checkout docs/skills/templates. Original external trial reports are in /tmp/harness-p0-evidence/04; long-lived platform evidence is linked through this PR and immutable evidence commit. An independent reviewer cannot author current content. The actual review is placed in review-evidence.json on a separate evidence branch outside candidate history, bound to head/base/merge by the trusted publisher. Temporary reports are retained for this validation; platform records support later revalidation.

Unchanged original English [CANARY.md](../CANARY.md) scope policy is registered as legacy; maintainer owns migration by 2026-11-01. Changed README is immediately bilingual, without migration exemption. Failure, missing translation/evidence, old snapshot or new governance drift blocks delivery. No production deployment; trial PRs close without merging.
