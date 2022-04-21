from PyQt5.QtWidgets import *


class Model:
    def __init__(self):
        self._playerTurn = 1

    def getPlayerTurn(self):
        return self._playerTurn
