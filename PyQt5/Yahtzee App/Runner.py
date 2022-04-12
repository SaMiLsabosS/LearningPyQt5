import sys
from PyQt5.QtWidgets import *
import Menu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Menu.PyYahtzeeUI()
    view.show()
    sys.exit(app.exec_())
