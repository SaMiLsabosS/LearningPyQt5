import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit


class PyYahtzeeUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyYahtzee')

        self.generalLayout = QHBoxLayout()
        self.firstLayout = QVBoxLayout()
        self.secondLayout = QVBoxLayout()

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self.generalLayout.addLayout(self.firstLayout)  # QStackedLayout()
        self.generalLayout.addLayout(self.secondLayout)
        self._centralWidget.setLayout(self.generalLayout)

        self._createDisplay()
        self._createButtons()

    def createDisplay(self):


def main():
    app = QApplication(sys.argv)
    view = PyYahtzeeUI()
    view.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
