# 开源情报池 · 2026 Week 24

> 收集时间：2026-06-10（周三补录）
> 覆盖范围：LLM / AI Agent / 开源基础设施
> 采集来源：GitHub Trending、OSSInsight、社区雷达

---

## 🔥 本周热点总览

| 项目 | 语言 | Stars | 本周增量 | 分类 |
|------|------|-------|----------|------|
| NousResearch/hermes-agent | Python | 186,263 | +1,112/日 | Agent 框架 |
| RyanCodrai/turbovec | Python/Rust | 7,465 | +1,554/日 | 向量索引 |
| odysseusai/odysseus | 多语言 | 37,000+ | +3,700/周 | 自托管 AI 工作台 |
| aaif-goose/goose | Rust | 47,630 | +322/日 | 终端 Agent |
| openhumanai/openhuman | Rust/TS | 26,000+ | +1,710/日 | 记忆 Agent 框架 |
| mvanhorn/last30days-skill | Python | 31,754 | +1,111/日 | Agent Skill |
| Leonxlnx/taste-skill | Shell | 37,174 | +1,103/日 | Agent Skill |
| lfnovo/open-notebook | TypeScript | 27,458 | +554/日 | 笔记本替代 |
| microsoft/pg_durable | Rust | 1,518 | +316/日 | 持久执行 |
| Crosstalk-Solutions/project-nomad | TypeScript | 29,816 | +309/日 | 离线 AI 服务器 |
| openai/plugins | JavaScript | 2,101 | +262/日 | Codex 插件 |
| DeepSeek-TUI | Rust | 11,499 | +1,077/周 | 终端编程 Agent |
| codegraphai/codegraph | 多语言 | 3,684+ | 持续 | 代码架构解析 |
| langgenius/dify | Python | 142,282 | 持续 | 工作流编排 |
| browser-use/browser-use | Python | 95,135 | 持续 | Web 自动化 |
| ollama/ollama | Go | 172,046 | 持续 | 本地推理 |
| mem0ai/mem0 | Python | 56,458 | 持续 | Agent 记忆层 |

---

## 🤖 AI Agent / Workflows

### 1. Hermes Agent — 持续领跑的自进化 Agent
- **仓库**：NousResearch/hermes-agent
- **核心**：闭环自我进化，从每次对话中提取技能并自动精炼
- **本周数据**：186,263 Stars，日增 +1,112，OpenRouter 日 Token 调用量 2910 亿
- **判断**：Agent 框架从"工具"向"平台"演进的标志，长期值得关注

### 2. Goose — 可扩展 AI Agent CLI
- **仓库**：aaif-goose/goose（原 block/goose）
- **核心**：Rust 全栈 Agent，支持安装-执行-编辑-测试完整工作流
- **本周数据**：47,630 Stars，日增 +322，MCP 插件市场 + 桌面应用
- **判断**：Rust 工程品质 + Block 背书，持续稳定上升

### 3. OpenHuman — 记忆树驱动的 Agent 框架
- **仓库**：openhumanai/openhuman
- **核心**：独创记忆树架构，分层存储对话/任务/知识，多 Agent 协同
- **本周数据**：26,000+ Stars，日增 +1,710，连续多日霸榜
- **判断**：解决 Agent 冷启动和长期记忆痛点的务实方案

### 4. odysseus — 自托管 AI 工作台
- **仓库**：odysseusai/odysseus
- **核心**：本地私有化部署的全能 AI 工作台，整合对话/代码/文档/自动化
- **本周数据**：37,000+ Stars，周增 3.7 万，本周涨幅最猛黑马
- **判断**：自托管 AI 从"小众需求"变为"行业标配"的标志

### 5. Agent Skill 生态爆发
| 项目 | Stars | 增量 | 描述 |
|------|-------|------|------|
| mvanhorn/last30days-skill | 31,754 | +1,111/日 | 研究 Reddit/X/YouTube/HN 合成摘要 |
| Leonxlnx/taste-skill | 37,174 | +1,103/日 | 阻止 AI 产生无聊通用内容 |
| openai/plugins | 2,101 | +262/日 | Codex 插件官方示例 |

- **判断**：Agent 从"框架竞争"进入"skill / plugin 资产化"阶段

### 6. DeepSeek-TUI — 国产终端编程 Agent
- **仓库**：Hmbown/DeepSeek-TUI
- **核心**：Rust 编写，1M 上下文，RLM 多智能体并发，Plan/Agent/YOLO 三档模式
- **本周数据**：11,499 Stars，周增 +1,077
- **判断**："DeepSeek 版 Claude Code"，国产替代方案值得关注

---

## 🧠 LLM / 训练 / 推理

### 1. Ollama — 本地推理事实标准
- **仓库**：ollama/ollama
- **更新**：持续新增模型支持，ollama launch 集成编码 Agent
- **判断**：本地推理生态中心节点，模型多样性加速

### 2. turbovec — TurboQuant 向量索引
- **仓库**：RyanCodrai/turbovec
- **核心**：Rust 实现，ARM 上比 FAISS 快 12-20%，10M×1536 维 31GB→4GB
- **本周数据**：7,465 Stars，日增 +1,554（全场增速第一）
- **判断**：向量检索"极压缩/极快"是 2026 RAG 基础设施硬需求

---

## 🔧 AI 基础设施 / 工具链

### 1. Rust 基础设施持续崛起
| 项目 | 用途 | 增量 |
|------|------|------|
| aaif-goose/goose | 终端 AI Agent | +322/日 |
| microsoft/pg_durable | PostgreSQL 内部持久执行 | +316/日 |
| RyanCodrai/turbovec | 向量索引 | +1,554/日 |
| openhumanai/openhuman | 记忆 Agent 框架 | +1,710/日 |

- **判断**：需要长时间运行/本地优先/内存安全的 AI 基础设施都在转向 Rust

### 2. 代码知识图谱
- **codegraphai/codegraph**：十分钟梳理百万行代码架构，交互式可视化
- **判断**：补齐 AI 编程的上下文理解短板

### 3. 离线/本地优先
- **project-nomad**：自带 Kiwix + Kolibri + ProtoMaps + AI 推理的离线知识服务器
- **判断**：对应"末日/离线/隐私"叙事，持续有需求

---

## 📦 垂直应用

### 1. MoneyPrinterTurbo — AI 短视频生成
- **仓库**：bearxun/MoneyPrinterTurbo
- **核心**：全自动短视频生成，零剪辑出片
- **判断**：AI 内容生产赛道标杆

### 2. 开源 CRM
- **twenty**：TypeScript 开源 AI CRM，替代传统商用工具

---

## 🌟 新兴信号

1. **OpenAI 官方 Codex 插件**：openai/plugins 发布，Codex 生态扩展
2. **Microsoft pg_durable**：PostgreSQL 内部持久执行，AI 工作流可靠性基础设施
3. **Skill 标准化**：Agent Skill 三剑客（last30days/taste/openai）同日爆发
4. **Rust 渗透加速**：AI 基础设施关键组件全面 Rust 化

---

## 📊 趋势判断

- **Agent 框架竞争格局**：从"框架之争"进入"skill / plugin 资产化"阶段
- **自托管成为刚需**：odysseus 周增 3.7 万星，开发者重视数据隐私和自主可控
- **Rust 渗透加速**：从工具链到运行时，Rust 在 AI 基础设施中的存在感持续增强
- **记忆层成为刚需**：openhuman 记忆树 + Hermes Agent 跨会话记忆，持久身份是下一个战场
- **国产终端 Agent**：DeepSeek-TUI 代表国产替代方案崛起

---

*情报池自动生成于 2026-06-10 · 由周三深度筛选任务触发（补录周一候选池）*
