from PyQt5.QtWidgets import *

button1 = QPushButton()
button1.setStyleSheet('background-color:#ff0000;')
color = button1.palette().button().color()
print(str(color))



