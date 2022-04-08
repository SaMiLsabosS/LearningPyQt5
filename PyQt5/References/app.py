import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    widget = QWidget() # creates a window that is visible
    widget.setFixedSize(800,600)
    widget.setWindowTitle('Dennis Bonsall')
    widget.setStyleSheet(
        'background-color: #3FBFBF;'
    )

    uicomponents(widget)

    widget.show() # displays window
    sys.exit(app.exec_())

def uicomponents(parent):
    # label
    top_label = QLabel('Click as many times as you can.', parent)
    top_label.setGeometry(50, 50, 700, 50)
    top_label.setAlignment(Qt.AlignCenter)
    top_label.setStyleSheet(
        'border: 2px solid red;'
        'font-size: 30px;'
    )
    # lineEdit
    line_edit = QLineEdit(parent)
    line_edit.setGeometry(50, 105, 700, 50)
    line_edit.setAlignment(Qt.AlignCenter)
    line_edit.setMaxLength(10)
    line_edit.setReadOnly(True)
    line_edit.setText(str(0))
    line_edit.setStyleSheet(
        'font-size: 25px;'
    )
    # button
    button = QPushButton('Click ME!!', parent)
    button.setGeometry(50, 170, 700, 50)
    button.setStyleSheet(
        'QPushButton {'
        'border: 2px solid green;'
        'font-size: 25px;'
        '}'
        'QPushButton:hover {'
        'border: 2px solid blue;'
        '}'
    )
    # the following line is used to make the button do something
    button.clicked.connect(lambda:line_edit.setText((str(int(line_edit.text()) + 1))))

    ilabel = QLabel(parent)
    ilabel.setGeometry(350,250,100,100)
    ilabel.setStyleSheet(
        'background-image: url(images.jpg)'
    )


if __name__ == '__main__':
    window()