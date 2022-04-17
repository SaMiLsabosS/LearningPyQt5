class Model:
    def __init__(self):
        self._sumOfRoll = 0

    def getSumOfRoll(self):
        return str(self._sumOfRoll)

    def addToSumOfRoll(self, num):
        self._sumOfRoll += int(num)

    def subtractFromSumOfRoll(self, num):
        self._sumOfRoll -= int(num)
