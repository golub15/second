import sys
from random import randint

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    #pass
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pass
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        x = randint(5, self.width() - 5)
        y = randint(5, self.height() - 5)
        pass
        r = min([randint(5, min(x, self.width() - x)),
                 randint(5, min(y, self.height() - y))])
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(x - r, y - r, r * 2, r * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())