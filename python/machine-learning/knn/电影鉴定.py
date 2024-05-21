'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-04-05 22:46:20
LastEditTime: 2024-05-21 19:13:14
Description: 电影鉴定 knn-临近算法学习
'''
import numpy as np
import matplotlib.pyplot as plt
from yuri_util import info, error
import operator

def createData():
  # 创建数据集
  # 第一个参数表示 动作方面镜头数
  # 第二个参数表示 爱情方面镜头数
  group = np.array([[1,101],[5,89],[108,5],[115,8]])

  # 创建标签集
  labels = np.array(['爱情片','爱情片','动作片','动作片'])

  return group, labels

def classify0(inX: np.ndarray, dataSet: np.ndarray, labels: np.ndarray, k):
    #numpy函数shape[0]返回dataSet的行数
    dataSetSize = dataSet.shape[0]
    #在列向量方向上重复inX共1次(横向)，行向量方向上重复inX共dataSetSize次(纵向)
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    #二维特征相减后平方
    sqDiffMat = diffMat**2
    #sum()所有元素相加，sum(0)列相加，sum(1)行相加
    sqDistances = sqDiffMat.sum(axis=1)
    #开方，计算出距离
    distances = sqDistances**0.5
    #返回distances中元素从小到大排序后的索引值
    sortedDistIndices = distances.argsort()
    info() << '和各点的距离 -> ' << distances
    info() << '排序后的结果 -> ' << sortedDistIndices
    #定一个记录类别次数的字典
    classCount = {}
    for i in range(k):
      #取出前k个元素的类别
      voteIlabel = labels[sortedDistIndices[i]]
      #dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
      #计算类别次数
      classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1

    # reverse降序排序字典
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    info() << sortedClassCount
    # 返回次数最多的类别,即所要分类的类别
    return sortedClassCount[0][0]

if __name__ == '__main__':
  group, labels = createData()
  test = [101, 100]
  #kNN分类
  test_class = classify0(test, group, labels, 3)
  xpoint = [p[0] for p in group]
  ypoint = [p[1] for p in group]
  xpoint.append(test[0])
  ypoint.append(test[1])
  plt.plot(xpoint, ypoint, 'o')
  #打印分类结果
  info() << (test_class)
  plt.show()