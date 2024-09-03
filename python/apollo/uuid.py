import uuid

def increment_uuid(uuid_str):
    # 将UUID字符串转换为整数
    uuid_int = int(uuid_str, 16)
    # 将整数加1，生成新的UUID字符串
    new_uuid_int = uuid_int + 1
    new_uuid_str = format(new_uuid_int, '032x')
    return new_uuid_str.lstrip('0')

start_uuid = "665ab5718577d0c6eae5ea92"

# 从起始UUID开始遍历
for _ in range(100):  # 遍历10个UUID为例
    start_uuid = increment_uuid(start_uuid)
    print(start_uuid)
