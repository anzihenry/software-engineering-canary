# 合成项目指令

[English](AGENTS.en.md)

## 必需入口

- 源码修改或评审使用 language-coding-standards，读取 common 和本次 Python references；项目命令为执行标准。
- 文档维护使用 documentation-maintenance；交付前交给非作者的 documentation-delivery-validation，另起上下文、读取实际材料、当前摘要与真实报告。
- 修改前使用 git-branch-management；fetch 后复用任务分支，main 不承载任务修改或提交。读取源码评审不获得修改/推送/合并权限。
- 固定知识位置 `/tmp/harness-p0-fixed`，提交 `952e840752741431c027097b5c242b7bc7fa3be5`；从该 checkout 的 skills/04-implementation-and-self-test 和 skills/05-integration-validation 读取上述 SKILL.md，common/Python 在 language-coding-standards/references。规范与模板也从同一 checkout 读取，不使用浮动 main。
- 工具不可访问、译文/证据/独立评审缺失、检查失败或当前版本变化时阻塞/重验，不自批例外，不执行生产动作。

## 项目实际命令

`docs/harness-adoption.json` 是唯一命令配置，format/lint 用当前 harness 虚拟环境 Ruff；build 用 Python py_compile，test 用 unittest，documentation 用固定文档检查器。argv 占位值由外部采用运行器显式替换；源码评审直接运行等价实际命令。Python 3.14 与 Ruff 0.16.7，源码为 synthetic.py/test_synthetic.py；没有生产依赖。

