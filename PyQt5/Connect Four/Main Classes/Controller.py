import sys
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
        colChooser[1].clicked.connect(lambda: self.rowChooserFunction(1))
        colChooser[2].clicked.connect(lambda: self.rowChooserFunction(2))
        colChooser[3].clicked.connect(lambda: self.rowChooserFunction(3))
        colChooser[4].clicked.connect(lambda: self.rowChooserFunction(4))
        colChooser[5].clicked.connect(lambda: self.rowChooserFunction(5))
        colChooser[6].clicked.connect(lambda: self.rowChooserFunction(6))

    def rowChooserFunction(self, buttonNum):
        self._model.checkSpot(buttonNum, self._model.getPlayerTurn(), self._view.getLabels(),
                              self._view.getPlayer1Color(), self._view.getPlayer2Color(), False, 5,
                              self._view.getPlayersTurnLabel())
        self._model.checkForWin(self._view.getLabels(), self._view.getPlayer1Color(), self._view.getPlayer2Color(),
                                self._view.getPlayersTurnLabel())
        if self._model.getWin() is True:
            self._view.createEndScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View.View()
    model = Model.Model()
    controller = Controller(view, model)
    view.show()
    sys.exit(app.exec_())
