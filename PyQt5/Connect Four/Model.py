from PyQt5.QtWidgets import *


class Model:
    def __init__(self):
        self._playerTurn = 1

    def setPlayerTurn(self, playerNum):
        self._playerTurn = playerNum

    def getPlayerTurn(self):
        return self._playerTurn

    def getPlayerText(self):
        return 'Player '+str(self._playerTurn)+'\'s Turn'
