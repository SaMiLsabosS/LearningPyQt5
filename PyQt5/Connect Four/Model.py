from PyQt5.QtWidgets import *


class Model:
    def __init__(self):
        self._playerTurn = 1
        self._win = False
        self._finish = False

    def setPlayerTurn(self, playerNum):
        self._playerTurn = playerNum

    def getPlayerTurn(self):
        return self._playerTurn

    def getPlayerText(self):
        return 'Player ' + str(self._playerTurn) + '\'s Turn'

    def checkSpot(self, buttonNum, playerTurn, labels, player1Color, player2Color, colorSet, index, playersTurnLabel):
        while not colorSet and index != -1:
            if labels[index][buttonNum].palette().window().color().name() != player1Color and \
                    labels[index][buttonNum].palette().window().color().name() != player2Color:
                if playerTurn == 1:
                    labels[index][buttonNum].setStyleSheet(
                        'background-color: ' + player1Color + ';'
                    )
                else:
                    labels[index][buttonNum].setStyleSheet(
                        'background-color: ' + player2Color + ';'
                    )
                colorSet = True
            index -= 1
        if not colorSet:
            playersTurnLabel.setText(self.getPlayerText() + ' | Column is Full')
        else:
            if playerTurn == 1:
                self._playerTurn = 2
            else:
                self._playerTurn = 1
            playersTurnLabel.setText(self.getPlayerText())

    def checkForWin(self, labels, player1Color, player2Color):
        # possibilities: horizontal matches, vertical matches, and diagonal matches
        self.checkHorizontalAndVertical(labels, player1Color, player2Color)
        self.checkDiagonals(labels, player1Color, player2Color)

    def checkHorizontalAndVertical(self, labels, player1Color, player2Color):
        for row in range(6):
            for col in range(4):
                if (labels[row][col].palette().window().color().name() == player1Color and
                    labels[row][col + 1].palette().window().color().name() == player1Color and
                    labels[row][col + 2].palette().window().color().name() == player1Color and
                    labels[row][col + 3].palette().window().color().name() == player1Color) or \
                        (labels[row][col].palette().window().color().name() == player2Color and
                         labels[row][col + 1].palette().window().color().name() == player2Color and
                         labels[row][col + 2].palette().window().color().name() == player2Color and
                         labels[row][col + 3].palette().window().color().name() == player2Color):
                    self._win = True
        for col in range(7):
            for row in range(3):
                if (labels[row][col].palette().window().color().name() == player1Color and
                    labels[row + 1][col].palette().window().color().name() == player1Color and
                    labels[row + 2][col].palette().window().color().name() == player1Color and
                    labels[row + 3][col].palette().window().color().name() == player1Color) or \
                        (labels[row][col].palette().window().color().name() == player2Color and
                         labels[row + 1][col].palette().window().color().name() == player2Color and
                         labels[row + 2][col].palette().window().color().name() == player2Color and
                         labels[row + 3][col].palette().window().color().name() == player2Color):
                    self._win = True

    def checkDiagonals(self, labels, player1Color, player2Color):
        # Ascending Diagonal and Descending Diagonal
        row = 0
        while not self._win and row != 3:
            col = 0
            while not self._win and col != 4:
                if ((labels[row + 3][col].palette().window().color().name() == player1Color and
                    labels[row + 2][col + 1].palette().window().color().name() == player1Color and
                    labels[row + 1][col + 2].palette().window().color().name() == player1Color and
                    labels[row][col + 3].palette().window().color().name() == player1Color) or
                        (labels[row + 3][col].palette().window().color().name() == player2Color and
                         labels[row + 2][col + 1].palette().window().color().name() == player2Color and
                         labels[row + 1][col + 2].palette().window().color().name() == player2Color and
                         labels[row][col + 3].palette().window().color().name() == player2Color) or
                    (labels[row][col].palette().window().color().name() == player1Color and
                     labels[row + 1][col + 1].palette().window().color().name() == player1Color and
                     labels[row + 2][col + 2].palette().window().color().name() == player1Color and
                     labels[row + 3][col + 3].palette().window().color().name() == player1Color) or
                    (labels[row][col].palette().window().color().name() == player2Color and
                     labels[row + 1][col + 1].palette().window().color().name() == player2Color and
                     labels[row + 2][col + 2].palette().window().color().name() == player2Color and
                     labels[row + 3][col + 3].palette().window().color().name() == player2Color)):
                    self._win = True
                col += 1
            row += 1
