list = [1, 2, 3, 4, 5]
list[2] = 666
print(list) # 列表

# 字典
stu = {
  'name': 'yuri',
  'age': 23
}
stu['age'] = 666
print(stu)

# 元组
print((1, 2, 3, 4))

# 实验 6

import re

str = """
In a world full of 你好 谢谢 constant change and uncertainty, it is important to adapt and evolve. The key to success lies in our ability to embrace new challenges and learn from our experiences. Every obstacle we face is an opportunity for growth and development. With determination and perseverance, we can overcome any hurdle that comes our way.
The beauty of . life 真的 lies in its unpredictability. Each day brings new possibilities and adventures waiting to be explored. It is up to us to seize the moment and make the most of every opportunity that comes our way. By staying curious and open-minded, we can continue to learn and grow throughout our lives.
As we navigate the , twists 谢谢 and turns of life, it is essential to stay true to ourselves and our values. Integrity and honesty will always lead us in the right direction, even when the path ahead seems unclear. By staying grounded and focused on what truly matters, we can weather any storm and emerge stronger than before.
So let us embrace the challenges that come our way, knowing that each obstacle is a stepping stone on the path to success. With courage and resilience, we can achieve our dreams and create a brighter future for ourselves and those around us. Let us face each day with optimism and determination, ready to conquer whatever challenges may arise.
"""

countWord = {}
for word in re.findall(r'[a-z|A-Z|\u4e00-\u9fa5]+', str):
  countWord.setdefault(word, 0)
  countWord[word] += 1

# 遍历字典
for key, value in countWord.items():
  print(f'{key} 出现了 {value}次!')