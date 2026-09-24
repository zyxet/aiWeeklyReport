# 周四论文精选 · W39 / 2026-09-24

> 筛选来源：`data/paper-pool-2026-W39.md`（46 篇候选）
> 评分依据：《论文评估打分表》（创新性 / 实用性 / 技术深度 / 机构背书 / 代码可得性，每项 1-5 分，总分 25 分）
> 数据验证：arXiv API 逐篇核对摘要、作者机构、开源声明（2026-09-24 14:00 CST）
> 保留规则：按总分排序，保留 8 篇；≥18 分未入榜者列入"关注级"

---

## 一、本周精选短名单（8 篇，按总分排序）

| # | 论文 | arXiv | 机构 | 一句话摘要 | 创新 | 实用 | 深度 | 背书 | 代码 | 总分 |
|---|------|-------|------|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression | 2609.19969 | DeepSeek-AI | 552B MoE 以 CSA2+FP4 把 KV cache 压至 890B/token，专为长程 Agent 负载降本 | 5 | 5 | 5 | 5 | 4 | **24** |
| 2 | RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents | 2609.22000 | 上海 AI Lab 等 34 人 | 五平台混合 CUA 环境，以可运行参考程序为 oracle 训练 GUI+编码双栖 Agent | 5 | 5 | 4 | 5 | 5 | **24** |
| 3 | EvoOntology: A Self-Evolving Ontology Layer for Data Agents | 2609.15779 | 人大数据工程实验室 | 自进化本体层封装为 MCP 服务，弥合 Agent 与异构数据间的语义鸿沟 | 4 | 5 | 4 | 4 | 5 | **22** |
| 4 | Scaling Discovery through Test-Time Communication | 2609.21032 | MSR / UW-Madison | Test-time 通信让 k 个 Agent 抵 4k 个独立 Agent，群体突破可复现 | 5 | 4 | 5 | 4 | 3 | **21** |
| 5 | GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills | 2609.21749 | 腾讯 AI Lab 等 | 把 Agent 技能表示为图并做进化优化，五基准稳定超过 SkillOpt | 4 | 4 | 4 | 4 | 5 | **21** |
| 6 | CogGym: Towards Large-Scale Comparative Evaluation of Human and Machine Cognition | 2609.21259 | MIT/Harvard/Stanford 等 60+ 人 | 标准化 258 个认知实验对比人类与 50 个 LLM，常识推理进步远慢于形式推理 | 4 | 3 | 5 | 5 | 3 | **20** |
| 7 | When AI Reviews Train AI Reviewers: Scientific-Judgment Collapse and Mitigation | 2609.20942 | UMD | 揭示 AI 评审递归训练导致判断多样性坍缩，开源 TrustReviewer 缓解 | 4 | 4 | 4 | 4 | 4 | **20** |
| 8 | CodeMidas: Scaling Agentic Coding RL Environments from Code Itself | 2609.22068 | 小米 MiMo 团队 | 从代码库直接提取多样化 RL 任务，规模化构建 Agent 编码训练环境 | 4 | 4 | 4 | 4 | 3 | **19** |

### 入选理由详注

1. **DeepSeek-V4.1-Flash** —— 本周唯一"模型层炸弹"。CED 架构 decode 激活 16B/prefill 仅 8B，KV cache 足迹压到 DeepSeek-V4-Flash 的 1/4（HBM）与 1/8（SSD），权重已在 HuggingFace 放出。长 horizon Agent 的输入密集型负载正是它瞄准的场景，直接改变 Agent 部署成本曲线。
2. **RecreationWorld** —— Hybrid CUA（GUI 操作 × 编码开发自由切换）首个可扩展训练环境，覆盖 Ubuntu/macOS/Windows/Android/Web 五平台；以"运行中的参考程序"为 oracle 提供执行级奖励，附带 250 题 RecreationBench。GPT-6 Astra 总分 58.1% 但全过程序化测试仅 2.8%——头部模型在混合任务上还很脆。环境、基准、测试套件全量开源。
3. **EvoOntology** —— 首个自进化本体层，schema/content/tool 三层封装为 MCP server，builder agent 自主构建 + 归因引导的类型化编辑 + 骨干条件配对评估。已在 4 个 LLM 骨干 × 3 个数据 Agent 基准上验证。**代码已开源（github.com/ruc-datalab/EvoOntology），且作为 MCP 插件接入 Claude Code / Codex**——与本周 OS 情报的 Skill/MCP 主线同频，是本篇入选的加分项。
4. **Scaling Discovery through Test-Time Communication** —— ARC-AGI-3 上 team@k 匹配 4k 个独立 Agent 的成功率且随 k 扩大；多连方块拼装上超过历史最优，MNIST 压缩赛 4 个 Agent 产出 1957 字节 / 99.4% 准确率的分类器，优于人类最优。 caveat 也诚实：算力受限或无明确进度信号时通信反而有害。多智能体"通信 Scaling Law"方向的标杆结果。
5. **GraphSkillEvo** —— 把 Agent 技能从非结构化自然语言升级为图结构（节点=执行步骤+操作指引，边=上下文迁移），再做种群进化优化。GPT-5.4-nano 上平均 +4.01%。**代码开源（github.com/ruisun7/GraphSkillEvo）**。恰逢本周"Skill 成为新交付单元"的社区共识，论文侧的理论化恰逢其时。
6. **CogGym** —— 认知科学全明星阵容（Tenenbaum、Frank、Linzen、Hawkins 等 60+ 作者）：半自动 pipeline 把 258 个实验标准化为 EML，对比 50 个 LLM 与人类反应。关键发现：模型-人类拟合最佳仅 R²≈0.59（人类分半信度 0.93），且常识推理的进步速度远慢于数学/编码——"形式推理 ≠ 人类式理解"的系统性证据。
7. **TrustReviewer** —— 量化"科学判断坍缩"：模型生成的评审进入训练语料后，评分分布压缩、语义多样性下降。训练期数据策展 + 测试期 activation steering 双阶段缓解，系统开源。AI 辅助同行评审已成现实，这篇给出一套可操作的风险缓解方案。
8. **CodeMidas** —— 不依赖 issue/commit，直接从代码库提取多样化 RL 任务（静态+动态分析），支撑 MiMo-V2.5 的 Agentic 编码训练。Agent 编码 RL 的"环境从哪来"问题的一个规模化答案；小米 MiMo 持续在 Agent 方向加码，值得跟踪。

---

## 二、论文+代码双料标记

| 论文 | 代码 | 说明 |
|------|------|------|
| EvoOntology | github.com/ruc-datalab/EvoOntology | 官方开源，MCP 插件形态可即插即用 |
| GraphSkillEvo | github.com/ruisun7/GraphSkillEvo | 官方开源 |
| RecreationWorld | 环境+基准+测试套件随论文发布 | 全量开源 |
| DeepSeek-V4.1-Flash | huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | 权重开源（训练代码未放） |
| TrustReviewer | 论文声明 open-source | 待核实仓库地址 |

**与开源候选池（os-shortlist-2026-W39）的关联**：本周论文侧与 OS 侧无同一仓库的直接重叠，但主题高度共振——EvoOntology 以 MCP 插件接入编码 Agent、GraphSkillEvo 对 Skill 做图结构化和进化优化，分别对应 OS 情报"Skill 标准化周"的协议层与优化层。周五联动任务建议在映射表中标注此对应关系。

---

## 三、关注级（≥18 分未入榜，6 篇）

| 论文 | arXiv | 总分 | 跟踪理由 |
|------|-------|:---:|---------|
| Verify, Don't Trust（EvoPilot） | 2609.21257 | 18 | YouTube 视频检索 37 天在线 autoresearch 实战：human-gated 验证纠正了 primitive 流程的 -22pp 误判。生产级 Agentic AutoML 的稀有完整案例 |
| DENSE | 2609.21423 | 18 | 美团 Longcat × 复旦：无结果标注下从轨迹蒸馏证据快捷树，重试通过率 +7.12~15.64pp，token 降 19-43.6%。若放代码可升档 |
| Chronicle | 2609.20625 | 18 | theagentplane：cut-point 重放让 Agent 失败可复现、可做回归测试。**代码已开源**（github.com/theagentplane/chronicle），工程实用性强 |
| ArenaFlow | 2609.21378 | 18 | 中科大 Zha 组：pairwise 评估 + 层级信用传播，解决开放式 Agent RL 奖励稀缺 |
| MERIT-Rank | 2609.20131 | 18 | 阿里：多轨迹推理重排序，4B 模型在 BRIGHT 上超多数 7B/32B。生产 rerank 直接可用 |
| Value-Sensitive Delegation in Everyday AI Agent Use: Evidence from OpenClaw | 2609.22067 | 15 | **主题特异**：基于 OpenClaw 社区 73,093 篇 Reddit 帖归纳用户委托 Agent 的 21 种价值诉求，提出"任务完成 ≠ 价值满足"。对 OpenClaw 类产品的设计有直接参考价值，分数不高但相关度极高 |

---

## 四、候选池全量评分表（46 篇）

> 每项均为 1-5 分；代码列：✓=官方开源，△=部分/权重，✗=无

| # | 论文 | 一句话摘要（≤50字） | 创新 | 实用 | 深度 | 背书 | 代码 | 总分 |
|---|------|--------------------|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Value-Sensitive Delegation（OpenClaw） | 7.3万Reddit帖归纳委托AI Agent的21种价值诉求 | 4 | 3 | 4 | 2 | ✗ | 15 |
| 2 | MCP-GRANITE Benchmark | 首个MCP工具粒度接口设计基准 | 4 | 4 | 3 | 3 | △ | 17 |
| 3 | DENSE | 无标注从轨迹蒸馏证据快捷树自我改进 | 4 | 4 | 4 | 4 | ✗ | 18 |
| 4 | ArenaFlow | 轨迹排序+层级信用传播解开放式Agent RL | 4 | 4 | 4 | 4 | ✗ | 18 |
| 5 | CodeMidas | 从代码库直接提取RL任务扩编码Agent环境 | 4 | 4 | 4 | 4 | △ | 19 |
| 6 | Harness Design for Coding Agents | 单变量对比编码Agent harness组件效能 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 7 | When Better Turns Do Not Make Better Agents | next-turn指标提升无法预测工作流成功率 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 8 | RetireOPD | 自退役机制解除student对teacher的依赖 | 4 | 3 | 4 | 3 | ✗ | 16 |
| 9 | Chronicle | 记录-重放让Agent失败可复现可回归测试 | 4 | 4 | 3 | 2 | ✓ | 18 |
| 10 | Scaling Discovery（Test-Time Comm） | k个通信Agent抵4k独立Agent且随规模放大 | 5 | 4 | 5 | 4 | △ | 21 |
| 11 | LEGIT | Agent市场的可验证凭证协议 | 3 | 3 | 3 | 2 | ✗ | 13 |
| 12 | Efficient Benchmarking in Production | 574次运行研究演进中Agent的高效复评 | 3 | 4 | 3 | 3 | ✗ | 15 |
| 13 | EvoPilot | 人门控在线autoresearch纠正-22pp误判 | 4 | 4 | 4 | 4 | ✗ | 18 |
| 14 | SERBench | 状态条件化最小充分证据恢复基准 | 4 | 4 | 4 | 3 | ✓ | 18 |
| 15 | Obstacle-Aware Harness（机器人） | coding agent机器人操作的障碍感知约束 | 3 | 3 | 3 | 3 | ✗ | 14 |
| 16 | Mind or Message? | 多Agent谈判依赖对话表面记录而非心智建模 | 4 | 3 | 4 | 3 | ✗ | 16 |
| 17 | Bayesian Belief Layer | 贝叶斯信念层实现立场动态可控可验证 | 4 | 3 | 3 | 2 | ✗ | 14 |
| 18 | LM Groups Overstate Consensus | LLM组系统性高估共识率（100组回放） | 4 | 3 | 4 | 3 | △ | 18 |
| 19 | RecreationWorld | 五平台混合CUA环境+oracle验证基准 | 5 | 5 | 4 | 5 | ✓ | 24 |
| 20 | MintAct | 统一视觉Agent，2B/4B/8B匹配闭源 | 3 | 4 | 3 | 3 | △ | 16 |
| 21 | EvoOntology | 自进化本体层MCP服务弥合agent-data gap | 4 | 5 | 4 | 4 | ✓ | 22 |
| 22 | GraphSkillEvo | 图结构技能+进化优化超SkillOpt | 4 | 4 | 4 | 4 | ✓ | 21 |
| 23 | TrustReviewer | AI评审递归训练致判断坍缩及缓解 | 4 | 4 | 4 | 4 | ✓ | 20 |
| 24 | DeepSeek-V4.1-Flash | KV cache压至890B/token服务长程Agent | 5 | 5 | 5 | 5 | △ | 24 |
| 25 | KV-COBRA | 联合优化秩截断与位宽的KV压缩 | 4 | 4 | 4 | 3 | ✗ | 17 |
| 26 | H-Spec | 免drafter侧KV cache的并行投机解码 | 4 | 4 | 4 | 4 | ✗ | 17 |
| 27 | L0-MoE | L0正则把dense LLM变轻量MoE加速2.5x | 4 | 4 | 4 | 4 | ✗ | 18 |
| 28 | RheoSampling | 解动态树投机解码随机解码坍缩 | 4 | 3 | 4 | 2 | ✗ | 15 |
| 29 | Abstention & Noise Filtering | attention值门控补弃权与噪声过滤原语 | 4 | 3 | 4 | 2 | ✗ | 15 |
| 30 | dQwen3.5 | 混合注意力AR模型改造扩散语言模型 | 4 | 3 | 4 | 4 | △ | 18 |
| 31 | MIRAGE | 动态切换心智视角的多路径推理 | 3 | 3 | 3 | 2 | ✗ | 13 |
| 32 | Reasoning in MT | 推理对翻译的帮助呈非单调 | 3 | 3 | 3 | 3 | △ | 15 |
| 33 | Privileged Info OPSD | 特权信息增益大半来自蒸馏本身 | 4 | 3 | 4 | 3 | ✗ | 16 |
| 34 | CogGym | 258认知实验对比人类与50个LLM | 4 | 3 | 5 | 5 | △ | 20 |
| 35 | Cal-OPD | 校准teacher自偏差净化蒸馏信号 | 4 | 3 | 4 | 2 | ✗ | 15 |
| 36 | RAILS | 检索增强增量聚类破标签空间爆炸 | 3 | 4 | 3 | 3 | ✗ | 15 |
| 37 | RegimeAbstain | 多跳检索失败可预测，置信弃权规避 | 4 | 3 | 4 | 2 | ✗ | 15 |
| 38 | MERIT-Rank | 多视角推理融合，4B超7B/32B重排 | 4 | 4 | 4 | 4 | ✗ | 18 |
| 39 | CASCADE | 19攻击×15防御的越狱组合部署评估 | 3 | 4 | 3 | 3 | △ | 16 |
| 40 | Xeno-Interpretability | LLM或有人类概念无法描述的内部表征 | 4 | 3 | 3 | 2 | ✗ | 14 |
| 41 | Geopolitical Divisions | 112种语言改变LLM对俄乌战争判断 | 4 | 4 | 4 | 3 | △ | 18 |
| 42 | SupportCal | 预训练模型作参考免标注校准 | 3 | 4 | 3 | 3 | ✗ | 15 |
| 43 | World Modeling in Transformers | TaxiGPT因果干预揭示世界模型被遮蔽 | 4 | 3 | 4 | 3 | ✗ | 16 |
| 44 | MATCH | 课程调度+门控奖励的工具学习RL | 4 | 4 | 4 | 4 | ✗ | 18 |
| 45 | Emergent Capabilities & Merging | 权重合并不保留涌现行为 | 4 | 3 | 4 | 3 | ✗ | 16 |
| 46 | Opinion Leader Dynamics | 稀疏注意力经意见领袖塑造token聚类 | 4 | 3 | 4 | 3 | ✗ | 16 |

**分布**：24(2篇) / 22(1) / 21(2) / 20(2) / 19(1) / 18(8) / 17(5) / 16(7) / 15(6) / 14(3) / 13(2)

---

## 五、本周核心判断

1. **Agent 环境供给成为新的瓶颈赛道**：RecreationWorld（混合 CUA 环境）、CodeMidas（从代码提取 RL 任务）、DENSE（从轨迹蒸馏反馈）三篇同周出现且全部入选/关注级——"Agent 数据/环境从哪来"已经取代"Agent 架构怎么搭"成为社区共识瓶颈。
2. **Skill 主题在论文侧开始理论化**：GraphSkillEvo + EvoOntology 入选，与 OS 情报的"Skill 标准化周"形成论文-开源共振。这是本周最值得写入周报的主线。
3. **KV cache 压缩进入"为 Agent 设计"阶段**：DeepSeek-V4.1-Flash 直接把长 horizon Agent 的输入密集型负载写进设计目标，推理效率研究与 Agent 需求正式合流。
4. **评估危机蔓延**：CogGym（人类拟合度低）、TrustReviewer（评审坍缩）、EvoPilot（无验证的 autoresearch 得出错误结论）三篇从三个角度指向同一问题——LLM 的"形式能力提升"与"真实可靠性"之间的裂口在扩大。

---

*筛选：Kimi Claw · 2026-09-24 14:00 CST · 46 篇候选全部经 arXiv API 逐篇核对*
*下一步：friday-merge（周五论文-开源联动）引用本短名单与 os-shortlist-2026-W39*
*【人工介入点】请确认以上短名单，回复"继续"以执行下一步，或回复"删除X"/"深入解读X"调整。*
