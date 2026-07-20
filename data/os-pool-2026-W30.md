# 周一开源项目速览 · 2026-W30

> 本周聚焦：Kimi K3 发布、MCP 最终规范定档、Agent 生态进入"实用主义"阶段
> 采集时间：2026-07-20 10:00 CST
> 周次：W30 (2026-07-14 ~ 2026-07-20)

---

## 一、模型层 · 开源大模型新标杆

### 🔥 Kimi K3 — 月之暗面 7/16 发布，权重将于 7/27 开源
- **参数**：2.8T 总参数，Stable LatentMoE 架构（896 专家，激活 16 个）
- **亮点**：GPQA Diamond 93.5%，1M token 上下文，原生多模态（文本/图像/音频/视频）
- **许可**：Modified MIT，完整权重 2026-07-27 发布
- **定位**：长程 Agent 场景，目前 API 可用，即将成为史上最大开源权重模型
- **对比**：Artificial Analysis Intelligence Index 57 分，略高于 GLM-5.2 的 51 分

### 🥇 GLM-5.2 — 智谱 AI，当前可自托管的最佳开源模型
- **参数**：744B（激活 40B），MoE 架构
- **亮点**：Code Arena 盲测榜首，Terminal-Bench 82.7%，MIT 完全开源
- **定价**：$1.40/$4.40 per 1M tokens（输入/输出），性价比优于 Kimi K3
- **部署**：单节点 8×H100 或 4×MI300 可跑，Hugging Face 已可下载
- **训练硬件**：华为昇腾 + MindSpore，未使用 NVIDIA

### 🆕 Hy3 — 腾讯 Hunyuan 推理 Agent 模型
- **发布时间**：2026-07-02
- **GitHub**：Tencent-Hunyuan/Hy3
- **定位**：推理与 Agent 能力，成本与部署灵活性有竞争力

---

## 二、框架与协议层 · Agent 基础设施加速成熟

### 🔌 MCP 2026-07-28 最终规范 — 倒计时 8 天
- **里程碑**：Model Context Protocol 自 2024-11 发布以来最大的一次版本升级
- **核心变化**：
  - 协议层变为 **stateless**，支持无状态负载均衡，不再依赖 sticky session
  - MCP Apps：server 可返回沙箱化 HTML UI，不再局限于纯文本/JSON
  - Tasks 原语从核心规范移至可选扩展
  - 引入正式 Extensions 框架 + 12 个月弃用缓冲期
- **生态现状**：2,000+ 社区 server，OpenCode/Claude Code/Cursor/Windsurf 原生支持
- **治理**：2025-12 Anthropic 捐赠给 Linux Foundation 下的 Agentic AI Foundation（OpenAI、Block 联合创立，AWS/Google/Microsoft/Salesforce 背书）

### ⚔️ 协议格局：MCP vs A2A vs ACP
- **MCP**：工具/数据连接（USB-C for AI），企业 78% 已部署至少一个 MCP agent
- **A2A (Google)**：Agent-to-Agent 通信，跨系统边界委托任务
- **ACP (IBM)**：异步消息队列，适合大规模批处理
- **实践建议**：工具连接用 MCP，跨系统 agent 用 A2A，批处理用 ACP

---

## 三、工具与基础设施层 · Agent 周边生态

### 🛡️ T3MP3ST — 多 Agent 安全红队测试框架
- **发布时间**：2026-07-02 | **Stars**：3,900+
- **用途**：授权安全测试工作流，多 Agent 协作的渗透测试/红队演练
- **信号**：Agent 安全测试正在成为一个独立品类

### 🔬 OpenScience — 开源 AI 科学工作台
- **发布时间**：2026-07-03 | **Stars**：1,800+
- **定位**：面向科研人员的本地优先 AI 工作台
- **信号**：AI 工具从通用聊天向垂直领域工作台演进（同类项目：ai4s-research/open-science）

### 💰 token-diet — 编码 Agent 的 Token 节食工具
- **发布时间**：2026-07-03 | **Stars**：560+
- **用途**：降低编码 Agent 的 token 消耗，延长有效会话长度
- **背景**：Agent 会话越来越长，成本控制成为刚需

### 🎯 agent-chief — 本地 Agent 注意力管理层
- **发布时间**：2026-07-04 | **Stars**：310+
- **用途**：决定 Agent/告警/信息流何时值得打断用户
- **洞察**：Agent 的难点不仅是"做工作"，更是"在正确的时间打扰你"

### 📝 gzh-design-skill — Markdown 转排版 HTML
- **发布时间**：2026-07-01 | **Stars**：1,600+
- **用途**：将 Markdown 转为微信公众号/发布平台风格的精美 HTML
- **信号**：Agent skills 正在变成狭窄、实用的生产工具

### 🔄 claude-code-merge-queue — 并行 Claude Code Agent 协调
- **发布时间**：2026-07-02 | **Stars**：290+
- **用途**：本地并行运行多个 Claude Code agent 的合并队列
- **洞察**：多 Agent 并行是趋势，但协调基础设施才刚刚起步

### 🎮 GameBlocks — Agent 生成浏览器 3D 游戏的积木
- **发布时间**：2026-07-01 | **Stars**：330+
- **用途**：为编码 Agent 提供预定义 3D 游戏积木，加速原型生成

### 🔊 homerail — 语音优先的本地 Agent 编排运行时
- **发布时间**：2026-07-07 | **Stars**：300+
- **定位**：语音 + 可审计工作流，替代黑盒语音助手

### 📹 short-video-generator-AI — 长视频转短视频工作流
- **发布时间**：2026-07-01 | **Stars**：320+
- **功能**：亮点检测、字幕、翻译、配音一体化

---

## 本周信号总结

| 维度 | 关键趋势 |
|------|---------|
| **模型** | 开源首次可信替代闭源 API — Kimi K3 / GLM-5.2 已逼近 Claude Opus 4.8 |
| **协议** | MCP 7/28 最终版将奠定未来 12 个月 Agent 工具连接标准 |
| **工具** | Agent 从"能做"走向"好用" — 安全、成本、注意力管理成为新战场 |
| **生态** | 中国实验室（月之暗面、智谱、腾讯混元）成为开源模型核心贡献者 |

---

*采集来源：GitHub Trending、Artificial Analysis、techsy.io、MCP 官方博客、各大模型发布页*
