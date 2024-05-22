'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-05-22 09:04:31
LastEditTime: 2024-05-22 19:12:36
Description: sklearn 的 knn算法学习
'''
from yuri_util import *
import numpy as np
from sklearn.neighbors import KNeighborsClassifier as KNN

# knn.predict_proba(testValue) 返回数据的概率
# knn.predict(testValue) 返回数据的预测结果
# knn.score(datas, labels) 返回准确率
# knn.fit(datas, labels) 训练数据
# knn.get_params() 获取估计器参数

def getLabel(xy):
  if xy[0] > 0 and xy[1] > 0:
    return 1
  elif xy[0] * xy[1] > 0:
    return -1
  else:
    return 0


knn = KNN(100)

x_random = np.random.randint(-100, 100, 20000)
y_random = np.random.randint(-100, 100, 20000)
datas = np.column_stack((x_random, y_random))
labels = [getLabel(xy) for xy in datas]

knn.fit(datas, labels)

testValue = [[100, 200]]

info() << f"预测 {testValue} 的概率为: " << knn.predict_proba(testValue) << " , 结果为: " << knn.predict(testValue)

x_random = np.random.randint(-100, 100, 2000)
y_random = np.random.randint(-100, 100, 2000)
datas = np.column_stack((x_random, y_random))
labels = [getLabel(xy) for xy in datas]

info() << "准确率: " << knn.score(datas, labels)