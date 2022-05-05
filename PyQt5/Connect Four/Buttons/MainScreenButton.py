from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QSize


class MainScreenButton(QPushButton):
    def __init__(self):
        QPushButton.__init__(self)
        self._anim = QPropertyAnimation(self, b'geometry')
        # self._anim.setDuration(250)
        self._anim.setEasingCurve(QEasingCurve.OutElastic)

    def enterEvent(self, event):
        # rect = self.geometry()
        self.anim.setStartingValue(self.size())
        # rect.translate(30, -30)
        self.anim.setEndValue(QSize(200, 200))
