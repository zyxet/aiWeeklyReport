# AI 开源周报（2026 年第 W44 周）

> 生成时间：2026-10-30（周五）
> 覆盖周期：2026-10-26 ~ 2026-10-30
> 数据来源：周三开源短名单（7 项目）+ 周四论文短名单（8 篇）
> 本周主题：**开放权重三连发**（Muse Spark Open / Nemotron 3.5 Super VL / FLUX 3 Klein 同日开源）· **Kimi K3.1 Pro 开源登顶** · **OpenCode 2.0 重写架构**

---

## 本周概览

| # | 项目 | 分类 | 一句话 | 本周最大变化 |
|---|------|------|--------|-------------|
| 1 | Kimi K3.1 Pro | 模型 | 2.8T MoE / 104B active，Terminal-Bench 4.0 开源 #1 | 10-23 发布，11-04 放权重，API 已可用 |
| 2 | Muse Spark Open | 模型 | Meta 816B / 42B active，两台 Mac Studio 本地跑 | 10-15 放权重，MLX 分布式推理范式确立 |
| 3 | Nemotron 3.5 Super VL | 模型 | NVIDIA 120B / 12B active 多模态 MoE，SWE-bench 71.10 | 10-15 发布，vLLM day-0，OpenMDW 许可 |
| 4 | FLUX 3 Image Klein | 模型 | BFL 5.6B 文生图+编辑+多参考，8GB VRAM 可跑 | 10-15 开源，消费级硬件可本地部署 |
| 5 | llm-d 1.0 | 框架 | CNCF Sandbox 推理路由，KV-cache 感知调度 | 5,063 ⭐，企业级 LLM 服务标准化 |
| 6 | OpenCode 2.0 | 工具 | 常驻 daemon 架构重写，月活 1,600 万+ | 222,474 ⭐，三端共享会话 |
| 7 | hallmark | 工具 | 反 AI-slop 设计引擎，50 套手工主题 | 42,335 ⭐，10-27 GitHub Trending #1 |

**本周趋势一句话**：10 月 15 日的"开放权重三连发"（Muse Spark Open / Nemotron 3.5 Super VL / FLUX 3 Klein）在本周持续发酵，三家公司在三种不同路线（超大 MoE 本地推理 / 企业级多模态 Agent / 消费级图像生成）上同时推进"开放权重可用性"边界；Kimi K3.1 Pro 紧随其后以 65.7% Terminal-Bench 4.0 刷新开源 Agent 编码上限。工具侧，OpenCode 2.0 的 daemon 架构重写和 hallmark 的反 AI-slop 设计引擎分别代表了"AI 编程工具工程化"与"AI 生成内容质量控制"两个方向的极端。

---

## 🔥 重磅推荐

### Kimi K3.1 Pro — 开源 Agent 编码新上限

**仓库/来源**: [Moonshot AI](https://moonshot.ai) · 模型发布 2026-10-23
**License**: 权重即将开放（预计 2026-11-04）
**本周Stars趋势**: API 已可用，权重发布倒计时中

Kimi K3.1 Pro 是 Moonshot AI 于 10 月 23 日发布的旗舰模型，2.8T 总参数 MoE 架构、每 token 激活 104B，支持 1M 上下文。核心数据：

- **Terminal-Bench 4.0 达 65.7%，开源模型 #1**，超越此前所有开放权重对手
- **Code Arena WebDev 排名第 8**（1,692 分），进入全模型前十
- API 定价 $2 / $10 per M tokens（输入/输出），权重预计 11 月 4 日释放

**为什么重要**：在 Agent 编码赛道上，开源与闭源的差距正在以"周"为单位缩小。K3.1 Pro 的 65.7% 不仅是一个数字——它意味着开源 Agent 已经跨过了"能用"到"好用"的临界点。等权重正式放出，自托管 Agent 编码的成本结构将彻底改变。

**风险**：2.8T 参数规模对推理基础设施要求极高；API 定价在当前市场中属于中高端。

---

### Muse Spark Open — Meta 的 816B 豪赌与 Apple 的意外红利

**仓库/来源**: [Meta AI](https://ai.meta.com) · [Hugging Face](https://huggingface.co/meta-models) · 2026-10-15
**License**: Muse Model License（商用需署名"Built with Muse Spark Open"，MaaS 营收超 $20M 需单独协议）

Meta 在 10 月 15 日放出了 816B 参数的 Muse Spark Open——MoE 架构、42B active、1M 上下文、原生多模态输入（文本/图像/视频/音频）。这不是一个"下载到笔记本就能跑"的模型，但"谁能跑"的答案比想象中更有趣：

| 部署方式 | 硬件 | 实测速度 |
|---------|------|---------|
| llama.cpp Q2_K | 单台 M3 Ultra 512GB | ~18 tok/s（测试可用） |
| MLX 双机流水线 | 2× M5 Ultra 512GB | 15.74 tok/s |
| MLX 双机张量并行 | 2× M5 Ultra 512GB | 24.99 tok/s |
| MLX 四机张量并行 | 4× M5 Ultra 512GB | 36.73 tok/s |
| NVFP4 云端 | 单节点 8× H200 | 生产可用 |

**关键数据**：256 experts / top-8 路由；NVFP4 权重 ~700GB，BF16 ~2TB。编码能力上 Terminal-Bench 2.1 76.4、DeepSWE 1.1 60——**低于 GLM 5.3 和 Kimi K3，但安全性领先**（StrongREJECT v2 自适应攻击得分显著更低）。

**为什么重要**：Meta×Apple 的合作让"两台桌面工作站跑前沿模型"从幻想变成可复现的现实。Apple 官方发布 MLX 分布式推理技术报告（machinelearning.apple.com），首次系统展示了 pipeline parallel 与 tensor parallel 在消费级硬件上的 trade-off。对"自托管 vs 调用 API"的决策者来说，这是迄今最有参考价值的实测数据。

**风险**：双机 M5 Ultra 参考配置成本 $30,000+；Muse Model License 的商用条款需要法务审核；编码性能并非开源最强。

---

## 工具框架类

### OpenCode 2.0 — 从 CLI 到常驻 Daemon

**仓库**: [anomalyco/opencode](https://github.com/anomalyco/opencode) · **License**: MIT
**本周Stars**: 222,474 ⭐ | **月活**: 1,600 万+

OpenCode 2.0 完成了从"终端 CLI 工具"到"常驻后台 daemon"的架构重写。核心变化：

- **常驻进程**：编辑器、终端、浏览器三端共享同一会话状态，不再每次启动冷加载
- **`@opencode/sdk`**：程序化控制接口，允许外部工具与 agent 会话深度集成
- **Code Mode**：面向代码审查和批量重构的专用模式

**为什么重要**：当 AI 编程工具月活达到 1,600 万，"启动速度"和"会话隔离"变成真正的工程瓶颈。Daemon 化意味着 agent 可以成为开发环境的常驻公民，而非按需调用的外部进程。这是 AI 编程工具从"助手"进化为"基础设施"的标志。

### llm-d 1.0 — CNCF 加持的推理路由

**仓库**: [llm-d/llm-d](https://github.com/llm-d/llm-d) · **License**: Apache 2.0
**本周Stars**: 5,063 ⭐ | **健康分**: 82 | **Commits**: 3,280 | **Contributors**: 813

llm-d 于 2026 年 3 月 12 日进入 CNCF Sandbox，本周 1.0 版本持续迭代。核心能力：

- **KV-cache 感知路由**：将请求调度到已缓存相关上下文的实例，显著降低 TTFT
- **Gateway API Inference Extension**：基于 Kubernetes 标准的推理服务入口
- **Prefill/decode 分离**：针对大上下文场景的资源优化

**为什么重要**：当企业开始同时部署多个开源模型（本周就有三个新模型要评估），推理层的路由和调度成为刚需。llm-d 是 CNCF 在这个方向上的押注，正在从"实验项目"变成"事实标准"。

### hallmark — 反 AI-Slop 设计引擎

**仓库**: [Nutlope/hallmark](https://github.com/Nutlope/hallmark) · **License**: MIT
**本周Stars**: 42,335 ⭐（日增 ~2,000+）| 10-27 GitHub Trending #1

hallmark 是一个面向 Claude Code / Cursor / Codex 的设计技能（skill），核心思路是**用规则约束防止 AI 生成千篇一律的网页**：

- **50 套手工主题**（v2）：每套是一个"材质"（纸张/印刷/织物/金属……），包含成品页面截图、调色板、组件规范和纹理——而非"布局模板"
- **sloplint.mjs**：在 8 个视口宽度下渲染页面并进行 lint 检查，再由 subagent 以"新鲜眼光"审查
- **755 张开放许可照片**：按主题自动选用，页面上标注署名
- **自包含输出**：每个页面是独立的 HTML+CSS 文件，决策记录在 CSS 首条注释中

**为什么重要**：当 AI 生成网页已经成为新常态，"AI slop"（蓝紫渐变、千篇一律的 hero section、没有观点的长文）成为新的公害。hallmark 不试图让 AI"更聪明"，而是用 50 个精心手工设计的材质约束 AI 的发挥空间——这个思路本身就是对"AI 创造力"的一种独到回应。

---

## 模型与算法类

### Nemotron 3.5 Super VL — NVIDIA 的企业级多模态 Agent

**来源**: [NVIDIA](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/) · 2026-10-15
**License**: OpenMDW License v1.1（开放权重）
**支持**: vLLM day-0 / NeMo 后训练 / DGX Spark 128GB

| 指标 | 分数 |
|------|------|
| SWE-bench Verified | 71.10 |
| SWE-bench Pro | 51.78 |
| Terminal-Bench 2.1 | 66.70 |
| LiveCodeBench v6 | 88.22 |
| GPQA Diamond | 89.52 |
| CharXiv（图表推理） | 80.8%（+Python 84%） |
| 上下文窗口 | 1M tokens |

120B 总参 / 12B active 的 MoE，混合 Mamba+Attention 架构，内置 multi-token prediction 草稿器。支持文本、图像、文档、视频四种输入，输出文本。

**为什么重要**：Nemotron 3.5 Super VL 的设计哲学是"一个模型替代文本+视觉双模型栈"。在企业 Agent 场景中（读截图→查 PDF→对照政策→调工具→输出结构化结果），每次模型切换都是上下文丢失的风险点。SWE-bench Verified 71.10 也证明了它不只是"能看图"，编码能力同样在线。

### FLUX 3 Image Klein — 消费级硬件的 4K 图像生成

**来源**: [Black Forest Labs](https://bfl.ai/models/flux-3-image-klein) · 2026-10-15
**License**: FLUX Kommunity License（年营收 <$5M 免费商用）
**API 定价**: $0.009 / 1K image

5.6B 参数，三种能力统一在同一组权重中：
- **文生图**：原生 4K 分辨率
- **指令编辑**：自然语言修改任意区域，未指定区域像素不变
- **多参考生成**：单次最多 10 张参考图，保持角色/风格/产品一致性
- **坐标框布局**：0-1000 网格坐标精确控制元素位置

**INT8 量化版可在 8GB VRAM 消费级显卡运行**，蒸馏版 16 步出图。BFL API 实测 1MP 图像 4 秒生成。

**为什么重要**：FLUX 3 Image Klein 把"前沿图像生成+编辑+多参考"压缩到了 RTX 3060 能跑的规模。对于需要数据主权（不把图片发到云端）或微调定制的团队，这是目前性价比最高的开放权重方案。

---

## 数据观察

### 开放权重"可用性"军备赛

本周三个同日（10-15）发布的开放权重模型恰好覆盖了三个完全不同档位：

| 模型 | 参数 | 最低部署门槛 | 目标用户 |
|------|------|-------------|---------|
| Muse Spark Open | 816B / 42B active | 2× 512GB Mac Studio 或 8× H200 | 有基础设施的组织 |
| Nemotron 3.5 Super VL | 120B / 12B active | 单节点企业级 GPU | 企业 AI 团队 |
| FLUX 3 Image Klein | 5.6B | 8GB VRAM 消费级显卡 | 个人开发者 / 初创公司 |

加上 Kimi K3.1 Pro（2.8T / API 可用 / 权重 11-04 放出），**"开放权重"已经覆盖了从个人工作站到超算集群的全光谱**。这一趋势的直接后果是：闭源 API 的定价压力将持续增大，而推理基础设施（llm-d 类路由、MLX 分布式、vLLM day-0 支持）成为新的竞争焦点。

### Agent 编码能力：开源正在逼近闭源

- Terminal-Bench 4.0：Kimi K3.1 Pro 65.7%（开源 #1）
- Terminal-Bench 2.1：Muse Spark Open 76.4 / Nemotron 3.5 Super VL 66.70
- SWE-bench Verified：Nemotron 3.5 Super VL 71.10

三个模型、三个 benchmark、三种架构——开源 Agent 编码能力已经在多个维度跨过"生产可用"阈值。论文侧（见联动周报），Agent S4 以 1.5% 成本达到 OSWorld V2 SOTA，进一步压低了 Agent 进化的门槛。

### 论文-开源联动密度

本周 8 篇精选论文中 6 篇附完整代码（🏆），其中 RSIHub（HF ⭐186）已具备直接复用条件。Agent 自我进化（Agent S4 / RSIHub）与本周开源的 Agent 编码模型（K3.1 Pro / Nemotron）形成方法论与基础设施的互补——详见《论文-开源联动周报》。

---

## 推荐阅读

1. **[Apple MLX 分布式推理技术报告](https://machinelearning.apple.com/research/mlx-distributed-inference)** — 首次系统披露 pipeline parallel vs tensor parallel 在 Mac Studio 集群上的实测数据，是本地部署超大模型的必读参考
2. **[NVIDIA Nemotron 3.5 Super VL 技术博客](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/)** — 混合 Mamba-Transformer MoE + multi-token prediction 的训练与推理技术细节
3. **[vLLM day-0 支持公告](https://vllm.ai/blog/2026-10-15-nemotron-3-5-super-vl-vllm)** — 新模型如何在发布当天完成推理引擎适配
4. **[hallmark 仓库](https://github.com/Nutlope/hallmark)** — 50 个手工设计主题的完整目录与 sloplint 管线实现
5. **[Agent S4 论文 (arXiv:2610.28601)](https://arxiv.org/abs/2610.28601)** — Meta-agent 群体进化自动构建工具接口，1.5% 成本达到 OSWorld V2 SOTA

---

*由 friday-report 任务自动生成 | intelligence-system*
*数据源：data/os-shortlist-2026-W44.md + data/paper-shortlist-2026-W44.md*
