'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-05-16 11:01:01
LastEditTime: 2024-05-24 19:01:34
Description: 手写数字识别代码
'''
import sys
import time
import threading
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QMessageBox, QMenu, QMenuBar
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QImage, QPainter, QPen, qRgb
from sklearn.neighbors import KNeighborsClassifier
import pathlib
import numpy as np
import os

class DrawWindow(QWidget):
  def __init__(self, *argv, **kwargs):
    super().__init__(*argv, **kwargs)
    self.isDrawing = False
    self.setStyleSheet("""
      background-color: gray;
    """)
    self.setWindowTitle("Draw Window")
    
  def paintEvent(self, event):
    painter = QPainter(self)
    painter.drawImage(self.rect(), self.image, self.image.rect())

  def mousePressEvent(self, event):
    self.isDrawing = True
    self.start_point = event.position()
    self.isDraw = True

  def mouseReleaseEvent(self, event):
    self.drawing = False

  def mouseMoveEvent(self, event):
    if self.isDrawing:
      current_point = event.position()
      painter = QPainter(self.image)
      pen = QPen(Qt.black, 15 * 3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
      painter.setPen(pen)
      painter.setRenderHint(QPainter.Antialiasing, True)
      painter.drawLine(self.start_point, current_point)
      self.start_point = current_point
      self.update()

  def resizeEvent(self, event):
    self.reDraw()

  @Slot()
  def reDraw(self):
    self.isDraw = False
    self.image = QImage(self.size(), QImage.Format_RGB32)
    self.image.fill(Qt.white)
    self.update()

class MainWindow(QWidget):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    

    ## 常用数据配置
    basePath = os.path.dirname(os.path.realpath(__file__))
    # 学习数据路径
    self.learnDataPath = f"{basePath}\\trainingDigits"
    # 测试数据路径
    self.testDataPath = f"{basePath}\\testDigits"
    
    # 初始化互斥锁
    self.mutex = threading.Lock()

    baseMargin = 20 # 基础边距
    baseBtnHeight = 60 # 按钮基础高度
    baseSize = 32 * 15 # 面板基础大小

    self.setWindowTitle("手写数字识别")
    self.resize(baseSize * 2 + baseMargin * 3, baseSize + baseBtnHeight + baseMargin * 3)
    self.setObjectName('mainWindow')

    # 设置手写板
    self.draw = DrawWindow(self)
    self.draw.resize(baseSize, baseSize)
    self.draw.move(baseSize + baseMargin * 2, baseMargin)
    self.draw.show()

    # 重新绘制按钮
    button = self.button = QPushButton('重新画', self)
    button.move(baseSize + baseMargin * 2, baseSize + baseMargin * 2)
    button.clicked.connect(self.draw.reDraw)
    button.resize(baseSize, baseBtnHeight)

    # 识别按钮
    button2 = self.button = QPushButton('立即识别', self)
    button2.move(baseMargin, baseSize + baseMargin * 2)
    button2.clicked.connect(self.identify)
    button2.resize(baseSize, baseBtnHeight)

    # 日志面板
    label = self.label = QLabel(self)
    label.move(20, 20)
    label.resize(baseSize, baseSize)
    label.setObjectName("label")
    label.setAlignment(Qt.AlignmentFlag.AlignTop)

    # 初始化KNN分类器
    self.log('欢迎使用手写数字识别系统')
    self.thread = threading.Thread(target=self.TestData)
    self.thread.start()

    # 设置样式
    self.setStyleSheet("""
      #mainWindow {
        background-color: gray;
      }
      #label { 
        background-color: white; 
        padding: 8px; 
      }
      .QPushButton { 
        font-size: 30px; 
      }
    """)

  @Slot()
  def identify(self):
    if self.isRunning:
      QMessageBox.warning(self, '错误', '正在训练数据中，请等待')
      return
    
    if not self.draw.isDraw:
      QMessageBox.warning(self, '错误', '请在右侧画板中画一个数字')
      return
    
    self.log('正在将图像转为32 x 32 的矩阵...')
    black = qRgb(0, 0, 0)
    w = self.draw.width()
    h = self.draw.height()

    # 初始化像素矩阵
    matrix = np.zeros((w, h))
    
    # 将 黑色画笔内容转为
    for i in range(h):
      for j in range(w):
        pixel = self.draw.image.pixel(j, i)
        matrix[i][j] = 1 if pixel == black else 0

    # 将像素矩阵 的列压缩成32列
    image = []
    for i in range(h):
      data: np.ndarray = matrix[i]
      ma = data.reshape(32, (int)(data.shape[0] / 32))
      image.append((ma.mean(axis=1) > 0).astype(int))
    image = np.array(image)

    matrix = []
    # 遍历被压缩的矩阵压缩行为32行
    for i in range(32):
      ma = image[:, i] # 将每一列转成1行
      ma = ma.reshape(32, (int)(ma.shape[0] / 32)) # 将数据分成32行
      ma = (ma.mean(axis=1) > 0).astype(int) # 将每行的平均值重新组装成新的01数据
      matrix.append(ma)
    # 转置矩阵
    matrix = np.array(matrix).T
    self.log('转换成功, 等待结果返回...')

    res = self.knn.predict(matrix.reshape(1, 1024))
    QMessageBox.information(self, '成功!', f'识别结果为: {res[0]}')
    # for i in range(32):
    #   info() << matrix[i]

  def log(self, text, last=False):
    self.mutex.acquire()
    current_time = time.strftime("%H:%M:%S", time.localtime())
    lines = self.label.text().split('\n')
    baseText = '' if lines.__len__() > 24 else self.label.text()
    if last:
      lines[-2] = f'{current_time} -> {text}'
      self.label.setText('\n'.join(lines))
    else:
      self.label.setText(baseText + f'{current_time} -> {text}\n')
    self.mutex.release()

  def GetData(self, dirName: str):
    labels = []
    datas = []
    try:
      path = pathlib.Path(dirName)
      self.log(f'读取 {path.name}成功, 正在获取测试样本总数')
      fileCount = sum(1 for _ in path.iterdir())
      self.log(f'样本总数为 {fileCount}\n')
      count = 0
      for file in path.iterdir():
        count += 1
        self.log(f'正在读取 {file.name} 进度 {count}/{fileCount}', last=True)
        labels.append(file.name[0])
        martx = []
        for line in file.read_text().replace('\n', ''):
          martx.append(int(line))
        datas.append(martx)
      self.log('读取完毕...')
      return np.array(datas), np.array(labels)
    except Exception as e:
      self.log(f'读取数据失败: {e}')
      return None, None

  def TestData(self):
    self.isRunning = True
    self.log('开始读取训练数据...')
    datas, labels = self.GetData(self.learnDataPath)
    if datas is None or labels is None:
      self.log('测试失败')
      return

    # 开始knn
    k = 5
    self.knn = KNeighborsClassifier(k)
    self.knn.fit(datas, labels)

    self.log('开始读取测试数据...')
    datas_t, labels_t = self.GetData(self.testDataPath)
    if datas is None or labels is None:
      self.log('测试失败')
      return
    # 测试
    errorCount: float = 0.0
    allCount: float = len(datas_t)
    count = 0
    self.log('开始对训练结果进行测试...\n')
    for i in range(len(datas_t)):
      res = self.knn.predict([datas_t[i]])
      count += 1
      self.log(f'测试结果: {res[0]} 实际结果: {labels_t[i]}, {count} / {allCount}', last=True)
      if res[0] != labels_t[i]:
        errorCount += 1.0
    self.log(f'测试完毕, 错误率: {round(errorCount / allCount * 100, 2)}%, 当前k为 -> {k}')
    self.isRunning = False

if __name__ == "__main__":
  app = QApplication(sys.argv)
  mainwindow = MainWindow()
  mainwindow.show()

  sys.exit(app.exec())