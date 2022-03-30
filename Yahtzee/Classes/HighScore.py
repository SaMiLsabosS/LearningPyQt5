import functools


@functools.total_ordering
class HighScore:
    def __init__(self, n, s):
        self._name = n
        self._score = s

    def getName(self):
        return self._name

    def getScore(self):
        return self._score

    def __lt__(self, other):
        if self.getScore != other.getScore():
            return self.getScore() - other.getScore()
        return NotImplemented

    def __eq__(self, other):  # Test this out to see if eq and lt are required
        return self.getScore() == other.getScore() or self.getScore() != other.getScore()

    def __str__(self):
        return self._name+' '+self._score
