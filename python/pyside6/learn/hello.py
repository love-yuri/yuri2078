import sys
import os
from PySide6 import QtWidgets, QtCore

class MainWindow(QtWidgets.QWidget):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.resize(300, 300)
    self.button = QtWidgets.QPushButton("请选择一个文件", self)
    self.button.clicked.connect(self.onClick)
    self.button.resize(300, 300)

  @QtCore.Slot()
  def onClick(self):
    dialog = QtWidgets.QFileDialog()
    fileName = dialog.getOpenFileName()[0]
    print(f'文件名 -> {fileName}')
    with open(fileName, 'r', encoding='utf-8') as file:
      QtWidgets.QMessageBox.information(self, f'{fileName}', f'{file.read()}')
      print(f'文件内容 -> {file.read()}')


if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  mainWindow = MainWindow()
  mainWindow.show()
  sys.exit(app.exec())