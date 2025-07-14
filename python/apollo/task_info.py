'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-08-05 12:21:53
LastEditTime: 2025-07-12 15:11:18
Description:
'''
import requests
from bs4 import BeautifulSoup  # type: ignore
import json
import time

url = "https://apollo.baidu.com/community/competition/57/{}"

# url = "https://apollo.baidu.com/api/v1/competition/question/environment/list?taskId=6871fa3ed3419710470d19e5&competitionId=57"

headers = {
    "Cookie": "connect.sid=s%3Ay7Ub5K8pU1CMMAo9bFDPBuUHb0d2-pFw.oCWDGWJ0Rc%2FBNhnDe8cxB8fE%2BaF9pTnhHyyemtmL5d8;",
}

start = 152594

response = requests.get(url.format(start), headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# print(f'正在处理 id: {start} {response.text}')

# 查找所有的 script 标签
scripts = soup.find_all('script')

with open('index.html', 'w', encoding='utf-8') as f:
  f.write(response.text)
