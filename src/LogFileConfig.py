import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.uic import loadUi


class LogFileConfig(QMainWindow):
    def __init__(self):
        super(LogFileConfig, self).__init__()
        loadUi('../ui/LogFileConfig.ui', self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = LogFileConfig()
    app.exec_()
