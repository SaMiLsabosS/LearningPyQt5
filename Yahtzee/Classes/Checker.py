class Checker:
    startOne = {0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, -1}
    startTwo = {True, True, True, True, True, True, False, False, False, False, False, False, False, False, True, False}

    def __init__(self, sON):
        self._list = self._startOne
        self._possible = self._startTwo
        self._sumsOfNums = sON

    def getList(self):
        return self._list

    # def change(self, roll):
    #