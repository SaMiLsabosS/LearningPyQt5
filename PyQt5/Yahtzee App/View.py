from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QMainWindow
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QSizePolicy


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        # initializing UI
        self.setWindowTitle('PyYahtzee')
        self.setStyleSheet(
            'background-image: url(Background.png);'
        )
        self.setFixedSize(952, 770)

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
        self._listOfUpperScoreTitles = [QLabel('Aces'), QLabel('Twos'), QLabel('Threes'), QLabel('Fours'),
                                        QLabel('Fives'), QLabel('Sixes'), QLabel('Bonus')]
        self._listOfLowerScoreTitles = [QLabel('3 of a kind'), QLabel('4 of a kind'), QLabel('Full House'),
                                        QLabel('Small Straight'), QLabel('Large Straight'), QLabel('Yahtzee'),
                                        QLabel('Chance')]
        self._listOfTopScores = [QLabel(' '), QLabel(' '), QLabel(' '), QLabel(' '),
                                 QLabel(' '), QLabel(' '), QLabel(' ')]
        self._listOfBottomScores = [QLabel(' '), QLabel(' '), QLabel(' '), QLabel(' '),
                                    QLabel(' '), QLabel(' '), QLabel(' ')]
        self._listOfFirstPossibleScores = [QPushButton('0'), QPushButton('0'), QPushButton('0'), QPushButton('0'),
                                           QPushButton('0'), QPushButton('0')]
        self._listOfSecondPossibleScores = [QPushButton('0'), QPushButton('0'), QPushButton('0'), QPushButton('0'),
                                            QPushButton('0'), QPushButton('0'), QPushButton('0')]
        self._topScoreTitlesVBOX = QVBoxLayout()
        self._bottomScoreTitlesVBOX = QVBoxLayout()
        self._thirdGrid = QGridLayout()
        self._fourthGrid = QGridLayout()
        self._topPossibleScoreVBOX = QVBoxLayout()
        self._bottomPossibleScoreVBOX = QVBoxLayout()
        self.createFirstVLayout()
        self.createSecondVLayout()

        self.generalLayout.addLayout(self.firstVLayout)
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

    def getLabel(self):
        return self._label

    def getListOfTopScores(self):
        return self._listOfTopScores

    def getListOfBottomScores(self):
        return self._listOfBottomScores

    def getListOfFirstPossibleScores(self):
        return self._listOfFirstPossibleScores

    def getListOfSecondPossibleScores(self):
        return self._listOfSecondPossibleScores

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
        self._topScoreTitlesVBOX.addWidget(upperSection)

        for index in range(len(self._listOfUpperScoreTitles)):
            self._listOfUpperScoreTitles[index].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )
            self._listOfUpperScoreTitles[index].setAlignment(Qt.AlignCenter)
            self._topScoreTitlesVBOX.addWidget(self._listOfUpperScoreTitles[index])

        self.firstHLayout.addLayout(self._topScoreTitlesVBOX)

        lowerSection = QPushButton('LOWER SECTION')
        lowerSection.setStyleSheet(
            'background-color: green;'
            'border: black;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        self._bottomScoreTitlesVBOX.addWidget(lowerSection)

        for index in range(len(self._listOfLowerScoreTitles)):
            self._listOfLowerScoreTitles[index].setStyleSheet(
                'background-color: transparent;'
                'border: black;'
                'font-size: 15px;'
            )
            self._listOfLowerScoreTitles[index].setAlignment(Qt.AlignCenter)
            self._bottomScoreTitlesVBOX.addWidget(self._listOfLowerScoreTitles[index])

        self.secondHLayout.addLayout(self._bottomScoreTitlesVBOX)

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
            self._listOfTopScores[index].setAlignment(Qt.AlignCenter)
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
                'font-size: 15px;'
            )
            self._listOfBottomScores[index].setAlignment(Qt.AlignCenter)
            self._fourthGrid.addWidget(self._listOfBottomScores[index], index + 1, 0)

        self.secondHLayout.addLayout(self._fourthGrid)

    def establishLabel(self):
        self._label.setText('The Yahtzee Manifesto')
        self._label.setGeometry(0, 0, 50, 80)
        self._label.setFont(QFont('Arial', 30))
        self._label.setStyleSheet(
            'background-color: #ffd9a7;'
            'font-style: italic;'
            'color: #ff221c'
        )
        self._label.setAlignment(Qt.AlignCenter)
        self._label.setAlignment(Qt.AlignCenter)
        self.firstVLayout.addWidget(self._label)

    def establishScoreButtons(self):
        invisibleHeader = QPushButton(' ')
        invisibleHeader.setStyleSheet(
            'background-color: transparent;'
            'border: none;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        self._topPossibleScoreVBOX.addWidget(invisibleHeader)

        for index in range(len(self._listOfFirstPossibleScores)):
            self._listOfFirstPossibleScores[index].setStyleSheet(
                'background-color: grey;'
                'border: black;'
                'font-size: 18px;'
            )
            self._topPossibleScoreVBOX.addWidget(self._listOfFirstPossibleScores[index])

        invisibleButton = QPushButton(' ')
        invisibleButton.setStyleSheet(
            'background-color: transparent;'
            'border: none;'
            'font-size: 18px;'
        )
        self._topPossibleScoreVBOX.addWidget(invisibleButton)

        self.firstHLayout.addLayout(self._topPossibleScoreVBOX)

        invisibleHeaderTwo = QPushButton(' ')
        invisibleHeaderTwo.setStyleSheet(
            'background-color: transparent;'
            'border: none;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        self._bottomPossibleScoreVBOX.addWidget(invisibleHeaderTwo)

        for index in range(len(self._listOfSecondPossibleScores)):
            self._listOfSecondPossibleScores[index].setStyleSheet(
                'background-color: grey;'
                'border: black;'
                'font-size: 18px;'
            )
            self._bottomPossibleScoreVBOX.addWidget(self._listOfSecondPossibleScores[index])

        self.secondHLayout.addLayout(self._bottomPossibleScoreVBOX)

    def createEndScreen(self, total):
        secondCentralWidget = QWidget(self)
        # secondCentralWidget.setStyleSheet(
        #     'background-image: url((wood.jfif));'
        # )
        self.setCentralWidget(secondCentralWidget)
        self.setStyleSheet(
            'background-image: url(wood.jfif);'
        )
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self._label)

        hbox1 = QHBoxLayout()
        # imageLabelOne = QLabel()
        # imageLabelOne.setStyleSheet(
        #     'background-image: url(transparent star.png);'
        # )
        # imageLabelTwo = QLabel()
        # imageLabelTwo.setStyleSheet(
        #     'background-image: url(transparent star.png);'
        # )

        # hbox1.addWidget(imageLabelOne)
        totalLabel = QLabel('Total = ' + str(total))
        totalLabel.setFont(QFont('Arial', 30))
        totalLabel.setAlignment(Qt.AlignCenter)
        hbox1.addWidget(totalLabel)
        # hbox1.addWidget(imageLabelTwo)

        vbox1.addLayout(hbox1)
        secondCentralWidget.setLayout(vbox1)


