import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    widget = QWidget()  # creates a window that is visible
    button1 = QPushButton("One")
    button2 = QPushButton("Two")
    button3 = QPushButton("Three")
    button4 = QPushButton("Four")
    button5 = QPushButton("Five")
    button6 = QPushButton("Six")

    ##    layout = QHBoxLayout(widget)
    ##    layout.addWidget(button1)
    ##    layout.addWidget(button2)
    ##    layout.addWidget(button3)

    grid = QGridLayout(widget)
    grid.addWidget(button1, 0, 0)
    grid.addWidget(button2, 1, 1)
    grid.addWidget(button3, 2, 2)
    grid.addWidget(button4, 3, 3)

    hbox = QHBoxLayout(widget)
    hbox.addWidget(button5)
    hbox.addWidget(button6)

    # widget.addLayout(hbox)

    ##    widget.setFixedSize(800,600)
    ##    widget.setWindowTitle('Steven Payne')
    ##    widget.setStyleSheet(
    ##        'background-color: #cca8a5;'
    ##    )

    widget.show()  # displays window
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()