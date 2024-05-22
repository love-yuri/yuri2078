'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-04-01 13:56:46
LastEditTime: 2024-05-22 21:31:34
Description: 自动将所有 /opt/apollo/neo/include 目录下的protobuf 头文件， 添加到系统include目录
'''

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QPen, QColor, QImage
from PySide6.QtCore import Qt, QPoint

class DrawingWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.drawing = False
        self.last_point = QPoint()
        self.current_point = QPoint()
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())
        # if self.drawing:
        #     pen = QPen(Qt.black, 3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        #     painter.setPen(pen)
        #     painter.setRenderHint(QPainter.Antialiasing, True)  # 启用抗锯齿
            # painter.drawLine(self.last_point, self.current_point)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.position()
            self.current_point = self.last_point

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.current_point = event.position()
            painter = QPainter(self.image)
            pen = QPen(Qt.black, 3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen)
            painter.setRenderHint(QPainter.Antialiasing, True)  # 启用抗锯齿
            painter.drawLine(self.last_point, self.current_point)
            self.last_point = self.current_point
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.update()

    def resizeEvent(self, event):
        print('resize')
        new_image = QImage(self.size(), QImage.Format_RGB32)
        new_image.fill(Qt.white)
        painter = QPainter(new_image)
        painter.drawImage(QPoint(0, 0), self.image)
        self.image = new_image
        super().resizeEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Drawing Application')
        self.drawing_widget = DrawingWidget()
        self.setCentralWidget(self.drawing_widget)
        self.resize(800, 600)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
