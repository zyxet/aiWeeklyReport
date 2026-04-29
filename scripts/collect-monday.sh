#!/bin/bash
# 周一情报收集任务 - intelligence-collect-monday
# 执行时间: 每周一 09:00

echo "🕘 [$(date '+%Y-%m-%d %H:%M')] 开始执行周一情报收集..."

# 确保工作目录存在
mkdir -p ~/.openclaw/workspace/intelligence-system/data
mkdir -p ~/.openclaw/workspace/intelligence-system/logs

# 获取当前日期和周数
CURRENT_DATE=$(date '+%Y-%m-%d')
WEEK_NUM=$(date +%W)
YEAR=$(date +%Y)

# 计算上周一到本周一的时间范围
LAST_MONDAY=$(date -d "last monday" '+%Y-%m-%d')
THIS_MONDAY=$CURRENT_DATE

echo "📅 收集周期: $LAST_MONDAY 至 $THIS_MONDAY"
echo "📝 输出文件: ~/.openclaw/workspace/intelligence-system/data/candidate-pool-${YEAR}-W${WEEK_NUM}.md"

# 创建候选池文件
POOL_FILE="~/.openclaw/workspace/intelligence-system/data/candidate-pool-${YEAR}-W${WEEK_NUM}.md"

cat > ${POOL_FILE} << EOF
# 本周候选池 - ${YEAR}年第${WEEK_NUM}周
收集日期: ${CURRENT_DATE}
收集周期: ${LAST_MONDAY} 至 ${THIS_MONDAY}
状态: 🔄 待筛选

## 📊 数据概览
本周共发现 X 个新项目，其中 LLM 领域 Y 个，Agent 领域 Z 个

## 🎯 候选项目列表

<!-- 以下为搜索整合后的项目信息 -->

EOF

echo "✅ 候选池文件已创建: ${POOL_FILE}"
echo "🤖 等待 AI 代理执行搜索和整合..."

# 输出任务完成标记
echo "COMPLETE|${POOL_FILE}|${YEAR}-W${WEEK_NUM}"
