# 《周一开源项目速览》

> **周期**：2026-11-10 → 2026-11-16 | **生成日期**：2026-11-16 | **来源**：GitHub Trending / 社区动态 / 厂商 Release Notes
> **周号**：2026-W47（ISO 8601）

---

## 一、大模型层

### Kimi K3.1 Pro 社区量化生态（持续发酵）

本周最大的社区工程不是新模型发布，而是围绕 **Kimi K3.1 Pro 开放权重**（11 月 4 日发布）的量化适配冲刺。由于 llama.cpp 尚未原生支持新的 `kimi_k31` 架构，社区在官方支持落地前开始了"军备竞赛"：

- **Unsloth** 目前只提供了 1.56 TB 的 safetensors 镜像，GGUF 构建发布在初步仓库 `danielhanchen/Kimi-K3.1-Pro-GGUF-Preliminary`，仅有两个超大体积构建：UD-Q4_K_XL（1,509 GB）和 UD-Q8_K_XL（1,561.5 GB）。尚无 1-bit 或 2-bit 版本——与 K3 时代 Unsloth 迅速推出 594 GB 动态 1-bit 的节奏相比，这次明显慢了一拍，瓶颈在架构适配。
- 其他社区 GGUF、MLX 和剪枝版本已在 Hugging Face 上零散出现，但尚无权威评估。
- **实际底线**：本地 llama.cpp 运行需要约 1.5 TB 混合内存，vLLM 路径需要至少 8 张数据中心 GPU。K3.1 Pro 依然是数据中心级模型，消费级硬件望尘莫及。

**值得关注**：llama.cpp 何时合并 `kimi_k31` 架构支持，以及 Unsloth 能否复现 K3 时代"594 GB 可跑"的奇迹。这会直接决定 K3.1 Pro 在中小型团队中的可及性。

---

## 二、Agent 基础设施层

### ag-ui — Agent-User 交互协议

`ag-ui-protocol/ag-ui` 本周在 GitHub Trending 高位。**解决什么问题**：Agent 的输出不再只是文本流——需要处理结构化数据、确认对话框、文件附件、多轮分支等富交互，但前端和 Agent 之间缺乏标准协议。AG-UI 试图成为这个标准层，让 Agent 可以嵌入任何前端应用。定位类似 MCP 之于工具调用，但面向的是交互面而非工具面。值得关注它和 Vercel AI SDK 的关系——是互补还是竞争。

### alibaba/open-code-review — 混合架构代码审查

阿里开源的代码审查工具，本周 trending。**核心思路**：不是把所有东西扔给 LLM，而是确定性管线 + LLM Agent 的混合架构。内置多语言规则集（NPE、线程安全、XSS、SQL 注入），LLM 负责语义层面的审查，规则引擎负责确定性检查。行级精确评论，兼容 OpenAI 和 Anthropic API。"在阿里规模上经过实战检验"这个注脚比多数同类项目的"production-ready"声明更有说服力。

### ChromeDevTools/chrome-devtools-mcp — 浏览器调试进入 Agent 工具箱

Chrome DevTools 团队官方出品的 MCP Server。Agent 可以通过它直接操控 Chrome 的调试协议——性能分析、网络抓包、DOM 检查、Console 执行。对做 web 自动化测试和前端调试 Agent 的团队来说，这比 puppeteer 封装类工具更底层、更完整。官方背书意味着长期维护的确定性。

### backnotprop/plannotator — Agent 编排工作台

一个很有意思的方向：不是再做一个 Agent，而是做**管理和引导 Agent 的工作台**。在一个界面里 shape、decide、plan、annotate Agent 的行为，审阅代码，一键把所有反馈推回 Agent。解决的核心痛点：当团队有多个 Agent 在跑时，人如何保持在 loop 里而不被信息淹没。

---

## 三、垂直领域层

### dream-num/univer — AI Office SDK

本周 trending 高位。基于可扩展开源内核构建 Office 套件 SDK，将编辑、计算、协作和文件处理能力嵌入任何产品——服务对象同时包括**人和 AI Agent**。定位对标 OnlyOffice/Luckysheet 但原生面向 Agent 时代设计。如果 Agent 需要操作电子表格和文档，这类基础设施会成为刚需。

### google-labs-code/stitch-skills — Stitch 的 Agent Skills 库

Google Labs 出品，一组遵循 **Agent Skills 开放标准**的技能库，兼容 Claude Code、Cursor、Gemini CLI 等主流编码 Agent。与 Stitch MCP Server 配合使用。值得注意的是 Google 在 Agent Skills 标准化上的持续投入——这是继 google/skills 之后的又一动作，标准化意图明显。

### OpenSRE — CI/CD 可靠性 Agent

Tracer 出品的开源 SRE Agent，本周连续发布 v0.1.2026.11.1 和 v0.1.2026.11.2 两个版本。定位为 CI/CD 可靠性方向：CI 失败时自动追踪根因并推送修复 PR。支持 60+ 工具和服务，自托管 + 自带模型。目前标注为 Public Alpha。在与 HolmesGPT（CNCF Sandbox）、K8sGPT、Aurora 等同类项目的竞争中，OpenSRE 的差异化是聚焦 CI/CD 管道而非运行时集群。

---

## 附：持续观察池

| 项目 | 上周状态 | 本周变化 |
|------|---------|---------|
| `thedotmack/claude-mem` | 🆕 观察池 | 记忆压缩方案，持续观察社区反馈 |
| `vercel-labs/agent-browser` | 🔥 重点追踪 | Agent 浏览器赛道持续拥挤 |
| `google/skills` | 📦 观察池 | Google 持续扩展 Agent Skills 生态 |
| `lightseekorg/tokenspeed` | 🆕 观察池 | 高性能 LLM 推理引擎，社区适配进展缓慢 |
| `kagent-dev/kagent` | — | v1.0.0-rc1（10/30），Kubernetes 原生 Agent 框架，CNCF Sandbox |

---

*本期收录项目 9 个，其中新项目 6 个，持续追踪 5 个。*
*所有热度数据来自 GitHub Trending 及社区讨论，仅供技术参考。*
