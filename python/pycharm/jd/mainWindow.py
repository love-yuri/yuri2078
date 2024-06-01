import time
import threading

from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, Slot
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import utils.JD
import numpy as np
import widgets.MainWindowUi
from utils.yuri_util import info, Utils


class MainWindow(QWidget):
  def __init__(self, *args, **kwargs):
    self.jd = utils.JD.JD(Utils.get_script_dir(__file__))
    self.jd.update.connect(self.updateCommentSize)
    # self.thread.start()
    
    super().__init__(*args, **kwargs)
    self.resize(1200, 800)
    self.setStyleSheet("""
      #log {
        font-size: 23px;
        padding: 10px;
        border: 2px skyblue dashed;
      }
    """)
    
    self.ui = widgets.MainWindowUi.Ui_Form()
    self.ui.setupUi(self)
    self.ui.label.setObjectName('log')
    self.ui.label.setText(
      f'<p style="font-size: 20px">目前共有 <span style="color: darkslategray;">{len(self.jd.comment)}</span> 条评论</p>')
    self.ui.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    self.ui.verticalLayout_2.setAlignment(Qt.AlignmentFlag.AlignTop)
    
    self.ui.pushButton_5.clicked.connect(self.startOrEndGetComment)
    
    # 处理显示图表
    self.figure = Figure()
    self.canvas = FigureCanvas(self.figure)
    self.ui.verticalLayout.addWidget(self.canvas)
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    
    self.ui.pushButton_6.clicked.connect(self.drawTimelineChart)
    self.ui.pushButton.clicked.connect(self.drawProductColorChart)
    self.ui.pushButton_2.clicked.connect(self.drawProductSizeChart)
    self.ui.pushButton_4.clicked.connect(self.drawLocationChart)
    self.ui.pushButton_3.clicked.connect(self.saveComments)
    self.startOrEndGetComment()
    
    self.drawTimelineChart()

  
  @Slot()
  def updateCommentSize(self, size: int):
    self.ui.label.setText(
      f'<p style="font-size: 20px">正在爬取评论... 目前共有 <span style="color: darkslategray;">{size}</span> 条评论</p>')
  
  @Slot()
  def saveComments(self):
    dialog = QFileDialog(self, )
    fileName = dialog.getSaveFileName(self, "保存文件", self.jd.basePath, "csv Files (*.csv)")
    if fileName[0]:
      self.jd.saveComment(path=fileName[0])
      time.sleep(1)
      QMessageBox.information(self, '结果', '保存成功')
      
    
  @Slot()
  def drawTimelineChart(self):
    self.figure.clear()
    x, y = self.jd.TimelineChart()
    
    ax = self.figure.add_subplot(111)
    ax.plot(x, y)
    ax.set_xticks([int(k) for k in x])
    ax.set_title(u"华为p70每月购买天数分析")
    
    # 更新图形
    self.canvas.draw()
  
  @Slot()
  def drawProductColorChart(self):
    self.figure.clear()
    
    ax = self.figure.add_subplot(111)
    labels, sizes = self.jd.ProductColorChart()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title(u"华为p70手机颜色分布图")
    self.canvas.draw()
  
  @Slot()
  def drawProductSizeChart(self):
    self.figure.clear()
    
    ax = self.figure.add_subplot(111)
    labels, sizes = self.jd.ProductSizeChart()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title(u"华为p70手机版本图")
    self.canvas.draw()
  
  @Slot()
  def drawLocationChart(self):
    self.figure.clear()
    
    ax = self.figure.add_subplot(111)
    labels, sizes = self.jd.LocationChart()
    ax.plot(range(1, len(labels) + 1), sizes)
    ax.set_xticks(range(1, len(labels) + 1))
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_title(u"华为p70购买者地域分布")
    self.canvas.draw()
  
  @Slot()
  def startOrEndGetComment(self):
    if self.jd.isAlive:
      self.ui.pushButton_5.setText("开始获取评论")
      self.ui.label.setText(
        f'<p style="font-size: 20px">目前共有 <span style="color: darkslategray;">{len(self.jd.comment)}</span> 条评论</p>')
      self.jd.isAlive = False
      self.jd.quit()
      self.jd.wait()
    
    else:
      self.ui.pushButton_5.setText("暂停获取评论")
      self.jd.isAlive = True
      self.jd.start()
  
  def closeEvent(self, event):
    self.jd.isAlive = False
    self.jd.quit()
    self.jd.wait()
    event.accept()
