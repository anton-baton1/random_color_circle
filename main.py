import random
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI import Ui_MainWindow

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.paint = False
        self.circle_btn.clicked.connect(self.click)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(
            QBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), Qt.SolidPattern))
        pos_x, pos_y = random.randint(0, 400), random.randint(0, 300)
        diameter = random.randint(0, 100)
        qp.drawEllipse(pos_x, pos_y, diameter, diameter)
        qp.end()

    def click(self):
        self.paint = True
        self.update()

    def paint(self, qp):
        qp.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        pos_x, pos_y = random.randint(0, 400), random.randint(0, 300)
        diameter = random.randint(0, 100)
        qp.drawEllipse(pos_x, pos_y, diameter, diameter)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
