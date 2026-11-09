# 《周一开源项目速览》2026-W46

- **周期：** 2026-W46（11月3日–11月9日）
- **生成日期：** 2026-11-09
- **来源：** GitHub Trending / GitHub Explore / Hacker News / 社区博客 / 官方公告

---

## 一、大模型层（模型权重 + 训练推理）

### 1. Kimi K3.1 Pro 权重如期开源 ⭐ 本周最大事件

- **仓库：** moonshotai/Kimi-K3.1-Pro（Hugging Face）
- **事件：** 11月4日按计划释放全部权重，1.56 TB MXFP4。W45 预告的"2026 年开源社区最大事件"兑现。仓库 11月2日上线后 5 天内下载量超 18,000 次
- **规格回顾：** 2.8T 参数 MoE，每 token 激活 104B；1M context；原生多模态（MoonViT-V2 视觉编码器，401M 参数）；Thinking 模式常开（reasoning_effort: low / high / max）
- **推理路径：** 官方支持 vLLM / SGLang / TokenSpeed（OpenAI 兼容端点）；入门级硬件 8×GB300 / B300 / MI355X（288GB）或等效 2 节点 H100
- **关键缺口：暂无 GGUF / llama.cpp 支持**，消费级量化被挡在门外——Home-lab 方案需等社区跟进
- **协议：** 自定义 Kimi K3.1 Pro License（Hugging Face 标记 license:other），非 OSI 认证开源，商用前需读协议原文
- **榜单位置：** Vals Terminal-Bench 4.0 第3（63.64%）、Artificial Analysis Index v5 46 分（开放权重第一）；API 定价 $2/$10（缓存命中 $0.20）
- **生态信号：** 第三方托管 11月6日已上架（vec3、Wavespeed）；系列还有 Highspeed 变体（2–3 倍速度，$4/$20）；Moonshot 10月31日关闭 K2 新用户接入，12月底退役
- **下周跟踪：** 社区量化/GGUF 进展、第三方托管降价、权重"数据清除"声明的独立安全验证

### 2. microsoft/VibeVoice —— 开源语音模型家族 ⭐ GitHub Trending

- **仓库：** microsoft/VibeVoice（Python，56k+ stars，本周日增 200+）
- **定位：** 前沿级开源语音系统，对标 ElevenLabs / Play.ht：语音克隆、多说话人合成、实时流式
- **三个模型：** 长文本转写（带说话人标签）、500M 参数实时 TTS、流式识别器；47 种语言预训练
- **协议：** MIT——语音合成从专有 API 变成可自托管的商品
- **Agent 集成：** 原生 MCP，Claude Code / Codex / OpenClaw 等 20+ harness 可直接以 tool call 调用语音能力
- **意义：** Agent 的"嘴巴和耳朵"完成开源化，语音不再是云厂商的收费墙

## 二、Agent 基础设施层

### 3. vercel-labs/agent-browser ⭐ GitHub Trending

- **仓库：** vercel-labs/agent-browser（Rust，47k+ stars）
- **定位：** 给 AI Agent 用的浏览器自动化 CLI
- **工作方式：** 原生 Rust 二进制，Agent 打开页面、以紧凑的 accessibility tree 读取、按引用点击；而非截图+坐标
- **亮点：** 走 a11y 树路线意味着 token 开销远低于视觉方案，与上周的 Lightpanda（Zig headless）同属"Agent 感官基础设施"新赛道，一个重抓取性能、一个重交互自动化
- **意义：** Vercel 下场验证：浏览器自动化是 Agent 时代的独立基础设施层，不是框架的附属功能

### 4. google/skills —— 平台大厂正式入场技能层 ⭐ GitHub Trending

- **仓库：** google/skills（Python，22.5k stars）
- **定位：** Google 官方 Agent 技能集：GCP 部署/监控/成本优化、Workspace（Docs/Sheets/Gmail/Calendar）自动化、Gemini 提示工程、Vertex AI 工作流、Firebase/Flutter/Angular
- **关键点：** 首个平台级大厂官方 skills 仓库；每个 skill 可装进 Claude Code / Codex / OpenClaw 等任意支持 skills CLI 的 harness
- **意义：** 技能层战争升级——此前该生态由独立开发者（mattpocock/skills、anthropics/skills 已达 19 万星）主导，现在 Google 带着产品深度进来，"平台官方技能"将成为默认选项

### 5. claude-mem 持续霸榜

- **仓库：** thedotmack/claude-mem（TypeScript，101k stars）
- **定位：** 跨会话持久记忆：捕获 Agent 行为、AI 压缩、后续会话注入相关上下文
- **兼容性：** Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode
- **本周动态：** 继续占据 GitHub Trending 周榜，编码 Agent 记忆赛道的头部位置进一步固化

### 6. NVIDIA auto-ontology ⭐ GitHub Trending

- **仓库：** NVIDIA/auto-ontology（Python）
- **定位：** 在数据之上构建语义图谱推理层：确定性查询生成、更好的上下文检索、可解释的 LLM/Agent 工作流
- **意义：** NVIDIA 在 Agent 基础设施上的又一落子（继 SkillSpector 之后）；图谱+推理作为 RAG 的进阶形态进入主流视野

### 7. worktrunk —— 并行 Agent 的 Git worktree 管理

- **仓库：** max-sixty/worktrunk（本周 GitHub Trending）
- **定位：** Git worktree 管理 CLI，为并行 AI Agent 工作流设计
- **意义：** "多 Agent 并行改代码"从演示变成日常工作流，配套的工程工具（worktree 隔离、分支编排）开始专门化

### 8. OpenMausBot

- **仓库：** milind-soni/OpenMausBot（TypeScript，18k+ stars，日增 1,400+）
- **定位：** 开源 Grok Bot 替代品，带虚拟机——bot 拥有自己的可编程运行环境
- **意义：** "给聊天 bot 配一台电脑"的架构快速获得社区认可

## 三、Agent 技能与编排层

### 9. scenario-labs/skills —— 创意生产技能库

- **仓库：** scenario-labs/skills（3.2k stars，单日 +667）
- **定位：** 生产级图像/视频/音频/3D 生成技能，通过 MCP 驱动 Blender、Maya、ZBrush、Unreal、Unity
- **意义：** 创意行业的工具链正在为 AI 原生工作流重建；"专家 Agent 团队操控行业标准软件"的模式出现

### 10. ConardLi/garden-skills —— 独立开发者技能集

- **仓库：** ConardLi/garden-skills（JavaScript，14k+ stars）
- **定位：** 单人开发的技能合集：响应式网页设计（无障碍+性能优先）、RAG 工作流（本地向量库）、图像生成管线
- **模式：** 模块化组合——小颗粒、可组合的 skill 单元，而非大一统技能包；7 个月冲到 14k 星，证明独立技能生态与平台官方技能同样有足够空间

### 11. Claude-Code-Game-Studios

- **仓库：** Donchitos/Claude-Code-Game-Studios（本周 GitHub Trending）
- **定位：** 把 Claude Code 变成游戏开发工作室：49 个 AI Agent、72 个工作流技能、完整协调系统，模拟真实工作室层级
- **意义：** 多 Agent 编排的极端案例——从"单 Agent+工具"到"组织架构即编排"

### 12. hallmark / humanizer —— 反 AI slop 赛道延续

- **hallmark（Nutlope/hallmark）：** 反 slop 设计 skill，本周仍在周榜，"让 Agent 产出不那么像 AI"的品类需求持续
- **humanizer（blader/humanizer）：** 去除文本 AI 痕迹的 Agent skill，新上榜
- **意义：** 上周判断验证中：输出下限被模型抬平后，"品味层"成为社区付费/给星意愿最高的方向

---

## 趋势观察与判断

1. **K3.1 Pro 权重落地，开放权重进入 3T 时代。** 如期开源兑现了 2026 年最大的开源承诺，但三个钩子留到了下周之后：GGUF/llama.cpp 缺席（自托管门槛仍是数据中心级）、自定义协议的非 OSI 性质、第三方托管是否会拉低官方 $2/$10 定价。建议：自托管评估先以 vLLM/SGLang 路径为准，量化方案继续观望。

2. **技能层战争正式开打。** google/skills 入场 + anthropics/skills 逼近 19 万星 + 上周的 SkillKit/SkillSpector 基础设施——平台官方与独立生态并存，harness 无关性（skills CLI 成为通用安装接口）是最大公约数。建议：内部 skill 管理流程本周就该建立，别等格式战争分出胜负。

3. **语音完成开源商品化。** VibeVoice（MIT）+ MCP 原生集成意味着语音 Agent 的 BOM 成本里少了一整块云 API 支出。做语音交互产品的团队应重新测算自托管 vs ElevenLabs 的成本拐点。

4. **Agent 感官基础设施二分天下。** agent-browser（交互自动化，a11y 树）与 Lightpanda（高性能抓取）路径分化明显；坐标点击的截图派在 token 成本面前节节败退。浏览器层的选型窗口正在打开。

5. **并行多 Agent 工程化落地。** worktrunk（worktree 隔离）、Game-Studios（49 Agent 组织架构）、OpenMausBot（bot 专用 VM）共同指向：多 Agent 不再是大厂 demo，社区开始造配套工程工具。

6. **下周关注（W47）：** K3.1 Pro 社区量化/GGUF 进展；第三方托管价格战是否开打；"数据清除"权重的独立红队评估；K3.1 系列后续成员（Moonshot 已暗示 Pro 只是系列第一款）。

---

**下期：** 2026-W47（11月10日–11月16日），重点关注 K3.1 Pro 自托管实测与技能层战争的后续动向。
