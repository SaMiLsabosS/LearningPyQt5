from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Button:

    def __init__(self, label):
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
        self._buttonNames = ['C', 'Del', '.', '+/-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '÷', '×', '-',
                             '+', '=']
        self._coordinates = ['02', '03', '52', '50', '51', '40', '41', '42', '30', '31', '32', '20', '21', '22', '13',
                             '23', '33', '43', '53']
        self._buttons = [self._clear, self._delete, self._decimal, self._posToNeg, self._zero, self._one, self._two,
                         self._three, self._four, self._five, self._six, self._seven, self._eight, self._nine,
                         self._division, self._multiplication, self._subtraction, self._addition, self._equals]
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
        self._clear.clicked.connect(lambda: self._label.setText(""))
        self._delete.clicked.connect(lambda: self.createDeleteButton())
        self._equals.clicked.connect(lambda: self.createEqualsButton())
        self._zero.clicked.connect(lambda: self.createClickableButton('0'))
        self._one.clicked.connect(lambda: self.createClickableButton('1'))
        self._two.clicked.connect(lambda: self.createClickableButton('2'))
        self._three.clicked.connect(lambda: self.createClickableButton('3'))
        self._four.clicked.connect(lambda: self.createClickableButton('4'))
        self._five.clicked.connect(lambda: self.createClickableButton('5'))
        self._six.clicked.connect(lambda: self.createClickableButton('6'))
        self._seven.clicked.connect(lambda: self.createClickableButton('7'))
        self._eight.clicked.connect(lambda: self.createClickableButton('8'))
        self._nine.clicked.connect(lambda: self.createClickableButton('9'))
        # create each connect button separately

    def createEqualsButton(self):
        equation = self._label.text()
        try:
            ans = eval(equation)
            self._label.setText(str(ans))
        except:
            self._label.setText('Wrong Input')

    def createDeleteButton(self):
        text = self._label.text()
        output = text[:len(text) - 1]
        print(output)
        self._label.setText(output)

    def createClickableButton(self, string):
        text = self._label.text()
        self._label.setText(text + string)

    def createBlueEqualSign(self):
        blue = QGraphicsColorizeEffect()
        blue.setColor(Qt.blue)
        self.getVar(len(self._buttonNames)-1).setGraphicsEffect(blue)


