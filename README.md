---
title: "合成领域参考"
status: current
owner: maintainer
updated: "2026-10-12"
---

# 合成领域参考

[English](README.en.md)

固定harness `eb674f606ba36b6b8e5b7da3c00c40b915c49f17`，maintainer对应anzihenry，范围 `github`。这是合成试点，不是正式发布或生产部署；真实命令清单在采用配置。另起非作者上下文实际读取固定规范并执行任务；可访问与摘要不能证明采用。入口/知识/命令/环境/责任/权限或规则变化后复验。

[文档](docs/README.md)

[变更](CHANGELOG.md)

```text
python -m unittest discover --start-directory tests
python tests/fixtures/domain-reference/server.py --port 8765
```
