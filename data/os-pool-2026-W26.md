# 周一开源项目速览 — 2026-W26

> 采集时间：2026-06-22 10:00 CST  
> 本周主题：Agent 基础设施爆发，多 Agent 编排与记忆系统成焦点

---

## 一、本周明星项目

### 1. calesthio/OpenMontage ⭐ 8,487（今日+993）
- **定位**：全球首个开源代理视频制作系统
- **亮点**：12条管道，52种工具，500+代理技能。把 AI 编码助手变成完整视频制作工作室
- **语言**：Python
- **趋势**：今日新增近1k star，爆发式增长

### 2. chopratejas/headroom ⭐ 44,115（今日+2,617）
- **定位**：LLM 输入压缩利器
- **亮点**：在工具输出、日志、文件和 RAG 块到达 LLM 前进行压缩，60-95% token 减少，答案质量不变
- **语言**：Python
- **趋势**：今日暴涨2600+ star，开发者对 token 优化需求强烈

### 3. bytedance/deer-flow ⭐ 72,514（今日+415）
- **定位**：开源长期超级 Agent 工具
- **亮点**：支持研究、编码和创作，通过沙箱、记忆、工具、技能、子代理和消息网关处理分钟到小时级任务
- **语言**：Python
- **趋势**：字节出品，持续稳健增长

---

## 二、分类扫描

### 🤖 AI Agents / Workflows

| 项目 | Stars | 简介 |
|------|-------|------|
| multica | +534 today | 开源托管 Agent 平台，任务分配、进度跟踪、技能复合 |
| superpowers | +1,576 today | Agent 技能框架与软件开发方法论 |
| agency-agents | +1,018 today | "AI 代理公司"开箱即用，预置专家代理与交付流程 |
| agentmemory | 14,183 | AI 编程 Agent 持久化记忆系统，跨会话记忆能力 |

### 🔧 AI Infrastructure

| 项目 | Stars | 简介 |
|------|-------|------|
| codegraph | +4,294 today | 预索引代码知识图谱，减少 token 和工具调用 |
| Oh-My-Pi | +500 today | 终端原生 AI 编码 Agent，哈希锚定编辑 + LSP 集成 |
| CLI-Anything | +656 today | 让任何软件"Agent 原生"的通用 CLI 接口框架 |
| forge | +398 today | 自托管 LLM 工具调用与多步 Agent 工作流框架 |

### 📦 AI Applications

| 项目 | Stars | 简介 |
|------|-------|------|
| Understand-Anything | +666 today | 将代码转为可交互查询的知识图谱 |
| streambert | +1,094 today | Electron 桌面流媒体应用，AI 内容发现 |

### 🧠 LLMs / Training

| 项目 | Stars | 简介 |
|------|-------|------|
| stable-pretraining | +234 | 可靠可扩展的基础模型预训练库 |
| vllm-omni | — | vLLM 多模态扩展，支持文本/图像/视频/音频全模态 |

### 🔍 RAG / Knowledge

| 项目 | Stars | 简介 |
|------|-------|------|
| academic-research-skills | +3,164 today | Claude Code 学术研究自动化工作流插件 |
| claude-mem | 77,283 | Agent 持久化上下文管理，跨会话压缩注入 |
| graphify | 50,764 | 将代码/文档转为可查询知识图谱 |

---

## 三、趋势洞察

1. **Agent 记忆成为刚需**：agentmemory、claude-mem 等项目高速增长，说明跨会话记忆已从概念验证进入实用化阶段
2. **多 Agent 编排升温**：multica、agency-agents、superpowers 代表社区正从单 Agent 演示走向生产级多 Agent 协作系统
3. **Token 优化受关注**：headroom 的爆发说明开发者开始严肃对待 LLM 上下文成本
4. **终端原生 Agent**：Oh-My-Pi、CLI-Anything 等信号显示 Agent 界面正在从 GUI 向 CLI 回流
5. **垂直场景深化**：学术研究(academic-research-skills)、视频制作(OpenMontage)、金融交易(TradingAgents)等垂直 Agent 涌现

---

*本周采集完成。数据来源于 GitHub Trending 及社区雷达。*
