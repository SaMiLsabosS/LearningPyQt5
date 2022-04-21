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
        colChooser = self._view.getColChooser()
        colChooser[0].clicked.connect(lambda: self.rowChooserFunction(0))

    def rowChooserFunction(self, buttonNum):
        playerTurn = self._model.getPlayerTurn()
        labels = self._view.getLabels()
        column = labels[buttonNum]
        player1Color = self._view.getPlayer1Color()
        player2Color = self._view.getPlayer2Color()
        colorSet = False
        index = len(column) - 1
        playersTurnLabel = self._view.getPlayersTurnLabel()
        while not colorSet or index == -1:
            if column[index].palette().window().color().name() != player1Color or \
                    column[index].palette().window().color().name() != player2Color:
                if playerTurn == 1:
                    column[index].setStyleSheet(
                        'background-color: ' + player1Color + ';'
                    )
                else:
                    column[index].setStyleSheet(
                        'background-color: ' + player2Color + ';'
                    )
                colorSet = True
            index -= 1
        if not colorSet:
            playersTurnLabel.setText(self._model.getPlayerText+' | Column is Full')
        else:
            if playerTurn == 1:
                self._model.setPlayerTurn(2)
            else:
                self._model.setPlayerTurn(1)
            playersTurnLabel.setText(self._model.getPlayerText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View.View()
    model = Model.Model()
    controller = Controller(view, model)
    view.show()
    sys.exit(app.exec_())
