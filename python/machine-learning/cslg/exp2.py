'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-05-17 13:38:36
LastEditTime: 2024-05-20 22:08:23
Description: 洗衣机洗涤时间的模糊控制
'''
import numpy as np
import re

# 定义模糊集合
mud_levels = np.array([0, 0.5, 1])  # 污泥
oil_levels = np.array([0, 0.5, 1])  # 油脂
wash_time = np.array([0, 0.25, 0.5, 0.75, 1])  # 洗涤时间

# 输入模糊集合
# mud_input = np.array([0, 0.83, 0.6])
# oil_input = np.array([0, 0.71, 0.7])
tips = '请输入{}的隶属度集合，每个集合包含三个值，用空格或者逗号分隔: '
mud_input = np.array([float(k) for k in re.findall(r'\d+\.{0,1}\d*', input(tips.format('污泥')))])
oil_input = np.array([float(k) for k in re.findall(r'\d+\.{0,1}\d*', input(tips.format('油脂')))])

# 规则结果
rule_result = {
  1: '短',
  2: '较短',
  3: '中等',
  4: '较长',
  5: '长'
}
rule_result_wash_time = {
  0: '短',
  0.25: '较短',
  0.5: '中等',
  0.75: '较长',
  1: '长'
}
# 模糊规则控制矩阵
rule_matrix = np.array([
  [1, 2, 3],
  [2, 3, 4],
  [3, 4, 5]   
])

# 计算模糊关系
def fuzzy_relation(input_set, levels):
  relation = np.zeros_like(levels)
  for i, level in enumerate(levels):
    relation[i] = np.max(np.minimum(input_set, level))
  return relation

mud_relation = fuzzy_relation(mud_input, mud_levels)
print(f'污泥模糊关系: {mud_relation}')
oil_relation = fuzzy_relation(oil_input, oil_levels)
print(f'油脂模糊关系: {oil_relation}')

# 模糊推理
fuzzy_result = np.zeros_like(wash_time)
for i in range(len(mud_relation)):
  for j in range(len(oil_relation)):
    fuzzy_result = np.maximum(fuzzy_result, np.minimum(mud_relation[i], oil_relation[j]) * rule_matrix[i][j])

print(f'模糊推理结果: {fuzzy_result}')

def find_nearest_smaller(arr, target):
  sorted_arr = sorted(arr)
  for val in sorted_arr:
    if val > target:
      break
    nearest_smaller = val
  return nearest_smaller

# 模糊决策
def defuzzify(fuzzy_set, method='centroid'):
  if method == 'max_membership':
    return rule_result.get(int(np.max(fuzzy_set))) 
  elif method == 'centroid':
    res = np.sum(fuzzy_set * wash_time) / np.sum(fuzzy_set)
    return rule_result_wash_time.get(find_nearest_smaller(wash_time, res))

print(f"最大隶属度法结果: {defuzzify(fuzzy_result, 'max_membership')}")
print(f"加权平均法结果: {defuzzify(fuzzy_result, 'centroid')}")