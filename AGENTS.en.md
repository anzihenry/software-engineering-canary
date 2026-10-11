# 合成项目指令 (English)

[中文](AGENTS.md)

## Required routes

- For source changes or reviews use language-coding-standards; read common and the Python reference. Project commands are authoritative.
- Use documentation-maintenance and obtain nonauthor documentation-delivery-validation in a separate context with actual materials, current digest and real reports.
- Before edits use git-branch-management; fetch and reuse a task feature branch. main carries no task edits/commits. Read-only code review grants no edit/push/merge permission.
- The fixed knowledge checkout is `/tmp/harness-p0-fixed`, commit `952e840752741431c027097b5c242b7bc7fa3be5`. Read the named SKILL.md files under skills/04-implementation-and-self-test and skills/05-integration-validation; common/Python references are under language-coding-standards/references. Standards/templates come from that same checkout; do not use floating main.
- Missing tools, required translations/evidence/independent review, failed checks or candidate changes require blocking/revalidation. Do not self-authorize exceptions or production actions.

## Actual project commands

`docs/harness-adoption.json` is the sole command configuration. format/lint use Ruff from the current harness virtual environment, build uses Python py_compile, test uses unittest, documentation uses the fixed checker. The external adoption runner explicitly substitutes argv placeholders; code review may execute equivalent actual commands. Python 3.14 and Ruff 0.16.7; source is synthetic.py/test_synthetic.py with no production dependencies.

