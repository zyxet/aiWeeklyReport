# 周一开源项目速览 · 2026-W28

> 生成时间：2026-07-06  
> 情报范围：LLM / AI Agent / 工具链 / 基础设施  
> 数据来源：GitHub Trending、OSSInsight、技术社区

---

## 一、情报概览

本周（W28）开源生态的热点集中在**Agent 安全加固**、**终端原生 AI 工具**、**MCP 基础设施成熟化**、以及**MoE 多模态模型**四个方向。GitHub 上新星项目数量显著，其中安全类工具（NVIDIA SkillSpector、CloakBrowser）和 Agent 编排框架（Omnigent、Multica）增速最快，显示出行业从"造 Agent"转向"管 Agent"的拐点信号。

| 方向 | 本周热度 | 代表项目 |
|------|----------|----------|
| Agent 安全与治理 | 高 | SkillSpector, SkillOpt, CloakBrowser |
| 终端原生 AI 工具 | 高 | oh-my-pi, Agent-Reach, last30days-skill |
| MCP 基础设施 | 持续 | MCP Gateway, FastMCP, codegraph |
| 多模态/MoE 模型 | 高 | GLM-5.2, Kimi K2.6, Qwen3.6-35B-A3B |
| Agent 编排与视频 | 中 | OpenMontage, Omnigent, Orca |

---

## 二、项目速览

### 🔒 安全与治理

#### 1. NVIDIA/SkillSpector
- **定位**：AI Agent 技能安全扫描器
- **亮点**：检测技能中的漏洞、恶意模式和安全风险。随着社区技能数量爆炸（OpenClaw 生态超 5700 个），技能层面的安全审计成为刚需。
- **指标**：314⭐ / 24 forks
- **价值**：填补了"Agent 供应链安全"的空白，类似 npm audit 但针对 Agent 技能

#### 2. microsoft/SkillOpt
- **定位**：冻结 LLM Agent 的文本空间技能优化器
- **亮点**：通过轨迹驱动编辑和验证门控更新，训练可复用的自然语言技能。将经验沉淀为 `best_skill.md` 工件。
- **指标**：176⭐ / 13 forks
- **价值**：解决 Agent "重复造轮子" 问题，让技能可以像代码一样版本管理

#### 3. CloakHQ/CloakBrowser
- **定位**：通过所有 bot 检测的隐身 Chromium
- **亮点**：源码级指纹补丁，Playwright 直接替换，30/30 测试通过。
- **指标**：130⭐ / 14 forks
- **价值**：Agent 自动化浏览的底层基础设施，对抗 bot 检测 arms race

---

### 🛠️ 终端原生 AI 工具

#### 4. can1357/oh-my-pi
- **定位**：终端原生 AI 编码代理
- **亮点**：哈希锚定编辑、优化工具 harness、LSP、Python、浏览器、子代理支持。TypeScript 写的，对标 Claude Code / Codex CLI。
- **指标**：195⭐ / 12 forks
- **价值**：在终端内完成完整开发循环，不依赖 IDE

#### 5. Panniantong/Agent-Reach
- **定位**：给 AI Agent 装上互联网双眼
- **亮点**：无需 API 费用，一站式搜索 Twitter、Reddit、YouTube、GitHub、Bilibili、小红书。单 CLI 覆盖多平台。
- **指标**：888⭐ / 66 forks
- **价值**：解决 Agent "信息孤岛" 问题，零成本获取社交/社区情报

#### 6. mvanhorn/last30days-skill
- **定位**：AI Agent 研究技能
- **亮点**：跨 Reddit、X、YouTube、HN、Polymarket、全网调研，合成有依据的总结。
- **指标**：868⭐ / 62 forks
- **价值**：将信息收集工作流封装为可复用技能

#### 7. headroomlabs-ai/headroom
- **定位**：LLM 上下文压缩层
- **亮点**：在工具输出、日志、文件、RAG 块到达 LLM 前压缩，减少 60-95% token，保持答案质量不变。
- **指标**：1,367⭐ / 106 forks
- **价值**：直接降低 API 成本，对长上下文 Agent 工作流意义重大

---

### 🏗️ Agent 编排与框架

#### 8. omnigent-ai/omnigent
- **定位**：开源 AI Agent 框架与元 harness
- **亮点**：编排 Claude Code、Codex、Cursor、Pi 等代理，无需重写即可切换 harness，支持策略沙箱和实时协作。
- **指标**：170⭐ / 24 forks
- **价值**：Agent 互操作性的中间层，避免被单一厂商锁定

#### 9. multica-ai/multica
- **定位**：开源托管 Agents 平台
- **亮点**：将编码代理变成真正的队友——分配任务、跟踪进度、累积技能。
- **指标**：116⭐ / 22 forks
- **价值**：从 "单兵作战" 到 "团队协作" 的 Agent 管理模式

#### 10. calesthio/OpenMontage
- **定位**：首个开源 Agentic 视频制作系统
- **亮点**：12 条流水线、52 个工具、500+ Agent 技能。把 AI 编码助手变成完整视频工作室。
- **指标**：586⭐ / 73 forks
- **价值**：AIGC 内容生产的新范式，Agent 执行复杂创意工作流

#### 11. stablyai/orca
- **定位**：并行 Agent 舰队 ADE（Agent Development Environment）
- **亮点**：用自己的订阅运行任何编码代理，桌面和移动端可用。
- **指标**：188⭐ / 12 forks
- **价值**："Agent 舰队" 管理，适合需要同时运行多个代理的场景

---

### 🧠 代码智能与知识管理

#### 12. colbymchenry/codegraph
- **定位**：预索引代码知识图谱
- **亮点**：代码变更自动同步，为 Claude Code、Codex、Cursor、OpenCode 等提供 100% 本地知识图谱，减少 token 和工具调用。
- **指标**：662⭐ / 47 forks
- **价值**：代码库级 RAG 的本地替代方案，保护代码隐私

#### 13. EverMind-AI/EverOS
- **定位**：每个 AI Agent 的便携记忆层
- **亮点**：本地优先、Markdown 原生、用户拥有、跨应用自进化。
- **指标**：107⭐ / 8 forks
- **价值**：Agent 记忆的"可移植性"，解决不同 Agent 之间记忆割裂的问题

#### 14. AgriciDaniel/claude-obsidian
- **定位**：自组织 AI 第二大脑
- **亮点**：Obsidian + Claude Code，丢入任何来源，自动读取、链接、归档为 Markdown 知识图谱。
- **指标**：83⭐ / 6 forks
- **价值**：个人知识管理的 Agent 化，基于 Karpathy 的 LLM Wiki 模式

---

### 🌐 基础设施与协议

#### 15. MCP 生态成熟化
- **信号**：MCP SDK 月下载量突破 **9700 万**，Linux Foundation AAIF（Agentic AI Foundation）接管治理
- **关键项目**：
  - **MCP Gateway**：Cloudflare 边缘网络托管，企业级认证、审计、访问控制
  - **FastMCP**：Python 框架，大幅降低 MCP Server 构建门槛
  - **AGENTS.md**：OpenAI 标准，已被 60,000+ 开源项目采用
- **安全风险**：过半互联网暴露的 MCP Server 缺乏有效访问控制，Cisco 在 RSA 2026 推出专门安全工具

#### 16. tashfeenahmed/freellmapi
- **定位**：堆叠 16 个 LLM 提供商免费额度（~17 亿 token/月）的 OpenAI 兼容代理
- **亮点**：智能路由、自动故障转移、加密密钥。
- **指标**：270⭐ / 28 forks
- **价值**：个人实验/原型阶段的零成本模型接入方案

---

### 🤖 模型层

#### 17. GLM-5.2 (Z.ai)
- **规格**：744B 总参数 / 40B 激活参数，MoE 架构，MIT 许可
- **亮点**：GPQA Diamond 91.2%，AIME 2026 99.2%，长程编码基准 Terminal-Bench 2.1 81.0%
- **局限**：暂不支持图像理解，2-bit 量化仍需约 245GB 显存
- **价值**：当前开源权重模型中推理能力最强

#### 18. Kimi K2.6 (Moonshot AI)
- **规格**：1T 总参数 / 32B 激活参数，MoE 多模态
- **亮点**：原生多模态 Agent 模型，支持 200-300 次连续工具调用，AIME 2025 99.1%
- **价值**：开源 Agent Swarm 的标杆，多智能体编排能力最强

---

## 三、趋势观察

### 1. 从 "造 Agent" 到 "管 Agent"
安全扫描（SkillSpector）、技能优化（SkillOpt）、访问网关（MCP Gateway）的密集出现，说明行业进入治理阶段。Agent 数量爆发后，如何审计、控制、优化 Agent 行为成为新战场。

### 2. 终端原生工具崛起
oh-my-pi、Agent-Reach、headroom 等项目都强调"终端优先"、"零成本"、"本地运行"。这反映开发者对云端依赖和 API 费用的疲劳，以及隐私敏感场景的刚需。

### 3. MCP 成为事实标准，但安全滞后
MCP 的月下载量从 0 到 9700 万只用了不到一年，Linux Foundation 背书后进入基础设施级。但安全部署严重滞后——"S in MCP stands for security" 这个圈内笑话值得警惕。

### 4. Agent 能力向长程、多模态、视频延伸
OpenMontage（视频）、Kimi K2.6（200+ 工具调用）、GLM-5.2（长程编码）都指向一个方向：Agent 不再只是"聊天机器人"，而是能执行复杂、长程、跨模态任务的自主系统。

### 5. 记忆层成为新基础设施
EverOS、Claude-Obsidian、codegraph 共同构建了一个新层次——Agent 记忆与知识管理。没有持久化记忆的 Agent 只是 stateless 函数调用，这个层正在快速标准化。

---

> 本周情报池共计 **18 个重点项目**，覆盖安全、工具、框架、基础设施、模型五个层级。后续筛选阶段（周三）将从中选出 6-8 个进入深度分析候选。

---

*文档编号：os-pool-2026-W28.md*  
*生成系统：intelligence-system v1.0*
