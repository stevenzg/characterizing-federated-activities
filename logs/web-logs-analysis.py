import os
from datetime import datetime

def analyze_log_file(file_path):
    line_count = 0
    start_time = None
    end_time = None

    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
            
            # Assuming the log format starts with a timestamp like "2023-05-21T00:00:00.000Z"
            try:
                timestamp_str = line.split()[0]
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                
                if start_time is None or timestamp < start_time:
                    start_time = timestamp
                if end_time is None or timestamp > end_time:
                    end_time = timestamp
            except (ValueError, IndexError):
                # Skip lines that don't start with a valid timestamp
                continue

    return line_count, start_time, end_time

log_file_path = './mastodon-web.log'

if os.path.exists(log_file_path):
    total_lines, start_date, end_date = analyze_log_file(log_file_path)
    
    print(f"分析结果：")
    print(f"日志文件总行数：{total_lines}")
    print(f"开始时间：{start_date}")
    print(f"结束时间：{end_date}")
else:
    print(f"错误：文件 {log_file_path} 不存在")
