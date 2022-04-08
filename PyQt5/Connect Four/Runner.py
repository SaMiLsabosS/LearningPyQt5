import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Board import Board


def window():
    app = QApplication(sys.argv)

    widget = QWidget()
    widget.setWindowTitle('Python Connect 4')
    widget.setGeometry(100, 100, 478, 524)
    widget.setStyleSheet(
        'background-color: white;'
        'border: none;'
        'font-size: 30px;'
        'font-weight: bold;'
    )

    label = QLabel()
    board = Board()
    grid = QGridLayout()

if __name__ == '__main__':
    window()