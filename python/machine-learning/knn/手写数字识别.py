'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-05-22 20:10:56
LastEditTime: 2024-05-23 11:35:45
Description: knn手写数字识别
'''
import numpy as np
import pathlib
from yuri_util import *
from sklearn.neighbors import KNeighborsClassifier

def GetData(dirName: str):
  labels = []
  datas = []
  path = pathlib.Path(dirName)
  for file in path.iterdir():
    labels.append(file.name[0])
    martx = []
    for line in file.read_text().replace('\n', ''):
      martx.append(int(line))
    datas.append(martx)
  return np.array(datas), np.array(labels)

if __name__ == "__main__":
  datas, labels = GetData("D:\\love-yuri\\yuri2078\\python\\machine-learning\\knn\\trainingDigits")
  
  # 开始knn
  knn = KNeighborsClassifier(10)
  knn.fit(datas, labels)

  datas_t, labels_t = GetData("D:\\love-yuri\\yuri2078\\python\\machine-learning\\knn\\testDigits")

  # 测试
  errorCount: float = 0.0
  for i in range(len(datas_t)):
    res = knn.predict([datas_t[i]])
    info() << "测试结果: " << res[0] << " 实际结果: " << labels_t[i]
    if res[0] != labels_t[i]:
      errorCount += 1.0
  info() << "本次测试错误率: " << round(errorCount / len(datas_t) * 100, 2) << "%"

