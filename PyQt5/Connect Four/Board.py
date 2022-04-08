from PyQt5.QtWidgets import *


class Board:
    def __init__(self):
        self._rowChooser = [[QPushButton()]*7]
        self._boardSlots = [[QPushButton()]*7]*7  # if this does not work then make them manually
        self._red = 1
        self._yellow = 2
