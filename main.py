from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from random import randrange
from PyQt5 import uic

class Paint(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui',self)
        self.setGeometry(0,0,600,600)
        self.f = False
        self.pushButton.clicked.connect(self.push)
    def push(self):
        self.f = True
        self.update()

    def paintEvent(self, event):
        if self.f:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        f = False

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 0, 0))
        qp.drawEllipse(0,0,randrange(0,600),randrange(0,600))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Paint()
    ex.show()
    app.exit(app.exec_())