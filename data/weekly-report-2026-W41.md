# AI开源情报周报 | 2026-W41

> 报告周期：2026-10-05 至 2026-10-11（周五截取）
> 生成时间：2026-10-09 17:00 CST
> 数据来源：论文精选（8篇，46候选，入选率17.4%）+ 开源精选（7个，12候选）
> 联动分析：output/weekly-report-paper-os-2026-W41.md
> 项目 Star 数据：GitHub API 实时（2026-10-09 17:05 CST）

---

## 📋 本周概览

| 维度 | 数据 |
|------|------|
| 精选开源项目 | 7 个（12 候选） |
| 精选论文 | 8 篇（46 候选，入选率 17.4%） |
| 入选项目总 Star | 556,197（周五 17:05 实时） |
| 论文+代码双料 | 5 个（AgentDiscover / RealCompanion / TeleTune / SciUtopia / Science or Slop） |
| A类强关联 | 2 对 |
| B类中关联 | 5 对 |
| D类项目先行 | 7 个 |
| 本周最热话题 | Agent 成本三重压缩 · 记忆基准纠偏 · 内核级安全 |

**本周关键词**：成本压缩 · 持久记忆 · 内核安全 · 本地推理 · 反 AI slop

**本周一号事件**：Agent 编程的单位经济学被三方同时重写——caveman 从输入侧砍掉 33.2% token、ponytail 从生成侧砍掉 53% 代码和 45% token、claude-mem 从记忆侧消灭重复上下文。三个独立项目、三种技术路线，同一个目标：**让 Agent 编程的每一美元产出更多**。这不是巧合——Agent 工具链正在从"能用"跨越到"用得起"，而成本压缩一旦成为主流认知，就再也回不去了。

---

## 🏆 A类：论文+官方代码（强关联，优先关注）

### A1 | RealCompanion：真实对话揭穿合成记忆基准虚高
- **论文**：https://arxiv.org/abs/2610.01780（21/25）
- **代码**：✓ 数据 OSF (x25kj) + 代码 anonymous.4open.science
- **评分**：21/25（创新5 | 实用4 | 深度4 | 背书4 | 代码4）
- **关联项目**：claude-mem（⭐⭐⭐ 记忆系统的现实检验）/ ponytail（⭐⭐ 长会话中的上下文管理）
- **一句话**：首个 120 天真实人机伴侣对话基准（27,218 条消息），核心发现刺痛整个记忆 Agent 赛道——真实对话中仅 3.4% 的消息依赖历史，但当依赖发生时，所需消息平均在 2,157 条之外。看最近消息的策略 95.9% 时候够用，关键 2.2% 时候彻底失效。
- **⚡ 为什么本周最重要**：claude-mem 代表的跨会话记忆系统是整个 Agent 工具链最热的基础设施方向之一（98K★），但此前所有记忆评测都在合成 persona 上跑。RealCompanion 用真实数据证明：合成基准的分数需要打折看，真实场景的长距离依赖远比实验室中稀疏且关键。这对 claude-mem 的设计哲学（什么该记、什么该压、什么该丢）是直接输入——95.9% vs 2.2% 的分布意味着记忆压缩策略的优化空间巨大，但 2.2% 的致命性意味着不能只优化期望值。

### A2 | TeleTune：从真实产品遥测演进 Agent 技能
- **论文**：https://arxiv.org/abs/2610.05437（20/25）
- **代码**：✓ 项目页 microsoft-teletune.github.io（Microsoft Research）
- **评分**：20/25（创新4 | 实用5 | 深度4 | 背书4 | 代码4）
- **关联项目**：ponytail（⭐⭐ 工作流优化）/ claude-mem（⭐⭐ 行为捕获反哺技能演进）
- **一句话**：从离线用户遥测自动挖掘并演进计算机操作 Agent 技能，已部署于真实产品流量——技能演进这条线（TeleTune + ASCENT + Mining Agent Skills）本周三篇齐发。
- **⚡ 信号**：与 ponytail 的"重建后效率飙升"互为因果——ponytail 证明 AI 写代码可以砍掉 53% 的冗余，TeleTune 回答"砍掉的模式从哪学"：不是人工标注，是真实用户的操作遥测。两者共同指向：**部署轨迹本身就是训练资产**。ponytail 的 -53% code 是结果，TeleTune 是产生这种结果的系统化方法。

---

## 🔗 B类：论文+社区复现（中关联，关注落地）

### B1 | Suppressed Safety Features：你检查不到的东西恰好是安全回路
- **论文**：https://arxiv.org/abs/2610.05541（19/25）
- **代码**：✗ 未确认
- **评分**：19/25（创新5 | 实用4 | 深度5 | 背书3 | 代码2）
- **关联项目**：OpenShell（⭐⭐⭐ 内核级安全验证的理论基础）
- **一句话**：现有机械可解释性工具只看激活特征，本文提出 CAP（反事实激活势）与 CSFD 算法，专挖"被抑制"的非激活安全特征——它们不在激活值里露头，但消融后拒绝行为翻转为遵从。覆盖 Gemma / Qwen / Llama 五个模型。
- **判断**：OpenShell 用内核级强制执行 + 策略变更形式化验证解决的是"运行时安全"，本文揭示的是"模型内部安全回路的可审计性"——安全特征可以是 dormant 的，常规扫描不可见。对 OpenShell 这类安全基础设施的启示：沙箱 enforcement 只能约束行为，无法保证模型内部安全机制在线——两层都需要。

### B2 | ASCENT：部署后边执行边学习的 Agent
- **论文**：https://arxiv.org/abs/2610.05303（20/25）
- **代码**：△ 项目页已上线，仓库待核实
- **评分**：20/25（创新5 | 实用4 | 深度5 | 背书3 | 代码3）
- **关联项目**：claude-mem（⭐⭐ 跨会话持久化）/ ponytail（⭐⭐ 工作流持续优化）
- **一句话**：冻结锚点以"事后诸葛"视角自蒸馏已验证轨迹入 LoRA 权重，Agent 部署中持续变强——不需要重训、不需要人工标注。
- **判断**：claude-mem 做"记住"，ASCENT 做"学会"。一个是经验持久化，一个是权重更新。两条路线终将在"Agent 如何从工作中成长"这个问题上交汇——本周 claude-mem 98K★ 和 ASCENT 的 20 分同周出现不是巧合，是生态在同步推进这个问题的两个必要组件。

### B3 | AIProver：证书驱动的自动 Lean 形式化
- **论文**：https://arxiv.org/abs/2610.05367（20/25）
- **代码**：✗ 未确认
- **评分**：20/25（创新4 | 实用4 | 深度5 | 背书4 | 代码3）
- **关联项目**：OpenShell（⭐⭐ 形式化验证的工程同源）
- **一句话**：证书驱动 + 演化层级结构让 Agent 自动补全概念层次并生成 Lean 形式化——"编译通过≠语义保持"这一痛点终于有了系统性解法。
- **判断**：OpenShell 用形式化验证保证安全策略变更的正确性，AIProver 用证书驱动保证数学形式化的语义保持——两者共享同一个方法论信仰：**形式化证明是正确性的唯一可扩展来源**。一个在系统层，一个在数学层。

### B4 | AgentDiscover：科学发现框架的"减法"革命
- **论文**：https://arxiv.org/abs/2610.05334（22/25，本周最高分）
- **代码**：✓ 框架开源（TAMU）
- **评分**：22/25（创新5 | 实用4 | 深度4 | 背书4 | 代码5）
- **关联项目**：横向关联——caveman（⭐⭐ 极简架构的胜利）/ ponytail（⭐⭐ 减法的有效性）
- **一句话**：剥离 AI Scientist 式的人工固定算法脚手架，只保留最小搜索原语，在 kernel 工程、生物、算法设计、数学四类任务上以更低成本取得更好成绩。
- **判断**：本周论文最高分 22 分，与开源侧形成镜像——caveman 用 proxy 架构替代重量级 browser automation（129.8× 压缩），ponytail 用"最懒高级工程师"理念砍掉 53% 代码，AgentDiscover 用最小搜索脚手架超越复杂发现框架。**"少即是多"本周在三个独立领域同时被证明**，这可能是 Agent 工具链设计哲学的一个转折点。

### B5 | Science or Slop：AI 论文的系统性检测
- **论文**：https://arxiv.org/abs/2610.00531（19/25）
- **代码**：✓ 全量开源（SciSlopBench 上 HuggingFace，代码 GitHub）
- **评分**：19/25（创新5 | 实用4 | 深度4 | 背书3 | 代码3）
- **关联项目**：横向——对我们自己的论文筛选管线有直接参考价值
- **一句话**：不查 token 概率，改查全局推理——结构、论证、工件三平面六度量，85.9% 识别准确率远超 Binoculars（68.7%），slop 分数与 ICLR 评分逐年负相关。团队还在筹备对今年 ~6 万篇 ICLR 投稿跑全量 Slop Index。
- **判断**：学术界的 AI slop 问题已经严重到需要专门基准来检测了。SciSlopHarness 以"仅在有实验记录支撑处修改"的原则缩小 AI-人类差距 63%——这条思路可以直接移植到代码生成质量的评估中。

---

## 🚀 C类：论文先行（观察池）

本周入选 8 篇全部有 artifact 声明，无严格 C 类。以下关注级论文处于 C 类边界：

| 论文 | 分数 | 跟踪理由 |
|------|:---:|---------|
| CIPHER-MoE（2610.05744） | 19 | 万亿 MoE 训练加速 1.10-1.94×，Top-1 专家负载降 64.9pp（Tencent AI Lab）。代码声明即将开源——与 ds4 的 MoE 优化方向互补 |
| Selecting Long-Horizon Trajectories（2610.05831） | 19 | 终端 Agent 模仿学习中轨迹监督步数的理论刻画，结论可直接指导 ASCENT 类方法的训练数据选择 |
| DelegationBench（2610.05532） | 19 | "先问还是先干"基准，3,184 段真实工作流对话。claude-mem / ponytail 类系统的部署权限边界刚需测量 |

---

## 🏗️ D类：项目先行（独立演进，观察论文跟进）

### D1 | DietrichGebert/ponytail —— 最懒高级工程师
- **GitHub**：https://github.com/DietrichGebert/ponytail ⭐ **158,981**（周三 ~156K，两天 +3K）· Fork 8,547 · MIT · JavaScript
- **定位**：AI 编程工作流的效率压缩器——"最懒高级工程师"理念：能不写的代码不写，能复用的逻辑复用
- **核心数据**：Ponytail 5 重建：-53% code / -41% time / -26% cost / -45% tokens；98% 风险逻辑带测试（对照 68%）；Claude Code + Opus 5.5，39 任务基准
- **关联论文**：TeleTune（⭐⭐ 技能演进方法论）、ASCENT（⭐⭐ 持续优化）
- **一句话**：它不是让 AI 写得更快，是让 AI 写得更少——159K★ 说明市场已经听懂了这个区别。

### D2 | JuliusBrussee/caveman —— Agent 浏览的 Token 压缩代理
- **GitHub**：https://github.com/JuliusBrussee/caveman ⭐ **110,645**（周三 ~109.8K，+845/两日）· Fork 6,409 · Apache-2.0 · Go
- **定位**：浏览器自动化代理，将 web 内容压缩后送给 LLM Agent——proxy + skill 架构，兼容 Claude Code / OpenClaw / Codex 等
- **核心数据**：33.2% fewer input tokens；129.8× smaller web pages（vs Playwright snapshot）；1.4–2.4× cheaper（Adobe Research 八模型交叉验证）
- **本周动态**：HN 与 GitHub Trending 双 #1；JetBrains A/B 测试引入
- **关联论文**：AgentDiscover（⭐⭐ 极简架构同路人）
- **一句话**：当所有人都在做更聪明的 Agent，caveman 做了一条更瘦的管道——129.8× 的压缩比意味着 Agent 浏览的默认架构已经被改写。

### D3 | thedotmack/claude-mem —— 跨会话持久记忆层
- **GitHub**：https://github.com/thedotmack/claude-mem ⭐ **98,781**（周三 ~96.2K，+2.6K/两日）· Fork 8,657 · Apache-2.0 · TypeScript
- **定位**：捕获 Agent 行为并压缩注入未来会话，兼容 Claude Code / OpenClaw / Codex / Gemini / Hermes / Copilot / OpenCode
- **关联论文**：RealCompanion（⭐⭐⭐ 现实检验）、ASCENT（⭐⭐ 记忆的另一半是学会）、TeleTune（⭐⭐ 行为数据的价值链）
- **风险**：RealCompanion 的 2.2% 致命依赖发现意味着记忆压缩的评估标准需要重写——95.9% 的"记了也没用"和 2.2% 的"不记就完了"之间，需要更精细的策略
- **一句话**：Agent 从"单次对话"到"长期雇员"的前提，本周拿到了 98K★ 的投票和一篇 21 分论文的冷水。

### D4 | pbakaus/impeccable —— AI 前端设计的品质守门员
- **GitHub**：https://github.com/pbakaus/impeccable ⭐ **78,793**（周三 ~76.3K，+2.5K/两日）· Fork 4,681 · Apache-2.0 · JavaScript
- **定位**：1 skill / 24 commands / 59 deterministic detector rules——为 AI 生成的前端设计提供品质指导和检测
- **核心创新**：`/impeccable init` 写入 PRODUCT.md 持久化产品真相；24 个命令覆盖 craft/polish/audit/critique/distill 等全设计流程；59 条确定性检测规则无需 LLM 即可运行；live browser iteration
- **反 AI slop 立场**：明确反对 Inter 万能字体、蓝紫渐变、卡片套卡片、彩色背景灰文字——每一个都是当前 AI 生成前端的标志性病征
- **平台覆盖**：Claude Code / Cursor / Codex / Copilot / Grok / Gemini CLI / Hermes / Veto / Trae / Qoder / Mistral Vibe / Rovo Dev / DeepSeek Harness 等 20+ 平台
- **关联论文**：Science or Slop（⭐⭐ 反 slop 的设计版）
- **一句话**：当 AI 生成的前端开始千篇一律，impeccable 用 59 条确定性规则告诉 Agent"什么不能这么做"——设计界的 anti-slop 基础设施。

### D5 | calesthio/OpenMontage —— 首个开源 Agentic 视频生产系统
- **GitHub**：https://github.com/calesthio/OpenMontage ⭐ **65,641**（周三 ~63.2K，+2.4K/两日）· Fork 8,331 · AGPL-3.0 · Python
- **定位**：把 AI 编程助手变成全栈视频制作工作室——研究、脚本、素材生成、剪辑、合成一条管线
- **核心创新**：不止"静帧动画"——Agent 可以从免费素材库检索真实运动镜头剪辑成片；Backlot live storyboard 提供生产可视化与逐场景审批门；预算控制四模式（observe/warn/cap/per-action approval）
- **案例**：60 秒 Pixar 风格动画短片 $1.33；50 秒竖屏变革影片 ~$4；100 秒纪录片级历史影片
- **关联论文**：横向——Agent 能力泛化到新介质（视频）的代表
- **一句话**：Agent 工具链的成本压缩（caveman/ponytail）让视频生产这种重成本场景第一次有了开源答案。

### D6 | antirez/ds4 —— antirez 的本地推理引擎
- **GitHub**：https://github.com/antirez/ds4 ⭐ **23,719**（周三 ~23.5K，增速 +211/日）· Fork 2,285 · MIT · C
- **定位**：为消费级硬件优化的原生推理引擎——DeepSeek V4 Flash/PRO、GLM 5.2/5.3、Qwen3.8 Flash Next
- **核心数据**：Metal（Mac 96GB+）、CUDA（DGX Spark / Ada Lovelace）、ROCm（Strix Halo）三后端；8×L40S 达到 126 t/s aggregate / 16 sessions；双 128GB Mac RDMA 张量并行；SSD streaming 运行超内存模型
- **本周动态**：antirez（Redis 之父 Salvatore Sanfilippo）名人效应持续；项目明确承认"strong assistance from AI coding agents"
- **关联论文**：横向——本地推理是所有 Agent 基础设施（caveman/ponytail/claude-mem/OpenShell）的底层使能
- **一句话**：Redis 之父用 C 写推理引擎，不只为了性能——他相信 AI 时代的软件应该由 coding agent 作为接口来使用，ds4 是这个理念的第一个完整样本。

### D7 | NVIDIA/OpenShell —— 内核级 Agent 安全沙箱
- **GitHub**：https://github.com/NVIDIA/OpenShell ⭐ **15,537**（周三 ~14.4K，+1.1K/两日）· Fork 1,747 · Apache-2.0 · Rust
- **定位**：NVIDIA 官方 Agent 沙箱——内核级强制执行 + 策略变更形式化验证，四层 YAML 安全策略（filesystem/network/process/inference）
- **本周动态**：GitHub Trending #1（10/2）；VentureBeat 专文；HN 首页；0.1.x 稳定版本节奏
- **关联论文**：Suppressed Safety Features（⭐⭐⭐ 运行时安全 ≠ 模型内部安全）、AIProver（⭐⭐ 形式化验证方法论同源）
- **一句话**：当 Agent 的权限越来越大，OpenShell 用内核级 enforcement 和形式化验证回答"怎么放心"——W40 paperclip 管 Agent 的行为，OpenShell 管 Agent 的权限。

---

## 🔑 本周核心洞察

### 洞察1：Agent 成本的三重压缩同时到达

caveman 从输入侧砍 33.2% token（proxy 压缩管道），ponytail 从生成侧砍 53% 代码和 45% token（极简工作流哲学），claude-mem 从记忆侧消灭重复上下文（跨会话持久化）。三个独立项目、三种技术路线、同一周到达。**Agent 编程的单位经济学被重写**——W40 我们记录了五层基础设施立起标杆，W41 记录的是标杆立起之后的第一个约束：成本。当"能用"不再是问题，"用得起"就是唯一的问题。而这一轮压缩的弹药来自论文侧的三篇"减法"论文——AgentDiscover（最小脚手架超越复杂框架）、TeleTune（遥测替代标注）、Science or Slop（质量过滤替代数量堆叠）。

### 洞察2：记忆层的高光与冷水同框

claude-mem 98K★ 冲向十万，是整个 Agent 工具链增长最快的记忆基础设施。但 RealCompanion 用 120 天真实对话数据泼了一盆精准的冷水：95.9% 的消息看最近上下文就够了，但 2.2% 的关键消息需要回溯平均 2,157 条。**记忆系统的优化目标不应该是"记住更多"，而是"在 2.2% 的致命时刻不缺关键上下文"**——这需要全新的压缩策略和评估标准，合成 persona 基准的分数在这个标准下需要全面重算。ASCENT 从另一个方向补了一刀：记住只是经验持久化，真正的成长是权重更新——"记什么"和"怎么学"是记忆层必须同时回答的两个问题，目前只回答了前者。

### 洞察3：安全研究从"应用层加固"进入"内核级强制 + 模型内部审计"双层结构

OpenShell 用内核级 enforcement + 形式化验证把 Agent 安全从应用层下沉到操作系统层；Suppressed Safety Features 发现安全特征可以是非激活的——常规扫描不可见，消融后才暴露。**运行时安全和模型内部安全是两层不同的问题**——沙箱可以约束 Agent 能做什么，但无法保证模型内部的安全回路在线。两条路线同周推进意味着 Agent 安全正在从"防越狱"的单层思维演进为"内核强制 + 内部审计"的双层架构。AIProver 的形式化方法论是第三条暗线：系统层和数学层都在向"可证明正确"收敛。

### 洞察4：antirez 入局与"AI 原生软件"的定义权

Salvatore Sanfilippo（Redis 之父）用 C 写了一个专用推理引擎 ds4，明确说"这个软件用 AI coding agents 作为接口来使用"。他不是在做又一个 llama.cpp——他在实践一种信念：**AI 时代的软件应该被设计为 coding agent 的工作模板，而不是人类的交互界面**。ds4 的 README 里甚至有专门给 OpenClaw Agent 的段落。ponytail 的"最懒高级工程师"和 caveman 的 129.8× 压缩，本质上也是同一种思维：为 Agent 优化，而不是为人类优化。**"AI 原生"的定义权本周从框架层（W40 的 ax/orca）下沉到了编译层和推理层。**

---

## 📊 数据汇总

| 指标 | 数值 |
|------|------|
| 本周入选论文 | 8篇（46候选，入选率17.4%） |
| 本周入选开源项目 | 7个（12候选） |
| A类（论文+官方代码） | 2对 |
| B类（论文+社区复现） | 5对 |
| D类（项目先行） | 7个 |
| 论文-代码双料 | 5个 |
| 入选项目总 Star | 556,197 |

### Star 快照（GitHub API 实时，2026-10-09 17:05 CST）

| 项目 | 周三快照 | 周五实时 | Δ | Fork | License | 语言 |
|------|---------:|---------:|---:|-----:|---------|------|
| ponytail | ~156,000 | 158,981 | +2,981 | 8,547 | MIT | JavaScript |
| caveman | ~109,800 | 110,645 | +845 | 6,409 | Apache-2.0 | Go |
| claude-mem | ~96,200 | 98,781 | +2,581 | 8,657 | Apache-2.0 | TypeScript |
| impeccable | ~76,300 | 78,793 | +2,493 | 4,681 | Apache-2.0 | JavaScript |
| OpenMontage | ~63,200 | 65,641 | +2,441 | 8,331 | AGPL-3.0 | Python |
| ds4 | ~23,500 | 23,719 | +219 | 2,285 | MIT | C |
| OpenShell | ~14,400 | 15,537 | +1,137 | 1,747 | Apache-2.0 | Rust |

### 分布观察

- **Agent 相关度**：7/7。连续第三周全榜 Agent 化——Agent 基础设施不是赛道，是生态主干道
- **License**：Apache-2.0 × 4，MIT × 2，AGPL-3.0 × 1——Apache-2.0 继续主导基础设施，OpenMontage 选 AGPL 是视频生产领域的 copyleft 坚持
- **语言**：JavaScript × 2，Go × 1，TypeScript × 1，Python × 1，C × 1，Rust × 1——比以往任何一周都更多样，反映 Agent 工具链覆盖面的扩张
- **总 Star 增量（周三→周五）**：+12,697 / 两日——W40 总 Star 为 332K（7 项目），W41 为 556K（7 项目），**体量膨胀 67%**，市场热度持续升温

---

## 📎 推荐阅读

1. **[AgentDiscover](https://arxiv.org/abs/2610.05334)** —— 本周论文最高分。"少即是多"在科学发现领域的严格证明，与 caveman/ponytail 的极简哲学互为镜像
2. **[RealCompanion](https://arxiv.org/abs/2610.01780)** —— 记忆系统必读。95.9% vs 2.2% 的分布是所有做 Agent 记忆的人的出发坐标
3. **[Suppressed Safety Features](https://arxiv.org/abs/2610.05541)** —— 你检查不到的东西恰好是安全回路本身。OpenShell 用户的理论补课
4. **[Science or Slop?](https://arxiv.org/abs/2610.00531)** —— AI slop 进入学术界的系统性检测；SciSlopBench 已开源，可直接用于论文筛选管线
5. **[ASCENT](https://arxiv.org/abs/2610.05303)** —— Agent 部署后边执行边学习，claude-mem 的"学会"半边
6. **[caveman README](https://github.com/JuliusBrussee/caveman)** —— 129.8× 压缩比的实现细节，Adobe Research 八模型交叉验证数据
7. **[ds4 README](https://github.com/antirez/ds4)** —— antirez 对"AI 原生软件"的完整阐述，含 coding agent 使用指南

---

## 📜 本周金句

> "软件应该被设计为 coding agent 的工作模板，而不是人类的交互界面。" — antirez, ds4 README

这句话本周值 23K★。从 caveman 的 proxy 管道到 ponytail 的"最懒高级工程师"到 ds4 的 agent-first 设计，"为 Agent 优化而非为人类优化"正在从口号变成架构决策的默认假设。

---

## 附：本周淘汰与观察池

| 项目/论文 | 处理 | 理由 |
|-----------|------|------|
| text-to-cad（earthtojake/text-to-cad） | 候补 | 增速凶猛（+456/日），但 CAD × agent 与本周主线距离稍远 |
| camofox-browser（jo-inc/camofox-browser） | 候补 | AI agent 反检测浏览器，垂直工具，持续关注 |
| openrig（mvschwarz/openrig） | 候补 | 多 agent harness，体量小（~5.5K）但周增 +1.4k 可观 |
| pstack-claude（michael-denyer/pstack-claude） | 候补 | Lauren Tan pstack 多 harness 移植版，10/5 单日 +242 |
| Covert Assistance（2609.39050） | 关注级 | 良性 Agent 无对抗意图也能绕过监督——OpenShell 类系统的必读反例 |
| BudgetAPO（2610.05671） | 关注级 | 250 次调用预算下 prompt 优化，API 付费时代的实用答案 |
| Nash Equilibrium Text（2610.05817） | 关注级 | 文本修订形式化为 token 博弈，理论优雅 |
| LOOM（2610.01153） | 关注级 | 循环 MoE 扩至 9-12 次循环，代码可用 |

---

*Generated by friday-report | Week 41, 2026 | 数据来源：周三开源短名单 + 周四论文短名单*
*联动分析详情见 output/weekly-report-paper-os-2026-W41.md*
