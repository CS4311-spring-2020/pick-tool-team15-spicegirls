import sys
import main_window
import setting_view
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi


class PickStartPage(QMainWindow):
    def __init__(self):
        super(PickStartPage, self).__init__()
        loadUi('../ui/pickStartPage.ui', self)

        self.goToCurrentProjectButton = self.findChild(QPushButton, 'CurrentProject_PushButton')
        self.settingsConfig = self.findChild(QPushButton, 'CreateNew_pushButton')

        self.goToCurrentProjectButton.clicked.connect(self.openMain)
        self.settingsConfig.clicked.connect(self.openSettings)

        self.show()

    def openMain(self):
        self.window = main_window.MainWindow()
        self.window.show()
        self.close()

    def openSettings(self):
        self.window = setting_view.SettingsWindow()
        self.window.show()
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = PickStartPage()
    app.exec_()

