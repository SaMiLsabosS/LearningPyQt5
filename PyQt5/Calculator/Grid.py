from PyQt5.QtWidgets import *
from Calculator import Calculator

class Grid():

    def __init__(self, widget, coordinates):
        self._grid = QGridLayout(widget)
        self._coordinates = coordinates

    def addToGrid(self):
        for index in range(len(self._coordinates)):
            self._grid.addToGrid()