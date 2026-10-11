---
title: "文档采用配置"
status: current
owner: maintainer
updated: "2026-10-11"
---

# 文档采用配置

[English](documentation.en.md)

规范源 anzihenry/software-engineering `952e840752741431c027097b5c242b7bc7fa3be5`，角色 maintainer 对应 anzihenry。配置 [documentation-check.json](documentation-check.json)；采用 [harness-adoption.json](harness-adoption.json)。任务事实仅保留在本轮 PR；独立评审通过受信维护者发布不可变 envelope，并回读真实 validate/lifecycle-policy。未触及 CANARY.md 作为限期旧资产，迁移责任 maintainer，截止 2026-11-01。当前无生产候选或部署。

## 采用范围与检查

本轮使用 Python 3.14、Ruff 0.16.7，无生产依赖。真实命令唯一维护在 [采用配置](harness-adoption.json)：format/lint 检查 synthetic.py 和 test_synthetic.py；build 使用 py_compile；test 使用 unittest；documentation 使用固定知识 checkout 的 documentation_check.py check，对照 main 基线。调用者显式替换配置占位值；本地输出保存在 [原始验证报告](../verification.txt)。

[validate workflow](../.github/workflows/validate.yml) 在 PR 上执行依赖安装、格式、静态检查、构建、测试及固定版本文档检查；[lifecycle-policy workflow](../.github/workflows/lifecycle-policy.yml) 检查当前 PR 记录。两项均为现有必过 GitHub Actions 检查，App ID 15368。远端独立评审状态只有真实验证通过后才由受信维护者发布；需要获授权的 ruleset 追加与回读后才宣称强制生效。PR 保留服务器 check URL、完整 head/base/merge 与不可变评审 URL，任务状态仅在 PR 维护。

## 原始资产与来源

[Agent 运行入口](../AGENTS.md)及英文入口只路由固定 harness 规则和本项目命令，不重新定义正式标准。[原始安装器说明](github-lifecycle-automation.md)为固定提交原文中文 harness 资产；[原始 PR 输入模板](../.github/PULL_REQUEST_TEMPLATE.md)为同一固定提交的英文机器输入。两份均由治理安装器按原始字节接入，登记 raw 及 SHA，不把它们当已翻译的项目正式指南；本页中英说明本轮用途与范围，安装器职责仅治理，未分发第一层规范技能。本项目正式知识文档列于 documentation-check.json 的 documents 清单。

## 复核与迁移

maintainer 在每次任务交付，以及入口/命令/知识 pin/责任/平台权限或规则变更后复验。外部资料为固定 harness checkout 的 docs、skills、templates；外部原始试点报告位于 /tmp/harness-p0-evidence/04，长期平台证据链接保存于本轮 PR 和独立证据提交。独立评审者不能参与当前内容编写，实际记录置于候选历史外独立证据分支 review-evidence.json，经受信发布者绑定 head/base/merge。临时报告保留期只限本轮验证，平台记录用于长期复验。

未触及 [CANARY.md](../CANARY.md) 的原始英文范围政策以 legacy 登记；maintainer 到 2026-11-01 处理迁移。本轮受影响 README 已立即补齐双语，不借迁移豁免。失败、缺译文、缺证据、旧快照或新治理漂移阻塞；不执行生产部署，试点 PR 关闭而不合入。
