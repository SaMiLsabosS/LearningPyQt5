from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Button:

    def __init__(self, label):
        self._clear = QPushButton('C')
        self._delete = QPushButton('Del')
        self._decimal = QPushButton('.')
        self._posToNeg = QPushButton('+/-')
        self._zero = QPushButton('0')
        self._one = QPushButton('1')
        self._two = QPushButton('2')
        self._three = QPushButton('3')
        self._four = QPushButton('4')
        self._five = QPushButton('5')
        self._six = QPushButton('6')
        self._seven = QPushButton('7')
        self._eight = QPushButton('8')
        self._nine = QPushButton('9')
        self._division = QPushButton('÷')
        self._multiplication = QPushButton('×')
        self._subtraction = QPushButton('-')
        self._addition = QPushButton('+')
        self._equals = QPushButton('=')
        self._squaring = QPushButton('x²')
        self._coordinates = ['02', '03', '52', '50', '51', '40', '41', '42', '30', '31', '32', '20', '21', '22', '13',
                             '23', '33', '43', '53', '11']
        self._buttons = [self._clear, self._delete, self._decimal, self._posToNeg, self._zero, self._one, self._two,
                         self._three, self._four, self._five, self._six, self._seven, self._eight, self._nine,
                         self._division, self._multiplication, self._subtraction, self._addition, self._equals,
                         self._squaring]
        self._label = label

    def getButtons(self):
        return self._buttons

    def getCoordinates(self):
        return self._coordinates

    def getVar(self, num):
        return self._buttons[num]

    def createButtons(self):
        self._clear.clicked.connect(lambda: self._label.setText('0'))
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
        self._decimal.clicked.connect(lambda: self.createDecimalButton())
        self._posToNeg.clicked.connect(lambda: self.createNegationButton())
        self._division.clicked.connect(lambda: self.createArithmeticButton('/'))
        self._multiplication.clicked.connect(lambda: self.createArithmeticButton('*'))
        self._subtraction.clicked.connect(lambda: self.createArithmeticButton('-'))
        self._addition.clicked.connect(lambda: self.createArithmeticButton('+'))
        for index in range(len(self._buttons)):
            self._buttons[index].setSizePolicy(
                QSizePolicy.Preferred,
                QSizePolicy.Expanding)
            self._buttons[index].setStyleSheet(
                'background-color: white;'
                'border-style: none;'
                'font-size: 15px;'
                'font-weight: bold;'
            )

    def createNegationButton(self):
        text = self._label.text()
        if text == 'Wrong Input' or text == '0':
            text = ''
        if text[0:1] != '-':
            self._label.setText('-'+text)
        else:
            self._label.setText(text[1:])

    def createEqualsButton(self):
        equation = self._label.text()
        if equation == 'Wrong Input' or equation == '0':
            text = ''
        try:
            ans = eval(equation)
            self._label.setText(str(ans))
        except:
            self._label.setText('Wrong Input')

    def createArithmeticButton(self, string):
        text = self._label.text()
        if text == 'Wrong Input':
            text = ''
        elif text == '0':
            text = text+string
        else:
            text = text + string
        self._label.setText(text)

    def createDeleteButton(self):
        text = self._label.text()
        if text == 'Wrong Input':
            text = '0'
        elif text != '0':
            text = text[:len(text) - 1]
            if text == '':
                text = '0'
        self._label.setText(text)

    def createClickableButton(self, string):
        text = self._label.text()
        if text == 'Wrong Input' or text == '0':
            text = ''
        self._label.setText(text + string)

    def createDecimalButton(self):
        text = self._label.text()
        if '.' not in text:
            self._label.setText(text + '.')

    def createBlueEqualSign(self):
        # blue = QGraphicsColorizeEffect()
        # blue.setColor(Qt.blue)
        # self._equals.setGraphicsEffect(blue)
        self._equals.setStyleSheet(
            'background-color: #2d79eb;'
            'border-style: none;'
            'font-size: 15px;'
            'font-weight: bold;'
        )

