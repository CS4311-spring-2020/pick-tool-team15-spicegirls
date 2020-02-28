import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi


class VectorDBConfig(QWidget):
    def __init__(self):
        super(VectorDBConfig, self).__init__()
        loadUi('../ui/VectDBConfig.ui', self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = VectorDBConfig()
    app.exec_()
