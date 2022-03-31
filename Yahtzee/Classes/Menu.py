from Classes.Printer import Printer
from Classes.Score import Score


class Menu:
    bonusNum = 35
    names = ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Sum', 'Bonus', '3Kind',
             '4Kind', 'FHouse', 'Sm Str', 'Lg Str', 'Yahtzee', 'Chance',
             'Total']
    options = ['1', '2', '3', '4', '5', '6', '-', '-', '3k', '4k', 'f', 's', 'l', 'y', 'c', '-']
    nums = ['1', '2', '3', ' 4', '5']
    kind = ['3k', '4k']
    other = 'fslyc'

    def __init__(self):  # no final variables for python
        self._optionIndex = 0
        self._list = []
        self._option = ''
        self._error = False
        self._score = Score()

    def setOption(self, oP):
        self._option = oP

    def setList(self, lis):
        self._list = lis

    def getError(self):
        return self._error

    def getScore(self):
        return self._score

    def change(self, roll):
        self._optionIndex = self.options.index(self._option)
        if self.checkOption():
            scoreList = self._score.getScore()
            sums = self._score.getSumsOfSingleDigitNums()

            scoreNum = self._list[self._optionIndex]
            add = False
            if scoreNum > 0:
                add = True
            if self._option in self.nums:
                scoreList[self._optionIndex] = sums[self._optionIndex]
                self._score.addToSum(sums[self._optionIndex])
            elif self._option in self.kind:
                num = self._option[0:1]
                self._score.addNumOfAKind(roll, num, self._optionIndex, add)
            else:
                moveOn = False
                index = 0
                while not moveOn and index < sum(self.other):
                    if self._option == self.other[index:index + 1]:
                        moveOn = True
                    index += 1
        else:
            self._error = True

    def checkOption(self):
        scoreList = self._score.getScore()
        if scoreList[self._optionIndex] > -1:
            return False
        return True

    def checkBonus(self):
        if self._score.getSumOfSingleDigitNums() >= 63:
            self._score.addToBonus(self.bonusNum)

    def finish(self):
        scoreList = self._score.getScore()
        for var in scoreList:
            if var == -1:
                return False
        return True

    def __str__(self):
        output = Printer(self._score.getScore(), self.names)
        return output.__str__()
