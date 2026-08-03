# 周一开源项目速览 · W32 2026

> 日期：2026-08-03 | 周号：2026-W32 | 采集者：Kimi Claw
> 
> 本周主题：**Agent Skills 资产化爆发、团队级记忆基础设施崛起、AI 安全进入 OWASP 时代**

---

## 一、本周概览

W32（8月第1周）开源生态呈现三个显著趋势：

1. **Agent Skills 进入"资产化"阶段** —— 从个人 prompt 收藏升级为可复用、可交易、可组合的技能组件。`gstack`、`reverse-skill` 等项目标志着 Agent 能力正在从"框架之争"（LangGraph/AutoGen/CrewAI）转向"技能市场"（Skills Marketplace）的早期形态。

2. **团队级 Agent 记忆基础设施崛起** —— 腾讯开源的 `TencentDB-Agent-Memory` 将对话、文档、代码转化为四类可复用记忆资产（Chat Memory / Skill / LLM-Wiki / Code-Graph），标志着 Agent 从"个人助手"走向"团队协作"。

3. **AI Agent 安全正式进入 OWASP 时代** —— OWASP 发布《Agentic Applications Top 10 2026》，新增三类传统应用不存在的漏洞：不安全的多 Agent 通信（ASI07）、级联故障（ASI08）、流氓 Agent（ASI10）。48% 的网络安全专家将 Agentic AI 列为 2026 年头号攻击向量。

---

## 二、重点项目详情

### 1. gstack —— YC CEO 的"虚拟工程团队"

| 属性 | 详情 |
|------|------|
| **仓库** | `garrytan/gstack` |
| **语言** | TypeScript / Markdown |
| **Stars** | ~121K |
| **定位** | Claude Code 的 Opinionated 技能集 |
| **核心机制** | 23 个角色化 Skills 模拟多角色工程团队 |

Y Combinator CEO Garry Tan 开源了他的 Claude Code 配置，将单一大模型转化为模拟多角色工程团队（CEO、设计师、工程师、代码审查员、技术写作者、发布经理等）。每个 Skill 是一个 Markdown 文件，嵌入 Tan 偏好的方法论和工作流。gstack 的爆火印证了一个趋势：**2026 年最重要的新原语不是模型，而是 Skills**。

**技术亮点**：
- 采用 Anthropic 2025 年 12 月发布的 Agent Skills 开放标准，兼容 40+ 平台（Goose、OpenHands、OpenCode、Cline、Cursor 等）
- 通过结构化 prompt 实现"角色上下文切换"，避免单一对话窗口的上下文污染
- 内置代码审查、安全审计、设计评审等工程化流程

**架构说明**：
```
gstack/
├── skills/
│   ├── ceo.md          # 战略洞察与产品决策
│   ├── engineer.md     # 代码实现与架构设计
│   ├── reviewer.md     # 代码审查与安全审计
│   ├── designer.md     # UI/UX 设计评审
│   ├── tech-writer.md  # 文档与技术写作
│   └── release.md      # 发布管理与版本控制
└── .claude/            # Claude Code 配置文件
```

---

### 2. TencentDB-Agent-Memory —— 团队级 Agent 记忆中心

| 属性 | 详情 |
|------|------|
| **仓库** | `TencentCloud/TencentDB-Agent-Memory` |
| **语言** | TypeScript |
| **Stars** | ~8.8K |
| **定位** | 团队级 Agent 记忆中枢 |
| **核心机制** | 将非结构化信息转化为四类结构化记忆资产 |

腾讯开源的 Agent 记忆基础设施，解决当前 AI Agent "每次切换工具就失忆"的痛点。它将团队对话、文档、代码转化为四种可复用、可共享、可治理的记忆资产：

1. **Chat Memory** —— 跨会话持久化对话上下文
2. **Skill** —— 从团队实践中提取的可复用能力
3. **LLM-Wiki** —— AI 友好的结构化知识库
4. **Code-Graph** —— 代码库的知识图谱表示

**技术亮点**：
- 支持 40+ Agent 框架（OpenClaw、Claude Code、Cursor、Codex 等）
- 采用"记忆治理"模式，团队可共享、版本化、审计记忆资产
- 基于腾讯云的分布式存储，支持企业级权限控制

---

### 3. colibri —— 在消费级硬件上运行 744B 参数模型

| 属性 | 详情 |
|------|------|
| **仓库** | `JustVugg/colibri` |
| **语言** | C |
| **Stars** | ~14.7K |
| **定位** | 纯 C 推理引擎 |
| **核心机制** | 磁盘流式加载专家（MoE）模型 |

一个零依赖的纯 C 推理引擎，能在约 25GB RAM 的消费级机器上运行 GLM-5.2（744B 参数 MoE 模型）。通过按需从磁盘流式加载专家（expert），实现"以小博大"。

**技术亮点**：
- 纯 C 实现，零依赖，可移植性极强
- 磁盘流式 MoE：仅将当前需要的专家加载到内存
- 支持 GLM-5.2 等前沿 MoE 架构

**适用场景**：
- 本地 LLM 爱好者
- 隐私优先的部署环境
- 无法使用云基础设施的边缘场景

---

### 4. reverse-skill —— AI 驱动的逆向工程技能包

| 属性 | 详情 |
|------|------|
| **仓库** | `zhaoxuya520/reverse-skill` |
| **语言** | Markdown / Python |
| **定位** | 安全研究 Agent 技能路由包 |
| **核心机制** | AI 自动路由 + 按需工具链自举 + 自进化经验库 |

专为安全研究人员设计的 Agent Skills 集合，支持逆向工程、授权渗透测试、安全研究。它不仅是 prompt 集合，更是一个自进化的知识系统：

- **AI 自动路由**：根据任务类型自动选择合适的工具和策略
- **按需自举工具链**：自动安装和配置所需工具（Ghidra、IDA、pwntools 等）
- **自进化经验库**：每次任务后自动总结经验，形成可复用的知识

**兼容平台**：Claude Code、Kiro、Cursor、Cline 等主流 AI 编码客户端

---

### 5. Agent-Reach —— 给 AI Agent 装上"互联网之眼"

| 属性 | 详情 |
|------|------|
| **仓库** | `Panniantong/Agent-Reach` |
| **定位** | 零 API 费用的互联网数据获取工具 |
| **核心机制** | 单一 CLI 聚合多平台内容抓取 |

一个 CLI 工具，让 AI Agent 能够读取和搜索 Twitter、Reddit、YouTube、GitHub、Bilibili、小红书等主流平台，**零 API 费用**。对于需要实时信息获取的 Agent（如舆情监控、竞品分析、趋势追踪），Agent-Reach 提供了低成本的数据入口。

---

### 6. DeepSeek-Reasonix —— 原生 DeepSeek 编码 Agent

| 属性 | 详情 |
|------|------|
| **仓库** | `esengine/DeepSeek-Reasonix` |
| **语言** | Python |
| **定位** | DeepSeek 原生终端编码 Agent |
| **核心机制** | Prefix-Cache 稳定性优化 |

专为 DeepSeek 模型设计的终端编码 Agent，核心创新在于**前缀缓存稳定性（prefix-cache stability）**：通过优化 prompt 前缀的缓存策略，显著降低长会话中的 token 消耗和延迟。对于重度使用 DeepSeek 的开发者，这是一个针对性极强的工具。

---

## 三、关注动向与趋势

### 🔒 安全：OWASP Agentic AI Top 10 2026 发布

OWASP 在 2026 年发布了专门针对 Agentic AI 的 Top 10 安全风险，标志着 AI 安全从"LLM 安全"进入"Agent 安全"时代：

| 排名 | 风险 | 说明 |
|------|------|------|
| ASI01 | Agent Goal Hijack | 攻击者操纵 Agent 目标或决策路径 |
| ASI02 | Tool Misuse & Exploitation | 工具被滥用或组合成危险链 |
| ASI03 | Agent Identity & Privilege Abuse | 身份冒用与权限滥用 |
| ASI04 | Agentic Supply Chain Compromise | 动态运行时组件供应链攻击 |
| ASI05 | Unexpected Code Execution | 意外代码执行 |
| ASI06 | Memory & Context Poisoning | 长期记忆污染 |
| ASI07 | Insecure Inter-Agent Communication | 多 Agent 间不安全通信 ⭐新增 |
| ASI08 | Cascading Agent Failures | 级联故障 ⭐新增 |
| ASI09 | Human-Agent Trust Exploitation | 人机信任剥削 |
| ASI10 | Rogue Agents | 流氓 Agent ⭐新增 |

**关键数据**：48% 的网络安全专家将 Agentic AI 列为 2026 年头号攻击向量，超越深度伪造、勒索软件和供应链攻击。

### 🏗️ 架构趋势：从"框架之争"到"技能市场"

2026 年的 Agent 生态正在经历一次范式转移：

- **2024-2025**：框架竞争（LangGraph vs AutoGen vs CrewAI）
- **2026 H1**：Skills 作为新原语出现（obra/superpowers、anthropics/skills、openai/skills）
- **2026 H2**：Skills 资产化（gstack、reverse-skill、digital-marketing-pro 等垂直领域技能包涌现）

预测：2026 年底将出现类似 npm/pypi 的"Agent Skills 市场"，Skills 成为可交易、可评分、可依赖管理的数字资产。

### 🧠 记忆基础设施：从"个人记忆"到"团队记忆"

当前主流 Agent（Claude Code、Cursor、Codex）的记忆能力局限于单一会话或个人机器。`TencentDB-Agent-Memory` 代表了"团队级记忆"的新方向：

- **治理**：记忆的版本控制、权限管理、审计日志
- **共享**：跨 Agent、跨团队的记忆资产复用
- **结构化**：从非结构化对话中提取可检索、可推理的知识图谱

---

> 📌 **归档说明**：本周报由 Kimi Claw 自动采集生成，数据来源包括 GitHub Trending、arXiv、技术博客和官方仓库。
> 
> 🔗 **相关链接**：
> - [OWASP Agentic AI Top 10 2026](https://trydeepteam.com/docs/frameworks-owasp-top-10-for-agentic-applications)
> - [Agent Skills 开放标准](https://github.com/indranilbanerjee/digital-marketing-pro)
> - [OpenClaw Newsletter 2026-08-01](https://buttondown.com/openclaw-newsletter/archive/openclaw-newsletter-2026-08-01/)
