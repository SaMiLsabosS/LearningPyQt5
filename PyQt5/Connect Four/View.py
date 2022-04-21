from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout, QStackedLayout


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self._red = '#ff0000'
        self._yellow = '#fff63a'
        # Initializing UI
        self.setWindowTitle('PyConnectFour')
        self.setFixedSize(952, 675)

        self._firstCentralWidget = QWidget(self)
        self.setCentralWidget(self._firstCentralWidget)
        self._startingVLayout = QVBoxLayout()

        # starting screen
        self._mainScreenLabel = QLabel('Welcome to Python\nConnect Four!')
        self._mainScreenButton = QPushButton('Click Here to Play!')
        self.createStartingScreen()

        # play screen
        self._playingVBoxLayout = QVBoxLayout()
        self._topGrid = QGridLayout()
        self._player1Label = QLabel('Player 1')
        self._yellowLabel = QLabel(' ')
        self._playersTurnLabel = QLabel('Player 1\'s Turn')
        self._redLabel = QLabel(' ')
        self._player2Label = QLabel('Player 2')

        self._selectGrid = QGridLayout()
        self._colChooser = [QPushButton('1st'), QPushButton('2nd'), QPushButton('3rd'), QPushButton('4th'),
                            QPushButton('5th'), QPushButton('6th'), QPushButton('7th')]
        self._boardOverImage = QStackedLayout()
        self._imageLabel = QLabel(' ')
        self._labels = [[QLabel(), QLabel(), QLabel(), QLabel(), QLabel(), QLabel(), QLabel()], [QLabel(), QLabel(),
                        QLabel(), QLabel(), QLabel(), QLabel(), QLabel()], [QLabel(), QLabel(), QLabel(), QLabel(),
                        QLabel(), QLabel(), QLabel()], [QLabel(), QLabel(), QLabel(), QLabel(), QLabel(), QLabel(),
                        QLabel()], [QLabel(), QLabel(), QLabel(), QLabel(), QLabel(), QLabel(), QLabel()], [QLabel(),
                        QLabel(), QLabel(), QLabel(), QLabel(), QLabel(), QLabel()]]  # make this into a two D array
        self._board = QGridLayout()

    def getMainScreenLabel(self):
        return self._mainScreenLabel

    def getMainScreenButton(self):
        return self._mainScreenButton

    def getColChooser(self):
        return self._colChooser

    def getPlayer1Color(self):
        return self._yellow

    def getPlayer2Color(self):
        return self._red

    def getLabels(self):
        return self._labels

    def getPlayersTurnLabel(self):
        return self._playersTurnLabel

    def createStartingScreen(self):
        self._mainScreenLabel.setGeometry(70, 80, 50, 90)
        self._mainScreenLabel.setStyleSheet(
            'background-color: transparent;'
            'border: black;'
            'font-weight: bold;'
        )
        self._mainScreenLabel.setFont(QFont('Arial', 50))
        self._mainScreenLabel.setAlignment(Qt.AlignCenter)
        self._mainScreenButton.setStyleSheet(
            'background-color: green;'  # change this eventually
            'border: black;'
            'font-size: 22px;' 
            'font-weight: bold;'
        )
        self._mainScreenButton.setGeometry(10, 10, 50, 100)
        self._startingVLayout.addWidget(self._mainScreenLabel)
        self._startingVLayout.addWidget(self._mainScreenButton)
        self._firstCentralWidget.setLayout(self._startingVLayout)

    def createPlayScreen(self):
        # eliminating the previous screen
        secondCentralWidget = QWidget(self)
        self.setCentralWidget(secondCentralWidget)
        secondCentralWidget.setStyleSheet(
            'background-image: url(connectfourboard.jpg);'
        )
        # creating the screen
        self._player1Label.setAlignment(Qt.AlignLeft)
        self._topGrid.addWidget(self._player1Label, 0, 0)
        self._yellowLabel.setStyleSheet(
            'background-color: '+self._yellow+';'
        )
        self._topGrid.addWidget(self._yellowLabel, 0, 1)
        self._playersTurnLabel.setAlignment(Qt.AlignCenter)
        self._topGrid.addWidget(self._playersTurnLabel, 0, 2)
        self._redLabel.setStyleSheet(
            'background-color: '+self._red+';'
        )
        self._topGrid.addWidget(self._redLabel, 0, 3)
        self._player2Label.setAlignment(Qt.AlignRight)
        self._topGrid.addWidget(self._player2Label, 0, 4)
        self._playingVBoxLayout.addLayout(self._topGrid)

        for index in range(len(self._colChooser)):
            self._selectGrid.addWidget(self._colChooser[index], 0, index)
        self._playingVBoxLayout.addLayout(self._selectGrid)

        # self._imageLabel.setStyleSheet(
        #     'background-image: url(connectfourboard.jpg);'
        # )
        # self._boardOverImage.addWidget(self._imageLabel)

        for row in range(6):
            for col in range(7):
                self._board.addWidget(self._labels[row][col], row, col)
        # self._boardOverImage.addChildLayout(self._board)

        self._playingVBoxLayout.addLayout(self._board)

        # self._playingVBoxLayout.addLayout(self._boardOverImage)
        secondCentralWidget.setLayout(self._playingVBoxLayout)


