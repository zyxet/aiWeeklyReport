# AI 开源周报 · 2026-W31

> 📅 2026-07-25 ~ 2026-07-31  
> 🏷️ 本期共 7 个入选项目 · 4 篇深度论文联动  
> 📝 编辑：intelligence-system 自动周报生成系统

---

## 📌 重磅推荐

### 1. codebase-memory-mcp — 代码知识图谱的「极速引擎」

**DeusData / MIT / ⭐ 36,295**

| 维度 | 数据 |
|------|------|
| 核心语言 | C（纯静态二进制，零依赖） |
| 支持语言 | 158 种 |
| 索引速度 | Linux 内核（28M LOC, 75K 文件）→ 3 分钟 |
| 查询延迟 | 结构查询 <1ms |
| Token 节省 | 99.2%（~3,400 vs ~412,000 tokens） |
| 客户端支持 | 43 个自动/条件激活（Claude Code, Codex, Cursor, Zed, OpenClaw 等） |

**一句话**：把任意代码库索引成持久知识图谱，让 AI 编码 Agent 用 1% 的 token 读懂你的项目。

**技术亮点**：
- 纯 C 实现，单静态二进制，无任何运行时依赖
- Tree-sitter AST + Hybrid LSP 语义解析，产出函数、类、调用链、HTTP 路由的完整图谱
- RAM-first pipeline：LZ4 压缩、内存 SQLite、融合 Aho-Corasick 模式匹配
- 团队共享图谱制品：`.codebase-memory/graph.db.zst` 提交到仓库， teammates 跳过重新索引
- 15 个 MCP 工具覆盖搜索、追踪、架构概览、影响分析、死代码检测、跨服务链接

**学术背书**：arXiv 论文 [2603.27277](https://arxiv.org/abs/2603.27277)，31 个真实仓库评估：83% 回答质量，10× 更少 token，2.1× 更少工具调用。

**为何入选**：MCP 生态的基础设施级项目。当每个人都在做 Agent 上层应用时，有人在底层做了极致的代码理解引擎。36K+ stars 说明社区认可这个方向。

> 🔗 [GitHub](https://github.com/DeusData/codebase-memory-mcp) · [论文](https://arxiv.org/abs/2603.27277) · [主页](https://deusdata.github.io/codebase-memory-mcp/)

---

## 🛠️ 工具框架类

### 2. Vibe-Trading — 你的个人 AI 量化交易 Agent

**HKUDS / MIT / ⭐ 28,407**

香港大学数据科学实验室出品。不是简单的「AI 选股器」，而是覆盖数据采集 → 因子分析 → 策略回测 → 实盘下单 → 多 Agent 协作的完整交易操作系统。

**核心能力**：
- 自然语言 → 交易策略生成（460+ 内置 alpha 因子）
- Shadow Account 科学验证层：模拟实盘行为提取
- 多智能体团队：investment / quant / crypto / risk 分工协作
- 跨市场回测：A/港/美 equities、crypto、futures、forex
- MCP 协议集成，可被任意 Agent 调用

**实测数据**：30 天纸面交易，150+ 交易信号，tech/energy/consumer 三板块覆盖。HKUDS 研究显示，系统使用 AI 分析工具的散户比手动交易者风险调整后收益高出 20-30%。

**增长曲线**：月增 14,868 ⭐（117% 增长率），单周 +2,584 ⭐，GitHub 月榜第 11。

> 🔗 [GitHub](https://github.com/HKUDS/Vibe-Trading)

---

### 3. ai-job-search — 求职全流程自动化

**MadsLorentzen / MIT / ⭐ 28,272**

基于 Claude Code 构建的求职 Agent。评估岗位匹配度 → 定制简历 → 生成求职信 → 准备面试题，全程本地运行。

**工作流**：
1. 读取职位描述 URL，8 维度匹配评分（80+ 分回调率高 2.3 倍）
2. 自动 tailoring 简历，高亮最相关经验
3. 生成针对性求职信
4. 准备面试问题和 talking points

**单份申请成本**：$0.10-$0.30（Claude Code 订阅 $20/月另计）
**单周增长**：+13K ⭐，AI Agents 类别增速第一（findarepo 数据）

**入选理由**：Agent 从「炫技」走向「解决日常」的代表作。在 AI 快速替代部分岗位的 2026 年，一个帮人「用 AI 找不会被 AI 替代的工作」的工具，热度的成因不言自明。

> 🔗 [GitHub](https://github.com/MadsLorentzen/ai-job-search)

---

### 4. Grok Build — xAI 完整开源编码 Agent Harness

**xai-org / Apache 2.0 / ⭐ 23,297**

7 月 15 日 xAI 完整开源了 grok CLI 的编码 Agent harness。这不是 API 客户端，是完整的运行环境：TUI（ratatui 512K 行）、Agent 运行时、工具调度、会话管理、沙箱配置。

**硬核数据**：
- 132 万行 Rust，77 crates
- 45% 是测试代码（测试/生产比 0.81:1）
- Agent Client Protocol（ACP）公开 JSON-RPC 协议，解耦 UI 与运行时
- 5 种工具方言：grok_build / concise / hashline / codex / opencode
- Landlock + Seatbelt 沙箱

**背景**：7 月 12 日数据泄露风波（grok CLI 默认上传用户目录到 xAI 云端）后，xAI 删除所有保留数据、禁用默认保留、开源完整源码以重建信任。

**意义**：前沿实验室首次完整开源生产级 Agent harness。当 Claude Code 闭源、Cursor 闭源时，Grok Build 给了社区一个可审计、可修改、可自托管的选择。

> 🔗 [GitHub](https://github.com/xai-org/grok-build)

---

### 5. Hallmark — 反「AI Slop」设计质量门禁

**Nutlope (Together AI) / MIT / ⭐ 19,450**

专门解决一个问题：AI 生成的网页为什么都长得一样？

**机制**：
- 21 种页面宏观结构，随机选择避免模板化
- 20+ 设计主题（Distil、Cold Snap、Bubble、Garden、Riso...）
- 57 项「slop 测试」关卡，自动检测 AI 设计反模式
- 预提交自我批评：不达标就拒绝输出

**四个动词**：
- `hallmark`（默认）：从 brief 生成设计
- `hallmark audit`：给现有代码打分
- `hallmark redesign`：换视觉指纹重建
- `hallmark study`：从截图/URL 提取设计 DNA

**增长**：月榜第 14，月增 13,382 ⭐，单周 +4,810 ⭐。

**入选理由**：开发者社区对低质量 AI 输出的 backlash 正在形成运动。Hallmark 是第一个系统性的开源解决方案。

> 🔗 [GitHub](https://github.com/Nutlope/hallmark) · [展示站](https://usehallmark.com)

---

## 🧠 模型与算法类

### 6. Colibri — 25GB 内存跑 744B MoE

**JustVugg / Apache 2.0 / ⭐ 20,691**

纯 C 推理引擎，零依赖，约 1,300 行代码。在消费级硬件上运行 GLM-5.2（744B 参数 MoE 模型）。

**核心洞察**：MoE 稀疏激活 — 744B 总参数，每 token 只激活约 40B（2 专家 × 8/256 × 75 层 + dense）。

**内存拆解**：
- 常驻 RAM（int4）：~9.9 GB（dense 层、attention、shared experts、embedding）
- 磁盘流式（int4）：~370 GB（21,504 个路由专家，每个 ~19MB）
- 按需加载 + LRU 缓存 + OS 页缓存

**性能**：
- 冷启动：0.05-0.1 tok/s
- M5 Max + 热缓存 + MTP 推测解码：2.2-2.8 tok/s
- MLA 注意力：KV 缓存压缩 57×（576 floats/token）

**入选理由**：本地大模型推理的工程极限探索。当云端 H100 月租 > ¥50,000 时，Colibri 证明消费级硬件也能跑前沿模型 — 用时间换 GPU 成本。

> 🔗 [GitHub](https://github.com/JustVugg/colibri)

---

### 7. OpenWiki — 代码库 → AI 可消费文档

**LangChain / MIT / ⭐ 13,507**

LangChain 官方出品的自动文档生成工具。为代码库生成并维护 AI Agent 可直接消费的 wiki。

**双模式**：
- **Code 模式**：为当前仓库生成 `openwiki/` 文档目录，自动生成 `AGENTS.md` 和 `CLAUDE.md`
- **Personal 模式**：构建本地个人知识库，连接 Gmail、Notion、Slack、X/Twitter、Hacker News

**CI 集成**：GitHub Actions / GitLab CI / Bitbucket Pipelines 自动更新文档 PR

**输出格式**：Google Open Knowledge Format（OKF）v0.1 兼容

**入选理由**：大型代码库文档过时是老大难问题。OpenWiki 试图标准化「代码库 → AI 可消费文档」的 pipeline，是 LangChain 生态的战略布局。

> 🔗 [GitHub](https://github.com/langchain-ai/openwiki)

---

## 📊 数据观察

### 本周趋势热力图

| 趋势主线 | 代表项目 | 热度 |
|----------|----------|------|
| MCP 基础设施爆发 | codebase-memory-mcp | 🔥🔥🔥🔥🔥 |
| AI Agent 透明化/本地优先 | Grok Build, Colibri | 🔥🔥🔥🔥 |
| Agent 落地日常场景 | ai-job-search, Vibe-Trading | 🔥🔥🔥🔥 |
| 反 AI Slop 质量运动 | Hallmark | 🔥🔥🔥🔥 |
| 代码库 → AI 可消费文档 | OpenWiki | 🔥🔥🔥 |

### Stars 分布

```
codebase-memory-mcp  ████████████████████████████████████ 36,295
Vibe-Trading         ██████████████████████████████ 28,407
ai-job-search        ██████████████████████████████ 28,272
Grok Build           ████████████████████████ 23,297
Colibri              ██████████████████████ 20,691
Hallmark             █████████████████████ 19,450
OpenWiki             ██████████████ 13,507
```

### 许可证分布

| License | 数量 |
|---------|------|
| MIT | 5 |
| Apache 2.0 | 2 |

### 语言分布

| 语言 | 数量 |
|------|------|
| C | 2 |
| Rust | 1 |
| TypeScript | 2 |
| Python | 1 |
| CSS/多语言 | 1 |

---

## 📚 推荐阅读

### 技术文章

1. **[Colibri 深度技术解析](https://dailyaiworld.com/blogs/colibri-glm-52-local-inference-workflow-2026)** — 纯 C 引擎跑 744B MoE 的完整实现指南
2. **[Grok Build 架构深潜](https://dailyaiworld.com/blogs/grok-build-open-source-harness-workflow-2026)** — 132 万行 Rust、ACP 协议、多客户端设计
3. **[Vibe-Trading 部署指南](https://dailyaiworld.com/blogs/vibe-trading-ai-agent-guide-2026)** — 30 天纸面交易实测报告
4. **[Hallmark 设计系统解读](https://dashen-tech.com/en/dev-tools/hallmark-anti-ai-slop-design-skill/)** — 57 项 slop 测试背后的设计哲学

### 论文联动

本周论文短名单共 8 篇，4 篇与开源项目直接形成「论文→实现」或「实现→验证」的联动关系，详见《论文-开源联动周报》。

### 社区动态

- GitHub Code Quality 于 7 月 20 日正式商业化（$10/活跃提交者/月）
- Skills 生态持续爆发：orca（28K ⭐）、OfficeCLI（22K ⭐）等 Agent 办公自动化项目上榜
- Show HN 热帖「Getting GLM 5.2 running on my slow computer」获 859 分

---

*周报生成于 2026-07-31 · W31*  
*数据来源：GitHub API、实时搜索、技术媒体、arXiv*
