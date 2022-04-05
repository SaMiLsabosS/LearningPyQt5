from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Button:

    def __init__(self, label, widget):
        self._clear = ''
        self._delete = ''
        self._decimal = ''
        self._posToNeg = ''
        self._zero = ''
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
        self._buttonNames = ['C', 'Del', '.', '+/-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '÷', '×', '-', '+',
                             '=']
        self._coordinates = ['02', '03', '52', '50', '51', '40', '41', '42', '30', '31', '32', '20', '21', '22', '13', '23', '33', '43', '53']
        self._buttons = [self._clear, self._delete, self._decimal, self._posToNeg, self._zero, self._one, self._two, self._three,
                         self._four, self._five, self._six, self._seven, self._eight, self._nine, self._division,
                         self._multiplication, self._subtraction, self._addition, self._equals]
        self._label = label
        self._widget = widget

    def getButtons(self):
        return self._buttons

    def getCoordinates(self):
        return self._coordinates

    def getVar(self, num):
        return self._buttons[num]

    def createButtons(self):
        for index in range(len(self._buttons)):
            self._buttons[index] = QPushButton(self._widget, clicked= lambda: self.createClickableButton(index))

    def createClickableButton(self, index):
        if self._buttonNames[index] == '=':
            equation = self._label.text()
            try:
                ans = eval(equation)
                self._label.setText(str(ans))
            except:
                self._label.setText('Wrong Input')
        elif self._buttonNames[index] == 'Del':
            text = self._label.text()
            output = text[:len(text) - 1]
            print(output)
            self._label.setText(output)
        elif self._buttonNames[index] == 'C':
            self._label.setText('')
        else:
            text = self._label.text()
            self._label.setText(text + str(self._buttonNames[index]))

    def createBlueEqualSign(self):
        blue = QGraphicsColorizeEffect()
        blue.setColor(Qt.blue)
        self.getVar(len(self._buttonNames)-1).setGraphicsEffect(blue)


