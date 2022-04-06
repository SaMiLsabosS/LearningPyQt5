import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Button import Button


def window():
    app = QApplication(sys.argv)

    widget = QWidget()
    widget.setWindowTitle('Python Calculator')
    widget.setGeometry(100, 100, 20, 523)
    widget.setStyleSheet("background-color: white")  # #1d1d1d

    label = QLabel(widget)
    label.setGeometry(5, 5, 324, 70)
    label.setWordWrap(True)
    label.setAlignment(Qt.AlignRight)
    label.setFont(QFont('Arial', 15))
    label.setText('0')

    buttons = Button(label)
    buttons.createButtons()
    buttons.createBlueEqualSign()

    grid = QGridLayout()
    coordinates = buttons.getCoordinates()
    for index in range(len(coordinates)):
        grid.addWidget(buttons.getButtons()[index], int(coordinates[index][0:1]), int(coordinates[index][1:2]))
    widget.setLayout(grid)

    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
