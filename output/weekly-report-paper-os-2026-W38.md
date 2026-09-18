# 📄 论文-开源联动周报 — 2026-W38

> 报告周期：2026-09-14 ~ 2026-09-20
> 生成日期：2026-09-18（周五）
> 论文来源：paper-shortlist-2026-W38.md（49 篇候选 → 8 篇入选）
> 开源来源：os-shortlist-2026-W38.md（7 个项目深度扫描）

---

## 一、主题分类

### 🛡️ Agent 安全

| 论文 | 一句话 | 分数 | 代码 |
|------|--------|------|------|
| [SoK: Jailbreaking Attacks and Defenses](https://arxiv.org/abs/2609.12413) | Agent 全链路越狱攻防系统综述，三大发现重塑安全认知 | 20/25 | 🔍 待确认 |
| [K-Bench: Scoring LLM Unlearning under Agentic Deployment](https://arxiv.org/abs/2609.12808) | 首个 Agent 部署下遗忘评测基准，20 种已发表方法均无法真正移除权重中的秘密 | 19/25 | 🔍 待确认 |

**关联开源**：DeepSeek Harness（CVE-2026-82533 沙箱逃逸）是本周最直接的案例——论文中"跨层执行感知防御"的理念在 Harness 沙箱逃逸事件中得到了血淋淋的验证。OpenClaw 的 Gateway 默认绑定 127.0.0.1 也是防御纵深的一个实例。

**本周洞察**：Agent 安全正在从"审查模型输出"转向"监控执行过程"。SoK 论文发现的"低最终响应攻击成功率可掩盖严重中间层沦陷"意味着现有的安全评估方法存在系统性盲区。K-Bench 的六通道泄露检测框架提供了更完整的评估视角。

---

### 🖥️ GPU 内核与推理优化

| 论文 | 一句话 | 分数 | 代码 |
|------|--------|------|------|
| [AMDKernelVault: Open HIP and Triton Kernel Corpus](https://arxiv.org/abs/2609.12471) | 首个 AMD GPU 开源算子语料库（6.2 万 HIP + 4 万 Triton），训练 Qwen3-8B 达最优正确率 | 21/25 | ⭐ 开源 |
| [SAS: Simple Attention Sparsification via Gated Sparse Attention](https://arxiv.org/abs/2609.13141) | 门控稀疏注意力端到端优化上下文排序，紧预算下优势显著 | 19/25 | 🔍 待确认 |

**关联开源**：AMDKernelVault 与本周开源项目无直接对应，但它填补的空白正是 NVIDIA 独占的 GPU 内核生态——CUDA 有 Triton、cuBLAS、CUTLASS 等成熟工具链，AMD ROCm 生态一直缺乏等价的内核语料库和训练框架。SAS 的 Triton 内核实现思路如果被广泛采用，将进一步降低长上下文推理的硬件门槛。

**本周洞察**：推理优化正在从"模型压缩"转向"执行路径优化"——SAS 通过注入连续选择器分数到注意力 logits 实现端到端优化，而非传统的蒸馏密集注意力分布。AMDKernelVault 则代表了"用 AI 写 GPU 内核"的规模化路径。

---

### 🎯 Agent 评测与基准

| 论文 | 一句话 | 分数 | 代码 |
|------|--------|------|------|
| [ZipBench: Simple, Low-Cost Benchmark Compression](https://arxiv.org/abs/2609.12475) | 少量锚点 LLM 构建 100+ 紧凑基准，Spearman 相关 0.98，评估成本降低一个数量级 | 21/25 | ⭐ 开源 |
| [TAM: Tasks over Application Manuals](https://arxiv.org/abs/2609.13005) | GPT-5 在真实程序推理上精确匹配仅 1-15%，暴露当前基准高估推理能力 | 19/25 | ⭐ 开源 |
| [K-Bench](https://arxiv.org/abs/2609.12808) | Agent 部署下遗忘评测，秘密在 Prompt/检索库中泄露率仍达 22-86% | 19/25 | 🔍 待确认 |

**关联开源**：ZipBench 对使用 Mastra 或 TrueForge 构建 Agent 的团队有直接的实用价值——快速评估不同模型在你的具体任务上的表现，而不用跑完整基准。TAM 的发现则对 Agent 框架开发者敲响了警钟：当前 Agent 框架（ReAct、RAG）在真实世界的程序推理任务上表现远低于预期。

**本周洞察**：评测领域出现两极化趋势——ZipBench 在做"减法"（压缩现有基准），TAM 在做"加法"（暴露现有基准测不到的能力盲区）。两者的共同点是：都对当前 LLM 评测的过度乐观提出了质疑。

---

### 🧠 知识检索与推理

| 论文 | 一句话 | 分数 | 代码 |
|------|--------|------|------|
| [CoG: Cognition on Graph](https://arxiv.org/abs/2609.12791) | 免训练认知启发知识探索，图-文双向协同，7 个多跳 QA 基准超越 SOTA | 19/25 | ⭐ 开源 |

**关联开源**：CoG 的 plan-explore-reflect 认知循环与 Mem0 的多信号检索有理念上的呼应——都在解决"如何在正确的时间检索到正确的信息"。CoG 通过知识图谱提供结构化探索路径，Mem0 通过实体链接和时序推理提供记忆检索。两者结合可能是下一代 Agent 记忆+推理的架构方向。

---

### 📱 GUI Agent 与移动设备

| 论文 | 一句话 | 分数 | 代码 |
|------|--------|------|------|
| [BlueLM-GUI: Real-Device-Centric Flywheel](https://arxiv.org/abs/2609.12394) | 35B-A3B 移动端 GUI 智能体，真机训练飞轮闭环，MobileGUI-VBench 87.4 分超越最强闭源模型 5.1 分 | 20/25 | 🔍 待确认 |

**关联开源**：BlueLM-GUI 的"Every Rollout Is Real"原则与 DeepSeek Harness 的沙箱逃逸问题形成对照——在真实设备上训练 Agent 比在沙箱中训练效果好，但安全风险也更大。这提出了一个开放问题：**如何在真实环境的训练效果和沙箱的安全性之间取得平衡？**

---

## 二、联动矩阵

| 论文 ↓ | OpenClaw | DeepSeek Harness | MCP Servers | Mem0 | Mastra | TrueForge | MOSS-TTS |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **SoK: Jailbreaking** | ● | ●● | ◐ | ◐ | ◐ | ● | — |
| **AMDKernelVault** | — | — | — | — | — | — | — |
| **ZipBench** | — | — | — | — | ◐ | ◐ | — |
| **BlueLM-GUI** | ◐ | ● | — | — | — | — | — |
| **K-Bench** | ● | ● | ◐ | ● | ◐ | ● | — |
| **TAM** | — | — | — | — | ◐ | ◐ | — |
| **CoG** | — | — | — | ● | — | — | — |
| **SAS** | — | — | — | — | — | — | — |

**图例**：●● 强关联 · ● 直接关联 · ◐ 间接关联 · — 无明显关联

### 关键联动解读

**SoK: Jailbreaking × DeepSeek Harness（●● 强关联）**：论文的理论框架（跨层执行感知防御）直接适用于 Harness 的 CVE-2026-82533 事件。沙箱逃逸本质上就是一种跨层攻击——攻击者从 Agent 执行层穿透到宿主机层。论文中"最终响应过滤无法阻止中间层泄露"的发现意味着即使 Harness 的 Agent 输出看起来正常，宿主机可能已被入侵。

**K-Bench × Mem0（● 直接关联）**：K-Bench 发现在 Agent 部署中，秘密存储在 Prompt 或检索库中时泄露率高达 22-86%。Mem0 作为记忆层，其 `memory.add()` 和 `memory.search()` 接口天然处理敏感信息——如果 Agent 通过 Mem0 存储了用户隐私数据，K-Bench 的六通道检测框架可以直接用于评估 Mem0 部署的隐私安全性。

**CoG × Mem0（● 直接关联）**：CoG 的图-文双向协同探索与 Mem0 的实体链接功能在架构上高度互补。CoG 专注于多跳 QA 场景下的知识图谱探索，Mem0 专注于跨会话的记忆持久化。一个自然的集成方向是：用 Mem0 做长期记忆管理，用 CoG 做任务时的知识推理。

**ZipBench × Mastra/TrueForge（◐ 间接关联）**：使用 Mastra 或 TrueForge 构建 Agent 的团队可以用 ZipBench 的压缩基准快速评估不同模型在自己工作流中的表现，大幅降低模型选型的评估成本。

**BlueLM-GUI × DeepSeek Harness（● 直接关联）**：BlueLM-GUI 在数百台真机上进行 Agentic RL 训练，不使用沙箱。这种"真实环境训练"范式虽然效果好，但 Harness 的 CVE 事件提醒：一旦训练环境被攻破，攻击面会覆盖所有连接的设备。

**SoK: Jailbreaking × TrueForge（● 直接关联）**：TrueForge 的声明式 YAML 配置天然适合做安全策略审计——安全团队可以直接审查 Agent 的工具权限和行为边界，而不需要读 Python 代码。这正是 SoK 论文提倡的"执行感知防御"的一种实现方式。

---

## 三、双料项目详情（论文+代码）

### AMDKernelVault ⭐
- **论文**: [arXiv:2609.12471](https://arxiv.org/abs/2609.12471)
- **代码**: 语料库 + 训练代码 + 生成管线均开源
- **价值**: AMD GPU 生态的基础设施级贡献——6.2 万 HIP 内核 + 4 万 Triton 内核，执行验证，SFT+RL 训练管线
- **意义**: 打破 NVIDIA CUDA 在内核生成智能体领域的垄断

### ZipBench ⭐
- **论文**: [arXiv:2609.12475](https://arxiv.org/abs/2609.12475)
- **代码**: ZipBench Zoo 已发布，含 100+ 压缩基准
- **价值**: MAE 0.002-0.02，Spearman ~0.98，附理论误差和排名一致性保证
- **意义**: 让算力受限的研究者也能做有意义的模型评估

### TAM ⭐
- **论文**: [arXiv:2609.13005](https://arxiv.org/abs/2609.13005)
- **代码**: 数据和代码公开发布
- **价值**: 从 ICD-10-CM 临床编码和联邦量刑真实手册构建多步推理任务
- **意义**: GPT-5 精确匹配仅 1-15%——当前 LLM 推理能力的真实边界

### CoG ⭐
- **论文**: [arXiv:2609.12791](https://arxiv.org/abs/2609.12791)
- **代码**: 代码和数据集已开源
- **价值**: 免训练，7 个多跳 QA 基准超越 SOTA
- **意义**: Graph RAG 方向的高质量工作

---

## 四、趋势总结

### 本周三大信号

**1. Agent 安全从理论走向实战**
DeepSeek Harness CVE-2026-82533 不是学术练习——它影响了成千上万的生产部署。SoK 论文和 K-Bench 提供了理论框架和评估工具，但整个生态的安全实践还远远落后。预计 2026 Q4 将出现更多 Agent 安全相关的开源工具（执行监控、行为审计、沙箱加固）。

**2. 评测的"去通胀"运动**
ZipBench 压缩评估成本，TAM 暴露能力盲区，K-Bench 揭示部署风险——三篇论文从三个维度对当前 LLM 评测体系提出质疑。基准通胀（benchmark inflation）已经是一个公认的问题，2026 年下半年将出现更多"做减法"的评测工作。

**3. 记忆层成为 Agent 竞争的下一个战场**
Mem0 65k 星、Letta 21.8k 星、Graphiti 24k 星、Zep、Cognee 14.8k 星——记忆层赛道的拥挤程度已经超过 Agent 框架本身。CoG 的图-文协同探索为记忆层提供了新的技术方向，但最终的竞争壁垒可能不在算法而在数据——谁拥有更多的真实 Agent 交互数据，谁的记忆系统就更聪明。

---

*Generated by friday-report | Week 38, 2026*
*论文筛选: thursday-paper-filter | 开源扫描: friday-report deep-scan*
