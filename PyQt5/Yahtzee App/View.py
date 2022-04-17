from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QMainWindow
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout


class PyYahtzeeUI(QMainWindow):
    def __init__(self):
        super().__init__()
        # initializing UI
        self.setWindowTitle('PyYahtzee')
        self.setGeometry(0, 0, 952, 575)

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self.generalLayout = QHBoxLayout()
        self.firstVLayout = QVBoxLayout()
        self.secondVLayout = QVBoxLayout()
        self.firstHLayout = QHBoxLayout()
        self.secondHLayout = QHBoxLayout()
        self._label = QLabel(self.centralWidget())
        self._rollButton = QPushButton('ROLL')
        self._diceGrid = QGridLayout()
        self._diceInventory = QGridLayout()
        self._listOfUpperScoreTitles = {
            'Aces': (1, 0),
            'Twos': (2, 0),
            'Three': (3, 0),
            'Fours': (4, 0),
            'Fives': (5, 0),
            'Sixes': (6, 0),
            'Bonus': (7, 0)
        }
        self._listOfLowerScoreTitles = {
            '3 of a kind': (1, 0),
            '4 of a kind': (2, 0),
            'Full House': (3, 0),
            'Small Straight': (4, 0),
            'Large Straight': (5, 0),
            'Yahtzee': (6, 0),
            'Chance': (7, 0)
        }
        self._listOfTopScores = [QPushButton(' '), QPushButton(' '), QPushButton(' '), QPushButton(' '),
                                 QPushButton(' '), QPushButton(' '), QPushButton(' ')]  # change buttons into labels
        self._listOfBottomScores = [QPushButton(' '), QPushButton(' '), QPushButton(' '), QPushButton(' '),
                                    QPushButton(' '), QPushButton(' '), QPushButton(' ')]
        self._firstGrid = QGridLayout()
        self._secondGrid = QGridLayout()
        self._thirdGrid = QGridLayout()
        self._fourthGrid = QGridLayout()
        self.createFirstVLayout()
        self.createSecondVLayout()

        self.generalLayout.addLayout(self.firstVLayout)  # Try QStackedLayout()
        self.secondVLayout.addLayout(self.firstHLayout)
        self.secondVLayout.addLayout(self.secondHLayout)
        self.generalLayout.addLayout(self.secondVLayout)
        self._centralWidget.setLayout(self.generalLayout)

    def getRollButton(self):
        return self._rollButton

    def getDiceGrid(self):
        return self._diceGrid

    def getDiceInventory(self):
        return self._diceInventory

    def getListOfTopScores(self):
        return self._listOfTopScores

    def getListOfBottomScores(self):
        return self._listOfBottomScores

    def createFirstVLayout(self):
        self.establishLabel()
        self._rollButton.setStyleSheet(
            'background-color: green;'
            'border: white;'
            'font-size: 15px;'
            'font-weight: bold;'
        )
        self._rollButton.setGeometry(10, 10, 50, 100)
        self.firstVLayout.addWidget(self._rollButton)

    def createSecondVLayout(self):
        upperSection = QPushButton('UPPER SECTION')
        upperSection.setStyleSheet(
            'background-color: green;'
            'border: black;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        self._firstGrid.addWidget(upperSection, 0, 0)

        for btntext, pos in self._listOfUpperScoreTitles.items():
            self._listOfUpperScoreTitles[btntext] = QPushButton(btntext)
            self._listOfUpperScoreTitles[btntext].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )
            self._firstGrid.addWidget(self._listOfUpperScoreTitles[btntext], pos[0], pos[1])

        self.firstHLayout.addLayout(self._firstGrid)

        lowerSection = QPushButton('LOWER SECTION')
        lowerSection.setStyleSheet(
            'background-color: green;'
            'border: black;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        self._secondGrid.addWidget(lowerSection, 0, 0)

        for btntext, pos in self._listOfLowerScoreTitles.items():
            self._listOfLowerScoreTitles[btntext] = QPushButton(btntext)
            self._listOfLowerScoreTitles[btntext].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )
            self._secondGrid.addWidget(self._listOfLowerScoreTitles[btntext], pos[0], pos[1])

        self.secondHLayout.addLayout(self._secondGrid)

        scoreOne = QPushButton('SCORE')
        scoreOne.setStyleSheet(
            'background-color: green;'
            'border: black;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        self._thirdGrid.addWidget(scoreOne, 0, 0)

        for index in range(len(self._listOfTopScores)):
            self._listOfTopScores[index].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )
            self._thirdGrid.addWidget(self._listOfTopScores[index], index + 1, 0)

        self.firstHLayout.addLayout(self._thirdGrid)

        scoreTwo = QPushButton('SCORE')
        scoreTwo.setStyleSheet(
            'background-color: green;'
            'border: black;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        self._fourthGrid.addWidget(scoreTwo, 0, 0)

        for index in range(len(self._listOfBottomScores)):
            self._listOfBottomScores[index].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )
            self._fourthGrid.addWidget(self._listOfBottomScores[index], index + 1, 0)

        self.secondHLayout.addLayout(self._fourthGrid)

    def establishLabel(self):
        self._label.setText('The Yahtzee Manifesto')
        self._label.setGeometry(70, 80, 50, 90)
        self._label.setStyleSheet(
            'background-color: #ffd9a7;'
            'border: none;'  # Figure out how to make it italicized
            'background-image: url(wood.jfif)'
        )
        self._label.setFont(QFont('Arial', 30))
        self._label.setAlignment(Qt.AlignCenter)
        self.firstVLayout.addWidget(self._label)
