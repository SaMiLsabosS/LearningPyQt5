class Printer:
    def __init__(self, lis, n):
        self._output = ''
        self._list = lis
        self._names = n

    def __str__(self):
        for index in range(len(self._names)):
            if index == 6 or index == 8 or index == 15:
                self._output += '-----\n'+self._names[index]+'\t'+self._list[index]+'\n'
            else:
                self._output += self._names[index]+'\t'+self._list[index]+'\n'
        return self._output
