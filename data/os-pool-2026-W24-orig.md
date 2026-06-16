# 开源情报池 · 2026 Week 23

> 收集时间：2026-06-08（周一）
> 覆盖范围：LLM / AI Agent / 开源基础设施
> 采集来源：GitHub Trending、OSSInsight、社区雷达

---

## 🔥 本周热点总览

| 项目 | 语言 | Stars | 本周增量 | 分类 |
|------|------|-------|----------|------|
| NousResearch/hermes-agent | Python | 65,964 | +32,572 | Agent 框架 |
| bytedance/deer-flow | Python | 35,068 | +1,508 | 多 Agent 编排 |
| affaan-m/everything-claude-code | JavaScript | 188,532 | +3,735 | Agent 性能优化 |
| block/goose | Rust | 36,053 | +935 | 终端 Agent |
| langgenius/dify | Python | 142,282 | 持续 | 工作流编排 |
| OpenHands/OpenHands | Python | 74,544 | 持续 | 自主编程 |
| browser-use/browser-use | Python | 95,135 | 持续 | Web 自动化 |
| ollama/ollama | Go | 172,046 | 持续 | 本地推理 |
| vllm-project/vllm | Python | 80,748 | 持续 | 高吞吐推理 |
| mem0ai/mem0 | Python | 56,458 | 持续 | Agent 记忆层 |
| Tencent/TencentDB-Agent-Memory | Python | 461 | +461 | 本地长期记忆 |
| HKUDS/ViMax | Python | 450 | 新增 | 视频生成 |

---

## 🤖 AI Agent / Workflows

### 1. Hermes Agent — 会自我进化的 Agent
- **仓库**：NousResearch/hermes-agent
- **核心**：闭环自我进化，从每次对话中提取技能并自动精炼，构建跨会话用户记忆模型
- **技术栈**：DSPy + GEPA（Genetic Evolution Prompt Architecture, ICLR 2026 Oral）
- **本周 v0.8.0**：209 个合并 PR，新增 Browser Use 集成、远程后端、工作树并行
- **部署**：Telegram / Discord / Slack / WhatsApp / Signal / CLI，支持 200+ 模型
- **判断**：Agent 框架从"工具"向"平台"演进的标志，长期值得关注

### 2. Deer-Flow 2.0 — 字节跳动的 SuperAgent
- **仓库**：bytedance/deer-flow
- **核心**：模块化多 Agent 架构 + LangGraph，支持分钟级到小时级任务
- **集成**：DuckDuckGo / Brave Search / 自定义 API
- **判断**：大厂入局 Agent 基础设施，与 AutoGPT 等早期项目不同，强调时间尺度差异

### 3. everything-claude-code — Agent 的 Agent
- **仓库**：affaan-m/everything-claude-code
- **核心**：Claude Code 性能优化系统，包括技能、本能、记忆、安全、研究优先开发
- **兼容**：Claude Code / Codex / Opencode / Cursor / Gemini CLI
- **判断**：社区开始构建"优化层"，说明底层工具已足够成熟

### 4. Goose — 超越代码建议的 Agent
- **仓库**：block/goose
- **核心**：开源可扩展 Agent，执行安装、编辑、测试等操作
- **语言**：Rust
- **判断**：Square 出品，质量稳定，值得关注其生态扩展

### 5. Browser-Use — AI 的 Web 自动化层
- **仓库**：browser-use/browser-use
- **核心**：让网站对 AI Agent 可访问，标准化 Web 自动化层
- **判断**：Agent 基础设施关键一环，未来"AI 员工"的标准工具之一

### 6. Dify — 生产级工作流平台
- **仓库**：langgenius/dify
- **核心**：可视化 Agentic 工作流编排，企业级成熟方案
- **判断**：已跨过"玩具"阶段，适合生产部署

---

## 🧠 LLM / 训练 / 推理

### 1. Ollama — 本地推理的 Docker
- **仓库**：ollama/ollama
- **更新**：新增 Kimi-K2.5、GLM-5、MiniMax、DeepSeek、gpt-oss 支持
- **判断**：本地推理生态的中心节点，模型多样性加速

### 2. vLLM — 高吞吐推理引擎
- **仓库**：vllm-project/vllm
- **动态**：MoE 模型支持优化、Nvidia Hopper GPU 性能优化
- **判断**：生产环境 LLM 服务的 backbone

### 3. 腾讯 Agent 本地记忆 — TencentDB Agent Memory
- **仓库**：Tencent/TencentDB-Agent-Memory
- **核心**：4 层渐进式管道，零外部 API 依赖的完全本地长期记忆
- **判断**：解决 Agent 长期记忆问题的务实方案，值得关注稳定性

### 4. 开源模型动态
- **Qwen 家族**：HuggingFace 累计下载超 Llama，Qwen 3.5 Coder 和 Wan 2.5/2.6 传闻待发
- **Nvidia Nemotron 3**：Nemotron 3 Ultra（前沿级）+ Nemotron 3 Omni（音频/视觉/语言原生集成）
- **DeepSeek R1**：推理模型持续迭代，成本效益突出

---

## 🔧 AI 基础设施 / 工具链

### 1. Code Knowledge Graphs — 解决 Token 经济学
| 项目 | 增量 | 核心能力 |
|------|------|----------|
| colbymchenry/codegraph | +3,684 | 预索引代码知识图，减少 Agent 运行 token 成本 |
| Lum1104/Understand-Anything | +1,393 | 交互式代码知识图，多 Agent CLI 兼容 |
| ChromeDevTools/chrome-devtools-mcp | +501 | 官方 Chrome DevTools MCP 服务器 |

- **判断**：MCP 生态已达逃逸速度，成为 AI Agent 的"USB-C"接口

### 2. Agent 记忆持久化 — 两种路线
| 项目 | Stars | 路线 |
|------|-------|------|
| thedotmack/claude-mem | 77,510 | 会话压缩 + 上下文注入 |
| mem0ai/mem0 | 56,458 | 通用记忆层，跨会话持久身份 |

- **判断**：两条路线的胜负将决定 Agent 如何保持跨交互身份

### 3. Rust 基础设施崛起
| 项目 | 用途 |
|------|------|
| ruvnet/RuView | WiFi 信号 → 空间智能/生命体征（无摄像头） |
| 0xPlaygrounds/rig | 模块化 LLM 应用 |
| meilisearch | 混合搜索 |
| aaif-goose/goose | 终端 AI Agent |
| deeplethe/forkd | AI Agent 微 VM 分支（100ms 内生成 100 个子进程） |
| yvgude/lean-ctx | 混合上下文优化器，减少 89-99% token 消耗 |

- **判断**：Rust 在性能关键 AI 组件中的份额持续增长，此前是 Python/Go 的领地

---

## 📦 垂直应用

### 1. 金融 Agent
| 项目 | Stars | 描述 |
|------|-------|------|
| TauricResearch/TradingAgents | 78,604 | 多 Agent LLM 金融交易框架 |
| santifer/career-ops | 46,702 | Claude Code 求职 Agent，14 种技能模式 |
| ZhuLinsen/daily_stock_analysis | 38,490 | 零成本 LLM 股票分析 |
| Fincept-Corporation/FinceptTerminal | 13,047 | 现代金融终端 + AI 分析 |
| brokermr810/QuantDinger | 297 | 加密货币/股票/外汇量化交易平台 |

- **判断**：金融服务业是首个出现系统性 Agent 专业化的行业

### 2. 视频生成
- **HKUDS/ViMax**：Agentic 视频生成，导演 + 编剧 + 制片人 + 视频生成器一体化
- **harry0703/MoneyPrinterTurbo**：AI 一键生成短视频，50K+ Stars

### 3. 安全 / 渗透测试
- **KeygraphHQ/shannon**：自主白盒 AI 渗透测试，39K+ Stars
- **0xSteph/pentest-ai-agents**：Claude Code 攻击性安全研究助手

---

## 🌟 新兴信号

1. **OpenAI 官方 Agent 框架**：`openai-agents-python` 发布，生产级多 Agent 调度
2. **MCP 生态爆发**：Chrome DevTools、.NET、ActivePieces（400+ 服务器）等纷纷接入
3. **教育 Agent 内容**：learn-claude-code（62K）、ai-engineering-from-scratch（+988/日）
4. **便携式 AI**：USB-Uncensored-LLM / Portable-AI-USB，零安装离线运行
5. **代码搜索优化**：MinishLab/semble，比 grep+read 减少 98% token
6. **文档自动化**：md2html、md2html 等 Markdown→HTML 技能涌现

---

## 📊 趋势判断

- **Agent 框架竞争格局**：Claude Code 生态正在形成"优化层"，社区围绕其构建工具链
- **记忆层成为刚需**：从"单次会话"到"持久身份"，记忆方案是下一个基础设施战场
- **Rust 渗透加速**：从工具链到运行时，Rust 在 AI 基础设施中的存在感持续增强
- **垂直化趋势**：金融、视频、安全等领域开始出现专门的 Agent 框架，而非通用方案
- **MCP 标准化**：Model Context Protocol 正在成为事实上的 Agent 接口标准

---

*情报池自动生成于 2026-06-08 · 由周一情报收集任务触发*
