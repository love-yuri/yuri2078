'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-04-18 20:12:46
LastEditTime: 2024-05-21 23:37:58
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
datas = []
labels = []

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

# 读取数据
with open(f'{basePath}/datingTestSet.txt', 'r') as file:
  for item in file:
    values = re.split(r'\s+', item.strip())
    datas.append(values[0:3])
    labels.append(labelMap[values[-1]])

datas: np.ndarray = np.array(datas).astype(float) # 数据集
labels: np.ndarray = np.array(labels) # 标签集

# 计算k个最近邻的标签
def knn_classify(x: np.ndarray, k):
  # 数据归一化 将每个数据 / (最大值 - 最小值)
  global datas, labels
  minVals = datas.min(0) # 获取最小值
  maxVals = datas.max(0) # 获取最大值
  ranges = maxVals - minVals # 获取范围

  datas_r = datas - np.tile(minVals, (datas.shape[0], 1)) # 减去最小值
  datas_r = datas / np.tile(ranges, (datas.shape[0], 1)) # 除以范围

  x = x - minVals
  x = x / ranges

  # 一共有n行数据
  row = datas_r.shape[0]
  dis = datas_r - np.tile(x, (row, 1))
  dis = np.sqrt(np.sum(np.square(dis), axis=1))
  sortIndex = np.argsort(dis)
  result = {}
  for i in range(k):
    result[labels[sortIndex[i]]] = result.get(labels[sortIndex[i]], 0) + 1
  # 排序
  info() << "结果统计: " << result
  return max(result.items(), key=lambda x: x[1])[0]


# 设置新的数据 --------- 测试
testVal = np.array([40000, 10, 1])
val = knn_classify(testVal, 100)

# 公有图例
didntLike = mlines.Line2D([], [], color='black', marker='.',markersize=6, label='不喜欢的人')
smallDoses = mlines.Line2D([], [], color='orange', marker='.',markersize=6, label='魅力一般的人')
largeDoses = mlines.Line2D([], [], color='red', marker='.',markersize=6, label='极具魅力的人')
testRes = mlines.Line2D([], [], color='gray', marker='.',markersize=14, label=resultLabelMap.get(val))

plt.rcParams["font.family"]="SimHei"
pig = plt.figure(figsize=(8, 8))

baseSize = [10 for k in labels]
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
