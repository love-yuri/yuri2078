'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2023-09-27 13:29:27
LastEditTime: 2023-11-27 20:34:20
Description: 
'''
from datetime import datetime
from time import mktime
from wsgiref.handlers import format_date_time
import hmac
import hashlib
import base64
from urllib.parse import urlencode




cur_time = datetime.now()
date = format_date_time(mktime(cur_time.timetuple()))

tmp = "host: " + "spark-api.xf-yun.com" + "\n"
tmp += "date: " + date + "\n"
tmp += "GET " + "/v1.1/chat" + " HTTP/1.1"
tmp_sha = hmac.new('YWVkMjdmYzJkOWM2YmY1ODUwMjgyNDI4'.encode('utf-8'), tmp.encode('utf-8'),digestmod=hashlib.sha256).digest()
signature = base64.b64encode(tmp_sha).decode(encoding='utf-8')
authorization_origin = f"api_key='a06ad13c5a3fcb31e55f64e2305652be'', algorithm='hmac-sha256', headers='host date request-line', signature='{signature}''"
authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
v = {
		"authorization": authorization, # 上方鉴权生成的authorization
        "date": date,  # 步骤1生成的date
    	"host": "spark-api.xf-yun.com" # 请求的主机名，根据具体接口替换
}
url = "wss://spark-api.xf-yun.com/v3.1/chat?" + urlencode(v)
print(url)