import json
import threading
import time
import logging
import websocket


init_uuid = "665ab5fe8577d09491e5ea93"
start_uuid = "66a8bd2567efaaaa00001000"

def increment_uuid(uuid_str):
    # 将UUID字符串转换为整数
    uuid_int = int(uuid_str, 16)
    # 将整数加1，生成新的UUID字符串
    new_uuid_int = uuid_int + 1
    new_uuid_str = format(new_uuid_int, '032x')
    return new_uuid_str.lstrip('0')

def on_message(ws, message):
    data = json.loads(message)
    with open('data.txt', 'a+', encoding='utf-8') as f:
      if 'data' in data:
        tt = f"{data['data']}"
        print(f'{start_uuid}, 时间: {tt}')
        f.write(f'{start_uuid}, 时间: {tt}\n')
      else:
        print(f'{start_uuid}, {message}')
        f.write(f'{start_uuid}, 没有记录\n')

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"WebSocket 连接关闭: {close_status_code} - {close_msg}")

def on_open(ws):
    print('连接成功')
    ws.send(f'{{"type":"RetrieveFrameCount","recordId":"{init_uuid}"}}')
    
    def run(*args):
        while True:
            try:
                global start_uuid
                message = f'{{"type":"RetrieveFrameCount","recordId":"{start_uuid}"}}'
                ws.send(message)
                # print(f"发送消息: {message}")
                start_uuid = increment_uuid(start_uuid)
                time.sleep(1)  # 每5秒发送一次消息
            except Exception as e:
                print(f"发送消息时出现错误: {e}")
                break
    
    threading.Thread(target=run).start()

websocket.enableTrace(True)
logger = logging.getLogger('websocket')
logger.setLevel(logging.CRITICAL)
ws = websocket.WebSocketApp("wss://apollo.baidu.com/offlineView",
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)
ws.on_open = on_open
ws.run_forever()
