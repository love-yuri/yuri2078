'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2025-11-03 18:57:27
LastEditTime: 2025-11-03 19:57:02
Description: 
'''
import sqlite3
from datetime import datetime
import re

file = '/home/yuri/love-yuri/yuri2078/python/yuri/journal.txt'
regex = r'(.*写于 *([\d \d\.\d]+))[ \n]*(.*)'

conn = sqlite3.connect('/home/yuri/love-yuri/Journal/composeApp/journal.db')

sql = """
INSERT INTO Journal (id, title, content, createdAt, updatedAt, mood, weather) 
VALUES (?, ?, ?, ?, ?, '', '多云 13℃')
"""
with open(file, 'r') as f:
  for line in f.read().split('\n\n'):
    line = line.strip()
    res = re.search(regex, line)

    if res:
      # print(f'-----------------------------------------------------------------------------------\n\n')
      dt = datetime.strptime(res.group(2), "%Y %m %d %H.%M")
      timestamp = int(dt.timestamp()) * 1000

      # print(f'匹配: {timestamp} -> {res.group(3)}')

      data = (timestamp, res.group(1), res.group(3), timestamp, timestamp)
      cursor = conn.cursor()
      cursor.execute(sql, data)
      conn.commit()
    else:
      print(f'没有匹配 {line}')

conn.close()