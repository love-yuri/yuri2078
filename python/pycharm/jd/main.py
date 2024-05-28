"""
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-05-26 13:24:43
LastEditTime: 2024-05-28 16:01:47
Description: 京东评论爬取-分析
"""
import sys
import time

import requests
from utils.yuri_util import *
from mainWindow import MainWindow
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
  app = QApplication(sys.argv)

  mainWindow = MainWindow()
  mainWindow.show()

  sys.exit(app.exec())
  
  
