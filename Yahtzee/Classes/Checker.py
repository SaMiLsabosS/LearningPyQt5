from Classes.Menu import *


class Checker(Menu):
    startOne = [0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, -1]
    startTwo = [True, True, True, True, True, True, False, False, False, False, False, False, False, False, True, False]
    nums = [0, 1, 2, 3, 4, 5]
    sums = [8, 9, 14]
    indexes = [10, 11, 12, 13]
    points = [25, 30, 40, 50]

    def __init__(self, sON):
        super().__init__() # eliminate if errors arise
        self._list = self.startOne
        self._possible = self.startTwo
        self._sumsOfNums = sON

    def getList(self):
        return self._list

    def change(self, roll):
        self.checkNumsOfAKind(roll)
        self.checkFullHouse(roll)
        self.checkSizeStraights(roll)
        for index in range(len(self._possible)):
            if self._possible[index]:
                if index in self.nums:
                    self._list[index] = self._sumsOfNums[index]
                elif index in self.sums:
                    self._list[index] = super().getScore().getSumOfRoll(roll)
                else:
                    moveOn = False
                    index2 = 0
                    while not moveOn and index2 < len(self.indexes):
                        if index == self.indexes[index2]:
                            self._list[index] = self.points[index2]
                        index2 += 1

    def checkNumsOfAKind(self, roll):
        numsOfAKind = [3, 4, 5]
        indexes = [8, 9, 13]
        rollNums = roll.getRoll()
        for index in range(3):
            match = False
            index2 = 0
            nums = super().getScore().getNums()
            while index2 < len(nums) and not match:
                temp = 0
                for dice in rollNums:
                    if nums[index2] == dice:
                        temp += 1
                if temp >= numsOfAKind[index] or temp == 5:
                    match = True
                else:
                    index2 += 1
            if match:
                self._possible[indexes[index]] = True

    def checkFullHouse(self, roll):
        finishTwo = False
        finishThree = False
        indexOfFullHouse = 10
        index = 0
        nums = super().getScore().getNums()
        rollNums = roll.getRoll()
        while index < len(nums) and (not finishTwo or not finishThree):
            temp = 0
            for num in rollNums:
                if nums[index] == num:
                    temp += 1
            if temp == 2:
                finishTwo = True
            elif temp == 3:
                finishThree = True
            index += 1
        if finishTwo and finishThree:
            self._possible[indexOfFullHouse] = True

    def checkSizeStraights(self, roll):  # check this, it doesn't work
        indexes = [11, 12]
        sequence = [3, 4]
        rollNums = roll.getRoll()
        rollNums.sort()
        for index in range(2):
            index2 = 0
            count = 0
            while index2 < len(rollNums)-1 and count != sequence[index]:
                if rollNums[index2+1] == rollNums[index2] + 1:
                    count += 1
                index2 += 1
            if count == sequence[index]:
                self._possible[indexes[index]] = True

    def __str__(self):
        output = Printer(self._list, super().names)
        return output.__str__()
