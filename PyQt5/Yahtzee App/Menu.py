from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLabel, QMainWindow
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QGridLayout, QSizePolicy


class PyYahtzeeUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyYahtzee')
        self.setGeometry(0, 30, 600, 300)

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
        label = QLabel(self.centralWidget())
        label.setText('The Yahtzee Manifesto')
        label.setGeometry(70, 80, 100, 100)
        label.setStyleSheet(
            'background-color: #ffd9a7;'
            'border: none;'  # if this doesn't work then figure out how
        )
        label.setFont(QFont('Arial', 30))
        label.setAlignment(Qt.AlignCenter)
        self.firstLayout.addWidget(label)

        rollButton = QPushButton('ROLL')
        rollButton.setStyleSheet(
            'background-color: green;'
            'border: white;'
            'font-size: 15px;'
            'font-weight: bold;'
        )
        rollButton.setGeometry(10, 10, 50, 200)
        self.firstLayout.addWidget(rollButton)

        grid = QGridLayout()
        self.createDice(grid)  # this will occur if the roll button is clicked on initially
        self.firstLayout.addLayout(grid)  # fix this grid layout when the roll dice button is pressed

    def createSecondLayout(self):
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        firstGrid = QGridLayout()
        upperSection = {'UPPER SECTION': (0, 0)}
        for btntext, pos in upperSection.items():
            upperSection[btntext] = QPushButton(btntext)
            upperSection[btntext].setStyleSheet(
                'background-color: green;'
                'border: black;'
                'font-size: 18px;'
                'font-weight: bold;'
            )
            firstGrid.addWidget(upperSection[btntext], pos[0], pos[1])

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

        hbox1.addLayout(firstGrid)

        secondGrid = QGridLayout()
        lowerSection = {'LOWER SECTION': (8, 0)}
        for btntext, pos in lowerSection.items():
            lowerSection[btntext] = QPushButton(btntext)
            lowerSection[btntext].setStyleSheet(
                'background-color: green;'
                'border: black;'
                'font-size: 18px;'
                'font-weight: bold;'
            )
            secondGrid.addWidget(lowerSection[btntext], pos[0], pos[1])

        listOfLowerButtons = {
            '3 of a kind': (9, 0),
            '4 of a kind': (10, 0),
            'Full House': (11, 0),
            'Small Straight': (12, 0),
            'Large Straight': (13, 0),
            'Yahtzee': (14, 0),
            'Chance': (15, 0)
        }
        for btntext, pos in listOfLowerButtons.items():
            listOfLowerButtons[btntext] = QPushButton(btntext)
            listOfLowerButtons[btntext].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )
            secondGrid.addWidget(listOfLowerButtons[btntext], pos[0], pos[1])

        hbox2.addLayout(secondGrid)

        thirdGrid = QGridLayout()

        scoreOne = {'SCORE': (0, 0)}
        for btntext, pos in scoreOne.items():
            scoreOne[btntext] = QPushButton(btntext)
            scoreOne[btntext].setStyleSheet(
                'background-color: green;'
                'border: black;'
                'font-size: 18px;'
                'font-weight: bold;'
            )
            thirdGrid.addWidget(scoreOne[btntext], pos[0], pos[1])

        listOfTopScores = [QPushButton(' '), QPushButton(' '), QPushButton(' '), QPushButton(' '), QPushButton(' '),
                           QPushButton(' '), QPushButton(' ')]
        for index in range(len(listOfTopScores)):
            listOfTopScores[index].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )
            thirdGrid.addWidget(listOfTopScores[index], index + 1, 0)

        hbox1.addLayout(thirdGrid)

        fourthGrid = QGridLayout()

        scoreTwo = {'SCORE': (8, 0)}
        for btntext, pos in scoreTwo.items():
            scoreTwo[btntext] = QPushButton(btntext)
            scoreTwo[btntext].setStyleSheet(
                'background-color: green;'
                'border: black;'
                'font-size: 18px;'
                'font-weight: bold;'
            )
            fourthGrid.addWidget(scoreTwo[btntext], pos[0], pos[1])

        listOfBottomScores = [QPushButton(' '), QPushButton(' '), QPushButton(' '), QPushButton(' '), QPushButton(' '),
                              QPushButton(' '), QPushButton(' ')]
        for index in range(len(listOfBottomScores)):
            listOfBottomScores[index].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )
            fourthGrid.addWidget(listOfBottomScores[index], index + 9, 0)

        hbox2.addLayout(fourthGrid)

        fifthGrid = QGridLayout()  # make this when the roll button in initially clicked

        listOfFirstPossibleScores = [QPushButton('0'), QPushButton('0'), QPushButton('0'), QPushButton('0'),
                                     QPushButton('0'), QPushButton('0')]  # might have to account for the bonus

        for index in range(len(listOfFirstPossibleScores)):
            listOfFirstPossibleScores[index].setStyleSheet(
                'background-color: grey;'
                'border: black;'
                'font-size: 15px;'
            )
            fifthGrid.addWidget(listOfFirstPossibleScores[index], index+1, 0)

        hbox1.addLayout(fifthGrid)

        sixthGrid = QGridLayout()

        listOfSecondPossibleScores = [QPushButton('0'), QPushButton('0'), QPushButton('0'), QPushButton('0'),
                                      QPushButton('0'), QPushButton('0'), QPushButton('0')]
        # might have to account for the bonus

        for index in range(len(listOfSecondPossibleScores)):
            listOfSecondPossibleScores[index].setStyleSheet(
                'background-color: grey;'
                'border: black;'
                'font-size: 15px;'
            )
            sixthGrid.addWidget(listOfSecondPossibleScores[index], index + 1, 0)

        hbox2.addLayout(sixthGrid)

        self.secondLayout.addLayout(hbox1)
        self.secondLayout.addLayout(hbox2)

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
        for btntext, pos in diceButtons.items():
            diceButtons[btntext] = QPushButton(btntext)
            diceButtons[btntext].setFixedSize(120, 280)
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
