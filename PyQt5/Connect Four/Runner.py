import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Board import Board


def window():
    app = QApplication(sys.argv)

    widget = QWidget()
    widget.setWindowTitle('Python Connect Four')
    widget.setGeometry(100, 100, 478, 524)
    widget.setStyleSheet(
        'background-color: white;'
        'border: none;'
        'font-size: 30px;'
        'font-weight: bold;'
    )

    label = QLabel()  # Show whose turn, and if slot is invalid
    label.setGeometry(10, 10, 324, 40)

    board = Board(label)  # The "Connect Four" Board
    board.createClickableButtons()

    grid = QGridLayout()
    rowChooser = board.getRowChooser()
    boardSlots = board.getBoardSlots()
    for index in range(len(rowChooser)):
        grid.addWidget(rowChooser[index], 0, index)
    for index in range(len(boardSlots)):
        for index2 in range(len(boardSlots[index])):
            grid.addWidget(boardSlots[index][index2], index+1, index2)

    vbox = QVBoxLayout()
    vbox.addWidget(label)
    vbox.addLayout(grid)

    widget.setLayout(vbox)

    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
