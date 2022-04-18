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
        self._listOfFirstPossibleScores = [QPushButton('0'), QPushButton('0'), QPushButton('0'), QPushButton('0'),
                                           QPushButton('0'), QPushButton('0')]
        self._listOfSecondPossibleScores = [QPushButton('0'), QPushButton('0'), QPushButton('0'), QPushButton('0'),
                                            QPushButton('0'), QPushButton('0'), QPushButton('0')]
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
        self._listOfFirstPossibleScores[0].clicked.connect(lambda: self.addToScoreAndReset(listOfTopScores, 0,
                                                           self._listOfFirstPossibleScores, 0))
        self._listOfFirstPossibleScores[1].clicked.connect(lambda: self.addToScoreAndReset(listOfTopScores, 1,
                                                           self._listOfFirstPossibleScores, 1))
        self._listOfFirstPossibleScores[2].clicked.connect(lambda: self.addToScoreAndReset(listOfTopScores, 2,
                                                           self._listOfFirstPossibleScores, 2))
        self._listOfFirstPossibleScores[3].clicked.connect(lambda: self.addToScoreAndReset(listOfTopScores, 3,
                                                           self._listOfFirstPossibleScores, 3))
        self._listOfFirstPossibleScores[4].clicked.connect(lambda: self.addToScoreAndReset(listOfTopScores, 4,
                                                           self._listOfFirstPossibleScores, 4))
        self._listOfFirstPossibleScores[5].clicked.connect(lambda: self.addToScoreAndReset(listOfTopScores, 5,
                                                           self._listOfFirstPossibleScores, 5))
        self._listOfSecondPossibleScores[0].clicked.connect(lambda: self.addToScoreAndReset(listOfBottomScores, 0,
                                                            self._listOfSecondPossibleScores, 6))
        self._listOfSecondPossibleScores[1].clicked.connect(lambda: self.addToScoreAndReset(listOfBottomScores, 1,
                                                            self._listOfSecondPossibleScores, 7))
        self._listOfSecondPossibleScores[2].clicked.connect(lambda: self.addToScoreAndReset(listOfBottomScores, 2,
                                                            self._listOfSecondPossibleScores, 8))
        self._listOfSecondPossibleScores[3].clicked.connect(lambda: self.addToScoreAndReset(listOfBottomScores, 3,
                                                            self._listOfSecondPossibleScores, 9))
        self._listOfSecondPossibleScores[4].clicked.connect(lambda: self.addToScoreAndReset(listOfBottomScores, 4,
                                                            self._listOfSecondPossibleScores, 10))
        self._listOfSecondPossibleScores[5].clicked.connect(lambda: self.addToScoreAndReset(listOfBottomScores, 5,
                                                            self._listOfSecondPossibleScores, 11))
        self._listOfSecondPossibleScores[6].clicked.connect(lambda: self.addToScoreAndReset(listOfBottomScores, 6,
                                                            self._listOfSecondPossibleScores, 12))

    def establishScoreButtons(self):
        invisibleHeader = QPushButton(' ')
        invisibleHeader.setStyleSheet(
            'background-color: transparent;'
            'border: none;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        self._fifthGrid.addWidget(invisibleHeader, 0, 0)

        for index in range(len(self._listOfFirstPossibleScores)):  # might have to account for the bonus
            self._listOfFirstPossibleScores[index].setStyleSheet(
                    'background-color: grey;'
                    'border: black;'
                    'font-size: 15px;'
            )
            self._fifthGrid.addWidget(self._listOfFirstPossibleScores[index], index + 1, 0)

        invisibleButton = QPushButton(' ')
        invisibleButton.setStyleSheet(
            'background-color: transparent;'
            'border: none;'
        )
        self._fifthGrid.addWidget(invisibleButton, 7, 0)

        self._view.firstHLayout.addLayout(self._fifthGrid)

        invisibleHeaderTwo = QPushButton(' ')
        invisibleHeaderTwo.setStyleSheet(
            'background-color: transparent;'
            'border: none;'
            'font-size: 18px;'
            'font-weight: bold;'
        )
        self._sixthGrid.addWidget(invisibleHeaderTwo, 0, 0)

        for index in range(len(self._listOfSecondPossibleScores)):
            self._listOfSecondPossibleScores[index].setStyleSheet(
                'background-color: grey;'
                'border: black;'
                'font-size: 15px;'
            )
            self._sixthGrid.addWidget(self._listOfSecondPossibleScores[index], index + 1, 0)

        self._view.secondHLayout.addLayout(self._sixthGrid)

    def rollButtonFunction(self):
        if self._tries == 0:
            self.createDice()
            self.createYourDiceInventory()
            if self._initial:
                self._initial = False
                self.establishScoreButtons()
            self._tries += 1
        elif 0 < self._tries < 3:
            self._tries += 1
            for index in range(len(self._roll)):
                if self._roll[index].text() != ' ':  # shift the dice to the left when less than 5
                    self._roll[index].setText(str(random.randint(1, 6)))

    def createDice(self):
        if self._initial:
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
            for index2 in range(len(self._yourDice)):
                if self._yourDice[index2].text() == ' ':
                    self._yourDice[index2].setText(dice)
                    self._model.addToSumOfRoll(dice)
                    self._roll[index].setText(' ')
                    self.updateSumOfRollAndScoreButtons()
                    break  # talk to Mr.Bonsall about using break

    def createYourDiceButton(self, index):
        dice = self._yourDice[index].text()
        for index2 in range(len(self._roll)):
            if self._roll[index2].text() == ' ':
                self._roll[index2].setText(dice)
                self._model.subtractFromSumOfRoll(dice)
                self._yourDice[index].setText(' ')
                self.updateSumOfRollAndScoreButtons()
                break  # talk to Mr.Bonsall about using break

    def updateSumOfRollAndScoreButtons(self):
        self._model.updateSumOfRoll(self._listOfSecondPossibleScores[6])
        self._model.updateSumsOfSingleDigitNums(self._yourDice)
        for index in range(len(self._model.getSumsOfSingleDigitNums())):
            if self._pushPossibleScores[index]:
                temp = self._model.getIndexOfSumsOfSingleDigitNums(index)
                if temp != '0':
                    temp = '+'+temp
                self._listOfFirstPossibleScores[index].setText(temp)
        count = 0
        for index in range(len(self._yourDice)):
            if self._yourDice[index].text() != ' ':
                count += 1
        if count == 5:
            self._model.checkUniqueScores(self._yourDice)
            listOfUniqueScores = self._model.getUniqueScores()
            for index2 in range(len(listOfUniqueScores)):
                if self._pushPossibleScores[6+index2]:
                    newNum = str(listOfUniqueScores[index2])
                    if newNum != '0':
                        newNum = '+'+newNum
                    self._listOfSecondPossibleScores[index2].setText(newNum)
        self._model.setUniqueScores([0, 0, 0, 0, 0, 0])
        # create a method that returns a set of places to update a score button to the score
        # this could reduce space within the controller and put more code in the model

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
            totalPoints = self._model.getTotal()
            totalPoints += total
            for index2 in range(len(self._roll)):  # IDEA: Make each dice an image of the dice needed
                randomNum = str(random.randint(1, 6))
                self._roll[index2].setText(randomNum)
            for index3 in range(len(self._yourDice)):
                self._yourDice[index3].setText(' ')
            self._model.setSumOfRoll(0)
            for index4 in range(len(self._listOfFirstPossibleScores)):
                if self._pushPossibleScores[index4]:
                    self._listOfFirstPossibleScores[index4].setText('0')
            for index5 in range(len(self._listOfSecondPossibleScores)):
                if self._pushPossibleScores[index5+6]:
                    self._listOfSecondPossibleScores[index5].setText('0')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Look at stack overflow for customizing the Application
    model = Model.Model()
    view = View.PyYahtzeeUI()
    controller = Controller(model, view)
    view.show()
    sys.exit(app.exec_())
