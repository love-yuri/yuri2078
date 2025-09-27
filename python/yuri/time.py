'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2025-09-11 20:37:21
LastEditTime: 2025-09-11 20:38:43
Description: 
'''
from datetime import datetime, timedelta

# 毫秒时间戳
timestamp_ms = 148044912790

# 转换为秒和毫秒
seconds = timestamp_ms // 1000
milliseconds = timestamp_ms % 1000

# 从Unix纪元开始计算
epoch = datetime(1970, 1, 1)
result_date = epoch + timedelta(seconds=seconds, milliseconds=milliseconds)

print(f"时间戳: {timestamp_ms} 毫秒")
print(f"转换为: {result_date.strftime('%Y年%m月%d日 %A %H:%M:%S.%f')[:-3]}")