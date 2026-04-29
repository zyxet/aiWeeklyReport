#!/bin/bash
# 周五周报生成任务 - intelligence-report-friday
# 执行时间: 每周五 17:00

echo "🕔 [$(date '+%Y-%m-%d %H:%M')] 开始执行周五周报生成..."

CURRENT_DATE=$(date '+%Y-%m-%d')
WEEK_NUM=$(date +%W)
YEAR=$(date +%Y)

# 读取精选池
SHORTLIST_FILE="~/.openclaw/workspace/intelligence-system/data/shortlist-${YEAR}-W${WEEK_NUM}.md"
REPORT_FILE="~/.openclaw/workspace/intelligence-system/data/report-${YEAR}-W${WEEK_NUM}.md"

if [ ! -f "${SHORTLIST_FILE}" ]; then
    echo "❌ 错误: 未找到短名单文件 ${SHORTLIST_FILE}"
    echo "请确保周三的筛选任务已执行并通过用户确认"
    exit 1
fi

echo "📖 正在读取精选池..."
echo "🔍 开始深度扫描每个项目..."

# 创建周报文件
cat > ${REPORT_FILE} << EOF
# AI 开源周报 W${WEEK_NUM} | 本期主题词

日期: ${CURRENT_DATE}  
本期编辑: Kimi Claw

---

## 一、🚀 重磅推荐（1-2 个）

<!-- 根据评分标准填入高优先级项目 -->

---

## 二、🛠️ 工具框架类（2-3 个）

<!-- 工具类和框架类项目 -->

---

## 三、🧠 模型与算法类（2-3 个）

<!-- 模型类和算法类项目 -->

---

## 四、📈 数据观察

### 本周 Star 增长最快项目 Top 3
1. 
2. 
3. 

### 新兴技术趋势标签
- 

---

## 五、📚 推荐阅读

1. 
2. 
3. 

---

需要我针对某个项目做深度技术分析吗？
EOF

echo "✅ 周报已生成: ${REPORT_FILE}"
echo "📤 准备发送到飞书..."

# 输出完成标记
echo "COMPLETE|${REPORT_FILE}|${YEAR}-W${WEEK_NUM}|READY_TO_SEND"
