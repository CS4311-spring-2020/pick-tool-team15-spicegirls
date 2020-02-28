from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction
from PyQt5.uic import loadUi
from fileDirectory import FileDirectory
from FilterConfiguration import FilterConfig
from SettingView import SettingsWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('../ui/MainWindow.ui', self)

        self.FilterConfigButton = self.findChild(QPushButton, 'filterButton')
        self.FilterConfigButton.clicked.connect(self.openFilterConfig)

        self.SettingsConfigButton = self.findChild(QPushButton, 'graphSearchButton')
        #self.SettingsConfigButton.clicked.connect(self.openFileDirectory)
        self.SettingsConfigButton.clicked.connect(self.openSettings)

        self.show()

    def openFilterConfig(self):
        self.window = FilterConfig()
        self.window.show()

    def openFileDirectory(self):
        self.window = FileDirectory()
        self.window.show()

    def openSettings(self):
        self.window = SettingsWindow()
        self.window.show()


if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    window = MainWindow()
    application.exec_()
