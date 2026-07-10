# AI 开源周报 · 2026-W28

> **周报期数**：2026-W28  
> **覆盖周期**：2026-07-06 至 2026-07-10  
> **生成时间**：2026-07-10  
> **数据来源**：GitHub Trending、Hugging Face、arXiv、技术媒体交叉验证  
> **短名单来源**：周三深度筛选（7/8）

---

## 一、本周重磅推荐

### 🏆 OpenMontage — 全球首个开源 Agentic 视频制作系统

| 属性 | 详情 |
|------|------|
| **作者/组织** | calesthio |
| **GitHub** | github.com/calesthio/OpenMontage |
| **实时 Star** | ~23K+（单日 +3,434 ⭐） |
| **许可证** | MIT |
| **领域** | Agentic 视频制作 |

OpenMontage 不只是一个视频生成工具，而是一套**完整的 Agentic 视频制作系统**。它让 AI 编码助手（Claude Code、Cursor、Copilot、Codex 等）能够协调从创意、脚本、素材生成、剪辑、字幕到最终渲染的全流程。

**核心亮点：**
- **12 条制作管线**：覆盖教程、社交媒体、演示文稿、纪录片等不同视频类型
- **52 个工具 + 500+ Agent 技能**：从脚本生成到 Remotion 合成，全链路覆盖
- **真实素材支持**：不仅支持 AI 生成，还能调用 Archive.org、NASA、Wikimedia、Pexels 等免费素材库制作"真正的视频"
- **成本极低**：官方示例中，60 秒 Pixar 风格动画短片《The Last Banana》总成本仅 **$1.33**

**为什么重要：**
OpenMontage 代表了 AI 视频从"单点生成工具"向"端到端生产系统"的跃迁。它不是用更好的模型生成更好的片段，而是用 Agent 协调整个制作流程——这是内容生产范式的根本转变。

---

## 二、工具框架类

### 1. SkillSpector — NVIDIA 出品的 Agent Skill 安全扫描器

| 属性 | 详情 |
|------|------|
| **作者/组织** | NVIDIA |
| **GitHub** | github.com/NVIDIA/skillspector |
| **实时 Star** | ~10.7K+ |
| **许可证** | Apache 2.0 |
| **领域** | Agent 安全 |

**核心能力：**
- 检测 **68 种攻击模式**，覆盖 17 个类别：提示注入、反拒绝、数据外泄、权限提升、供应链攻击、过度代理、系统提示泄露、记忆投毒、工具滥用等
- **两阶段分析管线**：第一阶段静态分析（regex、AST、YARA、OSV.dev CVE 查询），第二阶段可选 LLM 语义分析
- 基于对 **42,447 个真实 Skill** 的大规模实证研究
- 输出 SARIF 格式，可直接集成 GitHub Code Scanning 和 CI/CD 流水线
- 风险评分 0-100，自动给出 SAFE / CAUTION / DO NOT INSTALL 建议

**一句话评价：**
Agent 生态正在经历从"野蛮生长"到"安全治理"的拐点，SkillSpector 是这个拐点上的标志性工具。它不解决所有问题（动态威胁、时间炸弹 URL 仍需运行时防护），但把"安装前安全检查"这件事做到了当前最全面。

---

### 2. headroom — AI Agent 上下文压缩层

| 属性 | 详情 |
|------|------|
| **作者/组织** | headroomlabs-ai |
| **GitHub** | github.com/headroomlabs-ai/headroom |
| **实时 Star** | ~10K+ |
| **许可证** | MIT（实际为 Apache-2.0，见仓库） |
| **领域** | Context 压缩 |

**核心能力：**
- **60-95% token 削减**：在保持回答质量的前提下压缩 tool outputs、logs、RAG chunks、files、对话历史
- **本地优先架构**：所有压缩在本地运行，数据不出境
- **可逆压缩（CCR）**：原始内容本地缓存，LLM 可随时调用 `headroom_retrieve` 获取完整内容
- **多形态部署**：Library（Python/TypeScript SDK）、Proxy（零代码 `headroom proxy --port 8787`）、MCP Server、`headroom wrap` 一键包裹主流 Agent 工具
- **跨 Agent 记忆共享**：Claude、Codex、Cursor、Aider 等会话间自动去重共享上下文
- **`headroom learn`**：自动挖掘失败会话，将修正写入 `CLAUDE.local.md` 等规则文件

**一句话评价：**
Context 压缩不是"少发点 token"的省钱技巧，而是 Agent 规模化后的基础设施问题。headroom 把这个基础设施做成了一个完整的层次——从压缩算法到部署形态到记忆共享，思路非常完整。

---

### 3. Agent-Reach — 让 AI Agent 一键触达全网

| 属性 | 详情 |
|------|------|
| **作者/组织** | Panniantong |
| **GitHub** | github.com/Panniantong/agent-reach |
| **实时 Star** | ~48K+ |
| **许可证** | MIT |
| **领域** | 终端工具 / Agent 能力层 |

**核心能力：**
- **13+ 平台覆盖**：Twitter/X、Reddit、YouTube、GitHub、Bilibili、小红书、LinkedIn、Instagram、Facebook、V2EX、雪球、小宇宙播客等
- **零 API 费用**：使用轻量级爬虫和公开搜索方法，无需付费 API Key
- **智能后端路由**：每个平台配置"首选 + 备选"后端列表，某接入方式失效自动切换（如 yt-dlp 被 B 站风控后自动切到 bili-cli）
- **一句话安装**：复制安装链接给 Agent，几分钟内完成环境配置
- **内置诊断**：`agent-reach doctor` 一键检测各平台连通状态

**一句话评价：**
Agent-Reach 解决了一个看似简单但极其繁琐的问题：让 Agent 真正能"上网"。它不是又一个爬虫工具，而是**能力层（capability layer）**——比任何具体实现高一层，负责选型、安装、体检、路由。设计哲学很干净。

---

### 4. oh-my-pi — 终端原生 AI 编码 Agent

| 属性 | 详情 |
|------|------|
| **作者/组织** | can1357 |
| **GitHub** | github.com/can1357/oh-my-pi |
| **实时 Star** | ~9.3K+ |
| **许可证** | GPL-3.0 |
| **领域** | 终端 IDE / 编码 Agent |

**核心能力：**
- **IDE 级能力内嵌**：LSP（14 种操作）、DAP（28 种操作）直接接入 Agent，支持重命名、查找引用、断点调试等语义操作
- **Hashline 编辑**：基于内容哈希的锚点编辑，Grok 4 Fast 输出 token 减少 61%，编辑成功率从 6.7% 提升到 68.3%
- **~55,000 行 Rust 核心**：搜索、Shell、AST、高亮、PTY、图像解码、BPE 计数全部原生实现，热路径无 fork/exec
- **40+ 模型提供商**，32 个内置工具
- **Hindsight 记忆**：跨会话记忆代码库，项目级知识持久化
- **第一级子 Agent**：`task` 命令支持分派隔离工作树，返回结构化结果

**一句话评价：**
oh-my-pi 是 Pi 项目的一个深度 fork，但已经演化成完全不同的东西。它不是"在终端里装一个 Copilot"，而是把完整的 IDE 能力搬进了一个终端原生 Agent。Hashline 编辑和 LSP/DAP 集成是真正有技术深度的创新。

---

## 三、模型与算法类

### 5. GLM-5.2 — 753B MoE 开源权重模型

| 属性 | 详情 |
|------|------|
| **作者/组织** | Z.ai（智谱） |
| **模型页面** | HuggingFace: zai-org/GLM-5.2 |
| **许可证** | MIT |
| **领域** | 开源大语言模型 |

**核心规格：**
- **753B 总参数**，MoE 架构，每 token 激活 40B 参数
- **1M token 上下文窗口**，最大输出 128K
- **IndexShare 注意力优化**：每 4 层共享一个稀疏注意力索引器，1M 上下文下每 token 计算量减少 2.9 倍
- 支持 High / Max 两种推理深度模式

**关键基准：**
| 基准 | GLM-5.2 | 对比 |
|------|---------|------|
| FrontierSWE | 74.4% | Claude Opus 4.8: 75.1%, GPT-5.5: 72.6% |
| AIME 2026 | 99.2% | 较前版提升 3.9 个点 |
| SWE-bench Pro | ~62.1% | 开源模型领先水平 |

**API 定价：**
- Input: $1.4 / M tokens
- Output: $4.4 / M tokens
- 约为 GPT-5.5 / Claude Opus 的 **1/4 到 1/6**

**一句话评价：**
GLM-5.2 的发布时间点（Claude Fable 5 被美国政府限制后几小时）和 MIT 许可证（无区域限制）都带有明确的战略意图。但抛开地缘政治，它确实是当前**开源模型中最接近前沿水平的存在**——不是每一项都第一，但综合上下文长度、代码能力、成本和开放性，它是 2026 年最值得严肃评估的开源模型。

---

### 6. SkillOpt — 冻结 LLM 的文本空间 Skill 优化器

| 属性 | 详情 |
|------|------|
| **作者/组织** | Microsoft Research |
| **GitHub** | github.com/microsoft/SkillOpt |
| **实时 Star** | ~4.1K+ |
| **许可证** | MIT |
| **领域** | Agent 优化 |

**核心创新：**
- **不修改模型权重**，而是将自然语言 Skill 文档视为可训练的外部参数
- **完整深度学习训练循环**：epoch、mini-batch、learning rate、momentum、validation gate 全部在文本空间中实现
- **52/52 全胜**：在 6 个基准、7 个目标模型、3 个执行框架（直接对话、Codex CLI、Claude Code CLI）的所有组合中取得最佳或并列最佳
- **GPT-5.5 提升**：直接对话 +23.5 点，Codex 循环内 +24.8 点，Claude Code 内 +19.1 点
- **零推理时成本**：训练完成后仅保留 `best_skill.md`（通常 300-2000 tokens），可跨模型、跨框架部署

**训练循环：**
Rollout（执行）→ Reflect（分析轨迹）→ Aggregate（合并补丁）→ Select（筛选编辑）→ Update（更新 Skill）→ Evaluate（验证门控）

**一句话评价：**
SkillOpt 可能是 2026 年最重要的 Agent 研究之一。它解决了一个根本问题：如何系统性地提升 Agent 性能，而不需要微调模型或依赖人工 prompt engineering。"训练 Skill 而不是训练模型"这个思路一旦普及，Agent 的能力天花板会被彻底重新定义。

---

## 四、数据观察

### 本周 Star 增长趋势

| 项目 | 当前 Star | 本周增长 | 增长率 | 热度评级 |
|------|-----------|----------|--------|----------|
| Agent-Reach | ~48K | 显著 | 高 | 🔥🔥🔥 |
| OpenMontage | ~23K | +3,434 | 极高 | 🔥🔥🔥 |
| headroom | ~10K | 稳步 | 中高 | 🔥🔥 |
| SkillSpector | ~10.7K | 稳步 | 中 | 🔥🔥 |
| oh-my-pi | ~9.3K | 稳步 | 中 | 🔥🔥 |
| SkillOpt | ~4.1K | 从 303 飙升 | 爆发 | 🔥🔥🔥 |
| GLM-5.2 | N/A (权重) | N/A | N/A | 🔥🔥🔥 |

### 趋势解读

**1. Agent 基础设施成为主战场**
本周 7 个项目中有 6 个直接服务于 Agent 生态（安全、压缩、联网、编码、优化）。Agent 不再是"一个能聊天的模型"，而是一个需要完整工具链支持的工程体系。

**2. "不碰模型权重"成为新范式**
headroom（上下文压缩）、SkillOpt（Skill 优化）都在证明：不修改模型、不微调权重，也能大幅提升 Agent 表现。这意味着 Agent 能力的提升路径正在从"模型中心"转向"系统工程中心"。

**3. 中国开源模型进入第一梯队**
GLM-5.2 的发布标志着中国实验室在前沿开源模型竞争中已经不再是"追赶者"，而是"并跑者"。MIT 许可证 + 1M 上下文 + 商用级 API 定价，组合起来的竞争力不容小觑。

**4. 安全从"可选项"变成"必选项"**
SkillSpector 的出现和 NVIDIA 的背书说明：Agent Skill 的安全扫描正在从社区自发工具升级为行业基础设施。26.1% 的 Skill 含有漏洞、5.2% 存在恶意意图——这个数字会推动更多企业和平台强制实施安装前安全检查。

---

## 五、推荐阅读

### 技术文章

1. **[Context compression for AI agents: how Headroom cuts token costs](https://karvedigital.com/en/insights/context-compression-for-ai-agents)** — 深入解析上下文压缩的技术原理和 Headroom 的实现细节
2. **[NVIDIA SkillSpector: The Scanner That Proved AI Skills Security Needs More Than Static Analysis](https://www.tech86.com.br/en/blog/nvidia-skillspector-seguranca-skills-ia)** — 对 SkillSpector 能力边界和结构性局限的诚实评估
3. **[GLM-5.2 Is Here: Z.ai's 753B Open Model Built for Long-Horizon Agentic Work](https://www.toolmintx.in/blog/glm-5-2-zai-long-horizon-agentic-model)** — 全面的 GLM-5.2 技术解读，含 VRAM 计算和实际部署建议
4. **[Microsoft SkillOpt: 52 Out of 52 Wins with the Skill Optimizer](https://pasqualepillitteri.it/en/news/3452/skillopt-microsoft-text-space-optimizer-agent-skills-en)** — SkillOpt 研究结果的深度分析

### 项目文档

5. **[OpenMontage Agent Guide](https://github.com/calesthio/OpenMontage/blob/main/docs/AGENTS.md)** — 如何让 AI 编码助手在 OpenMontage 中工作
6. **[SkillOpt Paper (arXiv:2605.23904)](https://arxiv.org/abs/2605.23904)** — 文本空间优化的原始研究

### 本周语录

> "The most rigorous scanner in the world does not protect against what changes after inspection."  
> — tech86.com.br 对 SkillSpector 的点评

> "GLM-5.2 is Fully Open, Frontier Intelligence Belongs to Everyone."  
> — Z.ai 官方发布语

---

*本报告由情报系统自动生成。数据截至 2026-07-10，部分实时数据可能存在延迟。*
