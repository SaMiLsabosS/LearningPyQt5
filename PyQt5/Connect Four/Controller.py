import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
import View
import Model


class Controller:
    def __init__(self, view_obj, model_obj):
        self._view = view_obj
        self._model = model_obj
        self.establishStartButton()

    def establishStartButton(self):
        mainButton = self._view.getMainScreenButton()
        mainButton.clicked.connect(lambda: self.startButtonFunction())

    def startButtonFunction(self):
        self._view.createPlayScreen()
        self.establishPlayingButtons()

    def establishPlayingButtons(self):
        rowChooser = self._view.getRowChooser()
        rowChooser[0].clicked.connect(lambda: self.rowChooserFunction(rowChooser[0]))

    def rowChooserFunction(self, button):
        playerTurn = self._model.getPlayerTurn()
        board = self._view.getBoard()
        if playerTurn == 1:
            player1Color = self._view.getPlayer1Color()


        else:
            player2Color = self._view.getPlayer2Color()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View.View()
    model = Model.Model()
    controller = Controller(view, model)
    view.show()
    sys.exit(app.exec_())
