from PyQt5.QtWidgets import *


class Board:
    def __init__(self, label):
        self._col1 = QPushButton('1st')
        self._col2 = QPushButton('2nd')
        self._col3 = QPushButton('3rd')
        self._col4 = QPushButton('4th')
        self._col5 = QPushButton('5th')
        self._col6 = QPushButton('6th')
        self._col7 = QPushButton('7th')
        self._rowChooser = [self._col1, self._col2, self._col3, self._col4, self._col5, self._col6, self._col7]
        self._boardSlots = [[QPushButton()] * 7] * 7
        self._label = label
        self._userColor = 'White'
        self._red = ''
        self._yellow = ''

    def getRowChooser(self):
        return self._rowChooser

    def getBoardSlots(self):
        return self._boardSlots

    def createClickableButtons(self):
        self._col1.clicked.connect(lambda: self.createSelection(0))
        self._col2.clicked.connect(lambda: self.createSelection(1))
        self._col3.clicked.connect(lambda: self.createSelection(2))
        self._col4.clicked.connect(lambda: self.createSelection(3))
        self._col5.clicked.connect(lambda: self.createSelection(4))
        self._col6.clicked.connect(lambda: self.createSelection(5))
        self._col7.clicked.connect(lambda: self.createSelection(6))

    def createSelection(self, index):
        changed = False
        for index2 in range(len(self._boardSlots[index]) - 1, -1, -1):
            if self._boardSlots[index][index2].palette().button().color() != self._red \
                    or self._boardSlots[index][index2].palette().button().color() != self._yellow:
                self._boardSlots[index][index2].setStyleSheet(
                    'background-color: ' + self._userColor + ';'  # Might not work, if not then make a method
                    'border-style: None;'
                    'font-size = None;'
                    'font-weight = None;'
                )
                changed = True
                index2 = 0
        if not changed:
            self._label.setText('Invalid Spot')



