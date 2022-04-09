import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Button import Button


def window():
    app = QApplication(sys.argv)

    widget = QWidget()
    widget.setWindowTitle('Python Calculator')
    widget.setGeometry(100, 100, 478, 524)  # 321, 524
    widget.setStyleSheet("background-color: #e6e6e6")

    label = QLabel(widget)
    label.setGeometry(5, 5, 324, 70)
    label.setWordWrap(True)
    label.setAlignment(Qt.AlignRight)
    label.setFont(QFont('Sogue UI Bold', 35))
    label.setText('0')

    buttons = Button(label)
    buttons.createButtons()
    buttons.createBlueEqualSign()

    grid = QGridLayout()
    coordinates = buttons.getCoordinates()
    for index in range(len(coordinates)):
        grid.addWidget(buttons.getButtons()[index], int(coordinates[index][0:1]), int(coordinates[index][1:2]))

    vbox = QVBoxLayout()
    vbox.addWidget(label)
    vbox.addLayout(grid)

    widget.setLayout(vbox)

    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
