from PyQt5.QtCore import Qt
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

        self.generalLayout.addLayout(self.firstLayout)  # Try QStackedLayout()
        self.generalLayout.addLayout(self.secondLayout)
        self._centralWidget.setLayout(self.generalLayout)

    def createFirstLayout(self):
        label = QLabel(self._centralWidget)
        label.setText('The Yahtzee Manifesto')
        label.setStyleSheet(
            'background-color: #ffd9a7;'
            'border: none;'
            'font-size: 30px;'
            'font-weight: italic;'  # if this doesn't work then figure out how
        )
        self.firstLayout.addWidget(label)
        grid = QGridLayout()
        self.createDice(grid)  # this will occur if the roll button is clicked on initially
        self.firstLayout.addLayout(grid)  # fix this grid layout when the roll dice button is pressed
        rollButton = QPushButton('ROLL')
        rollButton.setStyleSheet(
            'background-color: green;'
            'border: white;'
            'font-size: 15px;'
            'font-weight: bold;'
        )
        self.firstLayout.addWidget(rollButton)

    def createSecondLayout(self):
        firstGrid = QGridLayout()
        upperSection = {'UPPER SECTION': (0,0)}
        for btntext, pos in upperSection:
            upperSection[btntext] = QPushButton(btntext)
            upperSection[btntext].setStyleSheet(
                'background-color: green;'
                'border: black;'
                'font-size: 18px;'
                'font-weight: bold;'
            )
            firstGrid.addWidget(upperSection[btntext], pos[0], pos[1])

        listOfUpperButtons = {
            QPushButton('Aces'): (),
            QPushButton('Twos'),
            QPushButton('Three'),
            QPushButton('Fours'),
            QPushButton('Fives'),
            QPushButton('Sixes'),
            QPushButton('Bonus')
        }
        for index in range(len(listOfUpperButtons)):
            listOfUpperButtons[index].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )

        lowerSection = QPushButton('LOWER SECTION')
        lowerSection.setStyleSheet(
            'background-color: green;'
            'border: black;'
            'font-size: 18px;'
            'font-weight: bold;'
        )

        listOfLowerButtons = [QPushButton('3 of a kind'), QPushButton('4 of a kind'), QPushButton('Full House'),
                              QPushButton('Small Straight'), QPushButton('Large Straight'), QPushButton('Yahtzee'),
                              QPushButton('Chance')]
        for index in range(len(listOfLowerButtons)):
            listOfLowerButtons[index].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )

        firstGrid.addWidget(upperSection)  # add coordinates
        for index in range(len(listOfUpperButtons)):
            firstGrid.addWidget(listOfUpperButtons[index])
        firstGrid.addWidget(lowerSection)
        for index in range(len(listOfLowerButtons)):
            firstGrid.addWidget(listOfLowerButtons[index])

        self.secondLayout.addLayout(firstGrid)

        secondGrid = QGridLayout()

        scoreOne = QPushButton('SCORE')
        scoreOne.setStyleSheet(
            'background-color: green;'
            'border: black;'
            'font-size: 18px;'
            'font-weight: bold;'
        )

        listOfTopScores = [[QPushButton(' ')] * 7]

        scoreTwo = QPushButton('SCORE')
        scoreTwo.setStyleSheet(
            'background-color: green;'
            'border: black;'
            'font-size: 18px;'
            'font-weight: bold;'
        )

        listOfBottomScores = [[QPushButton(' ')] * 7]

        secondGrid.addWidget(scoreOne)  # add coordinates
        for index in range(len(listOfTopScores)):
            secondGrid.addWidget(listOfTopScores[index])
        secondGrid.addWidget(scoreTwo)
        for index in range(len(listOfBottomScores)):
            secondGrid.addWidget(listOfBottomScores[index])
        self.secondLayout.addLayout(secondGrid)

        thirdGrid = QGridLayout()  # make this when the roll button in initially clicked

        listOfPossibleScores = [[QPushButton('0')] * 13]  # might have to account for the bonus
        for index in range(len(listOfPossibleScores)):
            thirdGrid.addWidget(listOfPossibleScores[index])

        self.secondLayout.addLayout(thirdGrid)  # add coordinates to the list, making a map

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
            grid.addWidget(diceButtons[btnText], pos[0], pos[1])
