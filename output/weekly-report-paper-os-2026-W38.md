# AI开源情报周报 | 2026-W38

> 报告周期：2026-09-14 至 2026-09-20
> 生成时间：2026-09-18 19:00 CST
> 数据来源：论文精选（8篇，49候选，入选率16.3%）+ 开源精选（7个，17候选）
> 联动分析：output/paper-os-linkage-2026-W38.md
> 编排方式：按 A-D 联动优先级排序（A=论文+官方代码 → D=项目先行）

---

## 📋 本周概览

| 维度 | 数据 |
|------|------|
| 精选论文 | 8篇（49候选，入选率16.3%） |
| 精选开源项目 | 7个（17候选） |
| 论文-代码双料 | 4个（AMDKernelVault / ZipBench / TAM / CoG） |
| A类强关联 | 5对（含 MOSS-TTS 项目+论文型） |
| B类中关联 | 4对 |
| D类项目先行 | 5个 |
| 本周最热话题 | Agent沙箱安全、声明式运行时、评估成本革命 |

**本周关键词**：沙箱逃逸 · 跨层防御 · 基准压缩 · 真机飞轮 · 声明式Agent · 全家族TTS

**本周一号事件**：DeepSeek Harness 沙箱逃逸漏洞（CVE-2026-82533，CVSS 9.4）与 SoK Jailbreaking 论文形成"学术-工程互证"——Agent 安全的战场已从输出审查转向执行环境本身。

---

## 🏆 A类：论文+官方代码（强关联，优先关注）

### A1 | AMDKernelVault：AMD GPU 首个开源算子语料库
- **论文**：https://arxiv.org/abs/2609.12471
- **代码**：⭐ 官方开源（6.2万HIP + 4万Triton内核语料库 + SFT/RL训练代码 + 生成管线）
- **评分**：21/25（创新性4 | 实用性4 | 技术深度4 | 机构背书4 | 代码可得性5）
- **关联项目**：DeepSeek Harness（⭐⭐⭐ 执行感知RL可直接用于Agent执行环境的训练）
- **一句话**：填补AMD GPU生态空白——内核生成智能体长期以CUDA/NVIDIA为中心，本文以6.2万执行验证内核训练Qwen3-8B，在PyTorch-to-HIP和TritonBench-G上取得最高正确率。

### A2 | ZipBench：低成本基准压缩框架
- **论文**：https://arxiv.org/abs/2609.12475
- **代码**：⭐ ZipBench Zoo 已发布（100+压缩基准）
- **评分**：21/25（创新性4 | 实用性5 | 技术深度4 | 机构背书4 | 代码可得性4）
- **关联项目**：OpenClaw（⭐⭐ CI集成评测成本可降一个数量级）
- **一句话**：仅用少量锚点LLM+伪评估合成即实现MAE 0.002-0.02、Spearman ~0.98的基准压缩，附带理论误差保证——算力受限团队的评估福音。

### A3 | MOSS-TTS：开源TTS的新标杆（项目+论文型A类）
- **GitHub**：[OpenMOSS/MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) ⭐ 4,109（Apache-2.0）
- **论文**：官方技术报告 arXiv:2603.18090
- **关联强度**：⭐⭐⭐ 单repo覆盖narration/对话/音效/流式/语音设计五场景，MOSS-TTSD v1.0主观评测超Doubao与Gemini 2.5-pro，支持vLLM-Omni推理，last push 2026-09-06维护活跃。
- **一句话**：Apache-2.0许可的高品质全场景TTS，可无障碍商用——语音Agent拼图中的TTS环节本周有了默认选型。

### A4 | TAM：长程序推理基准（真实手册任务）
- **论文**：https://arxiv.org/abs/2609.13005
- **代码**：⭐ 数据和代码公开发布
- **评分**：19/25（创新性4 | 实用性4 | 技术深度4 | 机构背书3 | 代码可得性4）
- **关联项目**：Mastra（⭐⭐ 真实手册任务是Agent框架的最难试金石）
- **一句话**：从ICD-10-CM临床编码和联邦量刑真实手册构建任务，GPT-5精确匹配仅1%（ICD-10）和15.5%（量刑）——RAG/ReAct/Agent框架全部失效，戳破传统基准的分数膨胀。

### A5 | CoG：免训练Graph RAG框架
- **论文**：https://arxiv.org/abs/2609.12791
- **代码**：⭐ 代码和数据集已开源
- **评分**：19/25（创新性4 | 实用性4 | 技术深度4 | 机构背书3 | 代码可得性4）
- **关联项目**：Mem0（⭐⭐⭐ 记忆检索的两条路线——CoG主动图谱探索 vs Mem0被动写入检索，可组合为Agent知识层完整方案）
- **一句话**：受人类plan-explore-reflect认知循环启发，图-文双向深度协同，7个多跳QA基准全面超越SOTA。

---

## 🔗 B类：论文+社区复现（中关联，关注落地）

### B1 | SoK: Jailbreaking Attacks and Defenses in the Era of Modern LLMs and Agentic AI — 本周学术侧头条
- **论文**：https://arxiv.org/abs/2609.12413
- **代码**：🔍 待确认（统一Agent框架下实证，预计可复现）
- **评分**：20/25（创新性4 | 实用性5 | 技术深度4 | 机构背书3 | 代码可得性3）
- **关联项目**：DeepSeek Harness（⭐⭐⭐）、TrueForge（⭐⭐⭐）、MCP servers（⭐⭐⭐）
- **一句话**：Agent全链路越狱安全综述——覆盖交互/规划/记忆/工具调用/通信五大攻击面。三大发现：强原生对齐≠抗越狱；防御效果高度依赖模型/攻击/组件；**最终响应过滤无法阻止中间层泄露**。
- **⚡ 本周联动**：最后一条发现与DeepSeek Harness CVE-2026-82533沙箱逃逸形成完美互证——安全战场不在最后一行输出，而在中间的每一次工具调用、每一次记忆读写、每一次规划推理。

### B2 | BlueLM-GUI：真机训练飞轮的移动端GUI Agent
- **论文**：https://arxiv.org/abs/2609.12394
- **代码**：🔍 待确认（模型在开源模型中最佳，预计权重开源）
- **评分**：20/25（创新性4 | 实用性5 | 技术深度4 | 机构背书4 | 代码可得性3）
- **关联项目**：Mastra（⭐⭐）、TrueForge（⭐⭐）
- **一句话**：vivo 35B-A3B模型，数百台真机Agentic RL训练，MobileGUI-VBench 87.4分超越最强闭源模型5.1分。"Every Rollout Is Real"原则直击沙箱训练与生产环境分布失配痛点。

### B3 | K-Bench：Agent部署下的遗忘评测基准
- **论文**：https://arxiv.org/abs/2609.12808
- **代码**：🔍 待确认（基准框架，预计开源）
- **评分**：19/25（创新性5 | 实用性4 | 技术深度4 | 机构背书3 | 代码可得性3）
- **关联项目**：Mem0（⭐⭐⭐）、MCP servers（⭐⭐⭐）
- **一句话**：首个Agent部署视角遗忘基准——6通道秘密泄露检测发现：秘密在prompt/检索库中时泄露率22-86%；**权重中的秘密，20种已发表方法均无法真正移除**。Mem0式ADD-only记忆架构在合规场景下是硬伤。

### B4 | SAS：门控稀疏注意力
- **论文**：https://arxiv.org/abs/2609.13141
- **代码**：🔍 待确认（Triton内核提及，预计开源）
- **评分**：19/25（创新性4 | 实用性4 | 技术深度5 | 机构背书3 | 代码可得性3）
- **关联项目**：AMDKernelVault（⭐⭐ 同技术栈，内核开源后可成为语料库高质量样本）
- **一句话**：端到端优化上下文排序的门控稀疏注意力，解决"蒸馏密集注意力导致排序与预测不对齐"核心痛点，紧预算下优势显著，FlashAttention风格Triton内核。

---

## 🚀 D类：项目先行（独立演进，观察论文跟进）

> 本周无C类（完全孤立的论文先行项）。以下为无直接对应论文、由工程实践驱动的项目。

### D1 | ⚠️ DeepSeek Harness 沙箱逃逸漏洞（CVE-2026-82533）— 本周工程侧头条
- **GitHub**：[deepseek-ai/harness](https://github.com/deepseek-ai/harness) ⭐ 225,726（MIT）
- **状态**：修复版0.1.2-alpha.1已于2026-08-27发布，漏洞详情09-08公开（OX Security披露）
- **风险**：CVSS 9.4危急级——构造特定输入可突破容器隔离，在宿主机执行任意命令
- **关联论文**：SoK Jailbreaking（⭐⭐⭐ 理论互证）、AMDKernelVault（⭐⭐⭐ 执行感知RL训练载体）、BlueLM-GUI（⭐⭐ 沙箱vs真机两路线对照）
- **行动**：所有运行不可信Agent代码的团队立即确认版本≥0.1.2-alpha.1；检查CI/CD集成点日志中的异常宿主机调用。
- **警钟意义**：Harness是Agent生态最大公约数（225k星），其沙箱逃逸意味着"Agent能生成并执行任意代码"时代的最后一道防线正在失守——执行层安全审计将成为企业adoption前置条件。

### D2 | OpenClaw — 个人AI助手的事实标准
- **GitHub**：[openclaw/openclaw](https://github.com/openclaw/openclaw) ⭐ 389,816（MIT）
- **本周动态**：v2026.9.4发布——ACP协议支持（Agent间通信）、安全加固（Gateway默认绑定127.0.0.1）、Lark/Feishu渠道原生集成增强
- **趋势信号**：创始人Peter Steinberger加入OpenAI后，项目过渡至独立开源基金会（OpenAI资助+MIT许可证+独立治理）；3,000+贡献者、13,700+ ClawHub Skills、50+通讯渠道、35+ AI提供商
- **安全提醒**：早期版本默认Gateway绑定0.0.0.0，旧实例升级后请确认已改为127.0.0.1
- **论文机会**：ACP协议的学术形式化（Agent间通信语义、能力协商）仍是空白

### D3 | Mem0 — Agent记忆层头号玩家
- **GitHub**：[mem0ai/mem0](https://github.com/mem0ai/mem0) ⭐ 65,372（Apache-2.0）
- **本周动态**：v2.0.20（9月2日）——OSS通知系统静态化（移除PostHog远程调用）、RedisDBConfig校验加固
- **核心算法**（4月版持续迭代）：单遍ADD-only提取、实体链接、多信号检索（语义+BM25+实体三路融合）、时序推理
- **关联论文**：K-Bench（⭐⭐⭐ 泄露警示）、CoG（⭐⭐⭐ 技术路线对照）
- **竞争格局**：Letta 21.8k / Graphiti 24k / Zep / Cognee 14.8k——记忆层赛道白热化，Mem0凭极简API（`memory.add()`/`memory.search()`两个调用）和20种向量后端稳坐头把交椅
- **隐忧**：K-Bench证明ADD-only记忆无真正删除能力，合规场景需外挂遗忘机制

### D4 | Mastra — TypeScript Agent框架领军者 + Factory发布
- **GitHub**：[mastra-ai/mastra](https://github.com/mastra-ai/mastra) ⭐ 28,090（Apache-2.0）
- **本周动态**：**Mastra Factory正式发布**（9月8日）——企业级Agent构建管理平台（可视化编排、部署监控、生命周期管理）；周NPM下载量约110万
- **技术亮点**：Observational Memory自动记忆压缩、Supervisor Pattern多Agent编排、Remote Sandbox（Daytona/E2B/Blaxel）、Model Router多提供商故障转移
- **生产案例**：Replit（96%任务成功率）、PayPal、Marsh McLennan、SoftBank
- **范式对照**：与TrueForge形成"代码优先 vs 配置优先"对峙——TypeScript写Agent获最大灵活性，YAML声明获最大可审计性
- **论文机会**：Observational Memory的长期评估研究缺失；声明式vs代码优先的范式对比研究

### D5 | MCP Reference Servers — 协议生态基石
- **GitHub**：[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) ⭐ 90,368（⚠️ NOASSERTION许可证）
- **本周动态**：Slack参考服务器归档至`servers-archived`（官方README指向社区维护者korotovsky/slack-mcp-server约1,800星）；协议规范2026-07-28推进CIMD取代DCR、无状态化、缓存化
- **生态规模**：10,000+生产MCP服务器、SDK月下载9,700万+；2025年12月Anthropic将MCP捐赠给Agentic AI Foundation（Linux Foundation下设）
- **关联论文**：K-Bench（⭐⭐⭐ 工具调用通道泄露）、SoK Jailbreaking（⭐⭐⭐ 工具调用是五大攻击面之一）
- **许可证提醒**：使用前逐子目录确认具体条款
- **论文机会**：MCP安全边界（OAuth范围、工具权限）无系统性学术研究，K-Bench是切入点

---

## 🔑 本周核心洞察

### 洞察1：学术与工程本周"互证"了同一件事

SoK Jailbreaking论文说：最终响应过滤无法阻止中间层泄露，防御必须跨层、必须执行感知。
DeepSeek Harness CVE说：攻击者可以突破沙箱在宿主机执行任意命令，CVSS 9.4。
K-Bench说：就算权重忘了，Agent部署后经prompt/检索库通道的泄露率仍有22-86%。

三条独立证据链指向同一结论：**Agent安全=系统安全，不是模型对齐问题。** 单独看论文是理论，单独看CVE是事故，放一起看是范式转移。

### 洞察2：评估赛道三连发，对象从"模型"转向"系统"

ZipBench（评估太贵→压缩）、TAM（评估太假→真实手册）、K-Bench（评估错位→部署视角）——本周三篇评估论文分别攻击三个不同痛点，共同信号是：当Agent通过MCP连接10,000+工具时，给单个模型打分已经没有意义。**评估的是模型×prompt×检索库×工具的组合。**

### 洞察3：声明式运行时与代码框架的范式对峙正式开局

TrueForge（30天5.7k星，YAML声明）与Mastra（28k星，TypeScript代码）分别吸引"可审计性优先"与"灵活性优先"的两类开发者。SoK论文的跨层防御框架理论上是TrueForge声明式策略层的最佳背书——安全团队审YAML比审Python容易得多。但Harness的CVE同时提醒：声明式策略管得住行为定义，管不住执行逃逸。

### 洞察4：TTS赛道进入"全家族"竞争，单模型repo集体出局

MOSS-TTS一个repo覆盖五场景且主观评测超闭源竞品，Chatterbox/Orpheus-TTS等单模型repo因维护停滞集体掉队。这与LLM开源的轨迹一致：从单模型到全栈家族。对语音Agent开发者，本周起TTS选型的默认答案变了。

---

## 📊 数据汇总

| 指标 | 数值 |
|------|------|
| 本周入选论文 | 8篇（49候选，入选率16.3%） |
| 本周入选开源项目 | 7个（17候选） |
| A类（论文+官方代码） | 5对 |
| B类（论文+社区复现） | 4对 |
| C类（论文先行） | 0对 |
| D类（项目先行） | 5个 |
| 强关联（⭐⭐⭐） | 8对 |
| 论文-代码双料 | 4个（AMDKernelVault / ZipBench / TAM / CoG） |
| 本周CVE | 1个（CVE-2026-82533，CVSS 9.4） |

### Star 增长趋势

| 项目 | Star | 趋势 |
|------|------|------|
| OpenClaw | 389,816 | → 稳步增长，v2026.9.4 ACP支持 |
| DeepSeek Harness | 225,726 | ⚠️ CVE事件或反而推高关注度 |
| MCP servers | 90,368 | → 协议生态持续扩张 |
| Mem0 | 65,372 | → 记忆层竞争白热化 |
| Mastra | 28,090 | ↑ Factory发布加速 |
| TrueForge | 5,669 | 🚀 <30天爆发式增长 |
| MOSS-TTS | 4,109 | ↑ Apache-2.0稀缺资源 |

---

## 📎 推荐阅读

1. **[SoK: Jailbreaking Attacks and Defenses](https://arxiv.org/abs/2609.12413)** — Agent全链路安全综述，与CVE-2026-82533直接互证
2. **[Cloud Security Alliance — Harness Sandbox Escape 研究笔记](https://labs.cloudsecurityalliance.org/research/csa-research-note-deepseek-harness-sandbox-escape-20260910-c/)** — CVE技术细节，安全团队必读
3. **[K-Bench](https://arxiv.org/abs/2609.12808)** — 20种遗忘方法全部失效的证据，合规团队必读
4. **[TAM](https://arxiv.org/abs/2609.13005)** — GPT-5真实手册任务1-15%精确匹配，评估信仰的退烧药
5. **[ZipBench](https://arxiv.org/abs/2609.12475)** — 评估成本降一个数量级，CI场景刚需

---

## 📜 本周金句

> "最终响应过滤无法阻止中间层泄露。" — SoK: Jailbreaking, 2026

Agent 安全的战场不在最后一行输出，而在中间的每一次工具调用、每一次记忆读写、每一次规划推理——以及，本周我们学到的：每一次沙箱边界突破。

---

*Generated by friday-paper-merge | Week 38, 2026 | A-D联动优先级编排*
*联动分析详情见 output/paper-os-linkage-2026-W38.md*
