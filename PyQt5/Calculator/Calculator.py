import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Button import Button


def window():
    app = QApplication(sys.argv)

    widget = QWidget()
    widget.setWindowTitle('Python Calculator')

    label = QLabel()
    label.setGeometry(5, 5, 350, 70)
    label.setWordTrap(True)
    label.setAlignment(Qt.AlignRight)
    label.setFont('Arial', 15)

    buttons = Button(label)
    buttons.createButtons()
    buttons.createBlueEqualSign()

    grid = QGridLayout(widget)
    coordinates = buttons.getCoordinates()
    for index in range(len(coordinates)):
        grid.addWidget(buttons.getButtons()[index], coordinates[index][0:1], coordinates[index][1:2])
    hbox = QHBoxLayout(widget)
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
