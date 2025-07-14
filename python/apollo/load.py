'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-08-05 12:21:53
LastEditTime: 2025-07-12 14:52:29
Description:
'''
import requests
from bs4 import BeautifulSoup  # type: ignore
import json
import time

url = "https://apollo.baidu.com/community/competition/57/{}"

# url = "https://apollo.baidu.com/api/v1/competition/question/environment/list?taskId=66a8bce072c09b06bc90a826"

headers = {
  "Cookie": "connect.sid=s%3Ay7Ub5K8pU1CMMAo9bFDPBuUHb0d2-pFw.oCWDGWJ0Rc%2FBNhnDe8cxB8fE%2BaF9pTnhHyyemtmL5d8;",
}

start = 154564

while True:

  try:
    response = requests.get(url.format(start), headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # print(f'正在处理 id: {start} {response.text}')

    # 查找所有的 script 标签
    scripts = soup.find_all('script')

    with open('data3.txt', 'a+', encoding='utf-8') as f:
      # 如果有 script 标签，则获取最后一个 script 标签的内容
      if scripts:
        last_script = scripts[-1]
        v = json.loads(last_script.string)
        data = v['props']['pageProps']['submitInfo']
        str = ''
        for item in data['contents']:
          str += f' {item['questionName']}: 得分: {item["score"]}, 用时: {item["taskDuration"]}, taskId: {item['taskId']}   '
        f.write(
            f'id: {start} 总分: {data["totalScore"]}, 总时长: {data['totalDuration']}, {str}\n')
        print(
            f'id: {start}  总分: {data["totalScore"]}, 总时长: {data['totalDuration']}')

  except Exception as e:
    print("Error: ", e)

  start += 1
  time.sleep(2)
