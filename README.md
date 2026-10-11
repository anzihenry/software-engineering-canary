---
title: "合成 Harness Canary"
status: current
owner: maintainer
updated: "2026-10-11"
---

# 合成 Harness Canary

[English](README.en.md)

# software-engineering-canary
Synthetic canary for software-engineering lifecycle automation

本仓库只验证合成项目，不含生产数据或部署。

[项目入口](AGENTS.md)、[文档](docs/README.md)、[变更](CHANGELOG.md)。

## 最短运行路径

环境需要 Python 3.14；开发检查安装 requirements-dev.txt 固定 Ruff 0.16.7 和 PyYAML。执行 `python -c "from synthetic import add; print(add(2, 3))"` 得到 `5`；add 只接收 int（拒绝 bool/float）。执行 `python -m unittest test_synthetic` 核对边界。完整检查与文档规范见 [文档配置](docs/documentation.md)。

这是保留验证证据的合成仓库，没有对外发布许可证或发布制品；试点用途见原始英文 [CANARY.md](CANARY.md)。
