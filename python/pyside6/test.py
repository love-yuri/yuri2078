'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-05-22 20:47:38
LastEditTime: 2024-05-22 21:51:19
Description: 测试
'''
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QImage, QPainter, QPen
from yuri_util import *
import sys

class DrawWindow(QtWidgets.QMainWindow):
  def __init__(self, *argv, **kwargs):
    super().__init__(*argv, **kwargs)
    self.isDrawing = False
    self.setStyleSheet('background-color: white;')
    self.setWindowTitle("Draw Window")
    self.resize(800, 800)
    self.image = QImage(self.size(), QImage.Format_RGB32)
    self.image.fill(Qt.white)
    painter = QPainter(self.image)
    painter.drawImage(QPoint(0, 0), self.image)
    
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
      pen = QPen(Qt.black, 3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
      painter.setPen(pen)
      painter.setRenderHint(QPainter.Antialiasing, True)
      painter.drawLine(self.start_point, current_point)
      self.start_point = current_point
      self.update()

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  window = DrawWindow()
  window.show()
  sys.exit(app.exec())