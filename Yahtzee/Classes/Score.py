class Score:
    start = [-1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, 0]
    nums = [1, 2, 3, 4, 5, 6]

    def __init__(self):
        self._score = self._start
        self._sumsOfSingleDigitNums = []
        self._sumOfSingleDigitNums = 0
        self._bonus = 0
        self._total = 0

    def getTotal(self):
        return self._total

    def getNums(self):
        return self._nums

    def getScore(self):
        return self._score

    def getSumsOfSingleDigitNums(self):
        return self._sumsOfSingleDigitNums

    def getSumOfSingleDigitNums(self):
        return self._sumOfSingleDigitNums

    def getSumOfRoll(self, roll):  # if things go wrong, create roll
        rollSum = 0
        for num in roll.getRoll():
            rollSum += num
        return rollSum

    def updateSum(self, roll):
        for i in range(len(self._sumsOfSingleDigitNums)):
            temp = 0
            for slot in roll.getRoll():
                if slot == self._nums[i]:
                    temp += self._nums[i]
            self._sumsOfSingleDigitNums[i] = temp

    def addToSum(self, num):
        self._sumOfSingleDigitNums += num
        self._score[15] = self._total
        self.addToTotal(num)

    def addToTotal(self, num):
        self._total += num
        self._score[15] = self._total

    def addToBonus(self, num):
        self._bonus += num
        self._score[7] = self._bonus
        self.addToTotal(self._bonus)

    def addNumOfAKind(self, roll, num, index, add):
        if add:
            if num == 3 or num == 4:  # 3 of a kind or 4 of a kind
                sumOfRoll = self.getSumOfRoll(roll)
                self._score[index] = sumOfRoll
                self.addToTotal(sumOfRoll)
            else:  # Yahtzee (5 of a kind) 50 points
                self._score[index] = 50
                self.addToTotal(50)
        else:
            self._score[index] = 0

    def addFullHouse(self, index, add):  # 25 points
        if add:
            self._score[index] = 25
            self.addToTotal(25)
        else:
            self._score[index] = 0

    def addSizeStraight(self, index, points, add):  # 30 or 40 points respectively
        if add:
            self._score[index] = points
            self.addToTotal(points)
        else:
            self._score[index] = 0

    def addChance(self, roll, index):
        sumOfRoll = self.getSumOfRoll(roll)
        self._score[index] = sumOfRoll
        self.addToTotal(sumOfRoll)
