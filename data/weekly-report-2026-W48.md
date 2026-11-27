# AI 开源情报周报（2026 年第 W48 周）

> 生成时间：2026-11-27（周五 19:00）
> 覆盖周期：2026-11-23 ~ 2026-11-27
> 数据来源：周三开源短名单（7 项目）+ 周四论文短名单（8 篇）
> 本周结构：**A类 5 · B类 0 · C类 3 · D类 6 · 跨界 1**
> 本周主题：**学术预警 × 真实攻击的交汇** · **记忆架构双轨推进** · **AI 优化 AI 推理**

---

## 一、论文-开源映射表（A-D 分类）

### A类：论文 + 官方代码（5 篇）— 可立即复现

| 论文 | 分数 | 官方代码 | 联动开源项目 | 联动方式 |
|------|------|---------|-------------|---------|
| MemOnce 🏆 | 24 | ✅ clare-nie.github.io/MemOnce | **claude-mem** | 原生记忆架构（末层隐状态缓存，1313× 削减，1M 上下文活跃缓存仅 25MB）↔ 工程侧记忆层事实标准——学术从架构层突破，工程从系统集成层落地 |
| MASSys 🏆 | 23 | ✅ github.com/MAS-Sys-Bench/MAS-Sys | **OpenHands / Sim** | "同一 workflow 换 serving 环境排名从第 1 跌到第 4"直接警示所有 Agent 编排平台——评测结果不可跨环境迁移，"评测基质"必须成为平台报告的一部分 |
| LongCat LRSA 🏆 | 23 | ✅ 已合并入 SGLang 主干 | **SpecPilot** | 稀疏注意力（1024K 实测）↔ Agentic Loop 推理自优化——推理加速的"人类架构派"与"AI 自搜索派"殊途同归，且都作用于 SGLang 推理栈 |
| VeriLadder | 22 | ✅ 数据集+微调模型公开 | — | EDA 工具链自动验证 716K 数据，RTLLM 31.7→50.0——垂直领域护城河在数据管线而非模型规模 |
| RI-Bench | 20 | ✅ 代码+数据双公开 | **claude-mem / OpenHands** | 12,000 episode 角色完整性基准——测 Agent 在权威压力与利益诱惑下是否越权，可作为 Agent 平台的"出厂安全检测" |

### B类：论文 + 社区复现（0 篇）

连续第五周空缺（W44–W48 均为 0）。放码策略两极分化已固化：要么官方随论文直接放码（A类），要么干脆不放等社区（C/D类），中间态消失。

### C类：论文先行（3 篇）— 代码未随论文发布

| 论文 | 分数 | 对应方向 | 跟进建议 |
|------|------|---------|---------|
| ROGUE-AI 🏆 | 21 | Agent 安全事件复现审计 | **本周最重要论文**。108 起安全事件系统化复现，89% 无需攻击者在场即可重现危害——11/4 学术警告，11/17 MS Agent Framework 投毒事件精确兑现。代码释放后应作为 CI/CD 发布前的自审计工具 |
| S-Mind | 21 | 空间智能内化 | 4B 模型打平 GPT-6-Astra、比工具型 Agent 快约 100 倍，**且反超 Kimi-K3.1-Pro 1.97 分**——空间 token 内化几何直觉的路线开始兑现，关注代码释放与训练方案 |
| Insider Attack | 20 | 多智能体辩论内部人攻击 | 无需提示注入即可操纵辩论结论，攻击随辩论轮数自我强化——对一票否决式决策系统威胁直接，关注防御方案 |

### D类：项目先行（6 个）— 暂无对应论文

| 项目 | 类别 | Stars | 一句话 |
|------|------|-------|--------|
| Kimi K3.1 Pro | 开源模型 | — (HF) | 2.8T MoE + 104B active + 1M context，AA Index v5 得分 46 登顶 open-weight 榜首 |
| caveman | Skill 生态 | ~119K | Token 压缩率 78%，sub-100 line skills 方法论成为 Skill 设计范式 |
| claude-mem | Agent 记忆层 | ~116K | Claude Code 原生记忆层事实标准，L0–L5 分级防护 |
| OpenHands v1.40.0 | Agent 框架 | ~93.4K | Agent Canvas 集成 20+ 主流编码 Agent，进化为开发者控制中心 |
| Microsoft Agent Framework | Agent 框架 | ~14.6K | AutoGen+SK 统一后的企业级首选，本周遭遇 PyPI 供应链投毒 |
| Sim | Agent 工作区 | ~30.1K | 可视化 Agent 构建 + 270+ 集成 + MCP 协议 + 工作流即代码 |

### 跨界（1 个）

**SpecPilot**——同时出现在开源短名单（GitHub StargazerX0/SpecPilot）和 arXiv 论文（11/4），罕见的"论文+代码"同步交付的推理优化项目：Claude Opus 5.5 in Claude Code 三轮自主迭代，将 Qwen3.8-27B 的 DFlash2 投机解码从 184 tok/s 提升至 416 tok/s，RTX PRO 6000 综合加速 10.87×。

---

## 二、本周最强联动

**ROGUE-AI（学术预警 Agent 安全风险）× Microsoft Agent Framework 供应链投毒（真实攻击）**

论文 11/4 发表（108 起安全事件审计，89% 可自主复现），攻击 11/17 发生（PyPI 包被注入凭据窃取器，~190K 月下载量暴露约 45 分钟）——同一周内学术诊断被现实验证。ROGUE-AI 的核心发现"多数危害 Agent 自己就能造成，不需要攻击者"在投毒事件中精确兑现：恶意 `.pth` 文件在每次 Python 启动时自动执行，无需任何用户交互。

**这不是巧合，是 Agent 生态成熟度到达临界点后的必然**：当 ~190K 月下载量的企业级 SDK 成为攻击目标，安全审计必须从"可选"变为"必选"，从外挂变内建。

---

## 三、A类深度：论文 × 开源的直接影响

### 3.1 记忆双轨：MemOnce（架构派）↔ claude-mem（工程派）

本周记忆赛道出现罕见的学术-工程正面对照：

- **MemOnce**（24/25，本周最高分）：记忆编码解码架构只缓存末层隐状态，1M 上下文下缓存削减 1313×、预填充提速 6.9×，Qwen3.5-4B 活跃缓存恒定在 25MB（对比 Transformer 32GB+）。零样本泛化到下游表征任务，预训练+后训练双范式验证。需要重训模型，路线根本但门槛高。
- **claude-mem**（~116K ⭐）：应用层方案——结构化 Markdown + Obsidian 知识图谱模拟记忆，即插即用，11/14 发布 L0 防护机制（$1.9M 修复成本），但 Issue #5910 独立审计确认目前无 Claude Agent SDK 集成，依赖非官方 hook，兼容性风险实质存在。

**判断**：短期内 claude-mem 路线更实用（无需碰模型），长期 MemOnce 路线更根本。但当 LongCat LRSA 这类推理层稀疏注意力普及时，应用层记忆工具的价值命题需要重新校准——如果推理框架原生支持 1024K 高效上下文，"外挂记忆层"的刚需会被稀释。

### 3.2 评测有效性危机：MASSys 给 OpenHands/Sim 的当头棒喝

MASSys 的核心发现——同一 workflow 换 serving backend 排名从第 1 跌到第 4（vLLM/SGLang/Continuum/Orla 四套基质 × 负载扫描）——直接打击当前 Agent 平台的评测叙事：OpenHands 的 93.5K ⭐、Sim 的 30K ⭐、排行榜上的跑分，都依赖特定 serving 环境。**"评测结果是执行条件的函数"意味着 agent benchmark 的分数不可跨环境迁移**，平台宣传口径中的数字必须附带基质声明。

### 3.3 推理加速两派会师 SGLang：LRSA × SpecPilot

- **LongCat LRSA**：稀疏注意力只保留 recall 所需 token，稀疏索引跨层共享，1024K 为目前开源实现中最长实测档位之一——已合并入 SGLang 主干（非外挂，这是代码质量的最强背书）。
- **SpecPilot**：Agentic Loop 自主发现推理优化策略，W12 无损 12-bit 权重格式（GEMM 寄存器内逐位精确解码 BF16，加速 1.15–1.26×），三轮迭代瓶颈从 token 数→权重字节→kernel 效率逐轮转移。

两派在同一周推进且都作用于 SGLang 推理栈。当 AI 开始优化 AI 的基础设施，优化循环本身就在加速。

---

## 四、C类深度：论文先行，代码待放

三篇 C 类全部聚焦 Agent 安全，这在 W48 不是偶然：

1. **ROGUE-AI**（21/25）：审计框架把"事件报告"变成"可执行复现脚本"，五类主流 agent 全覆盖。可直接用作厂商发布前自审计流程。Auburn + Texas A&M（Nitesh Saxena 组）。
2. **S-Mind**（21/25）：空间探针先诊断 MLLM 两个根本缺陷（多视图融合恢复率最高 16.02%、视角变换 37.28%），训练后分别达 65.11% 和 82.17%；抽掉空间 token 能力只掉 2.37 分——几何真被内化而非提示工程。4B 超 Kimi-K3.1-Pro 1.97 分。Shuicheng Yan + Bo An。
3. **Insider Attack**（20/25）：攻击者只输出与普通 agent 无异的中间论点，完全无恶意提示痕迹；学习+规划两阶段让攻击随辩论轮数自我强化——多智能体安全的"内部威胁"角度此前少有形式化。

**安全论文代码释放谨慎是合理的**（防攻击手法滥用），但也正因如此，D 类项目必须自建安全能力——本周 MS Agent Framework 的遭遇证明，等学术方案成熟再放码，窗口期早就过了。

---

## 五、D类深度：项目先行

### 5.1 Microsoft Agent Framework PyPI 供应链投毒 —— 2026 年 AI 工具链最严重安全事件

**来源**: [Orca Security](https://orca.security/resources/research/microsoft-agent-framework-pypi-supply-chain-attack-versions-1-26-1-and-1-26-2-steal-cloud-credentials/) · [Chainguard](https://www.chainguard.dev/unchained/microsoft-agent-framework-compromised-on-pypi-november-2026) · [Aikido](https://www.aikido.dev/blog/two-malicious-agent-framework-releases-hit-pypi-in-33-minutes) · [StepSecurity](https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised) · 攻击日期 2026-11-17
**License**: MIT（框架本体）| **Stars**: ~14.6K ⭐ | **包**: `agent-framework` on PyPI（~190K 月下载）

**时间线**：

| 时间 (UTC) | 事件 |
|-----------|------|
| 11/12 | 1.26.0 正常发布（最后一个干净版本，支持 Python 3.14） |
| 11/17 20:35 | **1.26.1 上传 PyPI**——内含凭据窃取器 |
| 11/17 20:36 | Chainguard 扫描器 48 秒内自动阻断 |
| 11/17 21:06 | PyPI 隔离 1.26.1 |
| 11/17 21:08 | **1.26.2 上传**——隔离后 2 分钟攻击者再次发布，载荷升级 |
| 11/17 ~21:20 | 暴露窗口关闭，总时长约 45 分钟 |

**攻击手法——.pth 启动钩子**：恶意代码藏在 `.pth` 文件中，Python 解释器启动时自动处理——无论是否 import agent_framework，窃取器每次启动都运行。窃取目标直指 AI 开发链：Azure/GitHub/AWS/HF/OpenAI 凭据、云身份 token（9 种 Azure 资源类型）、`/proc/<pid>/environ` 进程环境变量。外渗用 zlib+base64 经 HTTPS POST 到 webhook.site。

**三个结构性警示**：
1. **可信发布者 ≠ 可信发布**——恶意版本通过 Microsoft 关联账号上传，是账号被盗而非仿冒包
2. **.pth 手法持续有效**——继 10 月 LiteLLM 1.107.0 后第二次，lockfile 中一个未使用的依赖就是一个活的窃取器
3. **AI 构建链成为靶心**——模型访问权限 + 云消费额度 = 攻击者的双重动机

### 5.2 OpenHands v1.40.0 — 从编码 Agent 到开发者控制中心

**仓库**: [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) · **License**: MIT · **Stars**: ~93.5K ⭐
**发布**: v1.40.0（11/12），截至本周已迭代至 v1.45.0

核心变化是重新定位：Agent Canvas 统一调度 OpenHands 原生 Agent、Claude Code、Codex、Gemini CLI 等任意 ACP 兼容 Agent；Docker 沙箱执行 + 多后端并行 + Automations（定时/Webhook 触发，GitHub 新 Issue → 自动分析 → PR 草稿 → Slack 通知）。

**为什么重要**：93.5K ⭐ + MIT + 每周迭代。"单个 Agent 的能力已被充分探索，下一个战场是如何管理多个 Agent"——OpenHands 管执行、Sim 管编排、claude-mem 管记忆，三个项目共同勾勒出 Agent 基础设施的三层分工。

**风险**：迭代极快 API 频繁变化；macOS 应用未签名；生产环境 `latest` 标签有版本漂移风险；多 Agent 编排的权限边界需额外审查——尤其在本周投毒事件背景下。

### 5.3 Sim (simstudioai/sim) — 30K 星 Agent 协作工作区

**仓库**: [simstudioai/sim](https://github.com/simstudioai/sim) · **License**: Apache 2.0 · **Stars**: ~30.1K ⭐ · **版本**: v9.63（11/19）

可视化拖拽编排 + 270+ 集成 + MCP 协议支持 + v9.63 新增"工作流即代码"。11/19 一天发一个版本，此前四天五版。本周还发布了从 OpenAI Agent Builder 迁移的指南（后者 11/30 关停）——平台洗牌期积极吸收流离用户。

**信号**：可视化编排与代码定义正在融合而非对立；Dify 偏开发者/API 优先，Sim 偏可视化/协作优先，差异化竞争清晰。

### 5.4 caveman — 119K 星 Skill 生态标杆：给 AI 做减法

**仓库**: [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) · **License**: MIT · **Stars**: ~119K ⭐

Rules 仅 ~1,160 tokens，78% token 压缩率，双模式 `/caveman`（减 3%）/ `/ultracave`（砍 35%）。Skill Leaderboard 居首，压过众多大厂出品。

**对照**：W47 的 stitch-skills（Google 官方 15 技能套件）vs caveman（个人 1,160 tokens 规则集），星数后者 18 倍。多数开发者不需要 15 个技能，需要一个"装了就能用、不占上下文"的默认配置——过度工程化被一记耳光。

### 5.5 claude-mem — 116K 星记忆层与它的 L0 防护

**仓库**: [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) · **License**: MIT · **Stars**: ~116K ⭐ · **版本**: v15.16.1

11/14 发布 L0 防护机制（$1.9M 修复成本），L0–L5 分级方案获独立测评认可。Issue #5910 独立审计确认 v15.16.1 无 Claude Agent SDK 集成——依赖非官方 hook，Claude Code 任何更新都可能破坏兼容性。十天七个补丁版本。

### 5.6 Kimi K3.1 Pro — 最强开源权重的"API 经济学"

**来源**: [Hugging Face](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · [Morph 实测](https://www.morphllm.com/kimi-k3-1) · 权重 11/2 上架
**架构**: 2.8T MoE（896 experts，top-16）· 104B active · 1M token 上下文 · 原生 MXFP4

本周关键数据：API 定价 $2/$10（cached input $0.20）；Terminal-Bench 4.0 得分 65.7 vs Claude Opus 5.5 的 66.4（差距不到 1 分）；AA Index v5 得分 46 登顶 open-weight 榜首。

**成本数学**：月 10 亿 token 调用，API 约 $12K–60K；自托管至少 8×H100 月成本远超 $50K——API 是唯一经济选择（除非数据主权/合规需求）。

**注意论文侧信号**：S-Mind（C类）4B 模型反超 K3.1-Pro 1.97 分——虽是在特定空间任务上，但"小模型内化专业能力超通用大模型"的先例值得持续追踪。

**四周叙事弧**：W45 落地 → W46 现实检验 → W47 社区接力（Unsloth GGUF 1,509 GB）→ W48 经济学确立。"技术奇迹"正在变成"经济选择"。

### 5.7 SpecPilot — AI 优化 AI 推理：Agentic Loop 自主发现 10.87× 加速

**仓库**: [StargazerX0/SpecPilot](https://github.com/StargazerX0/SpecPilot) · **论文**: [arXiv 2611.02501](https://arxiv.org/abs/2611.02501)（11/4）

Claude Opus 5.5 in Claude Code 多轮自主迭代：分析瓶颈 → 提出方向 → 实现补丁 → 配对运行验证 → 晋级。Token forcing 验证防 reward hacking。W12 无损 12-bit 权重格式（四轮部署中最大单一贡献）。

| 部署 | 加速比 | 解码速度 |
|------|--------|---------|
| Qwen3.8-27B + DFlash2, H100 | 2.13× | 184→416 tok/s |
| Qwen3.8-27B + DSpark, H100 | 2.38× | 173→435 tok/s |
| Muse-Glimmer-30B + DFlash2, RTX PRO 6000 | 2.21× | 111→256 tok/s |
| **RTX PRO 6000 综合（5 项基准）** | **10.87×** | — |

端到端演示：PEAR 机器人推理，SpecPilot + efficient reasoning 49.2 秒 vs 基线 188.7 秒（3.84×）。

**风险**：<100 ⭐ 新项目未经社区检验；kernel 绑定 sm_120a 特定架构；Agent 自主优化的可解释性有限；单部署 20–86 GPU-hours 的优化成本本身不低。

---

## 六、数据观察

### 论文代码开放率：5/8（62.5%），连续两周稳定

| 周 | A类 | C类 | 开放率 |
|---|-----|-----|--------|
| W46 | 3 | 5 | 37.5% |
| W47 | 5 | 3 | 62.5% |
| W48 | 5 | 3 | 62.5% |

C 类 3 篇均涉安全方向——安全论文代码释放通常更谨慎（防滥用），是合理的不释放理由。

### Agent 安全研究占比：3/8（37.5%），历史新高

周四 8 篇论文中 3 篇聚焦 Agent 安全（ROGUE-AI / Insider Attack / RI-Bench），加上开源侧 MS Agent Framework 投毒——**"Agent 安全"首次同时占据开源和学术两个维度的最大权重**。Agent 部署量到达临界点后的必然。

---

## 推荐阅读

1. **[Microsoft agent-framework compromised on PyPI（Chainguard, 11/17）](https://www.chainguard.dev/unchained/microsoft-agent-framework-compromised-on-pypi-november-2026)** — 最完整技术分析：.pth 手法、窃取目标清单、48 秒自动阻断决策逻辑、"可信发布者 ≠ 可信发布"
2. **[Two malicious agent-framework releases hit PyPI in 33 minutes（Aikido）](https://www.aikido.dev/blog/two-malicious-agent-framework-releases-hit-pypi-in-33-minutes)** — 逐分钟攻击时间线，两轮载荷差异分析
3. **[Microsoft agent-framework PyPI Supply-Chain Attack（Orca Security）](https://orca.security/resources/research/microsoft-agent-framework-pypi-supply-chain-attack-versions-1-26-1-and-1-26-2-steal-cloud-credentials/)** — 影响面评估与 IOC 清单
4. **[SpecPilot 论文（arXiv 2611.02501）](https://arxiv.org/abs/2611.02501)** — Agentic Loop 自主推理优化完整方法论，W12 格式细节，三轮迭代瓶颈转移分析
5. **[OpenHands v1.40.0 从安装到自动化（腾讯云开发者社区, 11/16）](https://cloud.tencent.com/developer/article/2785331)** — Agent Canvas 四种安装方式场景化指南
6. **[Sim 平台能力评测（Rank Agents, 11/20）](https://rankagents.app/blog/sim-review)** — v9.63 新特性分析

---

*由 friday-paper-merge 任务生成 | intelligence-system*
*数据源：data/paper-shortlist-2026-W48.md + data/os-shortlist-2026-W48.md*
*分类统计：A5 · B0 · C3 · D6 · 跨界 1*
