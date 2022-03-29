import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv) # creates the app itself
    widget = QWidget() # creates boundaries and locations
    widget.setFixedSize(800,600)
    widget.setWindowTitle('Login')
    widget.setStyleSheet('background-color: #80807f;')
    # uicomponents(widget)
    widget.show()
    sys.exit(app.exec_())

# def uicomponents(parent):
#

if __name__ == '__main__':
    window()