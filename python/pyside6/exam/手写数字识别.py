'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-05-16 11:01:01
LastEditTime: 2024-05-17 14:36:44
Description: 手写数字识别代码
'''
import sys
from PySide6 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QWidget):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.resize(600, 600)

    self.setStyleSheet("#label { background-color: gray } \n .QPushButton { font-size: 30px; }")

    button = self.button = QtWidgets.QPushButton('上传文件', self)
    label = self.label = QtWidgets.QLabel(self)

    button.move(20, 20)
    button.clicked.connect(self.btnClick)
    button.resize(600 - 40, 60)

    label.move(20, 60 + 60)
    label.resize(600 - 40, 600 - 200)
    label.setObjectName("label")

    button2 = self.button = QtWidgets.QPushButton('立即识别', self)

    button2.move(20, 533)
    button2.clicked.connect(self.identify)
    button2.resize(600 - 40, 60)

  @QtCore.Slot()
  def btnClick(self):
    fileName = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件')[0]
    pixmap = QtGui.QPixmap(fileName)
    self.label.setPixmap(pixmap)
    

  @QtCore.Slot()
  def identify(self):
    QtWidgets.QMessageBox.information(self, '提示', '识别成功')


if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  mainwindow = MainWindow()
  mainwindow.show()

  sys.exit(app.exec())