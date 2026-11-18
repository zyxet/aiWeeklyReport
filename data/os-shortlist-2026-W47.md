# 《周三精选短名单》

> **周期**：2026-W47（ISO 8601）| **筛选日期**：2026-11-18 | **来源**：`os-pool-2026-W47.md`（9 候选 → 7 入选）
> **筛选规则**：Star < 100 且无媒体 coverage 的项目剔除

---

## 入选项目（7 个）

| # | 项目 | 实时 Stars | 本周增速 | 媒体 Coverage | 一句话定位 | 入选理由 |
|---|------|-----------|---------|--------------|-----------|---------|
| 1 | **Kimi K3.1 Pro 社区量化生态** | N/A (HF) | 持续发酵 | 🔴 极高 | 2.8T 参数模型的社区量化军备竞赛 | 11/4 权重开放后社区适配冲刺：Unsloth 发布 preliminary GGUF（UD-Q4_K_XL 1,509 GB / UD-Q8_K_XL 1,561.5 GB），llama.cpp `kimi_k31` 架构 PR 待合并，多家社区量化版陆续上架。morphllm、bestfreewebresources、DataCamp、什么值得买等密集报道 |
| 2 | **alibaba/open-code-review** | ~33,000+ | +951/day | 🔴 极高 | 混合架构代码审查工具 | 确定性规则引擎 + LLM Agent 混合管线，行级精确评论。InfoQ 专文报道，GitHub Trending 周榜第一，单周新增 14,000+ stars。阿里规模实战检验 |
| 3 | **ChromeDevTools/chrome-devtools-mcp** | ~57,000 | +841/day | 🔴 极高 | Chrome 调试协议官方 MCP Server | Chrome DevTools 团队官方出品。Agent 可直接操控性能分析、网络抓包、DOM 检查、Console 执行。比 puppeteer 封装更底层完整，官方背书 = 长期维护确定性 |
| 4 | **ag-ui-protocol/ag-ui** | ~16,500 | +791/day | 🟡 高 | Agent-User 交互协议 | 解决 Agent 富交互输出（结构化数据、确认对话框、文件附件）的标准化问题。定位类似 MCP 之于工具调用但面向交互面。Pydantic AI 官方文档已集成 |
| 5 | **dream-num/univer** | ~22,200 | +6,091/周 | 🟡 高 | AI Office SDK | v1.0.3 (9/29) 首个稳定版。Apache-2.0 开源内核 + 商业扩展。人和 AI Agent 共用同一套 Office 编辑/计算/协作引擎。Luckysheet 正统继任者 |
| 6 | **google-labs-code/stitch-skills** | ~6,400 | 稳定增长 | 🟡 高 | Google 官方 Agent Skills 库 | 遵循 Agent Skills 开放标准，兼容 Claude Code / Cursor / Gemini CLI / Codex。Google 在 Agent Skills 标准化上的持续投入信号。CSDN、github-wiki 等中文社区覆盖 |
| 7 | **backnotprop/plannotator** | ~1,300+ | +696/day | 🟡 高 | Agent 编排工作台 | 不做 Agent，做管理和引导 Agent 的工作台。兼容 Claude Code / Codex / Copilot CLI / Gemini CLI / OpenCode / OpenClaw 等 10+ 编码 Agent。解决多 Agent 场景下人如何保持在 loop 的核心痛点 |

---

## 剔除项目（2 个）

| 项目 | 实时 Stars | 剔除原因 |
|------|-----------|---------|
| OpenSRE (Tracer-Cloud/opensre) | ~3,200 | AI SRE 赛道拥挤（HolmesGPT / AURA / K8sGPT / Aurora 同质化竞争），Public Alpha 阶段，差异化不足以进入本周短名单。持续观察 |
| 持续观察池 5 项 | — | 非本周新收录，转入追踪列表 |

---

## 关键趋势解读

**本周主题：Agent 基础设施的"协议化"与"工具化"**

7 个入选项目中，5 个指向同一个趋势——Agent 时代的中间层正在快速固化：

- **交互协议**（ag-ui）：Agent ↔ 前端的通信标准
- **调试协议**（chrome-devtools-mcp）：Agent ↔ 浏览器的操控接口
- **技能标准**（stitch-skills）：Agent 能力封装的标准格式
- **编排工作台**（plannotator）：人 ↔ 多 Agent 的管理界面
- **文档引擎**（univer）：Agent ↔ Office 文件的操作引擎

加上大模型层 Kimi K3.1 Pro 的量化生态冲刺（基础设施的硬件维度），本周开源社区的主线非常清晰：**不是在造更多的 Agent，而是在造 Agent 需要的管道和扳手**。

---

*数据截至 2026-11-18 14:00 CST。Stars 数据来自 GitHub API / Trendshift / OSSInsight。*
