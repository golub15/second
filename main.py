from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen
import sys


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.ok = False

    def run(self):
        self.ok = True

    def paintEvent(self, event):
        if self.ok:
            self.qp = QPainter(self)
            self.qp.begin(self)
            self.draw()
            self.qp.end()
            self.update()

    def draw(self):
        self.qp.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
        self.qp.drawEllipse(100, 100, 100, 100)
        self.qp.drawEllipse(200, 200, 100, 100)
        self.qp.drawEllipse(100, 200, 100, 100)


app = QApplication(sys.argv)
ex = Example()
ex.show()
app.exit(app.exec())