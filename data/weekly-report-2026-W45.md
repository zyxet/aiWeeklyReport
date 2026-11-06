# AI 开源周报（2026 年第 W45 周）

> 生成时间：2026-11-06（周五）
> 覆盖周期：2026-11-02 ~ 2026-11-06
> 数据来源：周三开源短名单（7 项目）+ 周四论文短名单（8 篇）
> 本周主题：**Kimi K3.1 Pro 权重落地** · **超长上下文注意力双突破**（LSA / ZHA）· **Agent 基础设施分工细化**

---

## 本周概览

| # | 项目 | 分类 | 一句话 | 本周最大变化 |
|---|------|------|--------|-------------|
| 1 | Kimi K3.1 Pro | 模型 | 2.8T MoE 权重 11-04 Hugging Face 正式放出 | 从"承诺"到"现货"，开源权重可下载 |
| 2 | Kronos | 模型 | 首个金融 K 线开源基座，AAAI 2026，45+ 交易所 | 28 天 +20.2k ⭐，46,608 |
| 3 | Lightpanda | 基础设施 | Zig 无头浏览器 v1.0.0，11× 快 9× 省 | 41,183 ⭐，AI agent 浏览器层确立 |
| 4 | FreeToken | 基础设施 | 消费级显卡跑 290B+ MoE 的边缘推理引擎 | K3.1 权重放出后的直接受益工具链 |
| 5 | claude-mem | 基础设施 | Claude Code 跨会话持久记忆，支持多 agent 客户端 | 112,151 ⭐，持续活跃提交 |
| 6 | ECC | 基础设施 | Agent harness 性能优化系统，67 agents / 281 skills | 296,684 ⭐，日增 ~1.2k |
| 7 | hallmark | 效率工具 | 反 AI-slop 设计技能，22 主题 + 57 道质量关 | 一周 +7.8k，47,185 ⭐ |

**本周趋势一句话**：Kimi K3.1 Pro 权重在 11 月 4 日如期落地 Hugging Face，把上周"开源 Agent 编码上限"的讨论从"API 可用"推进到"自托管可行"；论文侧 LSA 和 ZHA 从两个方向同时证明亚二次注意力已抵达 10M+ token 实用区间，恰好回答了"2.8T 模型 + 1M 上下文"落地后的推理成本问题。工具侧，Lightpanda / claude-mem / ECC / hallmark 分别在浏览器、记忆、harness、设计四个层面推进 Agent 基础设施的分工细化——Agent 时代的"技术栈分层"正在加速成形。

---

## 论文-开源映射表（A-D 分类）

> 详细联动分析见 output/weekly-report-paper-os-2026-W45.md（含三大主题 + 联动矩阵）

**A类：论文 + 官方代码（5 篇）— 可立即复现**

| 论文 | 分数 | 联动开源项目 | 联动方式 |
|------|------|-------------|---------|
| LSA 🏆 | 24 | K3.1 Pro / FreeToken | SGLang 插件直接加速 1M 上下文推理 |
| RoboArchitect 🏆 | 24 | ECC | 编码模型自动进化 harness 的学术验证 |
| Mage-VL-Cowork 🏆 | 23 | Lightpanda | 4B GUI agent 的浏览器层基础设施 |
| SecPO 🏆 | 23 | ECC | 对抗训练防御 + AgentShield 扫描互补 |
| ASTC 🏆 | 22 | claude-mem | 免训练上下文压缩 × 持久化记忆召回 |

**C类：论文先行（3 篇）— 代码未随论文发布**

| 论文 | 分数 | 对应方向 | 跟进建议 |
|------|------|---------|---------|
| ZHA | 21 | 树索引亚二次注意力 | 关注 Zyphra 官方仓库；与 LSA 殊途同归，方法论可先行借鉴 |
| LARC | 20 | 连续潜空间多模态推理 | NeurIPS 2026，关注代码释放 |
| Flide | 19 | 决策模型推理引擎 | ForkAttention 架构可复现，关注开源进度 |

**D类：项目先行（7 个）— 暂无对应论文**：Kimi K3.1 Pro、Kronos、Lightpanda、FreeToken、claude-mem、ECC、hallmark

**B类（社区复现）本周为空** — 5 篇官方放代码，3 篇未放，同样两极分化。

---

## 🔥 重磅推荐

### Kimi K3.1 Pro — 权重落地，开源 Agent 编码的完整闭环

**来源**: [Moonshot AI](https://www.kimi.ai/blog/kimi-k3-1-pro) · [Hugging Face](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · 权重发布 2026-11-04
**License**: 修改版 MIT（>$20M MaaS 营收需单独协议，>100M MAU 需署名）

上周周报中"权重预计 11-04 放出"的悬念本周揭晓：**K3.1 Pro 完整权重已如期上架 Hugging Face**。2.8T 总参 / 104B 激活 MoE、896 experts top-16 路由、原生 1M token 上下文，文本+图像双模态输入。

核心数据回顾：

- **Terminal-Bench 4.0 达 65.7%，开源模型 #1**
- **SWE-Marathon 51.7**，长程编码任务领先
- **幻觉率（Hallu Bench Hard）8.3%**，较 K3 的 23.4% 断崖式下降
- API 定价 $2 / $10 per M tokens（输入/输出），Highspeed 变体 2-3× 速度

**权重落地意味着什么**：K3（7 月放权重）到 K3.1 Pro（11 月放权重）的间隔从 11 天拉长到 12 天，但模型能力跨度和上下文上限都有了量级提升。修改版 MIT 协议保留了商业使用门槛，但对于自托管场景——数据主权、定制推理、Agent 编码管线——这已经是当前可获得的最强开放权重。

**为什么重要**：K3 权重放出时社区问题还是"能不能跑"，K3.1 Pro 落地时问题已经变成"跑多快"——FreeToken 等边缘推理引擎（见下文）的存在让 2.8T MoE 在消费级硬件上交互式运行成为可讨论的问题。权重落地 + 推理优化工具链 + 注意力加速论文，三个条件在本周同时就位。

**风险**：2.8T 规模对推理基础设施要求极高（K3 的 MXFP4 权重 ~594GB，K3.1 Pro 预计同量级）；修改版 MIT 的商用条款需法务审核。

---

### Kronos — 金融 K 线的首个开源基座

**仓库**: [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) · **License**: MIT
**本周Stars**: 46,608 ⭐（28 天 +20.2k）| **论文**: [arXiv:2508.02739](https://arxiv.org/abs/2508.02739) · AAAI 2026 已接收

Kronos 是首个面向金融 K 线（OHLCV）的开源基座模型，用 45+ 全球交易所数据训练，AAAI 2026 正式接收。两阶段架构：BSQ（Binary Spherical Quantization）tokenizer 将连续价格序列离散为 codebook，再用自回归 transformer 预测未来 K 线 token。

| 模型规格 | 参数量 | 状态 |
|---------|--------|------|
| Kronos-mini | 4.1M | 开源 |
| Kronos-small | 24.7M | 开源 |
| Kronos-base | 102.3M | 开源 |
| Kronos-large | 499.2M | 闭源 |

**关键细节**：代码仓库最后提交 2026-04-13（活跃的是模型/论文侧），但 GitHub Trending 近 28 天 +20.2k——社区热度来自模型实用性和金融 AI 赛道空白。已有社区项目（AxisJu/kronos-prediction-skills）基于它做 A 股预测工具链。

**为什么重要**：金融时序是 LLM 基座从未真正攻克的领域——文本驱动的金融模型缺乏对价格形态的直接感知。Kronos 把 K 线当作"金融语言"来做基座预训练，这个范式转移比模型本身更重要。MIT 协议 + AAAI 接收 + 社区衍生工具链，三要素齐备。

**风险**：代码更新停滞（近 7 个月无提交）；K 线预测的实盘有效性缺乏独立第三方验证；499M 最强版本未开源。

---

## 工具框架类

### Lightpanda — AI Agent 的浏览器层，v1.0.0 正式发布

**仓库**: [lightpanda-io/lightpanda](https://github.com/lightpanda-io/lightpanda) · **License**: AGPL-3.0
**本周Stars**: 41,183 ⭐ | **版本**: v1.0.0（2026-10-02）

Lightpanda 是用 Zig 从零编写的无头浏览器，专为 AI agent 设计而非人类浏览。v1.0.0 于 10 月 2 日发布，单二进制 188MB。

- **性能**：比 Chrome headless 快约 11 倍、内存省约 9 倍
- **协议**：CDP 兼容（Playwright/Puppeteer 可直接接入）、原生 MCP 服务器、WebDriver 支持
- **并发**：单服务器可跑 140 个并发浏览器实例
- **部署**：Docker / CLI / 服务端嵌入

**为什么重要**：当 Mage-VL-Cowork（本周论文，OSWorld-Verified 66.0%）这类 GUI agent 要在真实网页上执行任务时，浏览器的性能、成本和可控性成为瓶颈。Chrome headless 是为人类开发者调试设计的，而 Lightpanda 是为"一百个 agent 同时爬一百个页面"设计的——这是基础设施层面的代际差异。

**风险**：AGPL-3.0 协议，服务端嵌入需注意合规；JavaScript 兼容性仍在追赶 Chrome（不支持 WebGL 等重渲染场景）。

### FreeToken — 消费级显卡跑 290B+ MoE 的边缘推理引擎

**仓库**: [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) · **License**: Apache-2.0
**本周Stars**: 16,537 ⭐（~880/周）| **论文**: [arXiv:2608.16157](https://arxiv.org/abs/2608.16157)

FreeToken 来自 Berkeley / MIT（Song Han、Ion Stoica、Matei Zaharia 团队），核心命题：**MoE 模型的稀疏激活特性天然适合"专家放在不同设备上"的边缘部署**。

| 模型 | 硬件 | 实测速度 |
|------|------|---------|
| Qwen3.6-35B | RTX 4060 8GB | ~39 tok/s |
| DeepSeek-V4-Flash (284B) | RTX 5090 | 交互式可用 |
| GLM-5.2 (753B) | 单工作站 GPU | 交互式可用 |

**为什么重要**：K3.1 Pro 权重落地（896 experts / top-16）后，第一个问题就是"2.8T 怎么跑"。FreeToken 的 MoE 感知调度恰好是这个问题的答案——不需要 64 卡集群，把工作站上所有可用显存/内存/磁盘带宽联合起来跑大 MoE。Apache-2.0 + 桌面 App + CLI，"数据中心级智能在个人硬件上"从口号变成下载链接。

**风险**：边缘场景下的延迟和吞吐仍无法替代数据中心；对 MoE 以外的稠密模型不适用；K3.1 Pro 官方适配进度需跟进。

### ECC — Agent Harness 性能优化操作系统

**仓库**: [affaan-m/ECC](https://github.com/affaan-m/ECC) · **License**: MIT
**本周Stars**: 296,684 ⭐（日增 ~1.2k）| **创建**: 2026-01-18（268 contributors）

ECC（Everything Claude Code）自 v2.0 起定位已从"配置包"硬化为 **"The Agent Harness Operating System"**——agent 工具链的系统级性能优化方案。

- **规模**：67 个 agents、281 个 skills、94 个 command shims
- **核心模块**：hooks（生命周期钩子）、persistent memory、持续学习、AgentShield 安全扫描
- **多 harness 支持**：Claude Code（最佳）、Codex、OpenCode、Cursor、Antigravity
- **语言规则**：TypeScript / Python / Go / Swift 专项编码规范

**为什么重要**：ECC 是"harness 工程"叙事的源头和最大载体——9 个月 296K 星的增长曲线说明这不是短期热度。它把"如何调教 agent 工具链"从一个手艺活变成了可复用的系统工程：规划 → 构建 → 验证 → 记忆 → 安全扫描的全链路自动化。本周 RoboArchitect 论文（Stanford，24 分🏆）从学术侧独立验证了同一结论：harness 工程是 agent 能力的新瓶颈。

**风险**：体量膨胀带来的维护复杂度；部分 skills 质量参差需筛选；对非 Claude Code harness 的支持深度不均。

---

## Agent 效率工具类

### claude-mem — Agent 记忆的持久化层

**仓库**: [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) · **License**: Apache-2.0
**本周Stars**: 112,151 ⭐ | **活跃度**: 11-04 仍在提交

claude-mem 是 Claude Code 的持久化记忆插件：捕获每次会话中 agent 的行为 → 用 AI 模型压缩成语义摘要 → 注入后续会话的上下文。存储在本地 SQLite + Chroma，数据不出机器。

- **多客户端**：除 Claude Code 外已支持 Codex、Gemini、Copilot、OpenCode
- **安装**：`npx claude-mem install` 或 plugin marketplace
- **隐私**：本地运行，可选 hosted observer（可跳过）

**为什么重要**：Agent 记忆赛道的体量最大项目。在 Agent 从"单次调用"进化为"长期协作者"的过程中，跨会话记忆是最基础也最容易被忽视的基础设施。与本周 ASTC 论文（免训练上下文压缩，-50.68% 注意力对）形成方法论互补——ASTC 解决单次会话内的上下文膨胀，claude-mem 解决跨会话的知识持久化。

**风险**：官方竞品功能挤压（Claude Code 内置 auto memory 持续增强）；压缩过程消耗额外 token；Windows 支持历史问题。

### hallmark — 反 AI-Slop 设计引擎，续集仍在升温

**仓库**: [Nutlope/hallmark](https://github.com/Nutlope/hallmark) · **License**: MIT
**本周Stars**: 47,185 ⭐（W44 后一周 +7.8k）

hallmark 是 Together AI 开发者关系负责人 Nutlope 开源的反 AI-slop 设计技能，W44 入选后本周以更高增速回归。核心机制：为 AI 编码 agent（Claude Code / Cursor / Codex）提供结构化的设计约束，拒绝落入"蓝紫渐变 + 三卡片 + 无观点长文"的模型默认输出。

- **22 个手工主题**：纸张 / 印刷 / 织物 / 金属等"材质"级设计系统
- **57 道 slop-test 质量关**：输出前逐项检查反模式
- **4 个动词**：`build`（新建）/ `audit`（评分）/ `redesign`（重构）/ `study`（提取设计 DNA）
- **安装**：`npx skills add nutlope/hallmark`

**为什么重要**：一周 +7.8k 的增速比 W44 入选时更高，说明"反 AI slop"不是一次性话题而是持续痛点。hallmark 的解决方案不是"让模型更聪明"，而是用规则压缩模型的发挥空间——这个思路与本周 SecPO 论文（对抗训练用规则约束模型安全行为）在方法论上遥相呼应。

**风险**：主题库长期维护成本；对复杂交互式应用的覆盖有限；社区主题质量参差。

---

## 数据观察

### K3.1 Pro 权重落地的连锁反应

K3.1 Pro 权重 11-04 落地后，围绕它的工具链在本周集体就位：

| 层级 | 项目 | 作用 |
|------|------|------|
| 推理引擎 | vLLM / SGLang | day-0 支持 |
| 边缘部署 | FreeToken | 消费级硬件跑 MoE |
| 注意力加速 | LSA（论文） | 10M token 预填充 22.7× 加速 |
| 浏览器层 | Lightpanda | Agent 网页交互基础设施 |
| 记忆层 | claude-mem | 跨会话知识持久化 |
| Harness 层 | ECC | 工具链性能优化 |

**从 API 可用到自托管可行，中间的距离正在被基础设施层的分工细化所填补**。这是"开放权重"叙事从模型发布转向生态建设的转折点。

### Agent 基础设施的分工细化

本周 7 个项目恰好覆盖了 Agent 技术栈的 7 个层面：模型（K3.1 Pro）、垂直领域模型（Kronos）、浏览器（Lightpanda）、推理（FreeToken）、记忆（claude-mem）、harness（ECC）、设计质量（hallmark）。每个层面都在独立演进、独立积累 stars——**Agent 时代的"技术栈"不再是一个框架，而是一组可组合的基础设施**。

### 论文-开源联动密度

本周 8 篇精选论文中 5 篇附完整代码（🏆），三条主线（超长上下文注意力 / Agent 系统效率 / Agent 安全）与 7 个开源项目形成高密度联动——详见《论文-开源联动周报》。特别值得注意的是 LSA 的 SGLang 插件与 K3.1 Pro 的 vLLM/SGLang day-0 支持形成"论文→插件→模型"的落地链路，这是从学术到工程最短路径的范本。

---

## 推荐阅读

1. **[Kimi K3.1 Pro 技术博客](https://www.kimi.ai/blog/kimi-k3-1-pro)** — Moonshot 官方对后训练栈、联合 RL 跨数百下游领域的完整技术披露
2. **[FreeToken arXiv 论文 (2608.16157)](https://arxiv.org/abs/2608.16157)** — 边缘 MoE 推理的形式化定义与消费级硬件实测数据
3. **[Kronos arXiv 论文 (2508.02739)](https://arxiv.org/abs/2508.02739)** — BSQ tokenizer + 自回归 transformer 的金融时序基座方法论
4. **[Lightpanda v1.0.0 发布公告](https://github.com/lightpanda-io/lightpanda)** — Zig 无头浏览器的架构决策与 CDP/MCP 双协议设计
5. **[LSA 论文 (arXiv:2610.42147)](https://arxiv.org/abs/2610.42147)** — 隐空间层次聚类实现亚二次注意力，10M token 预填充 22.7× 加速的完整方法

---

*由 friday-report 任务自动生成 | intelligence-system*
*数据源：data/os-shortlist-2026-W45.md + data/paper-shortlist-2026-W45.md*
