# 开源情报短名单 2026-W44

> 周三深度筛选产物 | 2026-10-28 14:00 CST
> 来源池：`data/os-pool-2026-W44.md`（12 个项目）
> 筛选规则：删除 Star < 100 且无媒体/技术测评 coverage 的项目；保留 5-7 个

---

## 验证方法

- **GitHub Star 数**：GitHub API 逐一实测（curl，2026-10-28 14:00）
- **Coverage**：kimi_search 交叉验证（英文科技媒体 + 中文社区 + 官方博客）
- 模型类项目无 GitHub repo，以独立第三方 coverage 为准

---

## 周三精选短名单（7 个项目）

| # | 项目 | 层 | 一句话 | Stars（实测） | Coverage | 备注 |
|---|------|-----|--------|--------------|----------|------|
| 1 | **Kimi K3.1 Pro** | 模型 | 国产开源模型本周最重磅：Terminal-Bench 4.0 达 65.7%（开源 #1），Code Arena WebDev 第 8（1,692 分）；权重 11 月 4 日前释放 | —（模型） | ✅ 多家独立第三方测评 | 本周头条 |
| 2 | **Muse Spark Open** | 模型 | Meta×Apple 联合优化 MLX，两台 512GB M5 Ultra Mac Studio 本地跑 816B（42B active）、1M 上下文 | —（模型） | ✅ MacRumors / CNBC / Business Insider / The Verge | 桌面推理里程碑；Muse Model License（开放权重） |
| 3 | **Nemotron 3.5 Super VL** | 模型 | NVIDIA 开放权重多模态 MoE：120B/12B active、1M 上下文、SWE-bench Verified 71.10、Terminal-Bench 2.1 66.70 | —（模型） | ✅ kie.ai / BuildFastWithAI / AI Profit Boardroom | OpenMDW-1.1；vLLM day-0；单台 DGX Spark 128GB 可跑 |
| 4 | **FLUX 3 Image Klein** | 模型 | BFL 开放权重图像模型：文生图 + 编辑 + 多参考图；RTX 8GB+ 本地可跑蒸馏版 | —（模型） | ✅ Business Insider / BFL 官方 | FLUX Kommunity License（<$5M 营收免费商用） |
| 5 | **llm-d 1.0** | 基础设施 | CNCF Sandbox 推理调度项目发布 v1.0：KV-cache 感知路由、多调度器、Gateway API Inference Extension | 5,063 ✅ | ✅ TechTarget / IBM Think / CNCF / Google Cloud | 生产级 Kubernetes LLM 推理堆栈 |
| 6 | **OpenCode 2.0** | 应用/Agent | 架构大改：CLI → 常驻后台服务（daemon），终端/桌面/Web 三端共享会话；发布 `@opencode/sdk` + Code Mode | 222,474 ✅ | ✅ The New Stack / Tech-Insider / 日文社区实测 | 月活 1,600 万+；MIT |
| 7 | **hallmark** | 应用/设计 | Anti-AI-slop 设计 skill：48 套手工主题 + 浏览器 lint 管线，专抓 AI 输出的设计毛病 | 39,395 ✅ | ✅ GitHub Trending 分析（coddykit）/ 掘金日报 / ioainsight | 10-27 GitHub Trending #1，日增 ~2,000+ |

---

## 剔除记录（5 个项目）

| 项目 | 原因 |
|------|------|
| GitHub AES（HydraFusion） | 企业级智能体框架，仅部分组件开源，与开源短名单定位不符 |
| vLLM × MiniMax day-zero | 框架增量支持，非独立新项目；归入 llm-d/vLLM 生态趋势即可 |
| TradingAgents | 117K stars、持续 trending，但属成熟项目，本周无增量新闻；转趋势跟踪 |
| cindy | 7,665 ✅ / coverage ✅（GitHub Trending #4-6），但 2026-07 上线、差异化尚不明显；转观察名单 |
| thinkrail | 4,285 ✅ / coverage ✅（GitHub Trending #3），JetBrains 官方 vibe-coding IDE 值得关注但过早期；转观察名单 |

---

## 数据附录

**GitHub API 实测（2026-10-28 14:00 CST）**

```
llm-d/llm-d              5,063  stars  Apache-2.0  updated 2026-10-28
anomalyco/opencode     222,474  stars  MIT         updated 2026-10-27
makecindy/cindy          7,665  stars  Apache-2.0  created 2026-07-22
Nutlope/hallmark        39,395  stars  MIT         created 2026-04-27
TauricResearch/TradingAgents 117,473  stars  Apache-2.0
JetBrains/thinkrail      4,285  stars  Apache-2.0  created 2026-07-08
vllm-project/vllm       95,731  stars  Apache-2.0
```

**关键 coverage 链接**

- Kimi K3.1 Pro — https://explainx.ai/blog/kimi-k3-1-pro-open-weights-benchmarks-price-terminal-bench-nov-4-2026 （2026-10-24）
- llm-d — https://www.techtarget.com/searchITOperations/news/366881594/IT-ops-platforms-tackle-cost-complexity-of-AI-inference （2026-10-22）
- OpenCode 2.0 — https://thenewstack.io/opencode-2-shared-service/ （2026-10-12）
- Muse Spark Open — https://www.macrumors.com/2026/10/15/meta-muse-spark-open-mac-studio/ （2026-10-15）
- Nemotron 3.5 Super VL — https://kie.ai/blog/what-is-nemotron-3-5-super-vl （2026-10-16）
- FLUX 3 Image Klein — https://markets.businessinsider.com/news/stocks/black-forest-labs-expands-access-to-frontier-visual-intelligence-with-open-weights-release-of-flux-3-image-klein-1036630617 （2026-10-15）
- hallmark — https://www.coddykit.com/pages/blog-detail?id=5130003 （2026-10-27，GitHub Trending 综合分析）
