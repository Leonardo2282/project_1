import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.click)
        self.qp = QPainter()

    def click(self):
        self.update()

    def paintEvent(self, event):
        self.qp.begin(self)
        self.draw()
        self.qp.end()

    def draw(self):
        self.qp.setBrush(QColor(randint(200, 250), randint(200, 250), 0))
        self.coord = [350, 250]
        size = randint(10, 200)
        self.qp.drawEllipse(*self.coord, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

