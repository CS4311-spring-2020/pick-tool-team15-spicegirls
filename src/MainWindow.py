from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QToolButton, QComboBox, \
    QTableWidget, QTableWidgetItem, QLabel
from PyQt5.uic import loadUi
from fileDirectory import FileDirectory
from FilterConfiguration import FilterConfig


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('../ui/MainWindow.ui', self)

        self.OV_TeamConfigButton = self.findChild(QPushButton, 'filterButton')
        self.OV_TeamConfigButton.clicked.connect(self.openFilterConfig)

        self.OV_TeamConfigButton = self.findChild(QPushButton, 'graphSearchButton')
        self.OV_TeamConfigButton.clicked.connect(self.openFileDirectory)

        self.show()

    def openFilterConfig(self):
        self.window = FilterConfig()
        self.window.show()

    def openFileDirectory(self):
        self.window = FileDirectory()
        self.window.show()


if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    window = MainWindow()
    application.exec_()
