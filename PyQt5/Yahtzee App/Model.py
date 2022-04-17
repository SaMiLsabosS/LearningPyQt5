class Model:
    nums = [1, 2, 3, 4, 5, 6]

    def __init__(self):
        self._sumOfRoll = 0
        self._sumsOfSingleDigitNums = [0, 0, 0, 0, 0, 0]

    def setSumOfRoll(self, newSum):
        self._sumOfRoll = newSum

    def getSumOfRoll(self):
        return str(self._sumOfRoll)

    def getSumsOfSingleDigitNums(self):
        return self._sumsOfSingleDigitNums

    def getIndexOfSumsOfSingleDigitNums(self, index):
        return str(self._sumsOfSingleDigitNums[index])

    def addToSumOfRoll(self, num):
        self._sumOfRoll += int(num)

    def subtractFromSumOfRoll(self, num):
        self._sumOfRoll -= int(num)

    def updateSumOfRoll(self, possibleScoresList):
        if possibleScoresList.text() != ' ':
            sumOfRoll = self.getSumOfRoll()
            if sumOfRoll != '0':
                sumOfRoll = '+'+sumOfRoll
            possibleScoresList.setText(sumOfRoll)

    def updateSumsOfSingleDigitNums(self, roll):
        for index in range(len(self._sumsOfSingleDigitNums)):
            temp = 0
            for num in roll:
                if num.text() != ' ':
                    if int(num.text()) == self.nums[index]:
                        temp += self.nums[index]
            self._sumsOfSingleDigitNums[index] = temp
