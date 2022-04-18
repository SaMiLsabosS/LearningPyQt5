class Model:
    nums = [1, 2, 3, 4, 5, 6]

    def __init__(self):
        self._sumOfRoll = 0
        self._sumsOfSingleDigitNums = [0, 0, 0, 0, 0, 0]
        self._uniqueScores = [0, 0, 0, 0, 0, 0]
        self._totalPoints = 0

    def setSumOfRoll(self, newSum):
        self._sumOfRoll = newSum

    def getSumOfRoll(self):
        return str(self._sumOfRoll)

    def getSumsOfSingleDigitNums(self):
        return self._sumsOfSingleDigitNums

    def getIndexOfSumsOfSingleDigitNums(self, index):
        return str(self._sumsOfSingleDigitNums[index])

    def getUniqueScores(self):
        return self._uniqueScores

    def getTotal(self):
        return self._totalPoints

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

    def checkUniqueScores(self, roll):
        self.checkNumsOfAKind(roll)
        self.checkFullHouse(roll)
        self.checkStraights(roll)

    def checkNumsOfAKind(self, roll):
        numsOfAKind = [3, 4, 5]
        for index in range(3):
            match = False
            index2 = 0
            while index2 < len(self.nums) and not match:
                temp = 0
                for index3 in range(len(roll)):
                    if self.nums[index2] == int(roll[index3].text()):
                        temp += 1
                if temp >= numsOfAKind[index] or temp == 5:
                    match = True
                else:
                    index2 += 1
            if match:
                if index < 2:
                    self._uniqueScores[index] = self._sumOfRoll
                else:
                    self._uniqueScores[5] = 50

    def checkFullHouse(self, roll):  # fix this, doesn't work at all
        finishTwo = False
        finishThree = False
        index = 0
        while index < len(self.nums) and (not finishTwo or not finishThree):
            temp = 0
            for index2 in range(len(roll)):
                if self.nums[index] == roll[index2].text():
                    temp += 1
            if temp == 2:
                finishTwo = True
            elif temp == 3:
                finishThree = True
            index += 1
        if finishTwo and finishThree:
            self._uniqueScores[2] = 25

    def checkStraights(self, roll):
        # fix this, roll might not be changing / returns same true categories from previous roll
        sequence = [3, 4]
        rollNums = [0, 0, 0, 0, 0]
        for index in range(len(roll)):
            rollNums[index] = int(roll[index].text())
        rollNums.sort()
        for index2 in range(2):
            index3 = 0
            count = 0
            while index3 < len(rollNums)-1 and count != sequence[index2]:
                if rollNums[index3+1] == rollNums[index3] + 1:
                    count += 1
                index3 += 1
            if count == sequence[index2]:
                if index2 == 0:
                    self._uniqueScores[3] = 30
                else:
                    self._uniqueScores[4] = 40
