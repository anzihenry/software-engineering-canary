---
title: "合成 Harness Canary (English)"
status: current
owner: maintainer
updated: "2026-10-11"
---

# 合成 Harness Canary (English)

[中文](README.md)

Synthetic canary for software-engineering lifecycle automation. This repository validates synthetic projects only, with no production data or deployment.

[Agent entry](AGENTS.en.md), [docs](docs/README.en.md), [changes](CHANGELOG.en.md).

## Shortest execution path

Python 3.14 is required; requirements-dev.txt pins development Ruff 0.16.7 and PyYAML. Run `python -c "from synthetic import add; print(add(2, 3))"` to print `5`. add accepts int only (rejects bool/float). Run `python -m unittest test_synthetic` to verify boundaries. Complete checks and documentation policy are in [project configuration](docs/documentation.en.md).

This synthetic evidence repository has no externally published license or released artifact; scope is in the original English [CANARY.md](CANARY.md).
