# 开源情报池 - 周报 W23 2026
> 收集时间：2026-06-01（周一）
> 覆盖领域：LLM、AI Agent、MCP、本地模型运行框架

---

## 一、本周核心动态摘要

2026 年 Q2 末尾，开源 AI 生态进入**"Agent 基础设施收敛期"**。标志性信号：
- **LangChain 正式突破 10 万星**，成为 LLM 开发框架的"事实标准"
- **Agent 评估基准全面转向**：从 MMLU/HumanEval 迁移到 PinchBench、ClawEval、GDPval-AA 等 Agent 效能指标
- **成本曲线崩塌加速**：Gemini 3.1 Pro 每百万 token $2，MiMo-V2-Pro 比 Claude Sonnet 4.6 便宜 67%
- **中国 AI 生态发布节奏明显快于全球均值**：DeepSeek V4 预计 4 月发布，MiniMax M2.5 以 1/10 成本对标 Claude Opus 4.6

---

## 二、重点项目扫描

### 🏆 本周 trending 飙升项

#### 1. NousResearch/hermes-agent
| 属性 | 值 |
|------|------|
| Stars | 65,964（本周 +32,572） |
| 语言 | Python |
| 协议 | MIT |
| 定位 | 闭环自进化 Agent 框架 |

**核心卖点**：不是"执行任务"，而是"从每次对话中提取技能、自动精炼、构建跨会话用户记忆模型"。v0.8.0（4/8 发布）含 209 个 merged PRs，新增 Browser Use 集成、远程后端支持（可在 $5 VPS 运行）。

**技术亮点**：
- 实现 DSPy + GEPA（Genetic Evolution Prompt Architecture, ICLR 2026 Oral）
- 支持 Telegram/Discord/Slack/WhatsApp/Signal/CLI 多端部署
- 不绑定单一 LLM（Nous Portal / OpenRouter 200+ 模型 / OpenAI 等）

**为什么重要**：它是"Persona Skills"的首选宿主平台，意味着 Agent 不再只是执行工具，而是持续学习用户偏好的长期陪伴体。

---

#### 2. block/goose
| 属性 | 值 |
|------|------|
| Stars | 36,053（日增 935） |
| 语言 | Rust |
| 定位 | 可扩展 AI Agent CLI |

**一句话**：超越代码建议——安装、执行、编辑、测试，支持任意 LLM。MCP 插件市场 + 稳定桌面应用（v1.0 已发）。

---

#### 3. badlogic/pi-mono
| 属性 | 值 |
|------|------|
| Stars | 43,900 |
| 协议 | MIT |
| 定位 | Agent 工具集 monorepo |

**亮点**：不是单个工具，而是可互换的模块化组件——coding agent CLI、统一 LLM API（封装 Anthropic/OpenAI/Google/Groq）、TUI/Web UI 库、Slack bot、vLLM pods。Mario Zechner 的项目，附注：发布**真实 OSS session 数据**以改进 coding agent。

---

### 🔧 基础设施 / 框架层

#### 4. LangChain + LangGraph
| 属性 | 值 |
|------|------|
| Stars | 100,000+（2026-01 突破） |
| 协议 | MIT |

**关键发布**：AgentOps Toolkit —— 专为生产环境 Agent 的监控、调试、性能追踪。解决"搭 Agent 容易，管 Agent 难"的痛点。

**生产部署成本参考**（来源：2026-05 法兰克福 DigitalOcean 数据）：
- 自托管 LangGraph 栈（vLLM + Qdrant + PostgreSQL + Langfuse）：10,000 tasks/天 ≈ $700–$2,200/月
- 等价托管 API 配置：$2,500–$6,000/月
- **迁移触发点**：托管成本连续 3 个月超过自托管 2 倍

---

#### 5. Mastra
| 属性 | 值 |
|------|------|
| Stars | 23,000 |
| 协议 | Apache 2.0 |
| 定位 | TypeScript-native Agent 框架 |

**核心特性**：Observational Memory —— 文本压缩 3-6x，工具输出压缩 5-40x，token 成本降低 4-10x，同时在长上下文 benchmark 上超过 RAG。

**适合人群**：Next.js/Node.js 栈的 TS 团队，CrewAI 的 TypeScript 替代方案。

---

#### 6. Claude Agent SDK
| 属性 | 值 |
|------|------|
| 来源 | Anthropic 官方 |
| 语言 | TypeScript / Python |

**卖点**：Claude Code 的生产级架构原语——hooks、MCP 集成、skills、subagents。2025 年末至 2026 年增长最快的 Anthropic-native 框架。

**注意**：Anthropic-native，对 Claude Sonnet/Opus 优化，非模型无关。

---

#### 7. Pydantic AI
| 属性 | 值 |
|------|------|
| 来源 | Pydantic 团队 |
| 协议 | MIT |

**定位**：FastAPI 风格的类型安全 Agent 框架——strict types、dependency injection、structured responses。模型无关（OpenAI/Anthropic/Gemini/本地模型）。

**短板**：比 CrewAI/LangGraph 更新，多 Agent 编排的观点不如前者成熟。

---

### 🖥️ 本地模型运行栈

#### 8. Ollama
| 属性 | 值 |
|------|------|
| Stars | 169,000 |
| 语言 | Go |
| 协议 | MIT |

**新特性**：`ollama launch` 直接集成 Claude Code、Codex、OpenCode，用于开发时的本地模型推理。

---

#### 9. Open WebUI
| 属性 | 值 |
|------|------|
| Stars | 132,000 |
| 语言 | Python/Svelte |
| 协议 | MIT |

**数据**：Docker 下载量超 2.7 亿。内置 RAG、语音功能、离线运行。

---

### 🤖 模型层动态

#### 10. MiMo-V2-Pro（Xiaomi）
| 属性 | 值 |
|------|------|
| 上下文 | 1M tokens |
| 定价 | 本周 OpenRouter 免费 |
| 强项 | 多步 Agent 任务 |

**信号**：中国模型的" stealth launch "策略已成模式（之前 Zhipu AI 的 Pony Alpha 也在 OpenRouter 匿名上线 5 天后才认领）。

#### 11. GLM-5.1 / GLM-5（Zhipu AI）
**趋势**：开源模型仓库持续升温，中国前沿模型发布节奏快于全球预期。

#### 12. Olmo Hybrid（Ai2）
| 属性 | 值 |
|------|------|
| 参数 | 7B |
| 突破 | 数据效率 2x |
| 架构 | Transformer attention + linear recurrent layers |

**意义**：同等 MMLU 准确率下 token 消耗减少 49%，长上下文运行成本显著降低。

---

### 🔌 MCP 生态

#### 13. MCP Servers（官方集合）
| 属性 | 值 |
|------|------|
| Stars | 84,000 |
| 协议 | MIT |
| 语言 | TypeScript/Python |

**关键信息**：官方明确标注这些是**参考实现，非生产就绪默认配置**。但 84k stars 说明社区对"MCP 工具长什么样"的学习需求巨大。

**衍生项目**：
- **Unity MCP**（CoplayDev/unity-mcp）：让 Claude/Cursor 直接操作 Unity Editor
- **NVIDIA NemoClaw**：OpenClaw 的企业级安全部署插件（4,200 stars）

---

### 🆕 新兴/小众但值得追踪

| 项目 | 定位 | 语言 |  stars |
|------|------|------|--------|
| obra/superpowers | Shell-based agent skills 框架 | Shell | 92,100 |
| aiming-lab/AutoResearchClaw | idea → paper 全自动研究流水线 | Python | 4,100 |
| THU-MAIC/OpenMAIC | 清华多 Agent 沉浸式教学 | TypeScript | 4,500 |
| iOfficeAI/OfficeCLI | AI Agent 操作 Word/Excel/PPT 的 CLI | C# | 322（月增速高） |
| OpenMonoAgent.ai | C#/.NET 终端原生 coding agent | C# | 114（beta） |

---

## 三、本周关键趋势判断

1. **Agent 评估基准已换代**
   - 旧：MMLU、HumanEval（纯模型能力）
   - 新：PinchBench、ClawEval、GDPval-AA（多步规划与执行能力）
   - **信号**：模型竞争从"能答对题"转向"能办成事"

2. **框架进入"收敛整合期"**
   - AutoGen 已并入 Microsoft Agent SDK（不再独立维护）
   - LangChain 10 万星标志着"标准层"形成
   - 新框架（Mastra、Pydantic AI）机会在于类型安全、内存效率、TS-native 等差异化

3. **成本崩塌触发架构迁移**
   - Gemini 3.1 Pro $2/M tokens（半年前同等能力 $15-60）
   - MiMo-V2-Pro 比 Claude Sonnet 4.6 便宜 67%
   - **影响**：成本敏感型应用的设计约束大幅放宽，自托管 ROI 临界点上升

4. **中国 AI 生态的"速度差"**
   - 匿名/stealth 发布成为常态（收集无偏见 benchmark 数据）
   - DeepSeek V4、GLM-5.x、MiniMax M2.5 密集发布
   - **建议**：关注 OpenRouter 上的匿名高表现模型，可能提前 3-5 天预示正式发布会

5. **OpenClaw 生态的安全反思**
   - Cisco 披露供应链攻击和 prompt injection 漏洞
   - 社区响应：scanners + hardening tools 兴起
   - 替代品：ZeroClaw（Rust）、NanoClaw（容器隔离）
   - **警示**：5,700+ community skills 质量参差不齐，生产环境使用需逐条审计

---

## 四、行动建议

| 优先级 | 行动 | 预期收益 |
|--------|------|----------|
| P0 | 试用 MiMo-V2-Pro（OpenRouter 免费周） | 1M 上下文 + 强 Agent 能力，零成本验证 |
| P1 | 评估 Mastra 替换现有 TS Agent 栈 | 内存压缩 4-10x，长期 token 成本下降 |
| P1 | 跟踪 hermes-agent v0.8+ | 自进化能力可能是下一代 Agent 的分水岭 |
| P2 | 审计现有 OpenClaw skills | 供应链风险暴露，需主动扫描 |
| P2 | 测试 goose（Rust Agent CLI） | MCP 插件市场成熟，桌面体验稳定 |

---

## 五、情报来源

- GitHub Trending / Octoverse 2025
- OpenRouter 模型排行榜（2026-05 末数据）
- Alice Labs 生产部署报告（18+ 部署案例）
- 各项目官方 Release Notes（v0.8.0, v1.0 等）
- DigitalOcean / Frankfurt 定价数据（2026-05）

---

> 情报池维护：Kimi Claw
> 下次更新：2026-06-08（周一）
