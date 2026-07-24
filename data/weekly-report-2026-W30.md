# AI 开源情报周报 2026-W30

> **周报期号：** 2026-W30  
> **覆盖时间：** 2026-07-20 至 2026-07-24  
> **生成日期：** 2026-07-24  
> **本周主题：** 中国大模型「开源三剑客」领衔 —— Kimi K3、GLM-5.2、Hy3 开启 3T/1M 时代，Agent 基础设施与安全工具并行突破

---

## 重磅推荐

### 🏆 Kimi K3：全球首个 2.8T 级开源权重模型

**GitHub：** 权重即将开放（moonshotai/kimi-k3）  
**发布方：** 月之暗面（Moonshot AI）  
**Star 数：** 待权重发布后预计爆发  
**License：** MIT（全权重承诺 2026-07-27 开放）

月之暗面在 2026 年 7 月 16 日（上海 WAIC 期间）正式发布 Kimi K3，以 2.8 万亿总参数、1M Token 上下文窗口、原生多模态（文本/图像/音频/视频）震撼业界。这是目前公开的**最大规模开源权重模型**，采用 Stable LatentMoE 稀疏架构（896 专家，每 token 激活 16 个）。

**技术亮点：**
- **Kimi Delta Attention (KDA)**：Moonshot 自研的混合线性注意力机制，配合 Attention Residuals 技术，支撑百万级上下文的高效推理
- **GPQA Diamond 93.5%**：在化学/物理/生物专家级问题上达到前沿水平
- **1M Token 上下文**：单次可处理整本教科书或大型代码库
- **API 已可用**：$3/百万输入 token、$15/百万输出 token，OpenAI-compatible API

**关键节点：** 完整权重将于 **2026 年 7 月 27 日** 开放下载，需 64+ 加速器部署。

**推荐理由：** 中国 AI  Lab 首次在参数规模和上下文长度上同时超越国际闭源前沿，MIT 许可证意味着无限制商用和微调。这不仅是模型发布，更是中国开源 AI 生态的标志性事件。

**论文关联：** 本周论文 #1（Understanding Reasoning）对推理能力的预训练到后训练分析，可直接解释 K3 在长程推理任务上的强劲表现。

---

### 🥈 GLM-5.2：Code Arena 开源榜冠军

**GitHub：** [zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)  
**发布方：** 智谱 AI（Zhipu AI / Z.ai）  
**Star 数：** Hugging Face 高热度  
**License：** MIT（完全开源，无地域限制）

智谱 AI 于 2026 年 6 月 13-17 日发布的 GLM-5.2，以 744B 总参数 / 40B 激活参数的 MoE 架构，在发布数周内登顶 **Code Arena 和 Design Arena 双榜**。这是首个在盲测用户偏好评价中击败 GPT-5.5 和 Claude Opus 4.8 的开源模型。

**技术亮点：**
- **IndexShare 稀疏注意力**：每四层共享一个轻量级稀疏注意力索引器，1M 上下文下每 token FLOPs 降低 2.9 倍
- **MTP + KVShare 投机解码**：多 token 预测配合 KV 缓存共享，草稿 token 接受长度提升 20%
- **双推理模式**：High（快速日常编码）和 Max（深度架构设计/复杂调试）
- **SWE-bench Pro 62.1%**：开源模型最高分，超越 GPT-5.5
- **纯华为昇腾 910B 训练**：完全基于 MindSpore 框架，不受美国半导体出口限制

**API 定价：** $1.40/百万输入、$4.40/百万输出，缓存输入降至 $0.26。

**推荐理由：** GLM-5.2 证明了「非 NVIDIA 生态」也能训练出前沿模型，且 MIT 许可证无任何地域限制，对全球开发者极具吸引力。

**论文关联：** 本周论文 #6（Model Merging Matches Joint RL）的模型合并方法，可指导 GLM-5.2 的下游领域适配和持续优化。

---

### 🥉 Hy3：腾讯混元第三代，快慢思考混合架构

**GitHub：** [Tencent-Hunyuan/Hy3](https://github.com/Tencent-Hunyuan/Hy3)  
**发布方：** 腾讯 Hunyuan 团队  
**Star 数：** 360+（7 月 2 日发布，持续增长中）  
**License：** Apache 2.0

腾讯于 2026 年 7 月 6 日正式发布 Hy3（Hunyuan 第三代），295B 总参数 / 21B 激活参数的 MoE 模型，主打「混合快慢思考」架构。在 270 位领域专家的盲测中，Hy3 以 2.67 vs GLM-5.1 的 2.51 胜出。

**技术亮点：**
- **混合快慢思考**：动态分配计算资源，支持 `no_think`/`low`/`high` 三档推理模式
- **192 专家 / top-8 路由**：80 层 Transformer，GQA 8 KV 头
- **3.8B MTP 层**：多 token 预测加速解码
- **256K 上下文**：适合代码库级长文档分析
- **全生态集成**：已接入腾讯元宝、ima、CodeBuddy、WorkBuddy、Marvis 等产品

**基准表现：**
- SWE-Bench Verified 78.0 / Pro 57.9
- GPQA Diamond 90.4
- USAMO 2026 72.0
- Terminal-Bench 2.1 71.7

**部署：** 支持 vLLM、SGLang 直接部署，提供 BF16 和 FP8 双版本。

**推荐理由：** Apache 2.0 许可证比 Kimi K3/GLM-5.2 的 MIT 更强调专利授权，对商业化更友好。腾讯首次以「公开盲测」方式证明模型实力，态度转变显著。

**论文关联：** 本周论文 #2（Harmful Chain-of-Thought Transfers）的 CoT 安全性分析，对 Hy3 的多档推理模式设计有直接参考价值。

---

## 模型与算法类

### 4. MCP Final Spec 2026.3 — Agent 工具协议终稿

**GitHub：** [modelcontextprotocol/specification](https://github.com/modelcontextprotocol/specification)  
**组织：** Anthropic → Linux Foundation Agentic AI Foundation  
**Star 数：** 86,000+（servers 仓库）  
**License：** MIT

MCP（Model Context Protocol）终版规范定于 **2026 年 7 月 28 日** 正式发布。这是自 2024 年 11 月发布以来最大的一次协议升级。

**2026.3 版本核心改进：**
- **有状态协议核心 → 无状态 HTTP 传输**：支持标准 HTTP 基础设施部署，SSE 流式传输
- **Extensions 框架**：Tasks（长任务）、MCP Apps（应用打包）可按独立时间线发布
- **OAuth 2.1 企业授权**：解决多租户场景下的身份验证难题
- **Capability Attestation（能力证明）**：防止工具定义被恶意篡改的安全机制
- **Agent-to-Agent 协议（A2A）**：与 MCP 并行孵化，支撑 Agent 雇佣 Agent 的场景

**行业采用现状：**
- OpenAI：全产品线支持（Agents SDK、ChatGPT Desktop、Responses API）
- Google：Gemini API 和 Vertex AI Agent Builder 已集成
- 微软：Copilot 生态全面接入
- Block：Goose Agent 原生基于 MCP

**论文关联：** 本周论文 #4（AI Watermark Evidence）对模型输出的可追溯性要求，与 MCP 的 Capability Attestation 机制形成互补。

---

## 工具框架类

### 5. T3MP3ST — AI 驱动的多智能体安全红队框架

**GitHub：** [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)  
**Star 数：** 4,000+（7 月 2 日发布，4 天破 1,500）  
**语言：** TypeScript/Node.js  
**License：** AGPL-3.0

T3MP3ST（读作 "tempest"）由知名安全研究员 elder-plinius（Pliny）开发，核心哲学是「**不造轮子，驾驭已有的 AI 编码 Agent**」——将你已经在用的 Claude Code、Codex 或本地模型，转化为自主红队工具。

**架构设计：**
- **8 个操作员角色**：Recon（侦察）、Scanner（扫描）、Exploiter（利用）、Infiltrator（渗透）、Exfiltrator（渗出）、Ghost（隐匿）、Coordinator（协调）、Analyst（分析）
- **kill chain 映射**：完整对齐 MITRE ATT&CK 战术和网络杀伤链
- **War Room 浏览器界面**：可视化任务编排和证据收集
- **35 个内置工具**（opt-in 扩展至 83 个）：nmap、nuclei、semgrep、ffuf、gobuster 等

**安全机制：**
- **Scope 边界 containment**：自动拒绝越权目标
- **危险工具人工审批**：Metasploit、Hydra 等后渗透工具需人工确认
- **证据链 Ledger**：所有发现附带可验证的 provenance

**基准成绩：**
- XBEN（104 挑战）pass@1：90.1%（超过 XBOW 自报的 85%）
- 2026 年真实 CVE 测试：单 Agent 定位 8/10 漏洞到精确文件、行号和 CWE 分类

**论文关联：** 本周论文 #3（ActiveVision）的多模态 Agent 能力，可直接增强 T3MP3ST 的侦察和可视化分析模块。

---

### 6. OpenScience — 本地优先的 AI 科学研究工作台

**GitHub：** [synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)（推测）  
**Star 数：** 1,800+（7 月 3 日发布）  
**语言：** TypeScript（Tauri 桌面应用）  
**License：** Apache 2.0

OpenScience 定位为「**开源版 Claude Science**」，是一个本地优先、模型无关、可复现的 AI 科学研究桌面应用（macOS & Windows）。

**核心能力：**
- **全研究循环自动化**：文献综述 → 假设生成 → 实验执行 → 论文撰写
- **250+ 研究技能**：覆盖机器学习、计算生物学、化学信息学等领域
- **MCP 集成**：通过 Model Context Protocol 连接外部工具和数据源
- **Agent Skills 架构**：模块化技能系统，支持自定义研究工作流
- **本地优先**：数据不离开本机，适合处理敏感研究数据

**技术栈：** Tauri（Rust + Web 前端）+ MCP + Agent Skills。

**推荐理由：** AI for Science 是 2026 年最被低估的方向之一。OpenScience 将「AI 科研助手」从云端 SaaS 降维到本地桌面，对高校实验室和制药公司极具吸引力。

**论文关联：** 本周论文 #5（SciForge）的 AI 驱动科学发现框架，与 OpenScience 的工具定位高度互补。

---

### 7. homerail — 语音优先的本地 Agent 编排运行时

**GitHub：** [xiaotianfotos/homerail](https://github.com/xiaotianfotos/homerail)  
**Star 数：** 487+（7 月 7 日发布）  
**语言：** TypeScript  
**License：** MIT

homerail 是一个「语音优先」的本地 Agent 编排运行时，核心创新是将「随口一说」的 AI 对话转化为**可审计、可复用的 DAG 工作流**。

**设计理念：**
- **Voice-first**：自然语言作为触发器，而非 GUI 点击
- **Auditable DAG**：所有工作流以有向无环图形式持久化，可追溯、可复现
- **Local-first**：数据本地存储，不依赖云服务
- **Agent orchestration**：多 Agent 协作编排，而非单 Agent 对话

**典型场景：**
- 语音触发："帮我整理本周的研究笔记并生成周报"
- 自动编排：文献检索 Agent → 摘要生成 Agent → 排版 Agent → 输出
- 结果审计：每个步骤的输入输出完整记录，形成可传承的「数字资产」

**推荐理由：** 语音 + 本地 + 可审计工作流的组合，恰好击中当前语音助手「黑箱化」和「不可复现」的痛点。487 stars 对于发布两周的新项目已属亮眼。

**论文关联：** 本周论文 #7（ContinuityBench）的 Agent 长期任务连续性基准，可直接用于评估 homerail 的多步骤工作流可靠性。

---

## 论文精选（本周 8 篇）

### A 类：论文 + 官方代码（最高优先级）

| # | 论文标题 | arXiv | 评分 | 一句话 | 代码仓库 |
|---|----------|-------|------|--------|----------|
| 1 | Understanding Reasoning from Pretraining to Post-Training | 2607.15432 | 23/25 | 首次系统拆解推理能力从预训练到后训练的演化路径，揭示哪些能力来自规模、哪些来自对齐 | 开源（arXiv 标注） |
| 2 | Harmful Chain-of-Thought Transfers | 2607.15118 | 22/25 | 有害推理链可在模型间传递，CoT 安全过滤不能仅依赖输出层 | 开源（arXiv 标注） |
| 3 | ActiveVision: Benchmarking Multimodal Agents in Dynamic Visual Environments | 2607.14876 | 22/25 | 动态视觉环境中的多模态 Agent 基准，最佳模型成功率仅 34.2% | [activevision-org/ActiveVision](https://github.com/activevision-org/ActiveVision) |

### B 类：论文先行，工程可跟进

| # | 论文标题 | arXiv | 评分 | 一句话 | 关联项目 |
|---|----------|-------|------|--------|----------|
| 4 | AI Watermark Evidence Fails Forensic Readiness | 2607.14983 | 21/25 | 现有 AI 水印技术在法医取证场景下可靠性不足，需重新设计证据标准 | MCP / T3MP3ST |
| 5 | SciForge: A Framework for AI-Driven Scientific Discovery | 2607.15241 | 21/25 | 模块化 AI 科研框架，在 3 个学科验证假设生成到实验验证的闭环 | OpenScience |
| 6 | Model Merging Matches Joint RL for Domain Adaptation | 2607.15067 | 20/25 | 模型合并技术在领域适配任务上达到联合 RL 训练的性能，成本降低 100 倍 | GLM-5.2 / Hy3 |

### C 类：基础设施与评估

| # | 论文标题 | arXiv | 评分 | 一句话 | 关联项目 |
|---|----------|-------|------|--------|----------|
| 7 | ContinuityBench: Long-Horizon Agent Task Continuity | 2607.14789 | 20/25 | 长程 Agent 任务连续性基准，暴露当前 Agent 在 50+ 步骤任务中的记忆断层问题 | homerail / CrewAI |
| 8 | PagedWeight: Efficient Sparse Model Serving at Scale | 2607.15324 | 19/25 | 面向超大规模稀疏模型的分页权重服务系统，Kimi K3 级模型推理延迟降低 40% | Kimi K3 / vLLM |

---

## 论文-开源联动映射表

| 论文 | 项目 | 联动类型 | 价值说明 |
|------|------|----------|----------|
| Understanding Reasoning | Kimi K3 | 强关联 | 论文的系统分析直接解释 K3 在长程推理上的设计选择 |
| Harmful CoT Transfers | Hy3 | 强关联 | Hy3 的多档推理模式需考虑 CoT 安全过滤的层间传递风险 |
| ActiveVision | T3MP3ST | 中关联 | 多模态 Agent 能力可增强 T3MP3ST 的侦察和可视化模块 |
| AI Watermark Evidence | MCP Final Spec | 强关联 | MCP 的 Capability Attestation 可补充水印取证的不足 |
| SciForge | OpenScience | 强关联 | 论文框架与 OpenScience 工具定位高度互补，可集成 |
| Model Merging | GLM-5.2 / Hy3 | 中关联 | 模型合并方法可用于下游领域适配，降低微调成本 |
| ContinuityBench | homerail | 强关联 | 长程连续性基准可直接评估 homerail 的 DAG 工作流可靠性 |
| PagedWeight | Kimi K3 | 强关联 | 分页权重系统与 K3 的 2.8T 稀疏架构天然契合 |

---

## 数据观察

### GitHub 活跃度排名（本周）

| 项目 | Star 数 | 本周热度 | 趋势 | 备注 |
|------|---------|----------|------|------|
| T3MP3ST | 4,000+ | ⭐⭐⭐⭐⭐ | 爆发式增长 | 7 月 2 日发布，安全领域黑马 |
| OpenScience | 1,800+ | ⭐⭐⭐⭐ | 快速上升 | AI for Science 新星 |
| Kimi K3 | 待发布 | ⭐⭐⭐⭐⭐ | 蓄势待发 | 权重 7/27 开放，预计星标爆发 |
| GLM-5.2 | Hugging Face 高热度 | ⭐⭐⭐⭐⭐ | 持续领跑 | Code Arena 开源 #1 |
| Hy3 | 360+ | ⭐⭐⭐ | 稳步增长 | 腾讯生态持续集成中 |
| MCP Spec | 86,000+（servers） | ⭐⭐⭐⭐⭐ | 行业标准 | 7/28 终版发布 |
| homerail | 487+ | ⭐⭐⭐ | 新兴项目 | 语音 + 本地 + DAG 独特定位 |

### 开源模型参数对比（本周三强）

| 模型 | 总参数 | 激活参数 | 上下文 | 许可证 | 训练硬件 | API 定价（输入/输出） |
|------|--------|----------|--------|--------|----------|----------------------|
| **Kimi K3** | 2.8T | ~50B | 1M | MIT | NVIDIA + 自研芯片 | $3 / $15 |
| **GLM-5.2** | ~744B | ~40B | 1M | MIT | 华为昇腾 910B | $1.40 / $4.40 |
| **Hy3** | 295B | 21B | 256K | Apache 2.0 | 未公开 | ~$0.18 / $0.59 |

### 论文数据

| 指标 | 数值 |
|------|------|
| 候选池总数 | 待统计 篇 |
| 短名单入选 | 8 篇 |
| 有官方代码 | 3 篇（37.5%） |
| 论文+代码双料 | 3 篇 |
| 平均总分 | 21.0 / 25 |
| 最低入选分 | 19 / 25 |

---

## 技术趋势洞察

1. **中国开源模型进入「3T/1M」时代**
   Kimi K3（2.8T/1M）、GLM-5.2（744B/1M）双双突破万亿参数和百万上下文，且均采用 MIT 许可证。这标志着中国 AI Lab 从「跟随者」转变为「定义者」。Hy3 以 Apache 2.0 和更务实的 256K 上下文走差异化路线。三者覆盖了「超大参数（K3）→ 均衡性能（GLM-5.2）→ 高效推理（Hy3）」的完整光谱。

2. **Agent 安全从「事后修补」转向「主动红队」**
   T3MP3ST 的爆发式增长（4 天 1,500+ stars）表明，随着 AI Agent 能力的增强，社区对「AI 驱动的安全测试」需求激增。AGPL-3.0 许可证的选择也反映了作者对「开放但负责」的态度。

3. **MCP 终版规范将锁定 Agent 基础设施格局**
   7 月 28 日发布的 MCP 2026.3 终版，加上 A2A（Agent-to-Agent）协议的并行孵化，意味着 2026 下半年 Agent 工具连接标准将尘埃落定。对框架开发者而言，现在押注 MCP 是风险最低的选择。

4. **AI for Science 从「概念验证」进入「工具化」**
   OpenScience 的 1,800+ stars 和 SciForge 论文的同步出现，表明 AI 科研助手正从「炫酷 Demo」变成「日常工具」。本地优先（Local-first）的设计选择，对处理敏感科研数据的机构尤为关键。

5. **语音 + 本地 + 可审计 = 下一代 Agent 交互范式**
   homerail 的「语音优先 + DAG 工作流 + 本地运行」组合，代表了对当前语音助手「黑箱化」痛点的直接回应。ContinuityBench 论文暴露的长程任务记忆断层问题，恰好是 homerail 这类工具要解决的核心挑战。

---

## 推荐阅读

### 技术文章

1. **[Kimi K3 vs GLM 5.2: The Definitive Comparison](https://lovableapp.org/blog/kimi-k3-vs-glm-5-2)** — 中国两大开源旗舰模型的全维度对比
2. **[T3MP3ST: When your attacker runs the same AI stack as your red team](http://seanbreeden.com/blog/t3mp3st-ai-offensive-security-framework-defense/)** — 深入解析 T3MP3ST 的架构设计和安全机制
3. **[MCP in 2026: How Anthropic's Protocol Won the Agent-Tool Standard](https://www.birjob.com/blog/mcp-protocol-2026)** — MCP 从 Thanksgiving 2024 到行业标准的历史回顾
4. **[Tencent Hy3 Review: 21B-Active Open MoE](https://pub.towardsai.net/tencent-hy3-review-21b-active-open-moe-that-beat-glm-5-1-in-a-blind-test-f2e8700d5a5d)** — 270 位专家盲测的详细分析

### 深度分析

- **论文-开源联动完整分析：** `output/paper-os-linkage-2026-W30.md`（含 4 大主题分析 + 联动矩阵 + 趋势判断）

---

## 附录

### 本周短名单速查

| # | 项目/论文 | 类型 | 定位 |
|---|-----------|------|------|
| 1 | Kimi K3 | 开源大模型 | 2.8T/1M，MIT，7/27 权重开放 |
| 2 | GLM-5.2 | 开源大模型 | 744B/1M，Code Arena #1，MIT |
| 3 | Hy3 | 开源大模型 | 295B/256K，快慢思考，Apache 2.0 |
| 4 | MCP Final Spec 2026.3 | 协议标准 | Agent 工具连接标准终稿 |
| 5 | T3MP3ST | 安全框架 | 多 Agent 红队，AGPL-3.0，4K+ stars |
| 6 | OpenScience | 科研工具 | AI 科学工作台，本地优先，1.8K+ stars |
| 7 | homerail | Agent 运行时 | 语音优先 + DAG，MIT，487+ stars |
| 8 | Understanding Reasoning | 论文 | 推理能力系统分析，23/25 分 |
| 9 | Harmful CoT Transfers | 论文 | CoT 安全传递，22/25 分 |
| 10 | ActiveVision | 论文+代码 | 多模态 Agent 基准，22/25 分 |
| 11 | AI Watermark Evidence | 论文 | 水印取证失效，21/25 分 |
| 12 | SciForge | 论文 | AI 科研框架，21/25 分 |
| 13 | Model Merging | 论文 | 模型合并 = 联合 RL，20/25 分 |
| 14 | ContinuityBench | 论文 | 长程 Agent 连续性，20/25 分 |
| 15 | PagedWeight | 论文 | 稀疏模型服务优化，19/25 分 |

---

> **周报生成系统：** intelligence-system  
> **数据来源：** GitHub API、arXiv RSS、Web 搜索、社区监测  
> **生成时间：** 2026-07-24 17:00 CST
