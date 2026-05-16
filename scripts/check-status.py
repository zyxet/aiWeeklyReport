#!/usr/bin/env python3
"""
复核脚本 - 读取 calendar yaml + execution log，输出计划 vs 实际对比

用法:
    python3 scripts/check-status.py [year] [--week W20] [--today]

示例:
    python3 scripts/check-status.py 2026              # 全年概览
    python3 scripts/check-status.py 2026 --week W20   # 本周详情
    python3 scripts/check-status.py 2026 --today      # 今日任务
"""

import yaml
import sys
import os
import datetime
import argparse
import re

def load_calendar(year, base_dir):
    """加载 calendar yaml"""
    path = os.path.join(base_dir, f"config/calendar-{year}.yaml")
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def parse_log(year, base_dir):
    """解析 execution log markdown，提取实际执行状态"""
    path = os.path.join(base_dir, f"logs/execution-log-{year}.md")
    if not os.path.exists(path):
        return {}
    
    status = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line.startswith('|') or '日期' in line or '---' in line:
                continue
            
            parts = [p.strip() for p in line.split('|')]
            if len(parts) < 10:
                continue
            
            # parts: ['', date, weekday, week, task_id, task_name, planned, actual, output_file, completed_at, notes, '']
            date_str = parts[1]
            task_id = parts[4] if parts[4] != '-' else None
            actual = parts[7]
            output_file = parts[8] if parts[8] != '-' else None
            completed_at = parts[9] if parts[9] != '-' else None
            
            if date_str not in status:
                status[date_str] = []
            
            if task_id:
                status[date_str].append({
                    "task_id": task_id,
                    "actual": actual,
                    "output_file": output_file,
                    "completed_at": completed_at
                })
    
    return status

def get_week_dates(year, week_str):
    """根据 ISO 周次返回该周的所有日期"""
    week_num = int(week_str.replace('W', ''))
    # ISO week starts on Monday
    jan4 = datetime.date(year, 1, 4)
    monday = jan4 + datetime.timedelta(weeks=week_num-1, days=-jan4.weekday())
    dates = []
    for i in range(7):
        dates.append((monday + datetime.timedelta(days=i)).strftime('%Y-%m-%d'))
    return dates

def print_overview(calendar, log_status, year):
    """打印全年概览"""
    total_scheduled = 0
    total_completed = 0
    total_pending = 0
    total_failed = 0
    total_rest = 0
    
    for date_str, day in calendar['schedule'].items():
        if not day.get('tasks'):
            total_rest += 1
            continue
        for task in day['tasks']:
            total_scheduled += 1
            # Check log for actual status
            actual = task.get('actual_status', 'pending')
            # If log has updated status, use that
            if date_str in log_status:
                for log_task in log_status[date_str]:
                    if log_task['task_id'] == task['task_id']:
                        actual = log_task['actual']
                        break
            
            if 'completed' in actual or '✅' in actual:
                total_completed += 1
            elif 'failed' in actual or '❌' in actual or 'error' in actual:
                total_failed += 1
            else:
                total_pending += 1
    
    print(f"\n{'='*60}")
    print(f"  {year}年执行概览")
    print(f"{'='*60}")
    print(f"  计划任务:  {total_scheduled}")
    print(f"  已完成:    {total_completed} ({total_completed/total_scheduled*100:.1f}%)")
    print(f"  待执行:    {total_pending}")
    print(f"  失败:      {total_failed}")
    print(f"  休息日:    {total_rest}")
    print(f"{'='*60}")
    
    # 本周状态
    today = datetime.date.today()
    current_week = f"W{today.isocalendar()[1]:02d}"
    print(f"\n  当前周次: {current_week} (今天: {today.strftime('%Y-%m-%d')})")
    
    week_dates = get_week_dates(year, current_week)
    print(f"\n  本周 ({current_week}) 计划:")
    for date_str in week_dates:
        if date_str in calendar['schedule']:
            day = calendar['schedule'][date_str]
            wday = datetime.datetime.strptime(date_str, '%Y-%m-%d').strftime('%a')
            if day.get('tasks'):
                for task in day['tasks']:
                    task_name = calendar['task_definitions'][task['task_id']]['name']
                    actual = task.get('actual_status', 'pending')
                    # Override with log if available
                    if date_str in log_status:
                        for lt in log_status[date_str]:
                            if lt['task_id'] == task['task_id']:
                                actual = lt['actual']
                                break
                    status_icon = '✅' if 'completed' in actual or '✅' in actual else ('❌' if 'failed' in actual or '❌' in actual else '⏳')
                    print(f"    {date_str} ({wday}) {status_icon} {task['task_id']:20s} {task_name}")
            else:
                print(f"    {date_str} ({wday}) ⏸ 休息日")

def print_week_detail(calendar, log_status, year, week_str):
    """打印指定周的详情"""
    print(f"\n{'='*60}")
    print(f"  {year}年 {week_str} 详情")
    print(f"{'='*60}")
    
    week_dates = get_week_dates(year, week_str)
    
    for date_str in week_dates:
        if date_str not in calendar['schedule']:
            continue
        
        day = calendar['schedule'][date_str]
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        wday_name = ['周一','周二','周三','周四','周五','周六','周日'][date_obj.weekday()]
        
        print(f"\n  📅 {date_str} ({wday_name})  {day['week']}")
        
        if not day.get('tasks'):
            print(f"     ⏸ 休息日")
            continue
        
        for task in day['tasks']:
            task_def = calendar['task_definitions'][task['task_id']]
            actual = task.get('actual_status', 'pending')
            output_file = task.get('output_file', '-')
            completed_at = task.get('completed_at', '-')
            
            # Override with log if available
            if date_str in log_status:
                for lt in log_status[date_str]:
                    if lt['task_id'] == task['task_id']:
                        actual = lt['actual']
                        if lt['output_file'] and lt['output_file'] != '-':
                            output_file = lt['output_file']
                        if lt['completed_at'] and lt['completed_at'] != '-':
                            completed_at = lt['completed_at']
                        break
            
            status_icon = '✅' if 'completed' in actual or '✅' in actual else ('❌' if 'failed' in actual or '❌' in actual else '⏳')
            print(f"     {status_icon} {task['task_id']}")
            print(f"        名称: {task_def['name']}")
            print(f"        计划: {task_def['hour']:02d}:00")
            print(f"        状态: {actual}")
            print(f"        产出: {output_file}")
            print(f"        完成: {completed_at}")

def print_today(calendar, log_status, year):
    """打印今日任务"""
    today_str = datetime.date.today().strftime('%Y-%m-%d')
    
    if today_str not in calendar['schedule']:
        print(f"  今天 ({today_str}) 不在执行日历中")
        return
    
    day = calendar['schedule'][today_str]
    print(f"\n  📅 今天: {today_str} ({day['week']})")
    
    if not day.get('tasks'):
        print(f"     ⏸ 休息日，无计划任务")
        return
    
    for task in day['tasks']:
        task_def = calendar['task_definitions'][task['task_id']]
        actual = task.get('actual_status', 'pending')
        
        # Override with log
        if today_str in log_status:
            for lt in log_status[today_str]:
                if lt['task_id'] == task['task_id']:
                    actual = lt['actual']
                    break
        
        status_icon = '✅' if 'completed' in actual or '✅' in actual else ('❌' if 'failed' in actual or '❌' in actual else '⏳')
        print(f"\n     {status_icon} {task_def['name']} ({task_def['hour']:02d}:00)")
        print(f"        模板: {task_def['output_template']}")
        print(f"        状态: {actual}")
        
        if 'completed' not in actual and '✅' not in actual:
            print(f"        产出: 待执行")
        else:
            output_file = task.get('output_file', '-')
            if today_str in log_status:
                for lt in log_status[today_str]:
                    if lt['task_id'] == task['task_id'] and lt['output_file']:
                        output_file = lt['output_file']
                        break
            print(f"        产出: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='复核周报系统执行状态')
    parser.add_argument('year', type=int, nargs='?', default=datetime.date.today().year, help='年份')
    parser.add_argument('--week', type=str, help='查看指定周，如 W20')
    parser.add_argument('--today', action='store_true', help='只看今天')
    args = parser.parse_args()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    
    calendar = load_calendar(args.year, base_dir)
    log_status = parse_log(args.year, base_dir)
    
    if args.today:
        print_today(calendar, log_status, args.year)
    elif args.week:
        print_week_detail(calendar, log_status, args.year, args.week)
    else:
        print_overview(calendar, log_status, args.year)
        # 同时打印本周
        today = datetime.date.today()
        current_week = f"W{today.isocalendar()[1]:02d}"
        print_week_detail(calendar, log_status, args.year, current_week)

if __name__ == '__main__':
    main()
