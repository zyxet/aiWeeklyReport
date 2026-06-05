# Paper Shortlist 2026-W23

> **Generation Date**: 2026-06-04
> **Week**: 2026-W23
> **Total Candidates**: 40 | **Shortlisted**: 8
> **Cutoff Score**: 17/25

---

## 精选论文

### #1 StateKV — Linear Scaling Video VLMs for Long Video Understanding

- **arXiv ID**: 2605.31598
- **Title**: Linear Scaling Video VLMs for Long Video Understanding
- **Authors**: Cristóbal Eyzaguirre, Jiajun Wu, Juan Carlos Niebles
- **Affiliation**: Stanford University
- **Published**: May 29, 2026
- **URL**: https://arxiv.org/abs/2605.31598
- **Code**: https://ceyzaguirre4.github.io/StateKV
- **中文摘要**: 用状态缓存替代时空自注意力，将视频VLM计算复杂度从二次降至线性
- **关联开源**: —

| 评分维度 | 分数 | 说明 |
|----------|------|------|
| 创新性 | 5 | 首次实现视频VLM线性复杂度缩放，颠覆二次注意力瓶颈 |
| 实用性 | 5 | 长视频理解直接可用，解决实际痛点 |
| 技术深度 | 4 | 状态缓存机制设计精巧，实验充分 |
| 机构背书 | 5 | Stanford University |
| 代码可得性 | 4 | 项目页面已发布，代码即将开源 |
| **总分** | **23** | |

---

### #2 RoadmapBench — Long-Horizon Agentic Software Development Benchmark

- **arXiv ID**: 2605.15846
- **Title**: RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades
- **Authors**: Xinbo Xu, Ruihan Yang, Haiyang Shen, Wendong Xu, Bofei Gao, Ruoyu Wu, Kean Shi, Weichu Xie, Xuanzhong Chen, Ming Wu, Jason Zeng, Michael Heinrich, Elvis Zhang, Liang Chen, Kuan Li, Baobao Chang
- **Affiliation**: Alibaba Cloud / 阿里云
- **Published**: May 15, 2026
- **URL**: https://arxiv.org/abs/2605.15846
- **Code**: https://github.com/UniPat-AI/RoadmapBench
- **中文摘要**: 基于真实开源项目版本升级的长周期编码基准，覆盖17仓库5语言115任务
- **关联开源**: https://github.com/UniPat-AI/RoadmapBench

| 评分维度 | 分数 | 说明 |
|----------|------|------|
| 创新性 | 4 | 首个基于真实版本升级的长周期编码基准 |
| 实用性 | 5 | AI编码Agent评估亟需此类基准，填补关键空白 |
| 技术深度 | 4 | 四级验证流程（挖掘→构建→静态验证→rollout质控） |
| 机构背书 | 4 | 阿里云团队，工程实力雄厚 |
| 代码可得性 | 5 | GitHub + DockerHub + HuggingFace 全链路开源 |
| **总分** | **22** | |

---

### #3 GraphBit — Graph-based Agentic Framework

- **arXiv ID**: 2605.13848
- **Title**: GraphBit: A Graph-based Agentic Framework for Non-Linear Agent Orchestration
- **Authors**: Yeahia Sarker, Md Rahmat Ullah, Musa Molla, Shafiq Joty
- **Affiliation**: MTSU, InfinitiBit GmbH, Salesforce Research
- **Published**: March 8, 2026
- **URL**: https://arxiv.org/abs/2605.13848
- **Code**: https://github.com/InfinitiBit/graphbit
- **中文摘要**: 用Rust引擎确定性执行DAG工作流，解决LLM编排中的幻觉路由和无限循环问题
- **关联开源**: https://github.com/InfinitiBit/graphbit

| 评分维度 | 分数 | 说明 |
|----------|------|------|
| 创新性 | 5 | 引擎编排替代LLM编排，确定性执行消除幻觉 |
| 实用性 | 4 | Rust引擎11.9ms延迟，生产可用 |
| 技术深度 | 4 | 三层内存隔离+DAG原生执行，架构完整 |
| 机构背书 | 4 | Salesforce Research |
| 代码可得性 | 5 | GitHub官方开源 |
| **总分** | **22** | |

---

### #4 Representation Forcing — Bottleneck-Free Unified Multimodal Models

- **arXiv ID**: 2605.31604
- **Title**: Representation Forcing for Bottleneck-Free Unified Multimodal Models
- **Authors**: Yuqing Wang, Zhijie Lin, Ceyuan Yang, Yang Zhao, Fei Xiao, Hao He, Qi Zhao, Zihan Ding, Fuyun Wang, Shuai Wang, Youliang Zhang, Haoqi Fan, Xihui Liu
- **Affiliation**: ByteDance, Shanghai Jiao Tong University, CUHK
- **Published**: May 29, 2026
- **URL**: https://arxiv.org/abs/2605.31604
- **Code**: https://yuqingwang1029.github.io/RepresentationForcing/
- **中文摘要**: 训练解码器自回归预测视觉表征token，消除统一多模态模型对预训练VAE的依赖
- **关联开源**: —

| 评分维度 | 分数 | 说明 |
|----------|------|------|
| 创新性 | 5 | 消除VAE瓶颈的全新范式，自回归预测内部表征 |
| 实用性 | 4 | 理论扎实，像素空间生成质量匹敌VAE基线 |
| 技术深度 | 5 | 完整数学推导+消融实验，理解性能同步提升 |
| 机构背书 | 4 | 字节跳动+上交大+港中文 |
| 代码可得性 | 2 | 项目页面存在，无明确代码仓库 |
| **总分** | **20** | |

---

### #5 Formal Methods + LLMs — Auditing & Monitoring

- **arXiv ID**: 2605.16198
- **Title**: Runtime Auditing and Predictive Monitoring of LLM Agents Using Formal Methods
- **Authors**: Parand A. Alamdari, Toryn Q. Klassen, Sheila A. McIlraith
- **Affiliation**: University of Toronto, Vector Institute
- **Published**: May 15, 2026 (FAccT 2026)
- **URL**: https://arxiv.org/abs/2605.16198
- **Code**: —
- **中文摘要**: 用线性时序逻辑(LTL)对LLM智能体进行离线审计和在线监控，显著降低违规率
- **关联开源**: —

| 评分维度 | 分数 | 说明 |
|----------|------|------|
| 创新性 | 5 | 形式化方法与LLM的交叉，LTL推理监控 |
| 实用性 | 4 | AI治理关键基础设施，FAccT 2026收录 |
| 技术深度 | 5 | 数学框架完整，证明监控器soundness |
| 机构背书 | 4 | 多伦多大学+Vector Institute |
| 代码可得性 | 1 | 未发现公开代码 |
| **总分** | **19** | |

---

### #6 Dr.LLM — Dynamic Layer Routing in LLMs

- **arXiv ID**: 2510.12773
- **Title**: Dr.LLM: Dynamic Layer Routing in LLMs
- **Authors**: Ahmed Heakl
- **Affiliation**: ParameterLab
- **Published**: ICLR 2026
- **URL**: https://arxiv.org/abs/2510.12773
- **Code**: https://github.com/parameterlab/dr-llm
- **中文摘要**: 基于MCTS监督的逐层动态路由，无需改变模型架构即可实现推理加速
- **关联开源**: https://github.com/parameterlab/dr-llm ⭐双料

| 评分维度 | 分数 | 说明 |
|----------|------|------|
| 创新性 | 4 | 动态路由概念不新，MCTS监督有新意 |
| 实用性 | 4 | 推理加速即插即用，ICLR 2026收录 |
| 技术深度 | 3 | 方法描述较简洁，实验规模适中 |
| 机构背书 | 2 | ParameterLab，非知名机构 |
| 代码可得性 | 5 | GitHub官方开源 |
| **总分** | **18** | |

---

### #7 TOBench — Omni-Modal Tool Benchmark

- **arXiv ID**: 2605.16909
- **Title**: TOBench: A Task-Oriented Omni-Modal Benchmark for Real-World Tool-Using Agents
- **Authors**: Yuwen Qu, Zhiqiang Liu, Wenhui Dong, Yilang Tan, Haochen Yin, Chenyang Si
- **Affiliation**: Nanjing University, HUST, SWJTU, CUHK
- **Published**: May 16, 2026
- **URL**: https://arxiv.org/abs/2605.16909
- **Code**: https://github.com/Pi3AI/TOBench
- **中文摘要**: 面向真实世界全模态工具使用Agent的基准测试，覆盖文档理解、代码执行、Web浏览等复合工作流
- **关联开源**: https://github.com/Pi3AI/TOBench ⭐双料

| 评分维度 | 分数 | 说明 |
|----------|------|------|
| 创新性 | 3 | 基准测试类工作，全模态复合工作流有新意 |
| 实用性 | 4 | Agent评估急需此类真实场景基准 |
| 技术深度 | 3 | 主要是数据集构建与评估协议设计 |
| 机构背书 | 3 | 多校合作，无单一顶级机构主导 |
| 代码可得性 | 5 | GitHub官方开源 |
| **总分** | **18** | |

---

### #8 CHARM — Multimodal JEPA for Time-Series

- **arXiv ID**: 2605.31580
- **Title**: Giving Sensors a Voice: Multimodal JEPA for Semantic Time-Series Embeddings
- **Authors**: U Dutta, Gerardo Pastrana, et al.
- **Affiliation**: Multiple Institutions (ICML 2026)
- **Published**: May 29, 2026
- **URL**: https://arxiv.org/abs/2605.31580
- **Code**: —
- **中文摘要**: 将通道级文本描述融入Transformer编码器，用JEPA训练时序嵌入，实现跨数据集泛化
- **关联开源**: —

| 评分维度 | 分数 | 说明 |
|----------|------|------|
| 创新性 | 4 | JEPA+文本描述用于时序是新应用方向 |
| 实用性 | 4 | 时序分析广泛适用，跨数据集泛化能力强 |
| 技术深度 | 4 | ICML 2026收录，多任务验证充分 |
| 机构背书 | 3 | 多机构合作，机构知名度中等 |
| 代码可得性 | 2 | 未找到官方代码仓库 |
| **总分** | **17** | |

---

## 未入选候选论文（部分）

| arXiv ID | 标题 | 未入选原因 |
|----------|------|-----------|
| 2605.19099 | Efficient Model Merging via... | 未获取完整信息 |
| 2605.04906 | Self-Tuning for Generalist... | 未获取完整信息 |
| 2505.10936 | ARPA: Adaptive Risk-Preference... | 未获取完整信息 |
| 2603.03005 | OrchMAS: A Scientific Domain-Oriented... | 总分18，与TOBench/Dr.LLM同分但领域更窄 |
| 2605.31597 | (其他候选) | 信息不完整 |

---

> **Status**: 待用户确认  
> **Next Step**: 用户确认后执行 `git add`, `git commit`, `git push`
