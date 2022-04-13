from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QMainWindow
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QSizePolicy


class PyYahtzeeUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self._initial = False

        self.setWindowTitle('PyYahtzee')
        self.setGeometry(0, 0, 952, 575)

        self.generalLayout = QHBoxLayout()
        self.thirdLayout = QHBoxLayout()
        self.fourthLayout = QHBoxLayout()
        self.firstLayout = QVBoxLayout()
        self.rollButton = QPushButton('ROLL')
        self.rollButton.setStyleSheet(
            'background-color: green;'
            'border: white;'
            'font-size: 15px;'
            'font-weight: bold;'
        )
        self.rollButton.setGeometry(10, 10, 50, 100)
        self.createFirstLayout()
        self.secondLayout = QVBoxLayout()
        self.createSecondLayout()

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self.generalLayout.addLayout(self.firstLayout)  # Try QStackedLayout()
        self.generalLayout.addLayout(self.secondLayout)
        self._centralWidget.setLayout(self.generalLayout)

    def createFirstLayout(self):
        label = QLabel(self.centralWidget())
        label.setText('The Yahtzee Manifesto')
        label.setGeometry(70, 80, 50, 90)
        label.setStyleSheet(
            'background-color: #ffd9a7;'
            'border: none;'  # Figure out how to make it italicized
        )
        label.setFont(QFont('Arial', 30))
        label.setAlignment(Qt.AlignCenter)
        self.firstLayout.addWidget(label)

        self.firstLayout.addWidget(self.rollButton)
        self.rollButton.clicked.connect(self.rollButtonFunction)

    def createSecondLayout(self):
        firstGrid = QGridLayout()

        upperSection = QPushButton('UPPER SECTION')
        upperSection.setStyleSheet(
            'background-color: green;'
            'border: black;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        firstGrid.addWidget(upperSection, 0, 0)

        listOfUpperButtons = {
            'Aces': (1, 0),
            'Twos': (2, 0),
            'Three': (3, 0),
            'Fours': (4, 0),
            'Fives': (5, 0),
            'Sixes': (6, 0),
            'Bonus': (7, 0)
        }
        for btntext, pos in listOfUpperButtons.items():
            listOfUpperButtons[btntext] = QPushButton(btntext)
            listOfUpperButtons[btntext].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )
            firstGrid.addWidget(listOfUpperButtons[btntext], pos[0], pos[1])

        self.thirdLayout.addLayout(firstGrid)

        secondGrid = QGridLayout()

        lowerSection = QPushButton('LOWER SECTION')
        lowerSection.setStyleSheet(
            'background-color: green;'
            'border: black;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        secondGrid.addWidget(lowerSection, 0, 0)

        listOfLowerButtons = {
            '3 of a kind': (1, 0),
            '4 of a kind': (2, 0),
            'Full House': (3, 0),
            'Small Straight': (4, 0),
            'Large Straight': (5, 0),
            'Yahtzee': (6, 0),
            'Chance': (7, 0)
        }
        for btntext, pos in listOfLowerButtons.items():
            listOfLowerButtons[btntext] = QPushButton(btntext)
            listOfLowerButtons[btntext].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )
            secondGrid.addWidget(listOfLowerButtons[btntext], pos[0], pos[1])

        self.fourthLayout.addLayout(secondGrid)

        thirdGrid = QGridLayout()

        scoreOne = QPushButton('SCORE')
        scoreOne.setStyleSheet(
            'background-color: green;'
            'border: black;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        thirdGrid.addWidget(scoreOne, 0, 0)

        listOfTopScores = [QPushButton(' '), QPushButton(' '), QPushButton(' '), QPushButton(' '), QPushButton(' '),
                           QPushButton(' '), QPushButton(' ')]
        for index in range(len(listOfTopScores)):
            listOfTopScores[index].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )
            thirdGrid.addWidget(listOfTopScores[index], index + 1, 0)

        self.thirdLayout.addLayout(thirdGrid)

        fourthGrid = QGridLayout()

        scoreTwo = QPushButton('SCORE')
        scoreTwo.setStyleSheet(
            'background-color: green;'
            'border: black;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        fourthGrid.addWidget(scoreTwo, 0, 0)

        listOfBottomScores = [QPushButton(' '), QPushButton(' '), QPushButton(' '), QPushButton(' '), QPushButton(' '),
                              QPushButton(' '), QPushButton(' ')]
        for index in range(len(listOfBottomScores)):
            listOfBottomScores[index].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )
            fourthGrid.addWidget(listOfBottomScores[index], index + 1, 0)

        self.fourthLayout.addLayout(fourthGrid)

        self.secondLayout.addLayout(self.thirdLayout)
        self.secondLayout.addLayout(self.fourthLayout)

    def createDisplay(self):
        label = QLabel(self._centralWidget)
        label.setText('The Yahtzee Manifesto')
        label.setStyleSheet(
            'background-color: #ffd9a7;'
            'border-style: none;'
            'font-size: 30px;'
            'font-weight: italic;'  # if this doesn't work then figure out how
        )

    def createDice(self, grid):
        diceButtons = {  # IDEA: Make each dice an image of the dice needed
            '1': (0, 0),
            '2': (0, 1),
            '3': (0, 2),
            '4': (0, 3),
            '5': (0, 4)
        }
        for btntext, pos in diceButtons.items():
            diceButtons[btntext] = QPushButton(btntext)
            diceButtons[btntext].setFixedSize(50, 150)
            grid.addWidget(diceButtons[btntext], pos[0], pos[1])
            diceButtons[btntext].setSizePolicy(
                QSizePolicy.Preferred,
                QSizePolicy.Expanding)
            diceButtons[btntext].setStyleSheet(
                'background-color: transparent;'
                'border-style: black;'
                'font-size: 15px;'
                'font-weight: bold;'
            )

    def rollButtonFunction(self):
        grid = QGridLayout()
        self.createDice(grid)
        self.firstLayout.addLayout(grid)

        fifthGrid = QGridLayout()

        invisibleHeader = QPushButton(' ')
        invisibleHeader.setStyleSheet(
            'background-color: transparent;'
            'border: none;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        fifthGrid.addWidget(invisibleHeader, 0, 0)

        listOfFirstPossibleScores = [QPushButton('0'), QPushButton('0'), QPushButton('0'), QPushButton('0'),
                                     QPushButton('0'), QPushButton('0')]  # might have to account for the bonus

        for index in range(len(listOfFirstPossibleScores)):
            listOfFirstPossibleScores[index].setStyleSheet(
                'background-color: grey;'
                'border: black;'
                'font-size: 15px;'
            )
            fifthGrid.addWidget(listOfFirstPossibleScores[index], index + 1, 0)

        invisibleButton = QPushButton(' ')
        invisibleButton.setStyleSheet(
            'background-color: transparent;'
            'border: none;'
        )
        fifthGrid.addWidget(invisibleButton, 7, 0)

        self.thirdLayout.addLayout(fifthGrid)

        sixthGrid = QGridLayout()

        invisibleHeaderTwo = QPushButton(' ')
        invisibleHeaderTwo.setStyleSheet(
            'background-color: transparent;'
            'border: none;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        sixthGrid.addWidget(invisibleHeaderTwo, 0, 0)

        listOfSecondPossibleScores = [QPushButton('0'), QPushButton('0'), QPushButton('0'), QPushButton('0'),
                                      QPushButton('0'), QPushButton('0'), QPushButton('0')]
        # might have to account for the bonus, I don't think I need to

        for index in range(len(listOfSecondPossibleScores)):
            listOfSecondPossibleScores[index].setStyleSheet(
                'background-color: grey;'
                'border: black;'
                'font-size: 15px;'
            )
            sixthGrid.addWidget(listOfSecondPossibleScores[index], index + 1, 0)

        self.fourthLayout.addLayout(sixthGrid)
