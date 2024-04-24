import re
import numpy as np

# 动物识别系统
class Animal:
  def __init__(self):
    self.features = {} # 特征map
    self.serialNumber = {
      '毛发': 0,
      '奶': 1,
      '羽毛': 2,
      '会飞': 3,
      '会下蛋': 4,
      '吃肉': 5,
      '犬齿': 6,
      '爪': 7,  
      '眼盯前方': 8,
      '蹄': 9,
      '哺乳动物': 10,
      '鸟': 11,
      '蹄类动物': 12,
      '食肉动物': 13,
      '反刍动物': 14,
      '黄褐色': 15,
      '暗斑点': 16,
      '黑色条纹': 17,
      '金钱豹': 18,
      '长脖子': 19,
      '长腿': 20,
      '虎': 21,
      '不会飞': 22,
      '长颈鹿': 23,
      '黑白二色': 24,
      '斑马': 25,
      '会游泳': 26,
      '鸵鸟': 27,
      '善飞': 28,
      '企鹅': 29,
      '信天翁': 30
    }
    
  def findValue(self, toFind):
    # 返回第一个 value 值为 toFind 的 key,
    return next(k for k, v in self.serialNumber.items() if v == toFind)
  
  def findKeys(self, toFind: int):
    # 返回所有 value 值为 toFind 的 key,
    return [k for k, v in self.features.items() if v == toFind]
    
  def findKey(self, toFind: list):
    toFind = sorted(toFind)
    toFind = tuple(toFind)
    if self.features.get(toFind):
      return self.findValue(self.features.get(toFind))
    else:
      return f'{toFind} 不存在'
  
  def getRules(self):
    baseRules = [
      ("IF 该动物有毛发 THEN 该动物是哺乳动物", "哺乳动物"),
      ("IF 该动物有奶 THEN 该动物是哺乳动物", "哺乳动物"),
      ("IF 该动物有羽毛 THEN 该动物是鸟", "鸟"),
      ("IF 该动物会飞 AND 会下蛋 THEN 该动物是鸟", "鸟"),
      ("IF 该动物吃肉 THEN 该动物是食肉动物", "食肉动物"),
      ("IF 该动物有犬齿 AND 有爪 AND 眼盯前方 THEN 该动物是食肉动物", "食肉动物"),
      ("IF 该动物是哺乳动物 AND 有蹄 THEN 该动物是有蹄类动物", "蹄类动物"),
      ("IF 该动物是哺乳动物 AND 是反刍动物 THEN 该动物是有蹄类动物", "蹄类动物"),
      ("IF 该动物是哺乳动物 AND 是食肉动物 AND 是黄褐色 AND 身上有暗斑点 THEN 该动物是金钱豹", "金钱豹"),
      ("IF 该动物是哺乳动物 AND 是食肉动物 AND 是黄褐色 AND 身上有黑色条纹 THEN 该动物是虎", "虎"),
      ("IF 该动物是有蹄类动物 AND 有长脖子 AND 有长腿 AND 身上有暗斑点 THEN 该动物是长颈鹿", "长颈鹿"),
      ("IF 该动物有蹄类动物 AND 身上有黑色条纹 THEN 该动物是斑马", "斑马"),
      ("IF 该动物是鸟 AND 有长脖子 AND 有长腿 AND 不会飞 AND 有黑白二色 THEN 该动物是鸵鸟", "鸵鸟"),
      ("IF 该动物是鸟 AND 会游泳 AND 不会飞 AND 有黑白二色 THEN 该动物是企鹅", "企鹅"),
      ("IF 该动物是鸟 AND 善飞 THEN 该动物是信天翁", "信天翁")
    ]

    for rule in baseRules:
      result = re.search(r'^IF(.*)THEN', rule[0])
      if result:
        ret = []
        for item in re.split(r'\s+AND\s', result.group(1).strip()):
          item = re.sub(r'该动物有|该动物是|是|有|身上|该动物|', '', item)
          # ret.append(item)
          if item in self.serialNumber:
            ret.append(self.serialNumber.get(item))
          else:
            print(f'{item} 不存在')
        if rule[1] in self.serialNumber:
          self.features[tuple(sorted(ret))] = (int)(self.serialNumber.get(rule[1]))
        else:
          print(f'{rule[1]} 不存在')

    # 寻找别的规则
    for key, value in self.features.copy().items():
      self.findAll(key, value)

    # 打印结果
    # for key, value in self.features.items():
    #   print(f'key -> {key}, value -> {value}')
  
  # 添加特征
  def add_feature(self, feature):
    self.features.add(feature)

  def findAll(self, baseList, value):
    for i, k in enumerate(baseList):
      for keys in self.findKeys(k):
        data = list(baseList)
        data[i:i+1] = list(keys)
        if not self.features.get(tuple(data)):
          self.features[tuple(sorted(data))] = value
          self.findAll(data, value)

  def getResult(self, feature: list):

    result = []
    for item in feature:
      if item in self.serialNumber:
        result.append(self.serialNumber.get(item))
      else:
        raise TypeError(f'{item} 不存在')
    print(self.findKey(result))



if __name__ == "__main__":
  animal = Animal()
  animal.getRules()
  conditions = []

  while True:
    condition = input("请输入条件(输入0结束): ")
    if condition == '0':
        break
    conditions.append(condition)
  animal.getResult(conditions)

  # animal.getResult(['奶'])