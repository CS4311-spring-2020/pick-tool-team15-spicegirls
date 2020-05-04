from PyQt5.QtCore import pyqtProperty
from PyQt5.QtGui import QPixmap
from PyQt5 import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class CustomIconWidget(QWidget):
    def __init__(self, img, parent=None):
        QWidget.__init__(self, parent)

        self._img = img

        self.setLayout(QVBoxLayout())
        self.lbPixmap = QLabel(self)
        self.layout().addWidget(self.lbPixmap)

        self.initUi()

    def initUi(self):
        self.lbPixmap.setPixmap(QPixmap(self._img).scaled(self.lbPixmap.size(), 1))

    @pyqtProperty(str)
    def img(self):
        return self._img

    @img.setter
    def total(self, value):
        if self._img == value:
            return
        self._img = value
        self.initUi()