# 开源情报池 - 2026 年第 25 周

> 收集时间: 2026-06-15  
> 领域: LLM / AI Agent / 开源基础设施

---

## 🏆 本周顶流

### 1. OpenClaw - AI Agent 框架标杆
- **⭐ Stars**: ~362k | **🔖 许可证**: MIT | **🔧 语言**: TypeScript
- **定位**: 开源、可自托管的个人全能 AI 助手
- **核心特性**:
  - 支持 WhatsApp、Telegram、Slack、Discord、Signal、iMessage、Teams 全通道
  - ClawHub 技能仓库已超 5,700+ 社区技能
  - 自带 LLM 编排层，BYOK（自带 API Key）模式
- **看点**: Cisco 披露供应链攻击和 prompt injection 漏洞后，社区正推进安全扫描和加固工具链。这不是玩具，是真基础设施。
- **GitHub**: https://github.com/openclaw/openclaw

### 2. MemPalace - AI 记忆基础设施
- **⭐ Stars**: 52,392 | **🔧 语言**: Python
- **定位**: 持久化 Agent 记忆的解决方案
- **看点**: 证明"AI 记忆"已从学术概念变成工程基础设施。Caveman Claude 之后，记忆层成了 Agent 架构的必争之地。
- **GitHub**: https://github.com/mempalace/mempalace

### 3. Caveman Claude - Token 优化利器
- **⭐ Stars**: 61,466 | **🔧 语言**: JavaScript
- **定位**: 极致压缩 LLM 调用成本
- **看点**: 开发者对 API 成本的焦虑已经到了需要用专门工具解决的地步。Token 优化正在成为一个独立赛道。
- **GitHub**: https://github.com/cavemanclaude/cavemanclaude

---

## 🚀 新兴热门

### 4. Terax AI - 轻量终端 AI IDE
- **⭐ Stars**: 3,695 | **🔧 语言**: Rust + Tauri + React
- **定位**: 7MB 的 AI 终端模拟器
- **看点**: Rust + Tauri 组合在 AI 工具链中开始发力，轻量 + 高性能成为新标杆。
- **GitHub**: https://github.com/terax-ai/terax

### 5. cc-switch - 跨平台 AI 助手统一入口
- **⭐ Stars**: 1,586 (月增迅猛) | **🔧 语言**: Rust
- **定位**: 一个桌面应用统一管理 Claude Code、Codex、OpenClaw、Gemini CLI 等
- **看点**: AI 工具碎片化到需要一个"工具的工具"来管理，这本身说明了生态的成熟。
- **GitHub**: https://github.com/farion1231/cc-switch

### 6. codegraph - 代码知识图预索引
- **⭐ Stars**: 3,112 | **🔧 语言**: TypeScript
- **定位**: 为 Claude Code、Codex、Cursor 等提供预索引的代码知识图
- **核心卖点**: 更少的 token、更少的 tool call、100% 本地
- **看点**: RAG 已不够，知识图 + 预索引正在成为代码理解的新范式。
- **GitHub**: https://github.com/colbymchenry/codegraph

### 7. Hermes Agent - 越用越聪明的 Agent
- **⭐ Stars**: 29,000+ | **🔧 语言**: Python
- **定位**: 自我进化型 AI Agent
- **核心架构**:
  - 技能学习系统：从任务经验自动提炼可复用技能
  - 三层记忆体系：事实记忆 / 对话记忆 / 技能记忆
  - 自改进循环：持续评估技能效果，主动优化
- **看点**: 普通 Agent 每次都从零开始，Hermes 会记住"上次怎么解决的"。
- **GitHub**: https://github.com/nousresearch/hermes-agent

---

## 🛠️ 基础设施与工具链

### 8. Mastra - TypeScript 原生 Agent 框架
- **⭐ Stars**: ~23k | **🔖 许可证**: Apache 2.0 | **🔧 语言**: TypeScript
- **定位**: Gatsby.js 团队打造的 TypeScript Agent 框架
- **核心特性**: Observational Memory - 文本记忆系统，token 成本降低 4-10x，长上下文表现超越 RAG
- **看点**: 压缩率惊人——文本 3-6x，工具输出 5-40x。成本敏感场景的杀手。
- **GitHub**: https://github.com/mastra-ai/mastra

### 9. TradingAgents - 多 Agent 金融交易框架
- **⭐ Stars**: 81,128 | **🔧 语言**: Python
- **定位**: 多 Agent LLM 金融交易框架
- **看点**: AI Agent 开始从"写代码"走向"赚钱"，金融是首个被冲击的严肃领域。
- **GitHub**: https://github.com/TauricResearch/TradingAgents

### 10. OpenMythos - LLM 架构实验场
- **⭐ Stars**: 13,113 | **🔧 语言**: Python
- **定位**: LLM 架构的前沿实验
- **看点**: 在架构层面探索 LLM 的新可能性，不只是应用层堆叠。
- **GitHub**: https://github.com/openmythos/openmythos

### 11. rtk-ai/rtk - Token 压缩代理
- **⭐ Stars**: 710 | **🔧 语言**: Rust
- **定位**: CLI 代理，LLM token 消耗降低 60-90%
- **看点**: 单二进制、零依赖。Rust 在 AI 基础设施层的性价比优势开始显现。
- **GitHub**: https://github.com/rtk-ai/rtk

### 12. withcoral/coral - Agent 统一 SQL 接口
- **⭐ Stars**: 378 | **🔧 语言**: Rust
- **定位**: 给 Agent 一个 SQL 接口，统一查询 API、文件、实时数据源
- **看点**: "给 Agent 一个统一查询层"——这个想法的潜力被严重低估。
- **GitHub**: https://github.com/withcoral/coral

---

## 🎯 趋势洞察

### 1. Token 优化成为独立赛道
Caveman Claude（61k+ stars）和 rtk（60-90% token 压缩）证明：当 LLM 调用成本成为日常开销，优化本身就成了产品。

### 2. "Skills" 生态爆发
从 Claude Skills 到 OpenClaw 的 5700+ 技能仓库，AI Agent 正从"写代码"转向"拼技能"。配置化、模块化、可复用是主旋律。

### 3. Rust 在 AI 基础设施层崛起
Terax AI（7MB 终端 IDE）、cc-switch、rtk、coral——Rust 在 AI 工具链中的存在感越来越强。不是替代 Python，而是在性能敏感的基础设施层找到自己的位置。

### 4. 记忆层成为 Agent 必争之地
MemPalace、Mastra 的 Observational Memory、Hermes Agent 的三层记忆体系——没有持久记忆的 Agent 只是玩具，有记忆的 Agent 才是生产力。

### 5. MCP 协议成为事实标准
MCP Servers 已超 84k stars，Unity MCP、Claude Code MCP 等扩展爆发。Agent 与工具的通信协议正在收敛。

---

## 📌 值得关注的早期项目

| 项目 | Stars | 语言 | 一句话 |
|------|-------|------|--------|
| earendil-works/pi | 782 | TypeScript | AI agent toolkit: 统一 LLM API + Agent loop + TUI |
| deeplethe/forkd | 138 | Rust | AI agent microVM 的 fork()，100ms 内 spawn 100 个子实例 |
| gi-dellav/zerostack | 132 | Rust | 极简 Rust 编码 Agent，优化内存占用和性能 |
| AlexsJones/llmfit | 117 | Rust | 一个命令测试数百个模型在本地硬件上的运行效果 |
| presenton/presenton | 232 | TypeScript | 开源 AI 演示文稿生成器，Gamma/Beautiful AI 替代品 |
| daniel3303/Equibles | 19 | C# | 自托管的 AI Agent 迷你彭博终端 |

---

## 🔗 参考来源

- OSSInsight GitHub Trending (2026-06)
- ecoa.vn Top 10 Trending AI Repositories
- buildmvpfast.com Best Open Source AI Projects
- cnbugs.com GitHub 热门 AI 开源项目盘点
- CSDN AI Weekly / GitHub 热门项目盘点

---

*本周情报收集完成。共追踪 18 个项目，覆盖 Agent 框架、记忆系统、Token 优化、基础设施工具链。*
