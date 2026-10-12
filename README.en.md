---
title: "Synthetic domain reference"
status: current
owner: maintainer
updated: "2026-10-12"
---

# Synthetic domain reference

[中文](README.md)

Fixed harness `eb674f606ba36b6b8e5b7da3c00c40b915c49f17`; maintainer is anzihenry; scope `github`. This is a synthetic trial, not a release or production deployment. Actual command lists are in the adoption configuration. A separate non-author reads the pinned rules and executes the task; availability and hashes alone do not prove adoption. Entry/knowledge/command/environment/roles/permission or rule drift requires revalidation.

[Documentation](docs/README.en.md)

[Changes](CHANGELOG.en.md)

```text
python -m unittest discover --start-directory tests
python tests/fixtures/domain-reference/server.py --port 8765
```
