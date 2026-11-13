# AI 开源周报（2026 年第 W46 周）

> 生成时间：2026-11-13（周五）
> 覆盖周期：2026-11-09 ~ 2026-11-13
> 数据来源：周三开源短名单（7 项目）+ 周四论文短名单（8 篇）
> 本周主题：**K3.1 Pro 自托管现实检验** · **Skills 层平台之争**（google vs anthropic）· **Agent 感官与并行工程**

---

## 本周概览

| # | 项目 | 分类 | 一句话 | 本周最大变化 |
|---|------|------|--------|-------------|
| 1 | Kimi K3.1 Pro | 模型 | 权重放出一周后：无 GGUF、无 llama.cpp 支持、自托管门槛 610GB 起 | 从"权重落地"到"现实检验"，社区叙事完成反转 |
| 2 | agent-browser | 基础设施 | Vercel 出品 Rust 浏览器自动化 CLI，a11y tree + @e 引用 | 50,465 ⭐，2 天 +1,057，本周增速最快之一 |
| 3 | google/skills | 基础设施 | Google 官方 Agent Skills 框架，Trending 回榜 | 24,108 ⭐，与 anthropics/skills（190k）形成平台对峙 |
| 4 | claude-mem | 基础设施 | 跨会话持久记忆，已支持 15+ agent 客户端 | 116,669 ⭐，4,604 commits，持续高频提交 |
| 5 | worktrunk | 效率工具 | Git worktree 管理 CLI，为并行 AI agent 设计 | 12,487 ⭐，5,541 commits，Rust 单二进制 |
| 6 | OpenMausBot | 基础设施 | 开源 Grok Bot 替代品：一群有电脑的 AI 机器人 | 21,901 ⭐，2 天 +1,090，本周增速最快 |
| 7 | VibeVoice | 模型 | 微软开源语音 AI 全家桶（ASR/TTS/Realtime） | 57,127 ⭐，MIT，Trending 常客 |

**本周趋势一句话**：上周 K3.1 Pro 权重落地点燃了"自托管"叙事，本周社区迅速完成了第一轮现实检验——GGUF/llama.cpp 不支持、原生权重 1.56TB、最小可用量化需 610GB 内存，结论是"权重开放了，但你的机器跑不动"；与此同时，Agent 基础设施层在三个维度同时推进：感知（agent-browser 的 a11y tree）、执行环境（OpenMausBot 的 bot VM）、并行隔离（worktrunk 的 worktree），加上 google/skills 与 anthropics/skills 的 Skills 层平台之争，Agent 技术栈的"感官-四肢-记忆"分层正在加速成形。

---

## 论文-开源映射表（A-D 分类）

> 详细联动分析见 output/weekly-report-paper-os-2026-W46.md（含三大主题 + 联动矩阵）

**A类：论文 + 官方代码（3 篇）— 可立即复现**

| 论文 | 分数 | 联动开源项目 | 联动方式 |
|------|------|-------------|---------|
| AMP1 🏆 | 24 | OpenMausBot / agent-browser | 通用模型直接操控机械臂 → Agent 获得"手"的工程范式 |
| BitDecoding-FP4 🏆 | 23 | K3.1 Pro | FP4 KV cache 直接降低自托管推理成本 |
| QGPM 🏆 | 20 | K3.1 Pro | training-free 缓解 1M 上下文 lost-in-the-middle |

**C类：论文先行（5 篇）— 代码未随论文发布**

| 论文 | 分数 | 对应方向 | 跟进建议 |
|------|------|---------|---------|
| Phantom Consensus | 20 | 多 Agent 社会信号安全 | 多 agent 部署必读，关注 PHANTOM-Bench 释放 |
| RPEG | 20 | 推理模型训练流水线 | 256 卡 GH200 标杆，关注开源进度 |
| Knowing When to Intervene | 19 | Agent 干预因果评估 | 与 OpenMausBot 审批卡机制互为表里 |
| MCQ Safety | 18 | 安全评测方法论纠偏 | MCQ 格式使安全评估失真，评测设计需重审 |
| Procedures→Permissions | 18 | Skills 授权 | 直接引用 google/skills 作为授权监督信号 |

**D类：项目先行（7 个）— 暂无对应论文**：Kimi K3.1 Pro、agent-browser、google/skills、claude-mem、worktrunk、OpenMausBot、VibeVoice

**本周观察**：论文代码开放率 3/8（W45 为 5/8），C 类占比上升至 62.5%——NeurIPS 2026 截稿季刚过，大量工作尚未释放代码，后续跟进有价值。

---

## 🔥 重磅推荐

### Kimi K3.1 Pro — 权重落地一周后的自托管现实检验

**来源**: [Hugging Face](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · 权重发布 2026-11-04 · 本篇为 W45 重磅的续篇
**License**: Kimi K3.1-Pro License（MIT 风格主体 + 两条附加条款：>$20M MaaS 营收需单独协议、>100M MAU 需署名）

W45 记录了 K3.1 Pro 权重如期上架的历史时刻。一周过去，社区的第一轮自托管实践给出了冷静得多的答案。

**三个硬核事实**：

1. **没有 GGUF，llama.cpp 跑不了**。llama.cpp 尚未支持新的 `kimi_k31` 架构。Hugging Face 上搜索不到任何官方或社区 GGUF 仓库。模型卡推荐的只有 vLLM、SGLang 和 TokenSpeed——全部是数据中心级方案。
2. **1.56 TB 原生权重，96 个 safetensors 分片**。权重已是 MXFP4 训练格式（MXFP8 激活），再量化空间有限——假设性的 2-bit 切分仍需约 780GB，且不存在这样的文件。参考 K3 的 GGUF 对照表，最小可用量化（UD-IQ1_S，594GB 文件）需约 610GB 内存+显存合计。
3. **唯一的桌面级实验几乎不可用时**。Inferencer Labs 发布了一个 220GB MLX 重打包版（专家卸载到存储），在 M3 Ultra 512GB 上测试——速度字段写的是 "~ tokens/s"，数字留空。

**成本数学**（以每月 2 亿输入 + 2000 万输出 token、60% 缓存命中计）：

| 方案 | 月成本 | 备注 |
|------|--------|------|
| K3.1 Pro API | ~$384 | 缓存输入 $0.20/M，标准输入 $2/M，输出 $10/M |
| K3.1 Pro Highspeed API | ~$744 | 2 倍单价换 2-3× 速度 |
| 自托管（租用） | ~$57,600/月 | benchlm.ai 数据（K3 同规模参考） |
| 自托管（购入） | 8× H100 起步加载，生产环境 64+ 加速器 | 官方 vLLM 配方 |

**结论**：API 月调用量在数十亿 token 以下时，自托管没有经济性。开放权重的真正价值不在"跑在自己机器上"，而在**选择权**——竞争服务商可以托管 K3.1 Pro 并在价格上有竞争力（已有第三方托管商接入），数据主权管辖区可以自证合规，下游可以基于权重做领域微调。

**协议细节**：主体为 MIT 风格，但两条附加条款值得注意——年营收超 $20M 的 MaaS 提供商需与 Moonshot 单独签约（类似 LLaMA 的商用阈值策略）；面向 >100M MAU 的产品需署名 Moonshot AI。对绝大多数开发者而言实际等效 MIT，对云厂商则留有商业化口子。

**技术规格回顾**：2.8T 总参 / 104B 激活 MoE（896 experts，top-16 路由）、1M token 上下文、69 KDA 层 + 24 Gated DSA 层。API 定价 $2/$10 per M tokens。

**为什么重要**：K3.1 Pro 的自托管检验是 2026 年"开放权重"叙事的一个缩影——权重发布 ≠ 可用性落地。从 GGUF 缺位到许可条款，从硬件门槛到成本数学，"开放权重"的实际含义正在从口号细化为工程问题。这一周社区做的事情，就是把这个模糊的口号翻译成了一张具体的检查清单。

**风险**：llama.cpp 支持 `kimi_k31` 的时间表未知；Unsloth 等社区量化团队尚未跟进（K3 的 GGUF 用了约 3 个月）；许可条款的非标准性可能在企业采用时增加法务审核成本。

---

## 工具框架类

### vercel-labs/agent-browser — 给 Agent 装上眼睛的 Rust CLI

**仓库**: [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) · **License**: Apache-2.0
**本周Stars**: 50,465 ⭐（2 天 +1,057）| **创建**: 2026-01-11 | **最后提交**: 2026-11-13（当天）

agent-browser 是 Vercel Labs 出品的浏览器自动化 CLI，专为 AI agent 设计。核心思路：不让 agent 看像素截图，而是**给 agent 看可访问性树（a11y tree）**。

```
$ agent-browser open example.com
$ agent-browser snapshot -i     # 交互元素带 @e 引用
$ agent-browser click @e1       # 按引用精确交互
$ agent-browser get url         # 获取当前页面 URL
$ agent-browser close
```

- **Rust 单二进制**，性能极快
- **a11y tree snapshot**：元素以 `@e1` `@e2` 引用编号，agent 不需要解析 HTML/CSS，直接操作语义化节点
- **安装**：`npm install -g agent-browser` / `brew install agent-browser` / `npx agent-browser`
- **活跃**：当天仍在提交，570 open issues 处理中

**为什么重要**：在 GUI agent 的技术路线之争中，"像素派"（截图 + 视觉模型）和"DOM 派"（HTML 解析）各有拥趸，agent-browser 代表了第三路线——**a11y tree 天然是结构化的、语义化的、对 LLM 极度友好的输入格式**。Vercel 的品牌背书 + 50K 星的社区体量，使这条路线在与 Lightpanda（W45 覆盖的 Zig 无头浏览器）等项目的竞争中占据了 CLI 易用性的制高点。本周论文 #1（AMP1，Apple 的 agentic manipulation）从学术侧证明了"给 agent 结构化环境表示"的价值——两者在方法论上完全一致。

**风险**：a11y tree 对复杂 Canvas/Shadow DOM 场景的覆盖有限；与 Playwright 等成熟方案的功能重叠度需持续评估。

### google/skills — Google 官方 Skills 框架，Trending 回榜续涨

**仓库**: [google/skills](https://github.com/google/skills) · **License**: Apache-2.0
**本周Stars**: 24,108 ⭐ | **创建**: 2026-03-31 | **最后提交**: 2026-11-12

google/skills 是 Google 官方的 Agent Skills 仓库，为 Gemini 及 Google 生态产品提供标准化技能包。首发于 2026 年 3-4 月（Cloud Next 期间），本周再次登上 GitHub Trending 并持续涨星。

**Skills 层平台之战**：这是本周最重要的叙事之一。Anthropic 在 2025 年 10 月推出 Agent Skills 概念并开源 anthropics/skills（当前约 190K ⭐），Google 随后跟进推出自己的 Skills 框架。两个生态的技能格式高度相似——都是"过程性知识"（how-to）而非"声明性知识"（what-is），都以文件夹 + SKILL.md 为最小单元，但分属不同的模型生态。

| 维度 | anthropics/skills | google/skills |
|------|-------------------|---------------|
| 星数 | ~190K | 24,108 |
| 生态绑定 | Claude / MCP | Gemini / Google Cloud |
| 许可 | Apache-2.0 | Apache-2.0 |
| 方向侧重 | 通用 agent 技能 | Google 产品与技术栈 |

**为什么重要**：Skills 正在成为 agent 时代的"应用商店"——谁定义技能格式，谁就定义了 agent 的能力扩展标准。本周论文 #8（Procedures→Permissions，arXiv:2611.08905）进一步抬升了这条赛道的重要性：论文证明 Skills 中的过程性知识可以直接作为授权监督信号，工具权限精度提升 13.4pp——**Skills 不只是能力扩展单元，还是安全授权的依据**。当学术侧开始围绕 Skills 做安全研究时，这个赛道的战略价值已经超越"提示词模板"的范畴。

**风险**：Google 侧的社区贡献活跃度仍远低于 Anthropic 生态（24K vs 190K）；两大格式之间的互操作性尚无标准；对非 Google/Anthropic 模型的中立性待观察。

### milind-soni/OpenMausBot — 开源 Grok Bot 替代品：一群有电脑的 AI 机器人

**仓库**: [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) · **License**: Apache-2.0
**本周Stars**: 21,901 ⭐（2 天 +1,090）| **创建**: 2026-08-11 | **最后提交**: 2026-11-13（当天）

OpenMausBot 是 2026 年下半年"个人 AI agent 产品大爆发"的直接回应。xAI 的 Grok Bot、Meta 的 Muse、OpenAI 的 dots、Manus 的 Cue——四款闭源个人 agent 产品在七周内密集发布，全部把模型、计算和数据锁在厂商侧。OpenMausBot 把这个形态开源了：

- **每个 bot 都是真 agent**：底层跑 Claude 或 Codex CLI（用你自己的登录和订阅），有独立人格、独立模型选择、独立云桌面
- **Local-first**：harness 服务器在 127.0.0.1，所有数据在 `~/.openmausbot`
- **Agents with hands**：每个 bot 可分配云 Linux 桌面、隔离 Local VM、或（opt-in 后）直接操控宿主机 + 500+ Composio 应用集成
- **审批卡机制**：关键操作需人工批准——这与本周论文 #6（Knowing When to Intervene）的"因果干预评估"形成学术-工程呼应
- **桌面客户端**：macOS（Apple Silicon & Intel，签名公证 .dmg）/ Windows / Ubuntu

**为什么重要**：21.9K 星 + 每天仍在高速增长 + 1031 个 open issues（极高的社区参与度），说明这个项目的火热程度。它不是"又一个聊天客户端"，而是**把 agent 的完整形态——人格 + 记忆 + 计算机 + 审批流程——包装成 IM 通讯录的范式**。当 AMP1 论文（Apple，24 分🏆）在实验室证明通用 AI 模型可以直接操控物理环境时，OpenMausBot 把同样的事情带到了消费级桌面——给每个 agent 一台云电脑。

**风险**：1031 个 open issues 说明项目处于快速迭代期，API 稳定性存疑；安全边界（宿主机控制）依赖显式 opt-in，但社区插件的安全性需要额外审查；xAI/OpenAI 官方客户端的 API 变动可能随时破坏兼容性。

---

## Agent 效率工具类

### claude-mem — 跨会话持久记忆的事实标准

**仓库**: [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) · **License**: Apache-2.0
**本周Stars**: 116,669 ⭐ | **4,604 commits** | **最后提交**: 2026-11-13（当天）

claude-mem 继续坐稳 agent 记忆赛道的头部位置。本周关键变化：**已明确支持 OpenClaw**——项目 README 现在有专门的 OpenClaw Gateway 安装命令（`curl -fsSL https://install.cmem.ai/openclaw.sh | bash`），提供持久记忆插件、Telegram/Discord/Slack 实时观察 feed。

架构核心：
- **Hooks 捕获**：agent 工作时，hooks 捕获每次工具调用
- **Observer 记录**：第二个 agent 将活动压缩成语义化 observation
- **渐进式披露**：新会话开始时，agent 获得紧凑索引，仅在需要时展开完整详情
- **本地存储**：SQLite + Chroma 混合搜索，数据不出机器
- **多客户端**：Claude Code、OpenClaw、Codex、Gemini、Copilot、OpenCode 等 15+

**为什么重要**：116K 星 + 4600 commits 的体量，已经是基础设施级项目而非"插件"。v5 架构的 worker service + HTTP API 意味着它可以脱离任何单一 agent 客户端独立运行。当 agent 从"单次调用"进化为"长期协作者"，跨会话记忆就是地基——claude-mem 是目前唯一同时做到多客户端覆盖 + 本地隐私 + 活跃迭代的方案。本周论文 #3（Phantom Consensus）揭示了多 agent 系统中社会信号的污染风险，这在方法论上提醒了记忆系统的设计者：**注入的上下文必须经过来源可信度筛选**。

**风险**：压缩过程消耗额外 token；免费试用后的订阅模式可能抬高个人用户门槛；Anthropic 官方 auto memory 功能持续增强带来的挤压。

### worktrunk — 并行 AI agent 的 Git worktree 管理

**仓库**: [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) · **License**: 自定义（FSF 认可）
**本周Stars**: 12,487 ⭐ | **5,541 commits** | **最后提交**: 2026-11-13（当天）

worktrunk 是 Rust 编写的 Git worktree 管理 CLI，创始人 Maximilian 将其定位为"为并行 AI agent 工作流设计"。README 直言：*"AI agent 可以无人值守处理长时间任务，因此可以同时管理 5-10+ 个并行任务——但 Git 原生 worktree 的 UX 太笨拙了。"*

三个核心命令让 worktree 像分支一样简单：

```bash
wt switch feat                    # 创建 worktree 并切换
wt switch -c -x claude feat       # 创建 worktree + 启动 Claude agent
wt list                           # 带 CI 状态/diff/PR 预览的列表
wt merge                          # squash + rebase + merge + 清理，一条命令
```

进阶能力：hooks 自动化（创建/pre-merge/post-merge）、LLM 生成 commit message、copy-on-write 构建缓存（APFS/btrfs/XFS）、交互式选择器、PR 直达 checkout。

**为什么重要**：12.5K 星不算最大，但 5,541 commits 的提交密度（超过 claude-mem 的 4,604）表明这是一个极度活跃的项目。它的洞察非常精准：**并行 agent 的根本瓶颈不是模型能力，而是状态隔离**——当 5 个 agent 同时改一个仓库，git worktree 是最简单的隔离方案，但 git 的 worktree UX 是为人设计的（需要输入三次分支名），不是为 agent 设计的。worktrunk 把这个 UX 压缩到了一次命令。本周论文 #4（RPEG）从学术侧关注了同类问题——大规模训练流水线的并行执行——两者共享同一个方法论内核：**并行化的效率取决于执行图的调度质量，而调度质量取决于抽象层的简洁度**。

**风险**：Rust 构建对非技术用户有一定门槛；Windows 支持（Winget/git-wt）相对较新；与 GitHub 官方 CLI 的功能边界需要用户自行判断。

---

## 模型与算法类

### microsoft/VibeVoice — 开源语音 AI 平台持续霸榜

**仓库**: [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) · **License**: MIT
**本周Stars**: 57,127 ⭐ | **创建**: 2025-08-25

VibeVoice 是微软研究院的开源语音 AI 项目，本周再次出现在 Trending 榜单上。项目已形成完整模型家族：

| 模型 | 功能 | 规格 |
|------|------|------|
| VibeVoice-ASR-7B | 单遍 60 分钟长音频转录，说话人分离 + 时间戳 + 内容 | 50+ 语言，已集成 Transformers |
| VibeVoice-ASR-Streaming | 流式转录，10 语言 + 自定义热词 | 2026-09-03 发布 |
| VibeVoice-ASR-BitNet | 边缘 CPU 推理引擎（I8_S + I2_S 异构量化） | 4.62GB → 1.58GB，3+ CPU 线程实时推理 |
| VibeVoice-Realtime-0.5B | 流式文本输入实时 TTS | 9 语言多语言声音 + 11 种英语风格 |
| VibeVoice-TTS-1.5B | 90 分钟多说话人长音频合成 | ICLR 2026 Oral |

核心技术：7.5Hz 超低帧率连续语音 tokenizer（最高 3200× 压缩）、LLM backbone + diffusion head 的 next-token diffusion 框架。

**为什么重要**：两件事使 VibeVoice 持续保有热度。其一，**ASR-BitNet 把边缘部署变成了纯 CPU 问题**——1.58GB 模型、RTF < 1、无需 GPU，意味着笔记本和 IoT 设备都能跑企业级语音识别，与本周论文 #2（BitDecoding-FP4，FP4 KV cache 推理加速）在"低精度推理"方法论上互为印证。其二，TTS 论文被 ICLR 2026 接收为 Oral，学术侧背书坚实。值得注意的是，TTS 原始代码因滥用问题于 2025 年 9 月从仓库移除——**这个项目正在探索"开放研究但限制使用"的中间路线**，其治理模式本身也是一个值得关注的社会实验。

**风险**：TTS 代码不可用（仅有论文和文档）；ASR 对中文方言和长音频的鲁棒性需独立验证；与 Whisper 生态的兼容性仍在完善。

---

## 数据观察

### 本周增速榜：agent-browser 与 OpenMausBot 领跑

| 项目 | 周三星数（11-11） | 周五星数（11-13） | 2 日增速 |
|------|------------------|------------------|---------|
| agent-browser | 49,408 | 50,465 | **+1,057** |
| OpenMausBot | 20,811 | 21,901 | **+1,090** |
| claude-mem | 115,922 | 116,669 | +747 |
| google/skills | 23,840 | 24,108 | +268 |
| worktrunk | 12,417 | 12,487 | +70 |
| VibeVoice | 56,985 | 57,127 | +142 |

两个增速最快的项目恰好代表了 Agent 技术栈的两端：agent-browser 解决"Agent 怎么看世界"（感知层），OpenMausBot 解决"Agent 怎么活在你的电脑里"（执行环境层）。加上 claude-mem（记忆层）和 worktrunk（并行隔离层），四个项目共同覆盖了 Agent 基础设施的四个关键切面。

### K3.1 Pro 自托管一周：叙事从"能不能跑"到"值不值得跑"

W45 的悬念是"权重能不能落地"，W46 的答案是"落地了，但大多数机器跑不动"。一周内的关键数据：

- Hugging Face 下载量 5 天 18,000+——收藏的人很多，跑起来的人极少
- 无 GGUF / 无 llama.cpp 支持——社区量化（Unsloth）尚未跟进
- API  vs 自托管成本差距约 150 倍（$384/月 vs $57,600/月）——在中低用量下自托管没有经济合理性
- 开放权价的真正价值：**选择权**（多供应商托管竞争、数据主权、下游微调），而非 DIY 推理

### 论文代码开放率回落

W45 为 5/8（62.5%），本周降至 3/8（37.5%）。NeurIPS 2026 截稿季后大量论文尚未释放代码，C 类（论文先行）占比上升——未来 2-4 周是跟踪这些论文代码释放的时间窗口，尤其 Phantom Consensus（PHANTOM-Bench）和 Procedures→Permissions（直接引用 google/skills）。

---

## 推荐阅读

1. **[How Much VRAM to Run Kimi K3 and K3.1 Pro? (freakyjolly, 2026-10-24)](https://freakyjolly.com/kimi-k3-1-pro-run-locally/)** — K3/K3.1 Pro 自托管硬件需求的最完整对照表，含 GGUF 各级别量化内存需求和硬件方案对比
2. **[Kimi K3.1 Pro Open Weights: Self-Hosting Guide (kissapi, 2026-11-05)](https://kissapi.ai/blog/kimi-k3-1-pro-open-weights-self-host-guide-2026.html)** — API vs 自托管成本数学的逐步推导，含 Highspeed 变体对比
3. **[Can I Run Kimi K3.1 Pro Locally? (openclawdc, 2026-11-04)](https://openclawdc.com/blog/can-i-run-kimi-k3-1-pro-locally/)** — 1.56TB 权重的现实检验，含 Inferencer Labs MLX 实验的空速度字段截图
4. **[VibeVoice Complete Guide (sacesta, 2026-04-13)](https://www.sacesta.com/our-work/blog/what-is-vibevoice-beginners-guide-2026)** — VibeVoice 全家桶技术架构解析，含 7.5Hz tokenizer 和 next-token diffusion 详解
5. **[BitDecoding-FP4 arXiv 论文 (2611.09825)](https://arxiv.org/abs/2611.09825)** — FP4 KV cache 算法-系统协同设计，B300 吞吐 2.4-3.0×，对 K3.1 Pro 自托管成本有直接参考价值

---

*由 friday-report 任务自动生成 | intelligence-system*
*数据源：data/os-shortlist-2026-W46.md + data/paper-shortlist-2026-W46.md*
