# 开源情报池 - W21 2026

> 周报 W21（2026.05.19–05.25）
> 采集时间：2026-05-25 10:00 CST

---

## 🎯 本周主题：多智能体架构 + Token 效率 + 端侧优先

从本周 GitHub  trending 趋势来看，创新重心已从「大模型本身」全面转向「外围基础设施」——记忆系统、代码索引、语音引擎、运行时、安全测试。模型单点优势不再足够，周边组件的质量决定成败。

---

## 📊 宏观数据

| 指标 | 数值 |
|------|------|
| Top 10 项目总星数 | ~29 万 |
| 7 天内新增星数 | 7.3 万+ |
| MCP 服务器总数 | 2.2 万+（Glama 注册表） |
| Anthropic MCP SDK 月下载量 | 9700 万+ |
| Agentic AI Foundation 成员数 | 150 家组织 |

---

## 🔥 热点项目速览

### 1. opencode / anomalyco — 开源编码代理之王
- ⭐ 14.8万+ | TypeScript | Apache 2.0
- 对标 Cursor 和 GitHub Copilot 的开源替代方案
- 支持多模型接入、终端交互、IDE 集成
- **本周增速**：+1,476 ⭐

### 2. pi-mono / badlogic — 智能体万能工具箱
- ⭐ 4.4万 | MIT | TypeScript/Rust
- AI agent toolkit：编码代理 CLI + 统一 LLM API + TUI/Web UI + Slack Bot + vLLM pods
- 所有组件可互换组合，200 行代码即可构建自定义 agent
- 发布真实 OSS 会话数据以改进编码代理

### 3. TradingAgents / TauricResearch — 多智能体交易公司
- ⭐ 6.3万 | Apache 2.0 | Python
- 镜像真实交易公司架构：基本面分析师 + 情绪分析师 + 技术分析师 + 交易员 + 风控
- 多智能体通过动态讨论、辩论、投票产生交易决策
- NeurIPS 相关论文背书
- **关键洞察**：这是目前最清晰的多智能体「角色专业化」架构范例

### 4. ml-intern / huggingface — 自主 ML 工程师
- ⭐ 8,100 | Hugging Face 出品 | Python
- 读论文 → 找数据集 → 微调模型 → 上传权重，全自动
- 300 次迭代 agentic 循环，敏感操作有审批门
- 会话痕迹自动上传到私有 HF 数据集，可调试可复现

### 5. claude-context / zilliztech — 语义代码搜索 MCP
- ⭐ 8,400 | TypeScript | 本周 +1,023 ⭐
- 为 Claude Code 提供基于向量搜索的代码库 MCP
- 解决大规模代码库上下文限制问题
- 企业级代码库智能重构和漏洞排查的关键基础设施

### 6. rtk / rtk-ai — Token 杀手
- ⭐ 3.3万 | Rust | 本周 +939 ⭐
- CLI 代理工具，减少 LLM 命令 Token 消耗 60-90%
- 零依赖 Rust 单二进制，智能压缩和缓存 LLM 请求
- 不修改业务代码即可接入

### 7. context-mode / mksglu — 上下文窗口优化
- ⭐ 9,400 | TypeScript | 本周 +302 ⭐
- AI 编码代理上下文窗口优化，减少 98% 工具输出
- 沙箱化工具输出 + 智能摘要，支持 12 个主流平台
- 解决长会话编程场景的「工作记忆」效率问题

### 8. cc-switch / farion1231 — AI 编码工具统一入口
- ⭐ 5.0万 | Rust | 本周 +725 ⭐
- 跨平台桌面 All-in-One 助手，整合 Claude Code + Codex + OpenCode + Gemini CLI
- 一键切换 + 会话共享
- 工具整合是生产力进阶方向

### 9. OpenClaw / openclaw — 开源个人 AI 助手
- ⭐ 36.2万+ | MIT | TypeScript
- 完全本地化运行，数据由用户掌控
- 5700+ 社区技能，50+ 渠道集成（WhatsApp/Telegram/Slack/Discord/Signal/iMessage）
- **注意**：Cisco 披露供应链攻击和提示注入漏洞，需审计每个集成技能

### 10. E2B / e2b-dev — 企业级代理沙箱
- ⭐ 1.2万 | Python
- 开源安全环境，为企业级代理提供真实工具
- 沙箱化代码执行

---

## 🏗️ 基础设施层

### MCP 协议生态
- **官方 MCP Servers**：⭐ 8.4万+，84k+ stars，提供文件系统、Git、数据库、搜索等参考实现
- **Context7**：⭐ 2.8万+，向上下文窗口注入 7000+ 库的实时文档
- **GitHub MCP Server**：⭐ 2万，⭐ 本周 +102
- **Sequential Thinking**：Anthropic 官方，结构化多步推理
- **Playwright Browser MCP**：浏览器自动化金标准
- **Memory MCP**：结构化知识图谱记忆系统

### 本地 LLM 栈
| 项目 | Stars | 角色 |
|------|-------|------|
| Ollama | 16.9万 | 本地运行 LLM 的最简方式 |
| Open WebUI | 13.2万 | ChatGPT 风格 Web 界面 |
| vLLM | 8.1万 | 高吞吐推理引擎 |
| llama.cpp | 9.0万 | C/C++ 高效推理 |
| LocalAI | 3.7万 | 本地 OpenAI API 兼容层 |

---

## 📈 趋势分析

### 1. 多智能体协作成为默认架构
单智能体 → 多智能体团队（专业化角色 + 辩论 + 投票）。TradingAgents 和 pi-mono 证明这不是 hype，而是实际架构演进。

### 2. Token 效率成为核心 KPI
- rtk（-60~90% Token）
- context-mode（-98% 工具输出）
- Mastra Observational Memory（文本压缩 3-6x，工具输出压缩 5-40x）
- 企业规模化运行 Claude Code/Codex/Cursor 的首要痛点

### 3. 端侧/本地优先成为主流
Top 10 中有 6 个项目声明端侧或本地优先架构。延迟、单调用成本、隐私是三大驱动约束。

### 4. MCP 成为 AI 工具的事实标准
- 从「有前途的想法」到「AI 智能体的默认集成层」，仅用 18 个月
- Claude Code、Cursor、Windsurf、VS Code、Red Hat OpenShift AI 全支持
- 预计 2026 年底所有主流 AI 平台都将支持 MCP

### 5. Claude Code Skills 成为独立品类
- academic-research-skills、codegraph 等垂直能力包
- 不是替代现有 agent，而是扩展它们
- 可安装、可卸载、可组合的模块化架构

---

## 🧠 值得追踪的新星

| 项目 | Stars | 描述 |
|------|-------|------|
| autoresearch / karpathy | 8.2万 | AI 代理在单 GPU NanoChat 自动训练上的研究 |
| UltraRAG / OpenBMB | 2,900+ | 低代码 MCP 框架，构建复杂 RAG Pipeline |
| airllm / lyogavin | 8,600+ | 单张 4GB GPU 跑 70B 模型 |
| modded-nanogpt / KellerJordan | 4,400 | 2 分钟训练 124M NanoGPT |
| hermes-agent / NousResearch | 4.2万 | 持续学习智能体 |
| DeepTutor / HKUDS | 1.4万 | AI 代理原生个性化学习助手 |
| PersonaPlex / NVIDIA | 8,600+ | 人物角色生成框架 |
| daily_stock_analysis / ZhuLinsen | 3.8万 | LLM 驱动 A/H/美股分析 |

---

## 🔗 参考链接

- [GitHub AI Trending 实时榜单](https://ossinsight.io/trending/ai)
- [awesome-ai-agents-2026 合集](https://github.com/Zijian-Ni/awesome-ai-agents-2026)
- [MCP 官方文档](https://modelcontextprotocol.io)
- [Top 5 Trending AI GitHub Repos May 2026](https://www.askglitch.com/blog/top-5-trending-ai-github-repos-may-2026)
- [GitHub Trending Top 10 May 2026](https://pasqualepillitteri.it/en/news/3327/github-trending-top-10-may-2026)

---

*周报 W21 开源情报池 — 采集完毕*
