import numpy as np
import os
import re
from yuri_util import info, get_script_dir
from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt

basePath = get_script_dir(__file__)

datas = []
labels = []

labelMap = {
  'didntLike': 1,
  'smallDoses': 2,
  'largeDoses': 3
}

# 读取数据
with open(f'{basePath}/datingTestSet.txt', 'r') as file:
  for item in file:
    values = re.split(r'\s+', item.strip())
    datas.append(values[0:3])
    labels.append(labelMap[values[-1]])

datas = np.array(datas).astype(float) # 数据集
labels = np.array(labels) # 标签集


# 计算k个最近邻的标签
def knn_classify(x: np.ndarray, k):
  # 数据归一化
  global datas, labels
  minVals = datas.min(0) # 获取最小值
  maxVals = datas.max(0) # 获取最大值
  ranges = maxVals - minVals # 获取范围

  datas = datas - np.tile(minVals, (datas.shape[0], 1)) # 减去最小值
  datas = datas / np.tile(ranges, (datas.shape[0], 1)) # 除以范围

  x = x - minVals
  x = x / ranges

  # 一共有n行数据
  row = datas.shape[0]
  dis = np.tile(x, (row, 1)) - datas
  dis = np.sqrt(np.sum(np.square(dis), axis=1))
  sortIndex = np.argsort(dis)
  result = {}
  for i in range(k):
    result[labels[sortIndex[i]]] = result.get(labels[sortIndex[i]], 0) + 1
  # 排序
  return max(result.items(), key=lambda x: x[1])[0]

# 测试
info() << knn_classify(np.array([2, 2, 1]), 10)
