import random
import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QSizePolicy, QGridLayout

import Model
import View


class Controller:
    def __init__(self, model_obj, view_obj):
        self._model = model_obj
        self._view = view_obj
        self._roll = [QPushButton('0'), QPushButton('0'), QPushButton('0'), QPushButton('0'),
                      QPushButton('0')]
        self._yourDice = [QPushButton(' '), QPushButton(' '), QPushButton(' '), QPushButton(' '),
                          QPushButton(' ')]
        self._pushPossibleScores = [True, True, True, True, True, True, True, True, True, True, True, True, True]
        # 6 + 7
        self._fifthGrid = QGridLayout()
        self._sixthGrid = QGridLayout()
        self._tries = 0
        self._initial = True

        self.establishButtonFunctions()

    def establishButtonFunctions(self):
        listOfTopScores = self._view.getListOfTopScores()
        listOfBottomScores = self._view.getListOfBottomScores()
        self._view.getRollButton().clicked.connect(self.rollButtonFunction)
        listOfFirstPossibleScores = self._view.getListOfFirstPossibleScores()
        listOfSecondPossibleScores = self._view.getListOfSecondPossibleScores()
        listOfFirstPossibleScores[0].clicked.connect(lambda: self.addToScoreAndReset(listOfTopScores, 0,
                                                                                     listOfFirstPossibleScores, 0))
        listOfFirstPossibleScores[1].clicked.connect(lambda: self.addToScoreAndReset(listOfTopScores, 1,
                                                                                     listOfFirstPossibleScores, 1))
        listOfFirstPossibleScores[2].clicked.connect(lambda: self.addToScoreAndReset(listOfTopScores, 2,
                                                                                     listOfFirstPossibleScores, 2))
        listOfFirstPossibleScores[3].clicked.connect(lambda: self.addToScoreAndReset(listOfTopScores, 3,
                                                                                     listOfFirstPossibleScores, 3))
        listOfFirstPossibleScores[4].clicked.connect(lambda: self.addToScoreAndReset(listOfTopScores, 4,
                                                                                     listOfFirstPossibleScores, 4))
        listOfFirstPossibleScores[5].clicked.connect(lambda: self.addToScoreAndReset(listOfTopScores, 5,
                                                                                     listOfFirstPossibleScores, 5))
        listOfSecondPossibleScores[0].clicked.connect(lambda: self.addToScoreAndReset(listOfBottomScores, 0,
                                                                                      listOfSecondPossibleScores, 6))
        listOfSecondPossibleScores[1].clicked.connect(lambda: self.addToScoreAndReset(listOfBottomScores, 1,
                                                                                      listOfSecondPossibleScores, 7))
        listOfSecondPossibleScores[2].clicked.connect(lambda: self.addToScoreAndReset(listOfBottomScores, 2,
                                                                                      listOfSecondPossibleScores, 8))
        listOfSecondPossibleScores[3].clicked.connect(lambda: self.addToScoreAndReset(listOfBottomScores, 3,
                                                                                      listOfSecondPossibleScores, 9))
        listOfSecondPossibleScores[4].clicked.connect(lambda: self.addToScoreAndReset(listOfBottomScores, 4,
                                                                                      listOfSecondPossibleScores, 10))
        listOfSecondPossibleScores[5].clicked.connect(lambda: self.addToScoreAndReset(listOfBottomScores, 5,
                                                                                      listOfSecondPossibleScores, 11))
        listOfSecondPossibleScores[6].clicked.connect(lambda: self.addToScoreAndReset(listOfBottomScores, 6,
                                                                                      listOfSecondPossibleScores, 12))

    def rollButtonFunction(self):
        if self._tries == 0:
            self.createDice()
            self.createYourDiceInventory()
            if self._initial:
                self._initial = False
                self._view.establishScoreButtons()
            self._tries += 1
        elif 0 < self._tries < 3:
            self._tries += 1
            for index in range(len(self._roll)):
                if self._roll[index].text() != ' ':
                    self._roll[index].setText(str(random.randint(1, 6)))

    def createDice(self):
        if self._initial:
            for index in range(len(self._roll)):  # IDEA: Make each dice an image of the dice needed
                randomNum = str(random.randint(1, 6))  # do that after everything works
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
            self._view.firstVLayout.addLayout(self._view.getDiceGrid())
        else:
            for index in range(len(self._roll)):
                randomNum = str(random.randint(1, 6))
                self._roll[index] = QPushButton(randomNum)
        self._roll[0].clicked.connect(lambda: self.createDiceButton(0))
        self._roll[1].clicked.connect(lambda: self.createDiceButton(1))
        self._roll[2].clicked.connect(lambda: self.createDiceButton(2))
        self._roll[3].clicked.connect(lambda: self.createDiceButton(3))
        self._roll[4].clicked.connect(lambda: self.createDiceButton(4))

    def createYourDiceInventory(self):
        if self._initial:
            for index in range(len(self._yourDice)):
                self._yourDice[index].setFixedSize(50, 150)
                self._yourDice[index].setSizePolicy(
                    QSizePolicy.Preferred,
                    QSizePolicy.Expanding)
                self._yourDice[index].setStyleSheet(
                    'background-color: transparent;'
                    'border-style: black;'
                    'font-size: 15px;'
                    'font-weight: bold;'
                )
                self._view.getDiceInventory().addWidget(self._yourDice[index], 0, index)
            self._view.firstVLayout.addLayout(self._view.getDiceInventory())
        self._yourDice[0].clicked.connect(lambda: self.createYourDiceButton(0))
        self._yourDice[1].clicked.connect(lambda: self.createYourDiceButton(1))
        self._yourDice[2].clicked.connect(lambda: self.createYourDiceButton(2))
        self._yourDice[3].clicked.connect(lambda: self.createYourDiceButton(3))
        self._yourDice[4].clicked.connect(lambda: self.createYourDiceButton(4))

    def createDiceButton(self, index):
        dice = self._roll[index].text()
        if dice != ' ':
            index2 = 0
            moved = False
            while index2 < len(self._yourDice) and not moved:
                if self._yourDice[index2].text() == ' ':
                    moved = True
                    self._yourDice[index2].setText(dice)
                    self._model.addToSumOfRoll(dice)
                    self._roll[index].setText(' ')
                    self.updateSumOfRollAndScoreButtons()
                index2 += 1

    def createYourDiceButton(self, index):
        dice = self._yourDice[index].text()
        index2 = 0
        moved = False
        while index2 < len(self._roll) and not moved:
            if self._roll[index2].text() == ' ':
                moved = True
                self._roll[index2].setText(dice)
                self._model.subtractFromSumOfRoll(dice)
                self._yourDice[index].setText(' ')
                self.updateSumOfRollAndScoreButtons()
            index2 += 1

    def updateSumOfRollAndScoreButtons(self):
        self._model.updateSumOfRoll(self._view.getListOfSecondPossibleScores()[6])
        self._model.updateSumsOfSingleDigitNums(self._yourDice)
        for index in range(len(self._model.getSumsOfSingleDigitNums())):
            if self._pushPossibleScores[index]:
                temp = self._model.getIndexOfSumsOfSingleDigitNums(index)
                if temp != '0':
                    temp = '+' + temp
                self._view.getListOfFirstPossibleScores()[index].setText(temp)
        count = 0
        for index in range(len(self._yourDice)):
            if self._yourDice[index].text() != ' ':
                count += 1
        if count == 5:
            self._model.checkUniqueScores(self._yourDice)
            listOfUniqueScores = self._model.getUniqueScores()
            for index2 in range(len(listOfUniqueScores)):
                if self._pushPossibleScores[6 + index2]:
                    newNum = str(listOfUniqueScores[index2])
                    if newNum != '0':
                        newNum = '+' + newNum
                    self._view.getListOfSecondPossibleScores()[index2].setText(newNum)
        self._model.setUniqueScores([0, 0, 0, 0, 0, 0])
        # create a method that returns a set of places to update a score button to the score
        # this could reduce space within the controller and put more code in the model
        # do this after everything works

    def possiblyAddBonus(self):
        bonus = 0
        for index6 in range(6):
            if not self._pushPossibleScores[index6]:
                bonus += 1
        if bonus == 6:
            listOfTopScores = self._view.getListOfTopScores()
            sumOfTopScores = 0
            for index7 in range(len(listOfTopScores) - 1):
                sumOfTopScores += int(listOfTopScores[index7].text())
            if sumOfTopScores >= 63:
                listOfTopScores[6].setText('35')
                self._model.addToTotal(35)
            else:
                listOfTopScores[6].setText('0')

    def addToScoreAndReset(self, listOfScores, index, score, indexOfPush):
        if self._pushPossibleScores[indexOfPush]:
            self._pushPossibleScores[indexOfPush] = False
            if listOfScores[index].text() == ' ':
                total = int(score[index].text())
            else:
                total = int(listOfScores[index].text()) + int(score[index].text())
            listOfScores[index].setText(str(total))
            score[index].setText(' ')
            score[index].setStyleSheet(
                'background-color: transparent;'
            )
            self._tries = 1
            self._model.addToTotal(total)
            finish = True
            for i in range(len(self._pushPossibleScores)):
                if self._pushPossibleScores[i]:
                    finish = False
            if not finish:
                for index2 in range(len(self._roll)):  # IDEA: Make each dice an image of the dice needed
                    randomNum = str(random.randint(1, 6))  # do this after everything works
                    self._roll[index2].setText(randomNum)
                for index3 in range(len(self._yourDice)):
                    self._yourDice[index3].setText(' ')
                self._model.setSumOfRoll(0)
                for index4 in range(len(self._view.getListOfFirstPossibleScores())):
                    if self._pushPossibleScores[index4]:
                        self._view.getListOfFirstPossibleScores()[index4].setText('0')
                for index5 in range(len(self._view.getListOfSecondPossibleScores())):
                    if self._pushPossibleScores[index5 + 6]:
                        self._view.getListOfSecondPossibleScores()[index5].setText('0')
                self.possiblyAddBonus()
            else:
                for index2 in range(len(self._roll)):
                    self._roll[index2].setText(' ')
                for index3 in range(len(self._yourDice)):
                    self._yourDice[index3].setText(' ')
                self.possiblyAddBonus()
                self._view.createEndScreen(self._model.getTotal())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model.Model()
    view = View.View()
    controller = Controller(model, view)
    view.show()
    sys.exit(app.exec_())
