# 《周三精选短名单》2026-W46

- **周期：** 2026-W46（11月3日–11月9日）
- **筛选日期：** 2026-11-11 14:00
- **输入：** data/os-pool-2026-W46.md（12 个候选）
- **验证方式：** GitHub REST API 实时星数（2026-11-11 14:0x UTC+8）+ 网络 coverage 检索
- **筛选规则：** 删除 Star < 100 且无 coverage 的项目；按星数动量、技术测评、媒体 coverage 综合排序保留 7 个

---

## 一、验证结果总表

| # | 项目 | 仓库 | 周一记录 | 实时 Star (11-11) | 验证结论 |
|---|------|------|---------|------------------|---------|
| 1 | Kimi K3.1 Pro | moonshotai/Kimi-K3.1-Pro (HF) | 5天 18,000+ 下载 | HF API 网络不可达，未复核* | ✅ coverage 极强，保留 |
| 2 | VibeVoice | microsoft/VibeVoice | 56k+ | **56,985** | ✅ 保留 |
| 3 | agent-browser | vercel-labs/agent-browser | 47k+ | **49,408** | ✅ 保留 |
| 4 | google/skills | google/skills | 22.5k | **23,840** | ✅ 保留 |
| 5 | claude-mem | thedotmack/claude-mem | 101k | **115,922** | ✅ 保留 |
| 6 | auto-ontology | NVIDIA/auto-ontology | 未记录 | 11,550 | ❌ 淘汰（coverage 薄） |
| 7 | worktrunk | max-sixty/worktrunk | 未记录 | 12,417 | ✅ 保留 |
| 8 | OpenMausBot | milind-soni/OpenMausBot | 18k+，日增 1,400 | **20,811** | ✅ 保留 |
| 9 | scenario-labs/skills | scenario-labs/skills | 3.2k | 3,663 | ❌ 淘汰（体量最小） |
| 10 | garden-skills | ConardLi/garden-skills | 14k+ | 14,912 | ❌ 淘汰（与 #4 叙事重叠） |
| 11 | Game-Studios | Donchitos/Claude-Code-Game-Studios | 未记录 | 38,152 | ❌ 淘汰（演示性质，非可用基础设施） |
| 12 | hallmark / humanizer | Nutlope/hallmark · blader/humanizer | 周榜延续 | 52,776 / 67,659 | ❌ 淘汰（W45 已覆盖，本周无新事件） |

\* Hugging Face API 在本环境网络不可达（HTTP 000），K3.1 Pro 数据以 11-09 候选池记录 + 今日 coverage 检索交叉验证。

**coverage 验证摘录（2026-11-11 检索）：**
- Kimi K3.1 Pro：lindy.ai（11-10 测评：Terminal-Bench 65.7%、AA Index 46、协议为 MIT-style + 两条大厂附加条款）、latenode.com（11-09）、shattered.io（11-06）、neoteo.com（11-08，模型卡细节：69 KDA + 24 Gated DSA 层，vLLM/SGLang  serving 指引）、aitoolsrecap.com（11-08，与 Inkling 2 Small 对比）——5 家独立媒体，本周 coverage 最强项目。
- google/skills：GitHub 仓库今日活跃（最后 push 11-11），Cloud Next 2026 官方发布背景，pinggy.io 专文。注意：该仓库实际首发于 2026 年 4 月 Cloud Next，本周为 Trending 回榜 + 星数续涨，非全新事件——周报措辞需修正候选池"正式入场"的表述。

---

## 二、周三精选短名单（7 项）

| 排名 | 项目 | 实时 Star | 协议 | 层 | 一句话入选理由 |
|------|------|----------|------|-----|---------------|
| 1 | **Kimi K3.1 Pro** | HF 18k+ 下载* | 自定义（MIT-style + 附加条款） | 模型层 | 2026 年最大开源承诺如期兑现；AA 开放权重第一；GGUF 缺席是唯一硬伤 |
| 2 | **microsoft/VibeVoice** | 56,985 | MIT | 模型层 | 前沿语音系统 MIT 开源 + MCP 原生，语音 Agent BOM 成本重构 |
| 3 | **vercel-labs/agent-browser** | 49,408 | 待查（仓BSD 系） | Agent 基础设施 | a11y 树路线浏览器自动化，token 开销碾压截图派；Vercel 下场验证赛道 |
| 4 | **google/skills** | 23,840 | Apache 2.0 | 技能层 | 平台大厂官方技能集进 Trending；harness 无关安装接口成最大公约数 |
| 5 | **thedotmack/claude-mem** | 115,922 | 待查 | Agent 基础设施 | 编码 Agent 持久记忆赛道头部固化，本周星数 +15% |
| 6 | **max-sixty/worktrunk** | 12,417 | 待查 | Agent 基础设施 | 并行 Agent 的 worktree 隔离工具，多 Agent 工程化落地的标志性配套 |
| 7 | **milind-soni/OpenMausBot** | 20,811 | 待查 | Agent 基础设施 | "bot 自带 VM"架构获社区快速认可，日增 1,400 动量全场最高 |

\* HF 下载量为 11-09 候选池记录值。

## 三、淘汰说明

- **NVIDIA/auto-ontology**（11,550★）：技术方向（图谱推理层）有价值，但本周无独立测评或媒体报道，星数动量平庸。
- **scenario-labs/skills**（3,663★）：创意生产技能库定位独特，但体量与 coverage 均为候选池末位。
- **ConardLi/garden-skills**（14,912★）：独立技能生态的佐证案例，与 google/skills 同叙事，短名单取一即可。
- **Claude-Code-Game-Studios**（38,152★）：星数高但属编排行为艺术，49 Agent 模拟工作室层级难以复用为日常工作流；与 worktrunk/OpenMausBot 的"可用工程工具"定位相比深度不足。
- **hallmark / humanizer**（52,776★ / 67,659★）：反 AI slop 赛道 W45 已作判断，本周无新事件，属趋势延续而非增量信息。

## 四、给周五周报的输入

1. **主线一：K3.1 Pro 自托管现实检查**——coverage 已确认权重如期释放（1.56TB、96 个 safetensors、MXFP4），但 GGUF/llama.cpp 仍缺席；协议被第三方测评定性为"MIT-style + >$20M 收入托管商附加条款"，商用门槛需读原文。
2. **主线二：技能层战争**——google/skills 回榜（注意首发实为 4 月 Cloud Next，本周是 Trending 二次发酵），与 anthropics/skills（19 万星）形成平台 vs 独立生态双轨。
3. **主线三：Agent 感官与并行工程化**——agent-browser（a11y 树）+ worktrunk（worktree 隔离）+ OpenMausBot（bot VM）分别对应交互、隔离、运行时三个工程缺口。
4. **数据备注**：本表所有 GitHub 星数为 2026-11-11 实时 API 返回值，与周一记录对比全部上涨，无 Star < 100 项目触发删除线。

---

**筛选执行：** 周三深度筛选（wednesday-filter） | **下一步：** 等待人工确认后进入周四论文精选
