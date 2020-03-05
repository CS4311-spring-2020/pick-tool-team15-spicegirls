from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, qApp, QMenu, QLineEdit, QTableWidget, QTableWidgetItem, QComboBox
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtCore
from fileDirectory import FileDirectory
from FilterConfiguration import FilterConfig
from SettingView import SettingsWindow
from ExportConfiguration import ExportConfig
from VectDBConfig import VectorDBConfig
from LogFileConfig import LogFileConfig


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('../ui/MainWindow.ui', self)

        self.FilterConfigButton = self.findChild(QPushButton, 'filterButton')
        self.FilterConfigButton.clicked.connect(self.openFilterConfig)

        self.settingsConfig = self.findChild(QAction, 'actionSettings')
        self.settingsConfig.triggered.connect(self.openSettings)

        #Search button functionality ##need to add keyword search still
        self.searchSearchButton = self.findChild(QPushButton, 'searchSearchButton')
        self.searchSearchButton.clicked.connect(self.openFilterConfig)

        # Enter press on qlineedit search tab triggers the search button
        self.searchLineEdit = self.findChild(QLineEdit, 'lineEdit_2')
        self.searchLineEdit.returnPressed.connect(self.searchSearchButton.click)

        #Search button on graph tab functionality ##need keyword functionality added
        self.graphSearchButton = self.findChild(QPushButton, 'graphSearchButton_2')
        self.graphSearchButton.clicked.connect(self.openFilterConfig)

        # Enter press on qlineedit graph tab triggers search button
        self.graphSearchEdit = self.findChild(QLineEdit, 'graphLineEdit')
        self.graphSearchEdit.returnPressed.connect(self.graphSearchButton.click)

        #Exit menu option functionality
        self.CloseMenuSelect = self.findChild(QAction, 'actionClose_Exit')
        self.CloseMenuSelect.setShortcut('Ctrl+Q')
        self.CloseMenuSelect.triggered.connect(qApp.quit)

        #Export menu option functionality
        self.exportConfig = self.findChild(QAction, 'actionExport')
        self.exportConfig.setShortcut('Ctrl+E')
        self.exportConfig.triggered.connect(self.openExportConfig)

        #VectorDBConfig linked to menu option
        self.versionControl = self.findChild(QAction, 'actionVersion_Control')
        self.versionControl.setShortcut('Ctrl+S')
        self.versionControl.triggered.connect(self.openVectDBConfig)

        self.actionLogFile = self.findChild(QAction, 'actionFileConfig')
        self.actionLogFile.setShortcut('Ctrl+F')
        self.actionLogFile.triggered.connect(self.openLogConfig)

        #drop down menus vector collumn search table
        self.searchSearchTableWidget = self.findChild(QTableWidget, 'tableWidget_2')
        i = 0
        while i < 10:
            combo = QComboBox()
            combo.addItems([' ', '1', '2', '3'])
            self.searchSearchTableWidget.setCellWidget(i, 3, combo)
            i += 1

        self.show()

    def openLogConfig(self):
        self.window = LogFileConfig()
        self.window.show()

    def openVectDBConfig(self):
        self.window = VectorDBConfig()
        self.window.show()

    def openExportConfig(self):
        self.window = ExportConfig()
        self.window.show()

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