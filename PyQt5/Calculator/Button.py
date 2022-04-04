from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Button:

    def __init__(self, label):
        self._clear = ''
        self._delete = ''
        self._decimal = ''
        self._posToNeg = ''
        self._one = ''
        self._two = ''
        self._three = ''
        self._four = ''
        self._five = ''
        self._six = ''
        self._seven = ''
        self._eight = ''
        self._nine = ''
        self._division = ''
        self._multiplication = ''
        self._subtraction = ''
        self._addition = ''
        self._equals = ''
        self._buttonNames = ['C', 'Del', '.', '+/-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '÷', '×', '-', '+',
                             '=']
        self._coordinates = ['02', '03', '52', '50', '40', '41', '42', '30', '31', '32', '20', '21', '22', '13', '23', '33', '43', '53']
        self._buttons = [self._clear, self._delete, self._decimal, self._posToNeg, self._one, self._two, self._three,
                         self._four, self._five, self._six, self._seven, self._eight, self._nine, self._division,
                         self._multiplication, self._subtraction, self._addition, self._equals]
        self._label = label

    def getButtons(self):
        return self._buttons

    def getCoordinates(self):
        return self._coordinates

    def getVar(self, num):
        return self._buttons[num]

    def createButtons(self):
        for index in range(len(self._buttons)):
            self._buttons[index] = QPushButton(self._buttonNames[index])
        for index in range(len(self._buttons)):
            if self._buttonNames[index] == '=':
                equation = self._label.text()

    def createBlueEqualSign(self):
        blue = QGraphicsColorizeEffect()
        blue.setColor(Qt.blue)
        self.getVar(len(self._buttonNames)-1).setGraphicsEffect(blue)


