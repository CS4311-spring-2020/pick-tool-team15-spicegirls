import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi


class FilterConfig(QWidget):
    def __init__(self):
        super(FilterConfig, self).__init__()
        loadUi('../ui/FilterConfiguration.ui', self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = FilterConfig()
    app.exec_()
