#!/bin/bash
# 周二论文雷达任务 - paper-collect-tuesday
# 执行时间: 每周二 09:00

echo "📚 [$(date '+%Y-%m-%d %H:%M')] 开始执行周二论文雷达..."

# 确保工作目录存在
mkdir -p ~/.openclaw/workspace/intelligence-system/data
mkdir -p ~/.openclaw/workspace/intelligence-system/logs

# 获取当前日期和周数
CURRENT_DATE=$(date '+%Y-%m-%d')
WEEK_NUM=$(date +%W)
YEAR=$(date +%Y)

# 计算上周二至本周一的时间范围
LAST_TUESDAY=$(date -d "last tuesday" '+%Y-%m-%d')
THIS_MONDAY=$(date -d "yesterday" '+%Y-%m-%d')

echo "📅 收集周期: $LAST_TUESDAY 至 $THIS_MONDAY"
echo "📝 输出文件: ~/.openclaw/workspace/intelligence-system/data/paper-pool-${YEAR}-W${WEEK_NUM}.md"

# 创建论文候选池文件
PAPER_POOL_FILE="~/.openclaw/workspace/intelligence-system/data/paper-pool-${YEAR}-W${WEEK_NUM}.md"

cat > ${PAPER_POOL_FILE} << EOF
# 本周论文候选池 - ${YEAR}年第${WEEK_NUM}周
收集日期: ${CURRENT_DATE}
收集周期: ${LAST_TUESDAY} 至 ${THIS_MONDAY}
状态: 🔄 待筛选

## 📊 数据概览
本周共收集 X 篇论文候选，筛选后保留 15-20 篇

## 🔍 信息源
- arXiv cs.CL (Computation and Language)
- arXiv cs.LG (Machine Learning)
- arXiv cs.AI (Artificial Intelligence)
- Hugging Face Papers Daily Trending
- PaperWeekly 中文精选

## 🎯 筛选关键词
LLM, Large Language Model, Agent, Multi-Agent, RAG, Prompt Engineering, 
Chain-of-Thought, Reasoning, Long Context, Multimodal, GPT, Claude, Llama,
智能体, 大模型, 提示词, 推理

## 📄 候选论文列表

<!-- AI Agent将按以下格式填充：
### 论文[N]
- 标题: [英文标题]
- 链接: https://arxiv.org/abs/xxxx.xxxxx
- 标签: #关键词1 #关键词2
- 一句话摘要: [中文摘要]
- 机构: [作者所属机构]
- 代码: [如有GitHub链接]
-->

EOF

echo "✅ 论文候选池文件已创建: ${PAPER_POOL_FILE}"
echo "🤖 等待 AI 代理执行搜索和整合..."

# 输出任务完成标记
echo "COMPLETE|${PAPER_POOL_FILE}|${YEAR}-W${WEEK_NUM}"
