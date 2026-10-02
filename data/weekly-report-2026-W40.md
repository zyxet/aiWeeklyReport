# AI开源情报周报 | 2026-W40

> 报告周期：2026-09-28 至 2026-10-04
> 生成时间：2026-10-02 19:15 CST
> 数据来源：论文精选（8篇，46候选，入选率17.4%）+ 开源精选（7个，10候选）
> 联动分析：output/paper-os-linkage-2026-W40.md
> 编排方式：按 A-D 联动优先级排序（A=论文+官方代码 → D=项目先行）
> 项目 Star 数据：GitHub API 实时（2026-10-02 19:10 CST）

---

## 📋 本周概览

| 维度 | 数据 |
|------|------|
| 精选开源项目 | 7 个（10 候选） |
| 精选论文 | 8 篇（46 候选，入选率 17.4%） |
| 入选项目总 Star | 332,453（周五 19:10 实时） |
| 论文+代码双料 | 4 个（ACG / ScopeIF / Choir / FRAIL） |
| A类强关联 | 4 对 |
| B类中关联 | 4 对 |
| D类项目先行 | 7 个 |
| 本周最热话题 | 五层基础设施成形 · 记什么↔怎么记 · 模型热切换 · Agent 社会学 |

**本周关键词**：Agent 操作系统 · 一致性图 · 记忆巩固 · KV 翻译 · 个体理性与集体崩溃 · 确定性优先

**本周一号事件**：Agent 基础设施**五层结构本周全部立起标杆项目**——执行（orca 兼容 25+ CLI Agent）→ 编排（google/ax）→ 组织管理（paperclip 96K★）→ 记忆（hindsight 巩固四杠杆）→ 决策（laya 33ms 判定引擎）——而论文侧罕见地为其中三层同时提供了理论（ACG→记忆层、Choir→编排层、FRAIL→组织层）。工程立杆、理论到货，同周发生。

---

## 🏆 A类：论文+官方代码（强关联，优先关注）

### A1 | ACG：长 horizon Agent 的自适应一致性图
- **论文**：https://arxiv.org/abs/2609.32754（22/25）
- **代码**：✓ 论文声明代码开源
- **评分**：22/25（创新4 | 实用5 | 深度4 | 背书4 | 代码5）
- **关联项目**：hindsight（⭐⭐⭐ 记什么↔怎么记）/ paperclip（⭐⭐⭐）
- **一句话**：自适应一致性图维护长序列 Agent 执行状态，GPT-5.6-luna 上 44.5%→50.2%（+5.7pp）。
- **⚡ 为什么本周最重要**：它与 hindsight 构成完美互补——ACG 回答长任务中"哪些状态必须以什么一致性级别维护"，hindsight 的巩固四杠杆回答"怎么持久化"。生产级长任务 Agent 的两个必要组件本周同时到齐，缺一即跛。

### A2 | ScopeIF：范围感知的精确指令遵循
- **论文**：https://arxiv.org/abs/2609.32189（22/25）
- **代码**：✓ 论文声明 code and data available
- **评分**：22/25（创新4 | 实用5 | 深度4 | 背书4 | 代码5）
- **关联项目**：paperclip / orca / ax（⭐⭐）/ open-code-review（⭐⭐）
- **一句话**：约束分解为 Scope/Target/Range 三维 + 工具验证 + 分级奖励，Qwen3-4B/8B 在范围感知指令遵循上比肩 Gemini-2.5-Pro。
- **⚡ 信号**：在"一个任务扇出给几十个 Agent"的世界里，scope 精度就是事故率。ScopeInstruct 数据集可直接改造成 paperclip/orca 这类平台的回归测试集。

### A3 | Choir：分布式多 Agent 数学形式化的开放协议
- **论文**：https://arxiv.org/abs/2609.31903（21/25）
- **代码**：✓ 全量开源（协议 + Lean 4 / Isabelle / Rocq 三适配）
- **评分**：21/25（创新4 | 实用3 | 深度5 | 背书4 | 代码5）
- **关联项目**：orca（⭐⭐⭐）/ ax（⭐⭐⭐）/ paperclip（⭐⭐）
- **一句话**：开放协议实现分布式多 Agent 数学形式化，打破单一团队集中运行的算力瓶颈。
- **⚡ 判断**：与 orca（IDE 路线）、ax（运行时路线）构成"协议 vs 环境 vs 运行时"的三位一体——TCP/IP 与 Kubernetes 当年也是这两种思路，最后分层共存。

### A4 | FRAIL：LLM Agent 社会的金融脆弱性
- **论文**：https://arxiv.org/abs/2609.30940（21/25）
- **代码**：✓ 论文声明 Code available
- **评分**：21/25（创新5 | 实用4 | 深度4 | 背书4 | 代码4）
- **关联项目**：paperclip（⭐⭐⭐）/ orca / ax（⭐⭐）
- **一句话**：个体理性 Agent 无需恶意指令即可导致集体崩溃——银行挤兑基线失败率 77%；三种稳定化机制成功时共享同一时序模式：**广泛承诺必须在防御行为自我强化之前形成**。
- **⚡ 信号**：paperclip 的预算控制、审批路径、审计留痕不只是管理功能，是多 Agent 系统的稳定化机制——而且必须在 Agent 学会自我封盘之前配置好。

---

## 🔗 B类：论文+社区复现（中关联，关注落地）

### B1 | CoWindow Attention：全因果覆盖是头集成的集体属性
- **论文**：https://arxiv.org/abs/2609.32704（22/25）
- **代码**：△ 部分开源
- **评分**：22/25（创新5 | 实用5 | 深度5 | 背书4 | 代码3）
- **关联项目**：laya（⭐⭐）
- **一句话**：远程窗口在 KV heads 间互补分配，128K 训练加速 7.4x、推理 3.0x，0.6B-14B scaling law 与 FullAttn 几乎重合。
- **判断**：如果可复现，注意力架构"全员全因果"的默认假设即被打破。与 laya 同属"效率 ≠ 更大模型"阵营——一个在架构层省计算，一个在决策路径消灭自回归。

### B2 | KV-Lingo：跨模型 KV 缓存翻译器
- **论文**：https://arxiv.org/abs/2609.32610（21/25）
- **代码**：△ 部分开源
- **评分**：21/25（创新5 | 实用5 | 深度4 | 背书4 | 代码3）
- **关联项目**：orca / ax（⭐⭐⭐）
- **一句话**：学习线性映射把源模型 KV cache 翻译为目标模型可读表示，模型切换首 token 延迟降 9.6-29x。
- **⚡ 为什么本周最工程友好**：orca 支持 25+ CLI Agent、ax 的 Model 原语天然多 provider——两个项目都在做模型切换，KV-Lingo 让切换从冷启动变热启动。"小模型先行、大模型接管"的动态路由因此从论文设想变成工程可选项。

### B3 | SphereGate：后训练各向异性的分工结构
- **论文**：https://arxiv.org/abs/2609.32792（21/25）
- **代码**：△ 部分开源
- **评分**：21/25（创新5 | 实用4 | 深度5 | 背书4 | 代码3）
- **关联项目**：laya（⭐⭐⭐）/ open-code-review（⭐⭐）
- **一句话**：~5% 残差通道构成相干基底（移除后 PPL 10→10⁶），SFT 重塑它、RL 保持它不动；仅训练 0.1M 参数即超全模型 GRPO（MATH-500 领先 2.0-7.3 分）。
- **判断**："冻结大模型 + 微门控小参数"正是 laya 的架构哲学在 post-training 侧的镜像——小模块有效不是巧合，是结构。

### B4 | BSD：信念自蒸馏提取用户模型
- **论文**：https://arxiv.org/abs/2609.31603（21/25）
- **代码**：△ 部分开源
- **评分**：21/25（创新5 | 实用4 | 深度5 | 背书4 | 代码3）
- **关联项目**：paperclip / hindsight（⭐⭐）
- **一句话**：提取 LLM 隐式用户信念，可读可写——保持请求不变、仅改变用户信念即可改变安全拒绝；跨模型共享表示几何。
- **⚡ 安全含义**：记忆系统写入"用户画像"类记忆的那一刻，就成了行为操控面。可写用户信念必须先过安全审计再谈产品化。

---

## 🚀 C类：论文先行（观察池）

本周入选 8 篇全部有官方 artifact，无严格 C 类。以下关注级论文处于 C 类边界：

| 论文 | 分数 | 跟踪理由 |
|------|:---:|---------|
| Decomposition Tax（2609.32825） | 19 | 四阶段 pipeline 接口损失 40.5 点。orca 的扇出、paperclip 的跨职能协作全是 pipeline，全在付接口税；✗无代码 |
| Alignment Paradox（2609.32617） | 20 | 后训练对齐使高置信错误增 10-35 倍——给 OCR 的"确定性优先"哲学一个严格理论注脚；△ |
| Stale-Doc Poisoning（候选池#22） | 19 | 过期检索文档翻转 30-75% 答案——记忆系统的投毒威胁模型；△ |
| Mandela-Bench（2609.32763） | 20 | 36 个 VLM 记住而非"看到"经典图像——AI 安全评估新维度 |

---

## 🏗️ D类：项目先行（独立演进，观察论文跟进）

### D1 | paperclipai/paperclip —— AI 劳动力控制面
- **GitHub**：https://github.com/paperclipai/paperclip ⭐ **96,040**（周三快照 ~90.9K，两天 +5.1K）· Fork 16,276 · MIT · TypeScript
- **定位**：Agent 管理层独立成层——"雇佣"Claude Code / OpenClaw / Codex 执行，自带任务分配、预算控制、审计留痕
- **本周动态**：+1,853★/日的增长仍在继续；8 月 CVE-2026-41679（CVSS 10.0）已修复
- **关联论文**：FRAIL（⭐⭐⭐ Agent 劳动力经济学）、ACG（⭐⭐⭐ 大规模协作一致性）、ScopeIF（⭐⭐ 任务范围精度）
- **风险**：96K★ 项目承载"企业 AI 员工"叙事，一旦多 Agent 集体故障（FRAIL 模式），叙事反噬会非常快
- **一句话**：它不替代执行端，它管执行端——Agent 从工具变劳动力的第一个管理系统样本。

### D2 | stablyai/orca —— 并行 Agent 舰队 ADE
- **GitHub**：https://github.com/stablyai/orca ⭐ **83,513**（+2.4K/两日）· Fork 5,402 · MIT · TypeScript
- **定位**：Agent Development Environment——一个 prompt 扇出到 5 个 Agent，隔离 git worktree 并行，对比合并
- **本周动态**：移动端伴侣 + Design Mode（Chromium 元素直送 prompt）；4 周涨 28K，YC 押注
- **关联论文**：Choir（⭐⭐⭐ 协议化的并行协作）、KV-Lingo（⭐⭐⭐ 多模型热切换）、Decomposition Tax（⭐⭐ 扇出-合并的接口税）
- **一句话**："一台机器一个 Agent"到"一个舰队几十个 Agent"的范式转移的操作台。

### D3 | vectorize-io/hindsight —— 会自我学习的 Agent 记忆
- **GitHub**：https://github.com/vectorize-io/hindsight ⭐ **44,498**（周三 38.6K，+5.9K/两日，本周增速王）· Fork 5,861 · Apache 2.0 · Python
- **定位**：RAG"检索即记忆"→"记忆需要巩固"：重要性/合并/衰减/淘汰四杠杆
- **本周动态**：9/28 单日 +4,520★（全榜最高增速）
- **关联论文**：ACG（⭐⭐⭐ 记什么↔怎么记）、BSD（⭐⭐ 信念写入=操控面）、Stale-Doc Poisoning（⭐⭐ 遗忘正确性欠账）
- **风险**：记忆巩固四杠杆的消融评测之外，安全评测（篡改/操控）完全空白——本周两篇论文恰好各戳一个
- **一句话**：Agent 从"单次对话"走向"长期雇员"的前提，2026 Q4 最被低估的基础设施。

### D4 | NandhaKishorM/laya —— 非自回归 System 1 决策引擎
- **GitHub**：https://github.com/NandhaKishorM/laya ⭐ **30,027** · Fork 2,611 · Apache 2.0 · Python
- **定位**：不生成文本、只做判定——单次前向 33ms，零 token 成本，支持 100+ 语言
- **本周动态**：typed-decisions 0.766 反超 Jev 0.727；9/22 进 AUR
- **关联论文**：SphereGate（⭐⭐⭐ 小模块接管子空间的机制证据）、CoWindow（⭐⭐）、KV-Lingo（⭐⭐ 大小模型协同的另一半）
- **短板**：>20 选项标签空间性能下降（每标签仅 3-4 tokens）——学术侧值得接手
- **一句话**：开源对闭源 Jev 最锋利的一击；"用大模型生成 vs 用小模型判定"的架构分层正在确立。

### D5 | alibaba/open-code-review —— 确定性优先的 AI 评审
- **GitHub**：https://github.com/alibaba/open-code-review ⭐ **43,264**（9/12 快照 22.4K，三周近翻倍）· Fork 3,116 · Apache 2.0 · Go
- **定位**：确定性工程 × LLM Agent 混合架构——同模型 precision 4.7× Claude Code，token 仅 1/9
- **本周动态**：HN 主串 284 分；阿里内部 2 年实战验证
- **关联论文**：ScopeIF（⭐⭐ 工具验证式约束）、SphereGate（⭐⭐ 小门控大作用）、Alignment Paradox（⭐⭐ 对齐提升自信非正确——确定性组件是必要纠偏层）
- **争议**：recall 故意压低是设计选择；Martian 第三方评测 12% 精度 vs 官方 33.9%，修复后尚无独立复验——保持标注
- **一句话**："harness 比模型更重要"迄今最有力的实证，分阶段混合架构的生产级教科书。

### D6 | dream-num/univer —— Agent 的 Office Harness
- **GitHub**：https://github.com/dream-num/univer ⭐ **22,287** · Fork 1,870 · Apache 2.0 · TypeScript
- **定位**：电子表格/文档/演示一体化 SDK——Agent 操作 Office 文件像调 API
- **本周动态**：已有 DeepSeek Harness 与 OpenClaw 官方集成；MCP 分类趋势榜 #2
- **关联论文**：本周论文横向关联为零——不是缺陷，是它站在"结构化文档可验证性"这个独立象限；Decomposition Tax 的重定位修复思路与公式引擎 oracle 化是最接近的接入点
- **一句话**：梦行科技（中国团队）在 Agent 工具链的结构化深水区拿到全球开源话语权。

### D7 | google/ax —— Agent 编排运行时
- **GitHub**：https://github.com/google/ax ⭐ **12,824** · Fork 629 · Apache 2.0 · Go
- **定位**：声明式 YAML 三原语（Task/Workspace/Model），CLI 对标 kubectl，"kubectl for agents"
- **本周动态**：v0.3.1；**最后一次 push 停在 9/27（已 5 天）**——对比前三周的迭代速度值得留意
- **关联论文**：Choir（⭐⭐⭐ 协议路线 vs 运行时路线对照）、FRAIL（⭐⭐ 资源限额=稳定化机制）、KV-Lingo（⭐⭐⭐ Model 原语的热切换）、ScopeIF（⭐⭐ YAML Task 的范围精度）
- **风险**：Google 明示 stable 前会有重大 breaking changes；Agent Substrate 依赖是最大部署门槛
- **一句话**：大厂第一次把 Agent 当作"一类新的工作负载"来做基础设施。

---

## 🔑 本周核心洞察

### 洞察1：五层结构不是叙事，是事实——且论文侧同步到了货

执行（orca）→ 编排（ax）→ 组织管理（paperclip）→ 记忆（hindsight）→ 决策（laya），五层本周各有标杆。更罕见的是论文侧为三层同时提供理论：ACG→记忆层、Choir→编排层、FRAIL→组织层。W38 我们记录 Harness 三层清晰化，W39 记录 Skill 分层，W40 记录五层完工——**周周递进，这不是分析师的叙事，是生态自己在收敛**。

### 洞察2：两条效率路线的同榜会师

"生成更便宜"（CoWindow 7.4x 训练加速 / KV-Lingo 29x 切换提速）与"干脆不生成"（laya 33ms 判定）本周同榜。Agent 双系统架构（System 1 判定 + System 2 生成）第一次有了两端的现成开源组件，SphereGate 从机制侧给了统一解释：大模型内部本就存在可供小模块接管的结构化子空间。

### 洞察3：Agent 社会学的第一周

FRAIL 证明个体理性 Agent 会集体崩溃（77% 挤兑失败率），稳定化的时序规律（广泛承诺先于防御行为）直接适用于 paperclip 的预算/审批设计；Choir 证明信任可以被协议化。**多 Agent 治理的两条路线——经济学（承诺/激励）与协议学（验证/合规）——同周到货，"Agent 社会学"从科幻词汇变成可立项的学科。**

### 洞察4：记忆层的高光与欠账同框

hindsight +5.9K/两日登顶增速王，同时被两篇论文各戳一个安全欠账：Stale-Doc Poisoning（陈旧记忆=投毒向量）与 BSD（用户信念写入=操控面）。**记住一切的前提是能安全地忘掉该忘的，以及写入的用户模型必须可审计。巩固四杠杆解决了前半句的一半，后半句还没开始。**

---

## 📊 数据汇总

| 指标 | 数值 |
|------|------|
| 本周入选论文 | 8篇（46候选，入选率17.4%） |
| 本周入选开源项目 | 7个（10候选） |
| A类（论文+官方代码） | 4对 |
| B类（论文+社区复现） | 4对 |
| D类（项目先行） | 7个 |
| 强关联（⭐⭐⭐） | 8对 |
| 论文-代码双料 | 4个 |
| 入选项目总 Star | 332,453 |

### Star 快照（GitHub API 实时，2026-10-02 19:10 CST）

| 项目 | 周三快照 | 周五实时 | Δ | Fork | License | 最后 push |
|------|---------:|---------:|---:|-----:|---------|-----------|
| paperclip | ~90,887 | 96,040 | +5,153 | 16,276 | MIT | 10/02 |
| orca | 81,114 | 83,513 | +2,399 | 5,402 | MIT | 10/02 |
| hindsight | 38,600 | 44,498 | +5,898 | 5,861 | Apache 2.0 | 10/02 |
| laya | 28,336 | 30,027 | +1,691 | 2,611 | Apache 2.0 | 10/01 |
| open-code-review | 22,389* | 43,264 | +20,875* | 3,116 | Apache 2.0 | 10/01 |
| univer | 16,327 | 22,287 | +5,960 | 1,870 | Apache 2.0 | 10/02 |
| ax | 11,313 | 12,824 | +1,511 | 629 | Apache 2.0 | 09/27 |

> *ocr 周三值为 9/12 flowtivity 快照，三周近翻倍；univer 周三值来自 rebang.today 快照，各源口径存在差异。ax 最后 push 停在 9/27，是 7 个项目中唯一 5 天未更新的——与其 v0.3.1 时期的迭代速度不符，列入观察。

### 分布观察

- **Agent 相关度**：7/7。连续第二周全榜 Agent 化——Agent 基础设施已经不是赛道，是生态主干道
- **License**：Apache 2.0 × 5，MIT × 2——Agent 基础设施首选 Apache 2.0 的趋势延续
- **语言**：TypeScript × 3，Go × 2，Python × 2——控制面/前端类 TS，运行时类 Go，模型/算法类 Python 的分工稳定
- **中国团队**：univer（梦行科技）+ open-code-review（阿里）+ laya——三席，全球话语权持续

---

## 📎 推荐阅读

1. **[ACG](https://arxiv.org/abs/2609.32754)** —— 记什么↔怎么记的另一半，hindsight 用户必读
2. **[FRAIL](https://arxiv.org/abs/2609.30940)** —— 个体理性→集体崩溃的系统性证据，做多 Agent 平台的先把"广泛承诺先于防御行为"抄进设计文档
3. **[KV-Lingo](https://arxiv.org/abs/2609.32610)** —— 模型热切换的最后一块拼图，orca/ax 集成预测的原始论文
4. **[Choir](https://arxiv.org/abs/2609.31903)** —— 多 Agent 协作的协议形态，对照 ax 的运行时形态一起看
5. **[Alibaba Open Code Review 深度评测](https://www.infoq.com/news/2026/09/alibaba-opencodereview/)** —— InfoQ 架构分析；确定性×LLM 混合架构案例
6. **[SphereGate](https://arxiv.org/abs/2609.32792)** —— 0.1M 参数超 GRPO 的机制解释，小模型路线的理论支撑
7. **[BSD](https://arxiv.org/abs/2609.31603)** —— 用户信念可写=安全拒绝可变；记忆系统产品的安全审计起点

---

## 📜 本周金句

> "广泛承诺必须在防御行为自我强化之前形成。" — FRAIL

这句话本周值 21 分。它同时是多 Agent 系统的设计约束、paperclip 的部署 checklist 第一条、以及"Agent 社会学"这门新学科的第一条定理。

---

## 附：本周淘汰与观察池

| 项目/论文 | 处理 | 理由 |
|-----------|------|------|
| NVIDIA/Model-Optimizer | 淘汰 | 成熟项目，本周无新突破 |
| mvschwarz/openrig | 淘汰 | 与 orca 赛道重叠，体量悬殊（2.4K vs 83.5K） |
| superdesigndev/treg | 淘汰 | 概念极早期（2.7K★），生态验证不足 |
| Decomposition Tax（2609.32825） | 关注级→C类边界 | pipeline 接口税 40.5 点，✗无代码；若放代码可升档 |
| Stale-Doc Poisoning（候选池#22） | 关注级→C类边界 | 记忆投毒威胁模型，hindsight 类项目的必答题 |
| Alignment Paradox（2609.32617） | 关注级 | 对齐放大高置信错误 10-35 倍，可复现则影响深远 |
| Mandela-Bench（2609.32763） | 关注级 | VLM"记住而非看到"，安全评估新维度 |

---

*Generated by friday-paper-merge | Week 40, 2026 | A-D联动优先级编排*
*联动分析详情见 output/paper-os-linkage-2026-W40.md*
