'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-04-16 09:10:01
LastEditTime: 2024-04-16 11:07:34
Description: 实验3
'''
import re
import pickle

# 输入数据
text = input('请输入一组数字: ')

# 处理数据 - 写入文本
with open('text.txt', 'w', encoding='utf-8') as file:
  file.writelines('\n'.join(re.split(r'\s+', text)))

# 判断是不是素数
def is_valid_number(number):
  number = int(number)
  if number < 2:
    return False
  for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
      return False
  return True

# 读取文件
with open('text.txt', 'r', encoding='utf-8') as file:
  num = []
  for item in file:
    item = item.strip()
    if re.search(r'^\d{4,8}$', item) and is_valid_number(item):
      print(f'{item} 是正确的数据')
      num.append(item)
    else:
      print(f'{item} 不是正确的数据， 该数据已经移除')
  with open('result.txt', 'w', encoding='utf-8') as file2:
    file2.writelines('\n'.join(num))

data = {
  "Grade":1,
  "Grade_desc":"这是一年级",
  "Class_Name": ("z094191","z094192"),
  "studentNo": [40,40],
}

# 写入文件
with open('class_information.data', 'wb') as file:
  pickle.dump(data, file)


# 读取文件
with open('class_information.data', 'rb') as file:
  print(pickle.load(file))
