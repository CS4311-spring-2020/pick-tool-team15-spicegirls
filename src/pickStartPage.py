import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class PickStartPage(QMainWindow):
    def __init__(self):
        super(PickStartPage, self).__init__()
        loadUi('../ui/pickStartPage.ui', self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = PickStartPage()
    app.exec_()

