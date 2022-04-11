from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton, QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QGridLayout


class PyYahtzeeUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyYahtzee')

        self.generalLayout = QHBoxLayout()
        self.firstLayout = QVBoxLayout()
        self.createFirstLayout()
        self.secondLayout = QVBoxLayout()
        self.createSecondLayout()

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self.generalLayout.addLayout(self.firstLayout)  # QStackedLayout()
        self.generalLayout.addLayout(self.secondLayout)
        self._centralWidget.setLayout(self.generalLayout)

    def createFirstLayout(self):
        label = QLabel(self._centralWidget)
        label.setText('The Yahtzee Manifesto')
        label.setStyleSheet(
            'background-color: #ffd9a7;'
            'border-style: none;'
            'font-size: 30px;'
            'font-weight: italic;'  # if this doesn't work then figure out how
        )
        self.firstLayout.addWidget(label)
        self.createDice()
        self.firstLayout.addLayout(QGridLayout())  # fix this grid layout when the roll dice button is pressed
        rollButton = QPushButton('ROLL')
        rollButton.setStyleSheet(
            'background-color: green;'
            'border-style: white;'
            'font-size: 15px;'
            'font-weight: bold;'
        )
        self.firstLayout.addWidget(rollButton)

    def createSecondLayout(self):
        firstGrid = QGridLayout()
        self.secondLayout.addLayout(firstGrid)
        # create the header
        # create the transparent buttons
        # create the second header
        items = ['UPPER SECTION', 'Aces']

        secondGrid = QGridLayout()
        self.secondLayout.addLayout(secondGrid)


        thirdGrid = QGridLayout()
        self.secondLayout.addLayout(thirdGrid)


    def createDisplay(self):
        label = QLabel(self._centralWidget)
        label.setText('The Yahtzee Manifesto')
        label.setStyleSheet(
            'background-color: #ffd9a7;'
            'border-style: none;'
            'font-size: 30px;'
            'font-weight: italic;'  # if this doesn't work then figure out how
        )

    def createDice(self):
        buttonsLayout = QGridLayout()
        diceButtons = {
            '1': (0, 0),
            '2': (0, 1),
            '3': (0, 2),
            '4': (0, 3),
            '5': (0, 4),
            '6': (0, 5)
        }
        for btnText, pos in diceButtons:
            diceButtons[btnText] = QPushButton(btnText)
            diceButtons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(diceButtons[btnText], pos[0], pos[1])
