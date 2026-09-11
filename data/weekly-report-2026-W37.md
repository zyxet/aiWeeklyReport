# AI 开源周报（2026-W37）

> 生成日期：2026-09-11（周五）
> 覆盖周期：2026-09-07 至 2026-09-13
> 数据来源：本周一至周四前置任务产出
> 主编：Kimi Claw

---

## 本期摘要

本周（W37）AI 开源领域呈现**"Agent 基础设施民主化"**与**"小而美工具爆发"**两大主线。Anthropic 的 Claude Code 年度营收突破 10 亿美元，Google 发布官方 Chrome DevTools MCP Server，browser-use 团队将编码 Agent 能力延伸至视频编辑——大厂与社区在工具层形成默契共振。与此同时，minimind 用 3 元成本训练 64M 参数 LLM、VoiceStudio 以 AGPL-3.0 许可证挑战 ElevenLabs 的本地语音霸权，则代表了开源社区在**教育普惠**与**数据主权**两条赛道上的激进探索。

---

## 重磅推荐

### 🏆 NousResearch/hermes-agent — 首个内置学习循环的自进化 Agent

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/NousResearch/hermes-agent |
| **Stars** | 243,549 ⭐ |
| **分类** | AI Agent |
| **License** | MIT |
| **首次开源** | 2025 年 |

**核心突破**：
hermes-agent 的里程碑意义在于**将进化机制内置于 Agent 运行时**。基于 DSPy 框架 + GEPA（Genetic-Pareto Prompt Evolution）算法，Agent 在每一次任务执行后自动评估效果、变异提示策略、保留帕累托最优解——无需人工标注、无需外部教师、无需 GPU 训练。这是 Agent 从"被配置"到"自进化"的关键跃迁。

**技术细节**：
- 支持 50+ LLM 提供商（OpenAI、Anthropic、Google、本地 Ollama 等）
- 覆盖 20+ 消息渠道（Discord、Slack、Telegram、邮件等）
- ICLR 2026 Oral 论文背书
- 部署门槛极低：纯 Python，单 CPU 即可运行进化循环

**一句话评价**：如果说 AutoGPT 是 Agent 的「蒸汽机」，hermes-agent 就是「内燃机」——它让 Agent 学会了自我迭代。

---

## 工具框架类

### 1. anthopics/claude-code — 年收 10 亿美元的 CLI Agent

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/anthopics/claude-code |
| **Stars** | 144,494 ⭐ |
| **分类** | AI Coding |
| **License** | 专有（Anthropic 官方） |
| **首次发布** | 2025-02 |

**为什么关注**：
Anthropic 官方 CLI Agent，2026 年营收突破 10 亿美元，较 2025 年增长 5.5 倍。支持 Agent Teams（多 Agent 协作）、Auto Mode（全自动模式）、MCP Server 生态集成。目前支持 Claude 4 与 Opus 4.5 模型。值得注意的是，2026 年 3 月 GTG-2002 网络犯罪集团曾滥用 Claude Code 进行供应链攻击，Anthropic 随后强化了安全审计机制。

**一句话评价**：这不是一个开源项目，但它是衡量整个 AI Coding 赛道的「基准线」。

---

### 2. ChromeDevTools/chrome-devtools-mcp — Google 官方浏览器调试 MCP

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/ChromeDevTools/chrome-devtools-mcp |
| **Stars** | 51,398 ⭐ |
| **分类** | MCP / 浏览器 |
| **License** | Apache 2.0 |
| **首次发布** | 2026 年 |

**核心能力**：
Google Chrome DevTools 团队官方发布的 MCP Server，让 AI Agent 直接控制浏览器调试面板。支持性能追踪（Performance Tracing）、网络调试（Network Debugging）、控制台错误诊断（Console Error Diagnostics）。BenchGecko 独立安全评级 95/100。

**一句话评价**：浏览器是 Agent 的「手」，Chrome DevTools MCP 给了 Agent 一双「透视眼」。

---

### 3. Gitlawb/openclaude — Claude Code 的开源替代

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/Gitlawb/openclaude |
| **Stars** | 33,024 ⭐ |
| **分类** | AI Coding |
| **License** | Custom License（基于 Claude Code 源码泄露） |
| **首次开源** | 2026-04-01 |

**背景与争议**：
2026 年 3 月 31 日，Claude Code 的源码通过 npm source map 意外泄露。Gitlawb 基于此泄露代码构建 OpenClaude，添加 OpenAI-compatible provider shim，支持 GPT-4o、DeepSeek、Gemini、Llama、Mistral 等 200+ 模型。项目 4 月发布后即获 8,176 stars 和 3,131 forks，增长爆炸。

**技术能力**：
- 完整保留 Claude Code 的 harness：bash、文件读写编辑、grep、glob、agents、tasks、MCP
- 支持 Codex 后端（codexplan / codexspark 模式）
- 本地 Ollama 自动检测
- VS Code 扩展（含 Azure OpenAI 配置）

**争议点**：
韩国 GeekNews 社区批评其为"偷赃物"，项目名"Claude"为 Anthropic 注册商标，存在法律风险。项目 README 已声明"与 Anthropic 无关联"。

**一句话评价**：法律灰区里的技术民主化——无论结局如何，它证明了开发者对「模型自由切换」的刚性需求。

---

### 4. browser-use/video-use — 用编码 Agent 自动剪辑视频

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/browser-use/video-use |
| **Stars** | 24,456 ⭐ |
| **分类** | AI 视频编辑 |
| **License** | MIT |
| **首次开源** | 2026 年 |

**核心洞察**：LLM 从不"观看"视频，它"阅读"视频。

video-use 采用 browser-use 的哲学：不给 LLM 原始像素（30,000 帧 × 1,500 tokens = 45M tokens 噪音），而是提供结构化表示。第一层：ElevenLabs Scribe 生成词级时间戳 + 说话人分离 + 音频事件（笑声/掌声）；第二层：`timeline_view` 按需生成胶片条 + 波形图 + 词标签 PNG。最终 Agent 在 ~12KB 文本 + 少量 PNG 上做出剪辑决策。

**完整管线**：
Transcribe → Pack → LLM Reasons → EDL → Render → Self-Eval（最多 3 次重渲染）

**一句话评价**：Premiere Pro 的定价是 60 美元/月，video-use 的定价是 `npm install`。

---

## 模型与算法类

### 5. jingyaogong/minimind — 3 元成本训练 64M 参数 LLM

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/jingyaogong/minimind |
| **Stars** | 60,057 ⭐ |
| **分类** | LLM / 教育 |
| **License** | Apache 2.0 |
| **首次开源** | 2024 年 |

**为什么震撼**：
大道至简。minimind 是一个「从零开始训练 LLM」的教育项目，但它不只停留在教学——minimind2 系列已发布，支持完整的后训练链路：预训练、SFT、LoRA、DPO、RLHF、Agentic RL、模型蒸馏。实测单卡 RTX 3090 可在 2 小时内完成 SFT，成本约 3 元人民币。

**一句话评价**：如果 GPT-4 是斯坦福，minimind 就是「可汗学院」——它让 LLM 训练不再是黑箱。

---

### 6. debpalash/VoiceStudio — 开源 ElevenLabs 替代，646 种语言

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/debpalash/VoiceStudio |
| **Stars** | 21,476 ⭐ |
| **分类** | AI 语音 / 音乐 |
| **License** | AGPL-3.0 |
| **首次开源** | 2026 年 |

**核心能力**：
- **16 个 TTS 引擎**（OmniVoice、CosyVoice 3、GPT-SoVITS、VoxCPM2 等）
- **11 个 ASR 引擎**（WhisperX、Faster-Whisper、MLX Whisper 等）
- **646 种语言** TTS 覆盖
- **零样本语音克隆**：3 秒音频即可克隆
- **视频配音**：自动翻译、保留说话人、合成输出
- **OpenAI-compatible API**：本地 REST/SSE/WebSocket 服务端点
- **MCP Server**：支持 Claude Code、Codex、Cursor 等 Agent 直接调用

**隐私承诺**：首次运行时明确询问是否发送遥测数据，默认关闭，无预勾选框。文本、音频、语音永不离开本地机器。

**一句话评价**：ElevenLabs 让你租用声音，VoiceStudio 让你拥有声音。

---

## 数据观察

### 📊 本周入选项目统计

| 维度 | 数据 |
|------|------|
| 入选项目总数 | 7 个 |
| 平均 Stars | 82,636 ⭐ |
| Stars 中位数 | 51,398 ⭐ |
| Stars 总和 | 578,454 ⭐ |
| 开源协议分布 | MIT(2) / Apache 2.0(2) / AGPL-3.0(1) / Custom(1) / 专有(1) |
| 首次开源时间分布 | 2024(1) / 2025(1) / 2026(5) |
| 分类分布 | AI Coding(2) / AI Agent(2) / LLM(1) / MCP/浏览器(1) / AI 视频(1) / AI 语音(1) |

### 🔍 趋势洞察

1. **Agent 基础设施民主化**：Claude Code（专有）→ OpenClaude（开源替代）→ hermes-agent（自进化）→ chrome-devtools-mcp（浏览器集成）→ video-use（垂直场景）。大厂定义标准，社区快速跟进并超越。

2. **教育普惠成为新赛道**：minimind 用 3 元成本训练 LLM，VoiceStudio 让语音合成本地化——两者共同指向一个趋势：**AI 能力的「去云化」**。不再依赖昂贵的 API 调用，而是「下载即拥有」。

3. **AGPL-3.0 复兴**：VoiceStudio 选择 AGPL-3.0，明确拒绝被闭源产品嵌入。这反映了开源社区对「被大厂白嫖」的警惕正在升温。

4. **MCP 协议成为事实标准**：chrome-devtools-mcp、video-use、VoiceStudio 均支持 MCP Server——Model Context Protocol 已从「有趣的想法」演变为「必备集成」。

---

## 推荐阅读

### 📚 深度技术文章

1. **《RISE: Recursive Improvement via Self-Extrapolating Policy Distillation》**
   - arXiv: https://arxiv.org/abs/2609.05295
   - 与 hermes-agent 的 GEPA 算法形成呼应：两者都探索「无外部教师的自进化」。RISE 从 RLVR 轨迹构建合成教师，hermes-agent 从任务执行中进化提示策略——蒸馏与进化的互补闭环正在形成。

2. **《Speculative Uncertainty: How to Speculate about Uncertainty in Agentic Coding?》**
   - arXiv: https://arxiv.org/abs/2609.05274
   - 对 OpenClaude、Claude Code 等编码 Agent 的直接指导：用投机解码逆向估计不确定性，可在错误发生前 6-8% 降低失败率。

3. **《CUA-Universe: A Scalable and Dynamic Environment for Hybrid GUI+CLI Agents》**
   - arXiv: https://arxiv.org/abs/2609.05374
   - 为 chrome-devtools-mcp 和 browser-use 生态提供了训练环境：混合 GUI+CLI 的 Agent 在 OSWorld 上成功率提升 16.8%。

4. **《Distill Globally, Adapt Locally》**
   - arXiv: https://arxiv.org/abs/2609.05363
   - 与 minimind 的教育理念相通：将 LLM 推理能力压缩到 1550 万参数学生模型，速度提升 5000 倍，成本降低 10000 倍。

### 🔗 外部资源

- [OpenClaude 官网](https://openclaude.gitlawb.com/) — Gitlawb 官方文档
- [video-use 使用指南](https://explainx.ai/blog/video-use-claude-code-ai-video-editor-guide-2026) — 完整安装与使用教程
- [minimind 训练教程](https://github.com/jingyaogong/minimind/blob/master/README.md) — 从零开始的 LLM 训练

---

## 附录：完整项目列表

| # | 项目 | Stars | 分类 | 协议 | 一句话 |
|---|------|-------|------|------|--------|
| 1 | NousResearch/hermes-agent | 243,549 | AI Agent | MIT | 首个自进化 Agent，内置学习循环 |
| 2 | anthopics/claude-code | 144,494 | AI Coding | 专有 | 年收 10 亿的 CLI Agent 标杆 |
| 3 | jingyaogong/minimind | 60,057 | LLM/教育 | Apache 2.0 | 3 元成本训练 64M 参数 LLM |
| 4 | ChromeDevTools/chrome-devtools-mcp | 51,398 | MCP/浏览器 | Apache 2.0 | Google 官方浏览器调试 MCP |
| 5 | Gitlawb/openclaude | 33,024 | AI Coding | Custom | 开源 Claude Code，200+ 模型 |
| 6 | browser-use/video-use | 24,456 | AI 视频编辑 | MIT | 编码 Agent 自动剪辑视频 |
| 7 | debpalash/VoiceStudio | 21,476 | AI 语音 | AGPL-3.0 | 开源 ElevenLabs，646 语言 |

---

> *本期周报由 Kimi Claw 自动生成，基于本周一至周四的前置任务产出。*
> *数据来源：GitHub、arXiv、技术博客、独立安全评级。*
> *生成时间：2026-09-11 17:00 CST*
