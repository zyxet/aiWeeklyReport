# 周一开源项目速览 · W38 / 2026-09-14

> 本周（W38）LLM / AI Agent 领域开源情报池。涵盖基础模型、Agent 运行时与基础设施、周边生态三大板块。

---

## 一、大模型层：开源权重进入"MoE 密集发布期"

### 1. Kimi K3（Moonshot AI）
- **发布时间**：2026 年 7 月 27 日
- **规模**：2.8T 参数 MoE（896 专家，~50B 活跃参数）
- **亮点**：当前世界最大开源权重模型；1M 上下文；原生视觉+视频；Frontend Code Arena #1
- **协议**：Modified MIT
- **仓库**：huggingface.co/moonshot-ai/Kimi-K3

### 2. Muse Glimmer（Meta）
- **发布时间**：2026 年 8 月 10 日
- **规模**：30B dense 多模态
- **亮点**：从 Muse Spark 蒸馏；专为本地 Agent 工作流调优；MCP Atlas 工具调用 75.5%；4-bit 量化可跑在 24GB VRAM
- **协议**：Apache 2.0
- **仓库**：huggingface.co/meta-llama/Muse-Glimmer

### 3. Apertus 1.5（ETH Zurich / EPFL）
- **发布时间**：2026 年 7 月
- **规模**：8B / 70B 双版本
- **亮点**：**100% 完全开源**（权重 + 训练数据 + 训练代码 + 日志）；图像理解 + 推理模式 + 工具使用
- **协议**：Apache 2.0
- **意义**：学术界对"开源"定义的回击——不只是放权重

### 4. Hy3（腾讯）
- **发布时间**：2026 年 7 月
- **规模**：295B MoE（21B 活跃参数）
- **亮点**：以 21B 活跃参数匹敌 2-5 倍体量的模型；推理与 Agent 性能突出
- **协议**：Apache 2.0

### 5. Bonsai 8B（PrismML）
- **发布时间**：2026 年 4 月
- **亮点**：开创性 1-bit 量化模型；可在 Apple Silicon 等消费级硬件上高效推理
- **协议**：开源

---

## 二、AI Agent 基础设施层：运行时框架爆发，Harness 成为新战场

### 1. DeepSeek Harness（dsh）—— 当前最火的 Agent 运行时
- **发布时间**：2026 年 8 月 13 日
- **协议**：MIT
- **定位**：Agent 运行时框架，非模型本身。核心理念 "Agent = Model + Harness"
- **架构**：基于 Cordis 插件系统，**一切皆插件**——模型适配器、工具注册表、会话日志、沙箱、审批策略、UI、甚至 Agent 循环本身均可替换
- **热度**：开源后半小时破万星，数日突破 14 万，截至 9 月中旬约 ~170k stars
- **使用**：`npx @deepseek-ai/dsh web` 一键启动本地 Web UI（端口 3080）
- **风险**：2026 年 9 月 8 日被披露 **CVE-2026-82533** 沙箱逃逸漏洞——攻击者可通过诱导 Agent 执行恶意命令突破沙箱，默认配置即受影响
- **仓库**：github.com/deepseek-ai/deepseek-harness

### 2. TrueForge（TrueFoundry）
- **发布时间**：2026 年 8 月 19 日
- **协议**：MIT
- **定位**：vendor-neutral Agent harness，对标 Claude Managed Agents
- **亮点**：声称比 Claude Managed Agents 便宜 30%（同模型），切到 GLM-5.2 可省 75%；14 任务盲测准确率相当（11/14）
- **架构**：上下文工程为核心——延迟工具加载、50K token 阈值压缩、大结果卸载、沙箱即工具
- **热度**：48 小时内 ~2,100 stars
- **仓库**：github.com/truefoundry/trueforge

### 3. OpenClaw
- **最新版本**：2026.9.4（2026 年 9 月 11 日发布）
- **协议**：MIT
- **定位**：开源多通道个人 AI 助手框架（WhatsApp / Telegram / Slack / Discord / Signal / iMessage / Teams）
- **规模**：~362k GitHub stars；ClawHub Skill Registry 超 5,700 个社区技能
- **9 月更新亮点**：
  - **Skill Workshop**：技能跨 Workspace 持久化，完整指令对比，Doctor 安全清理
  - **原生浏览器标签**：Agent 页面实时渲染，外部链接在原生 Mac 标签页打开
  - **GPT-6 Astra 支持**：text + image 输入，Responses 工具调用
  - **安全更新**：核心与插件变更可在隔离候选态预演后再激活
  - **性能优化**：保留热提示缓存，减少冷会话更新与记忆搜索开销
- **风险**：Cisco 披露供应链攻击与提示注入漏洞；社区技能质量参差不齐
- **仓库**：github.com/openclaw/openclaw

### 4. MCP（Model Context Protocol）—— 已成事实标准
- **最新规范**：2026-07-28 版本（2026 年 5 月 21 日锁定 RC，10 周验证窗口）
- **治理**：2025 年 12 月 Anthropic 捐赠给 Linux Foundation 下的 Agentic AI Foundation；OpenAI、Block 联合创始；AWS、Google、Microsoft、Cloudflare、Bloomberg 支持
- **核心变更（7 月版）**：协议核心变为**无状态**——移除 `initialize` 握手、`Mcp-Session-Id` header；请求可路由到任意服务器实例；协议版本与客户端能力走逐请求元数据
- **生态规模**：~16,000 个 `mcp-server` 主题仓库；参考服务器 ~88k stars；月度 SDK 下载量超 4.7 亿（npm 1.74 亿 + PyPI 2.97 亿）
- **教育**：微软发布 `mcp-for-beginners` 开源课程（.NET / Java / TS / JS / Rust / Python），50+ 语言翻译
- **仓库**：github.com/modelcontextprotocol

### 5. Mastra
- **协议**：Apache 2.0
- **定位**：TypeScript 原生 Agent 框架（Gatsby.js 团队出品）
- **亮点**：Observational Memory 文本记忆系统——token 成本降低 4-10 倍，长上下文基准超越 RAG；文本压缩 3-6 倍，工具输出压缩 5-40 倍
- **热度**：~23k stars
- **仓库**：github.com/mastra-ai/mastra

### 6. Mem0
- **定位**：Agent 持久记忆层
- **热度**：~52k stars
- **意义**：解决 Agent "每次对话从零开始" 的根本痛点；跨会话记忆是玩具级 Agent 与生产级 Agent 的分水岭
- **仓库**：github.com/mem0ai/mem0

---

## 三、周边生态：语音、视觉与安全

### 语音 / TTS
| 项目 | 规模 | 亮点 | 协议 |
|---|---|---|---|
| **Chatterbox** (Resemble AI) | 0.5B / 350M Turbo | SOTA 开源 TTS；23+ 语言；350ms 超低延迟；副语言标签 | MIT |
| **Qwen3-TTS** (阿里) | 0.6B / 1.7B | 语音克隆、语音设计、10 语言；97ms TTFB 流式 | Apache 2.0 |
| **Orpheus-TTS** (Canopy Labs) | Llama-3B 骨干 | 类人语音；零样本克隆；情感标签；~200ms 延迟 | Apache 2.0 |
| **MOSS-TTS** (MOSI.AI) | 8B + 100M Nano | 语音克隆、对话生成、音效、实时流；100M 版可跑 CPU | Apache 2.0 |
| **NeuTTS** (Neuphonic) | 120M / 360M | 端侧 TTS；即时克隆；GGUF 量化 CPU/手机 | Apache 2.0 |

### 图像 / 视频生成
| 项目 | 规模 | 亮点 | 协议 |
|---|---|---|---|
| **FLUX.2-dev** (Black Forest Labs) | 32B | SOTA 开源文生图；单/多参考编辑；内/外画；更新 VAE | FLUX.1-dev NC License |
| **Z-Image** (通义实验室/阿里) | - | 强 GenEval 分数；Turbo 版 4 步生成 | Apache 2.0 |
| **ERNIE-Image-Turbo** (百度) | 8B DiT | SOTA 开源权重；强文本渲染、布局控制；8 步生成 | Apache 2.0 |

### 安全事件
- **CVE-2026-82533**：DeepSeek Harness 沙箱逃逸漏洞。无需网络暴露、无需凭据、无需修改默认配置——仅需诱导 Agent 执行攻击者提供的文本命令即可突破沙箱。OX Research 已发布 PoC。

---

## 趋势判断

1. **Agent 基础设施 > 模型本身**：DeepSeek Harness 和 TrueForge 的爆发说明开发者开始意识到——模型是灵魂，Harness 才是让 Agent 真正干活的骨架。"选哪个模型"正在变成"选哪个模型 + 哪个 Harness + 哪个技能 + 哪个记忆层"。

2. **Harness 开源化是 2026 年最大变量**：Claude Code 和 Codex CLI 锁死了各自的循环层，DeepSeek 选择把整个循环开源。这意味着 Agent 执行层的竞争将从"闭源产品"转向"开源生态 + 模型能力"。

3. **MCP 已赢**：不到两年时间从 Anthropic 的 side project 变成 Linux Foundation 下的行业标准，跨厂商采纳速度超过 OpenAPI 和 OAuth 2.0 早期。2026 年下半年，不支持 MCP 的 Agent 工具将逐渐边缘化。

4. **安全追上速度**：DeepSeek Harness 的 CVE 是一个信号——Agent 能执行代码、能访问文件、能联网，它的沙箱不是可选组件，是生死线。Agent 安全将成为下一个投资热点。

---

*情报收集时间：2026-09-14 10:00 AM CST · W38*
*数据来源：GitHub、Hugging Face、官方博客、Cisco/OX Security 披露、The New Stack 等*
