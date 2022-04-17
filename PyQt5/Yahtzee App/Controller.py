import random
import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QSizePolicy

import Model
import View


class Controller:  # Ask if the controller should be created in the view
    def __init__(self, model_obj, view_obj):
        self._model = model_obj
        self._view = view_obj
        self._roll = [QPushButton('-1'), QPushButton('-1'), QPushButton('-1'), QPushButton('-1'),
                      QPushButton('-1')]
        self._tries = 0
        self._initial = False

        self.establishButtonFunctions()

    def establishButtonFunctions(self):
        self._view.getRollButton().clicked.connect(self.rollButtonFunction)

    def rollButtonFunction(self):
        if self._tries == 0:
            self._tries += 1
            self.createDice()
            self._view.createYourDiceInventory()
        elif 0 < self._tries < 3:
            self._tries += 1
            for index in range(len(self._roll)):
                self._roll[index].setText(str(random.randint(1, 6)))
        self._view.establishScoreButtons()

    def createDice(self):
        for index in range(len(self._roll)):  # IDEA: Make each dice an image of the dice needed
            randomNum = str(random.randint(1, 6))
            self._roll[index] = QPushButton(randomNum)
            self._roll[index].setFixedSize(50, 150)
            self._roll[index].setSizePolicy(
                QSizePolicy.Preferred,
                QSizePolicy.Expanding)
            self._roll[index].setStyleSheet(
                'background-color: transparent;'
                'border-style: black;'
                'font-size: 15px;'
                'font-weight: bold;'
            )
            self._view.getDiceGrid().addWidget(self._roll[index], 0, index)
        self._roll[0].clicked.connect(lambda: self.createDiceButton(0))
        self._roll[1].clicked.connect(lambda: self.createDiceButton(1))
        self._roll[2].clicked.connect(lambda: self.createDiceButton(2))
        self._roll[3].clicked.connect(lambda: self.createDiceButton(3))
        self._roll[4].clicked.connect(lambda: self.createDiceButton(4))

    def createDiceButton(self, index):
        dice = self._roll[index].text()
        listOfYourDice = self._view.getListOfYourDice()
        for index2 in range(len(listOfYourDice)):
            if listOfYourDice[index2].text() == ' ':
                listOfYourDice[index2].setText(dice)
                self._roll[index].setText(' ')
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Look at stack overflow for customizing the Application
    model = Model.Model()
    view = View.PyYahtzeeUI()
    controller = Controller(model, view)
    # a method of some sorts could go here
    # add in the .clicked.connect functions here
    view.show()
    sys.exit(app.exec_())
