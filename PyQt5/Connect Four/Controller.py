import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
import View
import Model


class Controller:
    def __init__(self, view_obj, model_obj):
        self._view = view_obj
        self._model = model_obj


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View.View()
    model = Model.Model()
    controller = Controller(view, model)
    view.show()
    sys.exit(app.exec_())
