'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-05-16 11:01:01
LastEditTime: 2024-05-22 22:39:43
Description: 手写数字识别代码
'''
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from yuri_util import *

class DrawWindow(QWidget):
  def __init__(self, *argv, **kwargs):
    super().__init__(*argv, **kwargs)
    self.isDrawing = False
    self.setStyleSheet('background-color: white;')
    self.setWindowTitle("Draw Window")
    self.resize(600, 600)
    
  def paintEvent(self, event):
    painter = QPainter(self)
    painter.drawImage(self.rect(), self.image, self.image.rect())

  def mousePressEvent(self, event):
    self.isDrawing = True
    self.start_point = event.position()

  def mouseReleaseEvent(self, event):
    self.drawing = False

  def mouseMoveEvent(self, event):
    if self.isDrawing:
      current_point = event.position()
      painter = QPainter(self.image)
      pen = QPen(Qt.black, 15, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
      painter.setPen(pen)
      painter.setRenderHint(QPainter.Antialiasing, True)
      painter.drawLine(self.start_point, current_point)
      self.start_point = current_point
      self.update()

  def resizeEvent(self, event):
    self.image = QImage(self.size(), QImage.Format_RGB32)
    self.image.fill(Qt.white)
    painter = QPainter(self.image)
    painter.drawImage(QPoint(0, 0), self.image)

class MainWindow(QWidget):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.setWindowTitle("手写数字识别")
    self.resize(1100, 600)
    self.draw = DrawWindow(self)
    self.draw.resize(32 * 15, 32 * 15)
    self.draw.move(600, 30)
    self.draw.show()

    self.setStyleSheet("#label { background-color: white; padding: 8px; } \n .QPushButton { font-size: 30px; }")

    button = self.button = QPushButton('上传文件', self)
    label = self.label = QLabel(self)

    button.move(20, 20)
    button.clicked.connect(self.btnClick)
    button.resize(600 - 40, 60)

    label.move(20, 60 + 60)
    label.resize(600 - 40, 600 - 200)
    label.setObjectName("label")
    label.setText('正在识别中...\n识别成功!')
    label.setAlignment(Qt.AlignmentFlag.AlignTop)

    button2 = self.button = QPushButton('立即识别', self)

    button2.move(20, 533)
    button2.clicked.connect(self.identify)
    button2.resize(600 - 40, 60)

  @Slot()
  def btnClick(self):
    fileName = QFileDialog.getOpenFileName(self, '选择文件')[0]
    if fileName != '':
      pixmap = QPixmap(fileName)
      self.label.setPixmap(pixmap)
    

  @Slot()
  def identify(self):
    QMessageBox.information(self, '提示', '识别成功')


if __name__ == "__main__":
  app = QApplication(sys.argv)
  mainwindow = MainWindow()
  mainwindow.show()

  sys.exit(app.exec())