'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-04-05 22:46:20
LastEditTime: 2024-04-18 19:57:24
Description: 电影鉴定 knn-临近算法学习
'''
import numpy as np
from yuri_log import info, error
import operator

def createData():
  # 创建数据集
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
    info() << sortedDistIndices
    #定一个记录类别次数的字典
    classCount = {}
    for i in range(k):
      #取出前k个元素的类别
      voteIlabel = labels[sortedDistIndices[i]]
      info() << sortedDistIndices[i]
      #dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
      #计算类别次数
      classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1

    #reverse降序排序字典
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    info() << sortedClassCount
    #返回次数最多的类别,即所要分类的类别
    return sortedClassCount[0][0]

if __name__ == '__main__':
  group, labels = createData()
  test = [101,200]
  #kNN分类
  test_class = classify0(test, group, labels, 3)
  #打印分类结果
  print(test_class)