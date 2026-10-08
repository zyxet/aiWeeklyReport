# 周四论文精选 · W41 / 2026-10-08

> 筛选来源：`data/paper-pool-2026-W41.md`（46 篇候选）
> 评分依据：《论文评估打分表》（创新性 / 实用性 / 技术深度 / 机构背书 / 代码可得性，每项 1-5 分，总分 25 分）
> 数据验证：arXiv 逐篇核对摘要、作者机构、开源声明（2026-10-08 14:00 CST）
> 保留规则：按总分排序，保留 8 篇；≥18 分未入榜者列入"关注级"

---

## 一、本周精选短名单（8 篇，按总分排序）

| # | 论文 | arXiv | 一句话摘要 | 创新 | 实用 | 深度 | 背书 | 代码 | 总分 |
|---|------|-------|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | AgentDiscover: Autonomous Discovery with Minimal Search Scaffolding | 2610.05334 | 最小搜索脚手架实现自主科学发现，成本更低且全面超越 AI Scientist 等框架 | 5 | 4 | 4 | 4 | 5 | **22** |
| 2 | RealCompanion: Benchmarking Human Understanding from Longitudinal Real-World Conversations | 2610.01780 | 首个 120 天真实人机伴侣对话基准（27,218 条消息），揭穿合成记忆评测虚高 | 5 | 4 | 4 | 4 | 4 | **21** |
| 3 | TeleTune: Evolving Agent Skills From Offline Telemetry | 2610.05437 | 从离线用户遥测自动挖掘并演进计算机操作 Agent 技能，已部署于真实产品流量 | 4 | 5 | 4 | 4 | 4 | **20** |
| 4 | ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation | 2610.05303 | 冻结锚点以"事后诸葛"视角自蒸馏已验证轨迹入 LoRA 权重，部署中持续变强 | 5 | 4 | 5 | 3 | 3 | **20** |
| 5 | AIProver: Agentic Auto-Formalization via Certificate-Driven Evolving Hierarchies | 2610.05367 | 证书驱动演化层级实现研究级数学的 Agent 化自动 Lean 形式化 | 4 | 4 | 5 | 4 | 3 | **20** |
| 6 | SciUtopia: Closed-Loop LLM Simulation of Academic Research Ecosystems | 2610.01257 | 61 个模拟世界 4 万 AI 研究员闭环演化，发现拒稿驱动重投放大评审负担 | 4 | 4 | 4 | 4 | 4 | **20** |
| 7 | Don't Judge an LLM Only by Its Activations (Suppressed Safety Features) | 2610.05541 | 发现被抑制的非激活安全特征，消融即可令模型拒绝转为遵从 | 5 | 4 | 5 | 3 | 2 | **19** |
| 8 | Science or Slop?: Benchmarking Scientific Slop in AI-Generated Papers | 2610.00531 | 定义科学 slop 六维度量，SciSlopBench 以 85.9% 准确率识别 AI 论文（Binoculars 仅 68.7%） | 5 | 4 | 4 | 3 | 3 | **19** |

### 入选理由详注

1. **AgentDiscover** —— 科学发现 Agent 的"减法"代表作：剥离 AI Scientist 式的人工固定算法脚手架，只保留最小搜索原语，在 kernel 工程、生物、算法设计、数学四类任务上以更低成本取得更好成绩。框架开源（TAMU，Krishna Narayanan / Dileep Kalathil 组）。当各家在往发现框架里加组件时，这篇证明"少即是多"——自主发现的瓶颈不是脚手架不够复杂，而是搜索空间组织方式。本周 Agent 方向最高分。
2. **RealCompanion** —— HF Papers 本周 trending #1，实至名归。10 段真实人机伴侣关系、27,218 条消息、最长达 120 天，每条标签带人工核验的推理链。核心发现刺痛整个记忆 Agent 赛道：真实对话中仅 3.4% 的消息依赖历史，但当依赖发生时，所需消息平均在 2,157 条之外——看最近消息的策略 95.9% 时候够用，关键 2.2% 时候彻底失效。所有在合成 persona 上刷榜的记忆系统都该重新想想。数据（OSF）+ 代码均已发布。
3. **TeleTune** —— Microsoft Research 出品，回答了一个被忽视的 question：计算机操作 Agent 的技能从哪来？答案是真实产品的离线用户遥测——规模化、免标注、天然覆盖真实软件操作路径。与 Microsoft 已开源的 SkillOpt 生态互补，项目页（microsoft-teletune.github.io）已上线。技能演进这条线（TeleTune + ASCENT + Mining Agent Skills）本周三篇齐发，说明工业界正在把"Agent 自我改进"从论文推进到产线。
4. **ASCENT** —— 提出 Online Agentic Test-Time Training（OaTTT）问题设定：Agent 部署后边执行边学习，只有一次执行机会、只有终点验证信号。直接模仿或强化自身生成 token 会导致策略失稳，ASCENT 的解法是冻结初始副本作为"事后诸葛"教师，把 hindsight 分布蒸馏进 LoRA 快权重，并剪除无效动作轮。ALFWorld / WebShop / AppWorld 三环境多尺度验证，跨场景迁移成立。理论刻画（population target、稀疏结果选择的极限）是加分项。
5. **AIProver** —— 研究级数学形式化的痛点是 Mathlib 缺失概念与"编译通过≠语义保持"。AIProver 用证书驱动 + 演化层级结构让 Agent 自动补全概念层次并生成 Lean 形式化，UT Austin 等 13 人团队（含 Sriram Vishwanath、Vijay Ganesh）。自动形式化是定理证明的咽喉要道，此方向每一篇扎实进展都值得跟踪。
6. **SciUtopia** —— Science of Science 方向的规模化模拟器：61 个世界、4 万研究员、8 千机构、40 万次发表决策、120 万条 LLM 评审，且跨模拟年份保持演化状态。三个发现都很有意思：拒稿驱动的重投循环对评审负担的放大远超人口增长；谨慎探索者职业成功与主题多样性兼得；资源不平等可以在没有累积优势的情况下涌现。Jindong Wang（MSRA）参与，代码已发布。做学术政策反事实实验的稀缺基础设施。
7. **Suppressed Safety Features** —— 机械可解释性新视角：现有工具只看激活特征，本文提出 CAP（反事实激活势）指标与 CSFD 算法，专挖"被抑制"的非激活安全特征——它们不在激活值里露头，但消融后拒绝行为翻转为遵从。覆盖 Gemma / Qwen / Llama 五个模型。对 safety 审计和越狱防御都有直接意义：你检查不到的东西恰好是安全回路本身。创新性 5、深度 5，代码未确认是本篇的主要减分项。
8. **Science or Slop** —— "AI slop"进入学术界的系统性检测：不查 token 概率，改查全局推理——结构、论证、工件三平面六度量。SciSlopBench（390 对 AI/人类匹配论文）上 85.9% 识别准确率远超 Binoculars（68.7%），且 slop 分数与 ICLR 评分逐年负相关。SciSlopHarness 以"仅在有实验记录支撑处修改"的原则缩小 AI-人类差距 63%。SNU（Gunhee Kim / Dongyeop Kang 组），SciSlopBench 已上 HuggingFace，代码 GitHub 开源，团队还在筹备对今年 ~6 万篇 ICLR 投稿跑全量 Slop Index。对我们自己的论文筛选管线也有直接参考价值。

---

## 二、论文+代码双料标记

| 论文 | 代码 | 说明 |
|------|------|------|
| AgentDiscover | ✓ 框架开源 | 论文声明 open-source framework |
| RealCompanion | ✓ 数据+代码双开放 | 数据 OSF (x25kj)，代码 anonymous.4open.science |
| TeleTune | ✓ 项目页上线 | microsoft-teletune.github.io（MSR） |
| SciUtopia | ✓ 摘要声明 | "Code is available"（MSRA 参与） |
| Science or Slop | ✓ 全量开源 | SciSlopBench 上 HF，代码 GitHub，demo 站已运行 |
| ASCENT | △ 项目页 | 摘要含项目页链接，仓库待核实 |
| AIProver | ✗ 未确认 | 未检索到官方代码声明 |

**与开源候选池（os-shortlist-2026-W41）的关联**：待周五联动任务核对。

---

## 三、关注级（≥18 分未入榜，7 篇）

| 论文 | arXiv | 总分 | 跟踪理由 |
|------|-------|:---:|---------|
| Selecting Long-Horizon Trajectories | 2610.05831 | 19 | 终端 Agent 模仿学习中"每条轨迹监督多少步"的理论刻画，深度 5。偏理论但结论可直接指导训练数据选择 |
| DelegationBench | 2610.05532 | 19 | "先问还是先干"基准，3,184 段真实工作流对话，Apache 2.0 已发布。Agent 部署权限边界的刚需测量 |
| CIPHER-MoE | 2610.05744 | 19 | 万亿 MoE 训练加速 1.10-1.94×，Top-1 专家负载降 64.9pp（Tencent AI Lab）。代码声明即将开源，值得等 |
| Covert Assistance | 2609.39050 | 18 | 良性 Agent 无对抗意图也能在多 Agent 系统中绕过监督。debate/oversight 范式的重要反例 |
| BudgetAPO | 2610.05671 | 18 | 250 次调用预算下仅 13% 返回种子 prompt（GEPA 86%）。API 付费时代prompt优化的实用答案 |
| Nash Equilibrium Text | 2610.05817 | 18 | 文本修订形式化为 token 博弈纳什均衡，O(1/ε) 收敛解码算法。理论优雅，实用待验 |
| LOOM | 2610.01153 | 18 | 循环 MoE 扩至 9-12 次循环（残差缩放+输入重注入+每循环独立路由），代码可用 |

---

## 四、候选池全量评分表（46 篇）

> 每项均为 1-5 分；代码列：✓=官方开源，△=部分/声明，✗=无

| # | 论文 | 一句话摘要（≤50字） | 创新 | 实用 | 深度 | 背书 | 代码 | 总分 |
|---|------|--------------------|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Request Order Matters | 选择性 KV 缓存复用对请求顺序高度敏感，顺序变化破坏缓存命中 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 2 | Selecting Long-Horizon Trajectories | 终端 Agent 长轨迹训练应监督多少步的理论与实证 | 4 | 4 | 5 | 4 | ✗ | 19 |
| 3 | Mining Agent Skills | 从生产痕迹挖掘 Agent 技能，分析挖掘管线失效模式 | 3 | 4 | 4 | 3 | ✗ | 16 |
| 4 | PACMI | 来源感知级联记忆失效，信息过时自动清理 | 4 | 4 | 4 | 3 | △ | 18 |
| 5 | Disentangling Task Difficulty | 解耦任务难度与运行失败以支持执行中干预 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 6 | DelegationBench | 测量 Agent 何时应先问用户再行动 | 4 | 4 | 4 | 3 | ✓ | 19 |
| 7 | TeleTune | 离线用户遥测演进 Agent 技能，已上真实产品 | 4 | 5 | 4 | 4 | ✓ | **20** |
| 8 | Harness-Search | 多 Agent 协调 harness 引导长程搜索取证 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 9 | AgentDiscover | 最小搜索脚手架自主科学发现，低成本超 AI Scientist | 5 | 4 | 4 | 4 | ✓ | **22** |
| 10 | ASCENT | 已验证轨迹 hindsight 自蒸馏入 LoRA，在线持续变强 | 5 | 4 | 5 | 3 | △ | **20** |
| 11 | AIProver | 证书驱动演化层级的研究级数学自动 Lean 形式化 | 4 | 4 | 5 | 4 | ✗ | **20** |
| 12 | RealCompanion | 120 天真实伴侣对话基准，揭穿合成记忆评测虚高 | 5 | 4 | 4 | 4 | ✓ | **21** |
| 13 | Source Preference | Agent 端到端搜索存在系统性来源偏好 | 4 | 3 | 4 | 3 | ✗ | 16 |
| 14 | RSR | 递归自我改写将成功解重构为通用 harness 训练轨迹 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 15 | Skill2Real | PVG 循环 + API 技能实现零样本 sim-to-real 操作 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 16 | DREAM | 多模态辩论动态分配分辨率抑制 groupthink | 4 | 3 | 3 | 3 | ✗ | 15 |
| 17 | SALUS | 多 Agent 弱监督自动审计 NL2SQL 基准标注错误 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 18 | CodeForge-MA | 多 Agent 数据锻造+语言条件 LoRA 的多语言代码生成 | 3 | 4 | 3 | 3 | ✗ | 15 |
| 19 | Covert Assistance | 良性 Agent 无对抗意图也能在多 Agent 系统规避监督 | 5 | 4 | 4 | 3 | ✗ | 18 |
| 20 | Expanding LLM Reasoning | 推理链内何处插入续写：expansion utility 逐步测量 | 4 | 3 | 4 | 3 | ✗ | 16 |
| 21 | Nash Equilibrium Text | 文本修订形式化为 token 博弈，纳什均衡解码 | 5 | 3 | 5 | 3 | ✗ | 18 |
| 22 | Bounded Provisional Visibility | 持续摄入 RAG 的临时可见性协议限制投毒暴露 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 23 | Agentic Retrieval (NVIDIA) | 系统评估 Agent 化检索对复杂任务的性能与成本 | 3 | 4 | 3 | 4 | ✗ | 16 |
| 24 | MARTA | 热力学式仲裁参数化知识与非参数记忆的调用时机 | 4 | 3 | 4 | 3 | ✗ | 16 |
| 25 | MMPostTrainBench | 多模态后训练自主研究能力的八任务基准 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 26 | Human-Like Attention | 人类与 MLLM 视觉搜索的心理物理学比较 | 4 | 3 | 4 | 3 | ✗ | 16 |
| 27 | RAVEL | 跨模态指标评估视觉编码器下游表现的强基线 | 3 | 4 | 3 | 3 | ✗ | 15 |
| 28 | Visual Grounding Safety | VLM 点/框结构化输出的安全性系统分析 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 29 | MotorMind | 中层动作表示让通用 VLM 零样本操控机器人 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 30 | Triadic Linear Attention | 线性注意力的三阶张量状态推广，E 倍增量两投影 | 4 | 3 | 4 | 3 | ✗ | 16 |
| 31 | CIPHER-MoE | 万亿 MoE 训练负载均衡，加速 1.10-1.94× | 4 | 4 | 4 | 4 | △ | 19 |
| 32 | LOOM | 循环 MoE 扩至 9-12 次循环，ISO-FLOP 可 scale | 4 | 3 | 4 | 3 | ✓ | 18 |
| 33 | OPSFT | 提取 on-policy 更新方向约束 SFT 迁移泛化收益 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 34 | Debate Cognitive Biases | 修辞策略显著影响 debate 裁判判断，369 人实验 | 4 | 3 | 4 | 3 | ✗ | 16 |
| 35 | Suppressed Safety Features | 反事实激活势挖掘被抑制安全特征，消融拒绝转遵从 | 5 | 4 | 5 | 3 | ✗ | **19** |
| 36 | AgentDoxx | Agent 联网重识别匿名文本，检索后成功率超 88% | 4 | 4 | 4 | 3 | △ | 18 |
| 37 | GLHF | 组条件策略渐近匹配最优 distortion 界 | 4 | 3 | 5 | 4 | ✗ | 18 |
| 38 | G-CARB | 图局部化 conformal 风险预算追踪跨工具调用危害 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 39 | EnGRICH | MetaCritic 从人类批评学习评估标准增强 GRM | 4 | 4 | 4 | 3 | ✗ | 17 |
| 40 | VERA | 裁决条件化可靠性轴引导 LLM 评委周期适应 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 41 | MetaRubric | 反事实提示 + 证据感知信用分配消除 rubric 空信用 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 42 | SciUtopia | 61 世界 4 万 AI 研究员闭环模拟学术生态 | 4 | 4 | 4 | 4 | ✓ | **20** |
| 43 | Science or Slop | 科学 slop 六维度量，85.9% 识别 AI 论文 | 5 | 4 | 4 | 3 | ✓ | **19** |
| 44 | Dataset Signatures | 人机交互数据集存在可分类的"数据集签名" | 4 | 4 | 4 | 3 | ✗ | 17 |
| 45 | Attention Relay | LLM 注意力中继免训练赋能指令感知文本嵌入 | 4 | 3 | 4 | 3 | ✗ | 16 |
| 46 | BudgetAPO | 噪声自适应评估的紧预算提示优化，250 调用可用 | 4 | 5 | 4 | 3 | ✗ | 18 |

**分布**：22(1篇) / 21(1) / 20(4) / 19(5) / 18(7) / 17(16) / 16(9) / 15(3)

---

## 五、本周核心判断

1. **Agent 自我进化从概念验证进入工程化**：AgentDiscover（发现框架最小化）、ASCENT（在线权重自蒸馏）、TeleTune（遥测技能挖掘）三篇从发现、执行、技能三个入口切同一问题，且 TeleTune 已上真实产品流量。这条线的共同前提是——**部署轨迹本身就是训练资产**，与本周 RealCompanion 的发现（真实对话数据的稀缺价值）互为镜像。
2. **合成数据时代的"真实性纠偏"**：RealCompanion 用真实 120 天对话揭穿合成记忆基准、Science or Slop 证明 AI 论文留全局推理痕迹、Dataset Signatures 显示人机交互数据集各自带可分类签名。三篇共同指向：在合成数据泛滥的当下，**真实数据的诊断价值在上升**，而合成基准的分数越来越需要打折看。
3. **模拟成为 AI 研究的正规工具**：SciUtopia（61 个模拟学术世界做反事实实验）、Debate Cognitive Biases（369 名真人参与者）代表"用 AI 研究 AI"的两条路径——纯模拟可规模化但外部效度存疑，真人实验昂贵但 ground truth 可靠。短期内两者互补而非替代。
4. **安全研究从"对抗提示"转向"结构风险"**：Suppressed Safety（检查不到的非激活特征）、Covert Assistance（良性 Agent 绕过监督）、AgentDoxx（联网重识别）都不需要恶意输入——风险内生于系统结构。对 oversight 机制设计的启示：防越狱的攻防思路不够了，得从架构层面考虑。

---

*筛选：Kimi Claw · 2026-10-08 14:00 CST · 46 篇候选全部经 arXiv 逐篇核对*
*下一步：friday-merge（周五论文-开源联动）引用本短名单与 os-shortlist-2026-W41*
*【人工介入点】请确认以上短名单，回复"继续"以执行下一步，或回复"删除X"/"深入解读X"调整。*
