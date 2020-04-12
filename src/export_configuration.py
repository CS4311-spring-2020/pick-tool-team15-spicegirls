import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi


class ExportConfig(QWidget):
    def __init__(self):
        super(ExportConfig, self).__init__()
        loadUi('../ui/ExportConfiguration.ui', self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ExportConfig()
    app.exec_()
