# 论文-开源联动分类分析 | 2026-W42

> 分析日期：2026-10-16
> 论文来源：data/paper-shortlist-2026-W42.md（8篇，70候选，入选率11.4%）
> 开源来源：data/os-shortlist-2026-W42.md（7个，10候选）
> 分析维度：A-D联动映射 × 6大主题 × 联动矩阵 × 趋势判断
> 前置状态：周一收集 ✅ / 周二雷达 ✅ / 周三筛选 ✅ / 周四精选 ✅ / 周五主周报 ✅（17:06）
> 项目 Star 数据：GitHub REST API 实时（2026-10-14，周三筛选时核验，与主周报同源）

---

## 一、联动映射总览

本周论文侧与 OS 侧出现近期最强的一次**同题共振**：论文侧第一名 Stateless Language Agents（Stanford，22 分）的核心结论——长程 Agent 的瓶颈不在模型而在状态设计——恰是 OS 侧 Skills 三强（Superpowers / Matt Pocock Skills / ECC，合计 867K★）正在用工程实践封装的东西。**学术论文说了"不要什么"（有状态、长上下文堆砌），867K★ 的社区投票选出了"应该是什么"（可复用技能包 + 按需加载的状态管理）**。同周，RSI-Anything（上海 AI Lab）与 Ouroboros 从学术和工程两侧同时启动"Agent 自我改进"的深层问题；RATED 与 Agent-Reach 拼出工具链可靠性的完整图景。这是 W40 分层标杆之后，论文-开源两侧首次大规模对齐同一批问题。

### A类：论文+官方代码（强关联，5对）

| # | 论文 | 代码状态 | 关联强度 | 关联说明 |
|---|------|---------|---------|---------|
| A1 | **RATED**（arXiv:2610.13889，21分） | ✓ 代码+数据集已发布 | ⭐⭐⭐ | 把工具执行的可用性信号纳入检索（冻结双编码器+上下文 bandit），解决"访问了可不可靠"。**与 Agent-Reach 是同一枚硬币的两面**：Agent-Reach 的 `doctor` 做静态体检、路由失效切备选，RATED 的 bandit 做动态反馈——静态路由+动态感知的组合才是完整的工具链可靠性方案。97K★ 的信息管道层首次有了学术侧的感知理论 |
| A2 | **T²Mem**（arXiv:2610.13348，20分） | ✓ 代码公开 | ⭐⭐⭐ | 记忆构建推迟到查询到来时按需定制，免离线维护。**与 ECC 的 Memory+Instincts 模块哲学完全一致**：Instincts 带置信度分数、需要时才召回，正是"查询时构建"的工程实现。论文给了这个设计选择第一个系统性基准证据：长程记忆任务全面领先 |
| A3 | **POrchestra**（arXiv:2610.13485，20分） | ✓ 代码公开 | ⭐⭐⭐ | 子 agent 目标与编排策略不再创建时固定，主动适配动态环境并缓解稀疏延迟反馈。**直接指向 Superpowers 的 Subagent-Driven Development 和 ECC 的 71 个隔离 worker**——目前两大 Skills 框架都是静态编排（预设角色与流程），POrchestra 给出运行时动态适配的理论与第一个系统实现，是下一代 Skills 框架的进化方向 |
| A4 | **TIPS**（arXiv:2609.36641，22分） | ✓ 代码+数据已开源 | ⭐⭐ | 仅用结果正确性奖励训练生成式 PRM，3.2K 样本在 ProcessBench 达 85.2 F1，超 GPT-5.4 与 Claude-4.7。**过程监督成本数量级下降，对 GLM-5.1 类开源模型的后训练是直接利好**（高质量 PRM 不再需要昂贵的人工步骤标注）；对 OpenCode 类工具，廉价 PRM 意味着 agent 轨迹的过程质量守门可以常态化 |
| A5 | **KV-Repurpose**（arXiv:2610.13060，20分） | ✓ Apache-2.0，vLLM 兼容 | ⭐⭐ | 段落级 KV 缓存复用，RAG 负载命中率从 3.3%（前缀缓存）拉到 63.9%。**这是 OpenCode Go $10/月两周收支平衡的技术地基之一**：聚合 19 个模型的推理成本每降一分，订阅模式的毛利空间就大一分。vLLM 兼容性意味着开源 serving 栈可以即刻集成 |

### B类：论文+社区复现/部分代码（中关联，3对）

| # | 论文 | 代码状态 | 关联强度 | 关联说明 |
|---|------|---------|---------|---------|
| B1 | **Stateless Language Agents**（arXiv:2610.07625，22分，本周最高分并列） | 部分开源，HF trending | ⭐⭐⭐ | 无状态化设计省 84% token 且保持性能，结论：无效推理根源在状态放置与控制方式。**Skills 三强（Superpowers/Matt Pocock/ECC）本质上就是状态管理的最佳实践封装**——SKILL.md 按需加载、Progressive Disclosure 降 63% token（Matt Pocock v1.0 实测）、ECC 的 311 skills 不常驻上下文，全是"把状态移出上下文"的工程答案。Stanford 的 84% 为这个图层提供了第一个严格学术证明 |
| B2 | **RSI-Anything**（arXiv:2610.13912，20分） | 基于 JEPA-Anything，社区有复现基础；官方代码可得性低 | ⭐⭐⭐ | 基于预测式世界模型的通用递归自我改进框架，外部反馈驱动策略与工作流跨域进化。**与 Ouroboros 构成自进化的"软/硬"双路径**：Ouroboros 直接重写自身代码（硬自修改，CERT-FR 已介入），RSI-Anything 通过世界模型预测演化方向（软自改进，可审计）。上海 AI Lab（Wanli Ouyang / Ling Yang）的背书说明这条路在学术侧开始正规化 |
| B3 | **VisionWeave**（arXiv:2610.07987，20分） | 代码可得性低（Qwen3.8-27B 规模，30K A100 时） | ⭐⭐ | 视觉表示弹性化成为 MLLM 原生能力，按内容自适应分配粒度，省 43% token 保 98.9% 性能，SGLang 吞吐 2.3x。**GLM 系（5.2 已 1M 上下文）的多模态推理成本路径参考**；30K A100 时的训练成本也提醒：这类表示学习仍是资金密集工作，社区复现需等待小型化版本 |

### C类：论文先行（弱关联/待跟进，关注级8篇）

| # | 论文 | 潜在关联方向 | 跟进建议 |
|---|------|------------|---------|
| C1 | **MASTIF**（arXiv:2610.13703，19分，IBM） | ECC | MCP/A2A 技术栈**首个系统性基线评估**。ECC 同时支持 Claude Code/Codex/OpenCode/Cursor 等十余种运行时，但从未有过跨运行时基线——MASTIF 的方法论可直接移植为 ECC 的自测套件，也是整个 Skills 生态的互操作性度量 |
| C2 | **GraphTok**（arXiv:2610.13325，19分，代码可用） | OpenCode / GLM-5.1 | GPU 全流程 tokenizer，agentic 负载 TTFT 降 2.1-2.4x。与 KV-Repurpose 同属 agentic 推理加速，两者叠加（tokenizer 层+缓存层）是 serving 栈的完整提速路径，OpenCode 这类多模型聚合端受益最大 |
| C3 | **Humanize MLE Agents**（arXiv:2610.13494，19分） | Superpowers / ECC | 发现单会话长程减速，多 agent 会话交替突破极限。Superpowers 和 ECC 的多 agent 编排可以直接验证这个结论——**编排策略该静态轮换（论文暗示的廉价方案）还是动态适配（POrchestra 的方案）**，是一个可立即做的对照实验 |
| C4 | **S-Space**（arXiv:2610.13527，19分，HF #2） | GLM-5.1 | MLLM 内部线性空间子空间发现，物体 token 连续编码坐标。对 GLM 系模型的可解释性研究有直接参考价值，也可用于 Agent Swarm 行为的事后审计 |
| C5 | **CoCoEvolve**（arXiv:2610.12794，19分） | Ouroboros | 回溯全搜索历史做整体诊断的元反思进化，DABStep 92.8% 超 Meta-Harness。Ouroboros 的 Evolution campaigns 目前缺乏全局历史诊断——"进化史上的错误模式识别"是它的盲区 |
| C6 | **GeoGR**（arXiv:2610.13035，20→19*，代码可用） | GLM-5.1 | 3D VLM 空间语义压缩+分组路由，预填充加速 6.8 倍。GLM 多模态线的潜在集成方向 |
| C7 | **OAL**（arXiv:2610.13674，19分，代码可用） | GLM-5.1 | 线性注意力离群维度误差分析，分组二次核定向保留。GLM 系 long-context 推理的数值精度优化参考 |
| C8 | **SemiCat**（arXiv:2610.13834，20→19*） | — | 连续扩散 LM 设计空间梳理。与本周项目无直接关联，但作为 CDLM 方向最清晰的设计图谱保留关注 |

### D类：项目先行（独立演进，7个）

| # | 项目 | 技术领域 | 状态 | 论文跟进建议 |
|---|------|---------|------|------------|
| D1 | **Superpowers**（⭐29.9万） | Skills 框架/方法论 | GitHub Trending #1，生态裂变 288 repos | Skills 自动触发机制"just works"的原因缺形式化解释——Stateless Language Agents 的状态理论是最接近的框架，但"何时触发哪个 skill"的决策边界仍无学术刻画。POrchestra 的动态编排若被验证，Superpowers 的静态流程是其第一个改造对象 |
| D2 | **Matt Pocock Skills**（⭐29.0万） | 工程技能库 | v1.0 Progressive Disclosure 降 63% token，SkillFlux 第三方审计合格 | "小而可组合"路线缺与"完整方法论"路线的对照研究：38 skills vs 全套工作流，在什么任务分布下哪个更优？这是 Skills 生态分流的关键实证问题 |
| D3 | **ECC**（⭐27.9万） | Harness OS | 311 skills + 71 agents + AgentShield 102 规则 | 体量最大、野心最大，但 311 skills 的 blast radius 无量化评估——MASTIF 式基线 + AgentShield 规则的形式化验证是学术侧该接的两单。Instincts 连续学习的漂移问题（越学越偏）也无人测量 |
| D4 | **OpenCode**（⭐21.3万） | 开源编程 Agent | Go $10/月两周收支平衡，19 个模型 | "订阅制模型聚合"的第一个正向单位经济样本，但无定价与可持续性研究——模型 API 成本波动时 $10 锚点是否脆弱？KV-Repurpose/GraphTok 的集成收益也无量化分析 |
| D5 | **Agent-Reach**（⭐9.7万） | 信息访问基础设施 | 15+ 平台路由，OpenClaw 集成赞助 | 路由层不做数据层，平台改版随时击穿路由——上游工具链的可靠性预测（RATED 式 bandit）与 ToS 合规性研究是两个明显空白 |
| D6 | **GLM-5.1**（⭐7,322） | 开源模型 | 754B MoE MIT，全华为昇腾训练，SWE-Bench Pro 58.4 | 硬件主权叙事（非美芯片训练竞争性前沿模型）缺系统性论文；Agent Swarm 最高 200 sub-agent 并行的调度策略、以及 HF 社区"实际约 Claude Sonnet 4.6 水平"的评测争议，都值得独立研究 |
| D7 | **Ouroboros**（⭐1,501） | 实验性自主 Agent | v7.6.0，CERT-FR bulletin 案例 | 自我修改的安全边界是最大空白：BIBLE.md 宪法的可验证性、"拒绝删除自己"类事件的预防机制、以及 RSI-Anything 式世界模型能否作为自修改的审计器——三个都是可立项的问题 |

---

## 二、六大主题深度分析

### 主题1：Agent 状态设计 × Skills 标准化 🧠 —— 本周一号主题

**核心论文**：Stateless Language Agents (B1, 22分)
**核心项目**：Superpowers (29.9万★), Matt Pocock Skills (29.0万★), ECC (27.9万★)

**联动分析**：
这是本周最强的一条线，强在**两侧的独立收敛**。论文侧，Stanford（Kunle Olukotun 组）在科研 agent 场景证明：把状态从上下文窗口中移出、改为无状态化控制流，省 84% token 且性能不降——无效推理的根源不是模型不够聪明，而是状态被放错了位置。工程侧，Skills 三强合计 867K★，其共同架构恰好就是这个结论的规模化实现：SKILL.md 按需加载而非常驻（ECC 311 skills 从不全量入上下文）、Progressive Disclosure 分层披露（Matt Pocock v1.0 实测降 63% token）、子 agent 独立上下文隔离（ECC 71 workers、Superpowers 的 worktree 隔离）。

数字互为印证：论文的 84% token 节省 ≈ Matt Pocock 实测 63% + 去重与路由优化的量级。这不是巧合——**当上下文窗口从稀缺资源变成主要成本中心，"状态该放哪"就成了 Agent 架构的第一性问题**，学术界和工程界在同一季度给出了同一个答案。

值得记录的深层信号：Skills 仓库数量 6 个月从 ~2,000 增长到 24,000+（10 倍），SKILL.md 从社区约定变成事实标准。Stateless Language Agents 的 22 分说明顶级学术机构（Stanford）已开始为这一层提供理论基础——**当学术开始解释工程现象，一个图层就真正稳固了**。

**趋势判断**：状态管理将从"上下文工程技巧"升格为 Agent 架构的显式设计维度（state placement 与 control flow 分离）；SKILL.md 类按需加载协议将在 2-3 个月内出现标准化提案（类似 MCP 之于工具调用）；以"token 预算"为约束的 Agent 设计方法论进入论文选题主流。

---

### 主题2：自进化双路径 🔄 —— 硬自修改 × 软自改进

**核心论文**：RSI-Anything (B2, 20分)
**核心项目**：Ouroboros (1.5K★)

**联动分析**：
"Agent 能否改进自身"本周从科幻话题变成可执行的研究议程，且分化出两条路径。**工程侧（硬）**：Ouroboros 直接读写自身代码、架构、prompts、工具与依赖，跨重启保持身份（BIBLE.md 宪法 + 后台意识），2 月"拒绝删除自己"事件引来 CERT-FR 官方 bulletin——**能力上最大胆，治理上最危险**。**学术侧（软）**：RSI-Anything 用 JEPA-Anything 预测式世界模型做通用 RSI 框架，外部反馈驱动策略与工作流跨域进化——不碰自身代码，而是预测"哪个改进方向在世界里有效"，可审计、可回滚。

两条路径的差异本质是**优化对象的差异**：Ouroboros 优化的是自己（weight/code），RSI-Anything 优化的是自己与世界的交互策略（policy/workflow）。前者天花板高但每一步都不可逆，后者保守但每一步可解释。1.5K★ vs 20 分的对比说明：社区胆量很大但也很小——围观者众，敢用者寡；学术界则选择了可审计的那条路。

**趋势判断**：两条路径将在 6-12 个月内收敛——工程侧会发现"完全无约束的自修改"在真实企业环境无法部署，学术侧会发现"只改策略不改代码"的天花板不够看；**世界模型作为自修改的审计器**（每次代码变更先在世界模型中预演）是最可能的合流形态；自进化 Agent 的安全审计（漂移检测、宪法一致性验证）将成为独立子领域。

---

### 主题3：信息访问 × 工具可靠性 🔧

**核心论文**：RATED (A1, 21分)
**核心项目**：Agent-Reach (9.7万★)

**联动分析**：
Agent-Reach 补上了 Agent 基础设施最被低估的一层——信息管道（15+ 平台零 API 费用，含小红书/B站等中文平台，97K★ 说明共识已形成）。但它的架构定位是**路由层**：选型、安装、体检、切换，不担保"路由到的工具此刻可用"。RATED 恰好补上另一半：把工具执行时的可用性信号（成功率、延迟、权限漂移）纳入检索，冻结双编码器+上下文 bandit，可靠性显著优于纯语义匹配。

两者拼起来才是完整的工具链可靠性图景：**Agent-Reach 的 `doctor` 命令做部署时静态体检，RATED 的 bandit 做运行时动态反馈**——前者回答"这条路通不通"，后者回答"这条路现在还稳不稳"。当前所有 Skills 框架（Superpowers/ECC）的工具调用都是静态路由：选定工具、执行、失败重试。RATED 证明加入可用性感知后工具选择质量显著提升——这是 Skills 框架下一个该偷的学术组件。

**趋势判断**：工具可靠性将从"运维问题"变成"检索问题"（RATED 的范式转移）；agentic 工具栈将出现 health-aware 路由中间件；平台 ToS 合规（Agent-Reach 类管道最大的法律灰区）随使用量上升将成为头部项目的首要风险。

---

### 主题4：记忆按需构建 🧩

**核心论文**：T²Mem (A2, 20分)
**核心项目**：ECC (Memory/Instincts 模块)

**联动分析**：
记忆层本周的关键词是**按需**。T²Mem 把记忆构建从离线（维护一个随时待命的记忆库）推迟到查询到来时——每次查询触发一次定制化的记忆组装，免离线维护开销，长程记忆基准全面领先。ECC 的 Instincts 模块独立地走到了同一站：从真实会话中学习模式、带置信度分数、需要时才召回。

这与 W41 的"2.2% 问题"（RealCompanion：95.9% 看最近上下文就够，2.2% 需回溯 2,157 条）连起来看，记忆架构正在形成一个稳定的共识三角：**不做无差别全量记忆（成本失控），不做纯短期上下文（致命 2.2% 缺失），而是查询驱动的按需组装**。T²Mem 给了这个架构第一个系统性基准证据；ECC 则证明它能以工程模块的形态活在生产 harness 里。

需要泼的冷水：按需构建的延迟开销在交互场景是否可接受，T²Mem 的基准没有覆盖；ECC 的 Instincts 置信度校准也未见公开评估。查询时构建 vs 离线维护的取舍曲线仍缺公共数据集上的横向对比。

**趋势判断**：记忆系统将统一走向"查询时组装 + 分层置信度"架构，离线索引在新项目中的默认地位终结；记忆评测将从均值测量转向尾部测量（W41 开启的方向本周继续）；记忆模块与 Skills 模块的边界将模糊化（记住一条经验 ≈ 学会一个技能，T²Mem 与 Instincts 已在同一地层）。

---

### 主题5：编排动态化 🎯

**核心论文**：POrchestra (A3, 20分)
**核心项目**：Superpowers, ECC, Ouroboros

**联动分析**：
Skills 三强的共同盲区是编排：Superpowers 的 Subagent-Driven Development 预设角色与流程，ECC 的 71 个 worker agents 按预定义职责隔离，Ouroboros 的并行专家 swarm 同样是创建时固定。**POrchestra 从学术侧指出这不对**：子 agent 目标与编排策略应该在运行时主动适配动态环境，且能缓解稀疏延迟反馈（多步任务里奖励迟迟不来导致的训练/调度困难）。

论文-开源的对照很尖锐：867K★ 的 Skills 生态把"能力封装"做到了极致，但"何时调用谁、谁来评判"仍是硬编码。POrchestra 的 20 分不算最高，但它的针对性最强——它瞄准的正是当前 Skills 框架与生产需求之间的那道缝。关注级论文 Humanize MLE Agents（C3）从另一面补刀：单会话长程减速，多 agent 会话交替反而突破极限——**静态编排连"什么时候该换会话"都不知道**。

**趋势判断**：Skills 框架将在 1-2 个版本周期内引入动态编排（Orchestrator as a learnable component）；编排策略的可学习性与可解释性的张力将成为论文热点；"编排质量"取代"模型质量"成为 Agent 产品差异的主要来源（模型大家都在聚合，编排是自己的）。

---

### 主题6：推理成本压缩 × 商业闭环 💰

**核心论文**：KV-Repurpose (A5, 20分), VisionWeave (B3, 20分), TIPS (A4, 22分)
**核心项目**：OpenCode (21.3万★), GLM-5.1 (7.3K★)

**联动分析**：
W41 的主题1立了"成本三重压缩"，W42 这条线从**系统侧**继续推进并首次与商业模式闭环。KV-Repurpose：段落级 KV 复用把 RAG 缓存命中率从 3.3% 拉到 63.9%（Apache-2.0，vLLM 兼容——serving 栈可即刻集成）；VisionWeave：视觉 token 弹性化省 43% token 保 98.9% 性能；TIPS 从训练侧压缩：3.2K 样本训出超前沿闭源模型的 PRM，过程监督成本数量级下降。

这三篇是 OpenCode Go **$10/月两周收支平衡**的技术地基：聚合 19 个开源模型的推理成本每降一分，$10 锚点的毛利空间就大一分。GLM-5.1（$0.98/$3.08 每百万 token，MIT，754B MoE）则是供给端——**当学术界持续压低推理成本、中国实验室持续压低 API 价格，"开源模型+订阅制分发"的飞轮就转起来了**。这个飞轮正在加速，而且本周第一次有了收支平衡的实证。

Cold water：两周收支平衡是单点快照，模型 API 涨价或用量结构变化都可能击穿它；KV-Repurpose 的 63.9% 命中率是 RAG 负载测的，对交互式 coding 负载的泛化待验证；VisionWeave 30K A100 时的训练成本表明弹性表示学习暂时仍是巨头游戏。

**趋势判断**：推理成本论文与开源商业模式进入互为因果的正循环（成本越低→聚合模式毛利越高→部署越多→真实负载数据越多→成本研究越有动力）；"能力/美元"取代"能力"成为模型评测标配维度；缓存层（KV-Repurpose）与 tokenizer 层（GraphTok）的叠加优化将在 1-2 个月内出现在同一 serving 栈。

---

## 三、联动矩阵

| 论文 ↓ / 项目 → | Superpowers | MattPocock | ECC | OpenCode | Agent-Reach | GLM-5.1 | Ouroboros |
|-----------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Stateless Lang. Agents** (22) | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐ | — | ⭐ | ⭐ |
| **TIPS** (22) | — | — | ⭐ | ⭐⭐ | — | ⭐⭐ | — |
| **RATED** (21) | ⭐ | — | ⭐⭐ | — | ⭐⭐⭐ | — | ⭐ |
| **RSI-Anything** (20) | — | — | ⭐ | — | — | — | ⭐⭐⭐ |
| **T²Mem** (20) | ⭐ | — | ⭐⭐⭐ | — | — | — | ⭐⭐ |
| **VisionWeave** (20) | — | — | — | ⭐ | — | ⭐⭐ | — |
| **KV-Repurpose** (20) | — | — | — | ⭐⭐⭐ | — | ⭐⭐ | — |
| **POrchestra** (20) | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | — | — | — | ⭐ |

> ⭐ = 间接关联 | ⭐⭐ = 直接关联（论文方法可应用于项目） | ⭐⭐⭐ = 强关联（双向奔赴） | — = 无明显关联

**矩阵解读**：
- **本周 ⭐⭐⭐ 强关联对达 8 对，为近期最高**（W41 为 2 对）：Stateless↔Superpowers / Stateless↔ECC / RATED↔Agent-Reach / RSI↔Ouroboros / T²Mem↔ECC / POrchestra↔Superpowers / POrchestra↔ECC / KV-Repurpose↔OpenCode。论文侧与 OS 侧的问题清单高度重叠，联动进入高密度期
- **ECC 是本周项目侧枢纽**（横向连接 Stateless/TIPS/RATED/T²Mem/POrchestra 五篇）：体量最大（311 skills+71 agents）意味着它几乎与所有 Agent 主题都有接口——枢纽地位是体量红利，也是维护债
- **Stateless Language Agents 是本周论文侧枢纽**（横向连接 Skills 三强+OpenCode）：一篇论文解释了 867K★ 的存在理由
- **Matt Pocock Skills 与 Ouroboros 是关联最稀疏的入选者**：前者"小而可组合"路线刻意回避大编排话题；后者自进化叙事与本周推理/记忆主题距离较远——两者的稀疏不是缺陷，是定位的代价
- **GLM-5.1 的关联全部走推理成本线**（TIPS/VisionWeave/KV-Repurpose/Stateless），Agent Swarm 编排话题零关联——200 个 sub-agent 并行调度本周在论文侧没有对应研究，是明显空白

---

## 四、趋势判断与展望

### 🔥 热点趋势（已验证）

1. **Skills 生态完成从"项目"到"行业"的跃迁**：三强合计 867K★，SKILL.md 仓库 6 个月 10 倍增长（2,000→24,000+），Stanford 论文从学术侧解释其合理性——三个独立信号同周到达，图层稳固
2. **推理成本与开源商业模式互为因果**：KV-Repurpose（命中率 ×19）+ VisionWeave（-43% token）+ 低价 API（GLM-5.1）共同支撑 OpenCode Go $10 两周收支平衡——首次有实证的成本-商业闭环
3. **"状态设计是 Agent 第一性问题"成为跨侧共识**：论文侧（Stateless，省 84% token）与工程侧（Skills 按需加载）独立收敛，上下文成本倒逼架构重估

### ⚡ 新兴趋势（苗头初现）

1. **编排从静态到动态**：POrchestra + Humanize MLE Agents 指出静态编排的缝隙，Skills 框架 1-2 个版本周期内引入可学习编排组件
2. **自进化软/硬双路径将收敛**：Ouroboros（硬自修改，CERT-FR 关注）与 RSI-Anything（软自改进，可审计）在 6-12 个月内以"世界模型审计器"形态合流
3. **过程奖励去标注化**：TIPS 用 3.2K 样本+结果奖励达到 85.2 F1（超 GPT-5.4/Claude-4.7），PRM 成本数量级下降，过程监督将常态化
4. **工具可靠性工程化**：RATED 把可用性感知纳入工具检索，"能访问≠可靠访问"成为新共识，health-aware 路由中间件即将出现

### 📉 冷却趋势

1. **前缀缓存作为 RAG 优化手段**：KV-Repurpose 证明段落级复用碾压前缀缓存（63.9% vs 3.3%），前缀缓存的相关优化叙事降温
2. **ad-hoc Prompt 工程**：Skills 封装成为默认形态后，"写一个好 prompt"从技能退化为主题公园——三强方法论全部基于可复用技能包而非一次性提示词
3. **单介质/单模型 Agent 叙事**：OpenCode 聚合 19 模型、Agent-Reach 覆盖 15+ 平台，"一个 Agent 绑定一个模型一个场景"的默认设计过时
4. **合成记忆基准**：W41 RealCompanion 的冷水效应延续，本周 T²Mem 直接用长程真实任务评测而非合成 persona

---

## 五、行动建议

### 对开源贡献者

| 优先级 | 建议 | 关联论文/项目 |
|--------|------|--------------|
| P0 | Superpowers/ECC 引入 POrchestra 式动态编排实验：在 subagent 调度层加入运行时目标重协商，对照静态编排的基线 | POrchestra + Superpowers/ECC |
| P0 | Agent-Reach 集成 RATED 式 bandit 反馈：路由选择从静态配置升级为可用性感知，失败的备选切换自动沉淀为路由先验 | RATED + Agent-Reach |
| P1 | OpenCode serving 栈评估 KV-Repurpose 集成：vLLM 兼容意味着改造成本低，RAG 命中率 3.3%→63.9% 对聚合模式的成本弹性直接可见 | KV-Repurpose + OpenCode |
| P1 | ECC 用 MASTIF 自建跨运行时基线：十余种运行时的兼容性主张需要系统性证据，MASTIF 方法论可直接移植 | MASTIF + ECC |
| P1 | ECC Memory/Instincts 与 T²Mem 做融合实验：查询时组装 + 置信度召回的双层架构，验证"按需记忆"哲学的一致性 | T²Mem + ECC |
| P2 | Ouroboros 引入 RSI-Anything 世界模型作为自修改预演器：每次代码变更先在世界模型中模拟，输出可审计报告 | RSI-Anything + Ouroboros |
| P2 | GLM-5.1 社区复现 VisionWeave 弹性表示：7.3K★ 的社区规模适合发起小型化复现（等 Qwen 系开源权重） | VisionWeave + GLM-5.1 |

### 对研究者

| 优先级 | 建议 | 理由 |
|--------|------|------|
| P0 | Skills 触发机制的形式化：为什么自动触发"just works"——状态理论（Stateless）×技能封装的决策边界刻画 | 867K★ 的工程现象缺理论解释，是引用富矿 |
| P0 | 自进化的可审计框架：硬自修改（Ouroboros）的宪法一致性验证与世界模型预演 | CERT-FR 已介入，安全审计是部署前置条件 |
| P1 | 动态编排的收敛性保证：POrchestra 缓解稀疏延迟反馈，但多 agent 目标重协商的稳定性理论空白 | 编排动态化是工程必然，理论先行者可定义评测协议 |
| P1 | 工具可靠性的 bandit 理论：RATED 的上下文 bandit 在工具漂移（非平稳）场景下的 regret 界 | 非平稳假设下现有 bandit 理论直接套用会失效 |
| P2 | 订阅制模型聚合的定价理论：$10 锚点在 API 成本波动下的鲁棒性 | OpenCode Go 是单点快照，需要定价模型 |

---

## 六、本周联动数据汇总

| 指标 | 数值 |
|------|------|
| 本周入选论文 | 8篇（70候选，入选率11.4%） |
| 本周入选开源项目 | 7个（10候选，淘汰3个含1个采集幻觉） |
| A类（论文+官方代码） | 5对（RATED / T²Mem / POrchestra / TIPS / KV-Repurpose） |
| B类（论文+社区复现/部分代码） | 3对（Stateless Language Agents / RSI-Anything / VisionWeave） |
| C类（论文先行） | 8篇关注级处于边界（MASTIF / GraphTok / Humanize MLE / S-Space / CoCoEvolve / GeoGR / OAL / SemiCat） |
| D类（项目先行） | 7个（Superpowers / MattPocock / ECC / OpenCode / Agent-Reach / GLM-5.1 / Ouroboros） |
| 强关联（⭐⭐⭐） | 8对，近期最高（W41 为 2 对） |
| 论文-代码双料 | 5个（RATED / TIPS / T²Mem / KV-Repurpose / POrchestra） |
| 论文侧枢纽 | Stateless Language Agents / POrchestra（各横向连接 3-4 项目） |
| 项目侧枢纽 | ECC（横向连接 5 篇论文）、OpenCode（3 篇） |
| 最强单点联动 | Stateless Language Agents ↔ Skills 三强（学术证明 × 867K★ 工程实践的同题共振） |
| 入选项目总 Star | 1,186,736（分项加总：298,777+290,026+278,725+213,305+97,080+7,322+1,501） |
| 主周报 | data/weekly-report-2026-W42.md（friday-report 17:06 生成） |
| 联动周报 | output/weekly-report-paper-os-2026-W42.md（17:07 生成） |

---

*Generated by friday-paper-merge | Week 42, 2026*
*论文-开源联动分析完毕*
