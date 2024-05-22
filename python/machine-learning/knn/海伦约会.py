'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-04-18 20:12:46
LastEditTime: 2024-05-22 08:46:14
Description: 海伦约会
'''
import numpy as np
import os
import re
from yuri_util import info, Utils
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

basePath = Utils.get_script_dir(__file__)

# 0：每年获得的飞行常客里程数
# 1：玩视频游戏所消耗时间百分比
# 2：每周消费的冰淇淋公升数

# 标签map
labelMap = {
  'didntLike': 1,
  'smallDoses': 2,
  'largeDoses': 3
}

resultLabelMap = {
  1: '不喜欢的人',
  2: '魅力一般的人',
  3: '极具魅力的人'
}

colorMap = {
  1: 'black', 
  2: 'orange', 
  3: 'red'
}

# 读取测试数据
def getTestData():
  # 读取数据
  with open(f'{basePath}/datingTestSet.txt', 'r') as file:
    datas = []
    labels = []
    for item in file:
      values = re.split(r'\s+', item.strip())
      datas.append(values[0:3])
      labels.append(labelMap[values[-1]])
  return np.array(datas).astype(float), np.array(labels)

# 计算k个最近邻的标签
# x: 待测试的数据
# k: 最近邻的个数
# datas: 数据集 包含所有数据 用于计算距离和标签
# labels: 标签集 包含所有标签 用于计算标签
def knn_classify(x: np.ndarray, k, datas: np.ndarray, labels: np.ndarray):
  # 数据归一化 将每个数据 / (最大值 - 最小值)
  minVals = datas.min(0) # 获取最小值
  maxVals = datas.max(0) # 获取最大值
  ranges = maxVals - minVals # 获取范围

  datas = datas - np.tile(minVals, (datas.shape[0], 1)) # 减去最小值
  datas = datas / np.tile(ranges, (datas.shape[0], 1)) # 除以范围

  x = x - minVals
  x = x / ranges

  # 一共有n行数据
  row = datas.shape[0]
  dis = datas - np.tile(x, (row, 1))
  dis = np.sqrt(np.sum(np.square(dis), axis=1))
  sortIndex = np.argsort(dis)
  result = {}
  for i in range(k):
    result[labels[sortIndex[i]]] = result.get(labels[sortIndex[i]], 0) + 1
  # 排序
  # info() << "结果统计: " << result
  return max(result.items(), key=lambda x: x[1])[0]

# 测试数据正确性
# ratio 测试集比例
# k 最近邻个数
def datingClassTest(ratio: float, k: int, datas: np.ndarray, labels: np.ndarray):
  # 测试数据集比例 10%, 前10%用作测试数据，后90%用作训练数据
  numTest = int(ratio * datas.shape[0])
  # 错误计数器 用于记录错误率
  errorCount: float = 0.0
  for i in range(numTest):
    res = knn_classify(datas[i], k, datas[numTest:].copy(), labels[numTest:].copy()) # 测试数据
    if res != labels[i]: # 如果分类结果与标签不一致，则错误计数器加1
      errorCount += 1.0
    info() << "分类结果: " << res << " 真实结果: " << labels[i]  << " 是否正确: " << (res == labels[i]) # 输出分类结果和真实结果，以及是否正确

  info() << "错误率: " << errorCount / numTest * 100.0 << "%" # 输出错误率

def showData(datas: np.ndarray, labels: np.ndarray):
  # 设置新的数据 --------- 测试
  testVal = np.array([40000, 10, 1])
  val = knn_classify(testVal, 30, datas.copy(), labels.copy())

  # 公有图例
  didntLike = mlines.Line2D([], [], color='black', marker='.',markersize=6, label='不喜欢的人')
  smallDoses = mlines.Line2D([], [], color='orange', marker='.',markersize=6, label='魅力一般的人')
  largeDoses = mlines.Line2D([], [], color='red', marker='.',markersize=6, label='极具魅力的人')
  testRes = mlines.Line2D([], [], color='gray', marker='.',markersize=14, label=resultLabelMap.get(val))

  plt.rcParams["font.family"]="SimHei"
  pig = plt.figure(figsize=(8, 8))

  baseSize = [10 for _ in labels]
  baseColor = [colorMap.get(k) for k in labels]

  # 添加最后的测试数据
  baseSize.append(140)
  baseColor.append('gray') # 测试数据颜色

  datas = np.append(datas, [testVal], axis=0)
  labels = np.append(labels, val)

  ax = pig.add_subplot(221)
  ax.scatter(datas[:, 0], datas[:, 1], s=baseSize, c=baseColor)
  ax.set_title('每年获得的飞行常客里程数与玩视频游戏所消耗时间占比', fontsize=7)
  ax.set_xlabel('每年获得的飞行常客里程数', fontsize=8)
  ax.set_ylabel('玩视频游戏所消耗时间百分比', fontsize=8)

  #添加图例
  ax.legend(handles=[didntLike, smallDoses, largeDoses, testRes])
  ax.legend(handles=[didntLike, smallDoses, largeDoses, testRes])
  ax.legend(handles=[didntLike, smallDoses, largeDoses, testRes])
  ax.legend(handles=[didntLike, smallDoses, largeDoses, testRes])

  ax = pig.add_subplot(222)
  ax.scatter(datas[:, 0], datas[:, 2], s=baseSize, c=baseColor)
  ax.set_title('每年获得的飞行常客里程数与每周消费的冰淇淋公升数', fontsize=7)
  ax.set_xlabel('每年获得的飞行常客里程数', fontsize=8)
  ax.set_ylabel('每周消费的冰淇淋公升数', fontsize=8)

  #添加图例
  ax.legend(handles=[didntLike, smallDoses, largeDoses, testRes])
  ax.legend(handles=[didntLike, smallDoses, largeDoses, testRes])
  ax.legend(handles=[didntLike, smallDoses, largeDoses, testRes])
  ax.legend(handles=[didntLike, smallDoses, largeDoses, testRes])

  ax = pig.add_subplot(223)
  ax.scatter(datas[:, 1], datas[:, 2], s=baseSize, c=baseColor)
  ax.set_title('玩视频游戏所消耗时间占比与每周消费的冰淇淋公升数', fontsize=7)
  ax.set_xlabel('玩视频游戏所消耗时间百分比', fontsize=8)
  ax.set_ylabel('每周消费的冰淇淋公升数', fontsize=8)

  #添加图例
  ax.legend(handles=[didntLike, smallDoses, largeDoses, testRes])
  ax.legend(handles=[didntLike, smallDoses, largeDoses, testRes])
  ax.legend(handles=[didntLike, smallDoses, largeDoses, testRes])
  ax.legend(handles=[didntLike, smallDoses, largeDoses, testRes])

  ax = pig.add_subplot(224)


  plt.show()

if __name__ == '__main__':
  datas, labels = getTestData()
  datingClassTest(0.1, 10, datas, labels)
  showData(datas, labels)