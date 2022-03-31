import random


class Roll:
    startOne = [-1, -1, -1, -1, -1]
    startTwo = [False, False, False, False, False]

    def __init__(self):
        self._roll = self.startOne
        self._changes = self.startTwo
        self._empty = False

    def setEmpty(self, e):
        self._empty = e

    def getRoll(self):
        return self._roll

    def getChanges(self):
        return self._changes

    def length(self):
        return len(self._roll)

    def generateRoll(self):
        for index in range(len(self._roll)):
            if self._empty or self._changes[index]:
                self._roll[index] = random.randint(1, 6)
        self._changes = [False, False, False, False, False]
        self._empty = False

    def __str__(self):
        return str(self._roll)
