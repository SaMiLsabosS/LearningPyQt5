import sys
from PyQt5.QtWidgets import *
import View
import Model


class Controller:  # Ask if the controller should be created in the view
    def __init__(self, model_obj, view_obj):
        self._model = model_obj
        self._view = view_obj


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Look at stack overflow for customizing the Application
    model = Model.Model()
    view = View.PyYahtzeeUI()
    # a method of some sorts could go here
    # add in the .clicked.connect functions here, I think
    view.show()
    sys.exit(app.exec_())
