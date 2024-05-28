'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-05-26 22:26:13
LastEditTime: 2024-05-28 23:00:39
Description: 日志窗口
'''
import sys
import time
import threading

from PySide6.QtWidgets import QWidget, QMenuBar, QMenu, QLabel, QApplication, QScrollArea
from PySide6.QtGui import QPixmap, QPen, QPainter, QAction
from PySide6.QtCore import Qt, Slot, QPoint, QThread, Signal

from yuri_util import info


class LogWidget(QWidget):
  def __init__(self, *args, **kwargs):
    self.isAlive = True
    self.mutex = threading.Lock()
    super().__init__(*args, **kwargs)
    
    self.resize(600, 600)
    
    self.label = QLabel(self)
    self.label.setStyleSheet('padding: 10px')
    self.label.setAlignment(Qt.AlignmentFlag.AlignTop)
    
    self.scrollArea = QScrollArea(self)
    self.scrollArea.resize(self.size())
    self.scrollArea.setWidgetResizable(True)
    self.scrollArea.setWidget(self.label)
    
    self.work = Worker()
    self.work.update.connect(self.needUpdate)
    self.work.start()
  
    self.log('')
    
    #
    # self.thread = threading.Thread(target=self.test)
    # self.thread.start()
  
  def log(self, text, reLog=False):
    self.mutex.acquire()
    # current_time = time.strftime("%H:%M:%S", time.localtime())
    # if reLog:
    #   lines = self.label.text().split('\n')
    #   lines[-2] = f'{current_time} -> {text}'
    #   self.label.setText('\n'.join(lines))
    # else:
    #   self.label.setText(self.label.text() + f'{current_time} -> {text}\n')

    self.mutex.release()
  
  def closeEvent(self, event):
    self.isAlive = False
    self.work.isAlive = False
    self.work.quit()
    self.work.wait()
    event.accept()
    
  @Slot()
  def needUpdate(self):
    self.label.setText("""
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>Title</title>
          <style>
              * {
                  box-sizing: border-box;
                  color: red;
                  margin: 0;
                  padding: 0;
              }
          </style>
      </head>
      <body>
          <p>Hello World</p>
      </body>
      </html>
    """)


class Worker(QThread):
  update = Signal()
  isAlive = True
  
  def __init__(self):
    super().__init__()
  
  def run(self):
    while self.isAlive:
      time.sleep(1)
      self.update.emit()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = LogWidget()
  ex.show()
  sys.exit(app.exec())
