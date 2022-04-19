from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout, QStackedLayout


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self._red = '#ff0000'
        self._yellow = '#fff63a'
        # Initializing UI
        self.setWindowTitle('PyConnectFour')
        self.setGeometry(0, 0, 952, 575)

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
        self._rowChooser = [QLabel(' '), QPushButton('1st'), QPushButton('2nd'), QPushButton('3rd'), QPushButton('4th'),
                            QPushButton('5th'), QPushButton('6th'), QPushButton('7th'), QLabel(' ')]
        self._boardOverImage = QStackedLayout()
        self._imageLabel = QLabel(' ')
        self._board = QGridLayout()

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

        # creating the screen
        secondCentralWidget = QWidget(self)
        self.setCentralWidget(secondCentralWidget)

        self._topGrid.addWidget(self._player1Label, 0, 0)
        self._yellowLabel.setStyleSheet(
            'background-color: '+self._yellow+';'
        )
        self._topGrid.addWidget(self._yellowLabel, 0, 1)
        self._topGrid.addWidget(self._playersTurnLabel, 0, 2)
        self._redLabel.setStyleSheet(
            'background-color: '+self._red+';'
        )
        self._topGrid.addWidget(self._redLabel, 0, 3)
        self._topGrid.addWidget(self._player2Label, 0, 4)
        self._playingVBoxLayout.addLayout(self._topGrid)

        for index in range(len(self._rowChooser)):
            self._selectGrid.addWidget(self._rowChooser[index], 0, index)
        self._playingVBoxLayout.addLayout(self._selectGrid)

        self._imageLabel.setStyleSheet(
            'background-image: connectfourboard.png'
        )
        self._boardOverImage.addWidget(self._imageLabel)
        # add labels to the self._board and then add that to self._boardOverImage

        self._playingVBoxLayout.addLayout(self._boardOverImage)
        secondCentralWidget.setLayout(self._playingVBoxLayout)


