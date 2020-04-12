from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QToolButton, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QFileDialog
from PyQt5.uic import loadUi
import main_window
import shelve


class SettingsWindow(QMainWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        loadUi('../ui/SettingView.ui', self)

        self.configDB = shelve.open('../Resouces/ConfigDB/TestConfig')  # Initialize values to avoid exeptions
        self.configDB.close()

        self.mainStackedView = self.findChild(QStackedWidget, 'StackView')
        
        self.OV_TeamConfigButton = self.findChild(QPushButton, 'OV_TeamConfigButton')
        self.OV_EventConfigButton = self.findChild(QPushButton, 'OV_EventConfigButton')
        self.OV_DirectoryConfigButton = self.findChild(QPushButton, 'OV_DirectoryConfigButton')
        self.OV_VectorConfigButton = self.findChild(QPushButton, 'OV_VectorConfigButton')
        self.OV_IconConfigButton = self.findChild(QPushButton, 'OV_IconConfigButton')

        self.SaveEventConfig = self.findChild(QPushButton, 'SaveEventPushButton')

        self.ENLineEdit = self.findChild(QLineEdit, 'EventNameLineEdit')  # This goes to test persistence db
        self.EDLineEdit = self.findChild(QLineEdit, 'EventDescriptionLineEdit')
        self.ESLineEdit = self.findChild(QLineEdit, 'EventStartLineEdit')
        self.EELineEdit = self.findChild(QLineEdit, 'EventEndLineEdit')

        self.configDB = shelve.open('../Resouces/ConfigDB/TestConfig')
        self.ENLineEdit.setText(self.configDB['EventName'])
        self.EDLineEdit.setText(self.configDB['EventDescription'])
        self.ESLineEdit.setText(self.configDB['EventStartTime'])
        self.EELineEdit.setText(self.configDB['EventEndTime'])
        self.configDB.close()

        self.ENLineEdit.textChanged.connect(self.updateED)
        self.EDLineEdit.textChanged.connect(self.updateED)  # Temp config Stuff

        self.ApplyButton = self.findChild(QPushButton, 'applyButton')

        self.BlueTeamToolButton = self.findChild(QToolButton, 'BlueTeamToolButton')
        self.BlueTeamLineEdit = self.findChild(QLineEdit, 'BlueTeamLineEdit')

        self.RootDirectoryToolButton = self.findChild(QToolButton, 'RootDirectoryToolButton')
        self.RootLineEdit = self.findChild(QLineEdit, 'RootDirectoryLineEdit')

        self.RedTeamToolButton = self.findChild(QToolButton, 'RedTeamToolButton')
        self.RedTeamLineEdit = self.findChild(QLineEdit, 'RedTeamLineEdit')

        self.WhiteTeamToolButton = self.findChild(QToolButton, 'WhiteTeamToolButton')
        self.WhiteTeamLineEdit = self.findChild(QLineEdit, 'WhiteTeamLineEdit')

        # self.OV_TeamConfigButton.clicked.connect(self.applyChanges)

        self.OV_TeamConfigButton.clicked.connect(lambda: self.btn(0))
        self.OV_EventConfigButton.clicked.connect(lambda: self.btn(1))
        self.OV_DirectoryConfigButton.clicked.connect(lambda: self.btn(2))
        self.OV_VectorConfigButton.clicked.connect(lambda: self.btn(3))
        self.OV_IconConfigButton.clicked.connect(lambda: self.btn(4))

        self.RootDirectoryToolButton.clicked.connect(lambda: self.setDir(0))
        self.RedTeamToolButton.clicked.connect(lambda: self.setDir(1))
        self.BlueTeamToolButton.clicked.connect(lambda: self.setDir(2))
        self.WhiteTeamToolButton.clicked.connect(lambda: self.setDir(3))

        self.completeSettings = self.findChild(QPushButton, 'completeSetupButton_pushButton')
        self.completeSettings.clicked.connect(self.openMain)

        # Vector configuration table checkboxes
        self.VCtable = self.findChild(QTableWidget, 'VC_TableView')
        i = 0
        while i < 50:
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            self.VCtable.setItem(i, 0, checkbox)
            i += 1

        # Icon configuration table checkboxes
        self.ICtable = self.findChild(QTableWidget, 'IC_IT_TableWidget')
        i = 0
        while i < 50:
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            self.ICtable.setItem(i, 0, checkbox)
            i += 1

        self.connectButton = self.findChild(QPushButton, 'TeamConfigConnectpushButton')
        self.connectStatus = self.findChild(QLabel, 'ConnectionStatus')
        self.connectButton.clicked.connect(self.connectButtonClicked)

        self.show()

    def connectButtonClicked(self):
        if self.connectButton.text() == 'Disconnect':
            self.connectButton.setText('Connect')
            self.connectStatus.setText('Not Connected')
        else:
            self.connectStatus.setText('Connected')
            self.connectButton.setText('Disconnect')

    def btn(self, index):
        if index < 5:
            self.StackView.setCurrentIndex(index)

    def setDir(self, index):
        temp_dir = QFileDialog.getExistingDirectory(self, 'Choose Directory', "", QFileDialog.ShowDirsOnly)
        if index == 0:
            self.RootLineEdit.setText(str(temp_dir))
        elif index == 1:
            self.RedTeamLineEdit.setText(str(temp_dir))
        elif index == 2:
            self.BlueTeamLineEdit.setText(str(temp_dir))
        elif index == 3:
            self.WhiteTeamLineEdit.setText(str(temp_dir))

    def updateED(self):
        db = shelve.open('../Resouces/ConfigDB/TestConfig')  # Shelve will create data.db
        db['EventName'] = self.ENLineEdit.text()
        db['EventDescription'] = self.EDLineEdit.text()
        db['EventStartTime'] = self.ESLineEdit.text()
        db['EventEndTime'] = self.EELineEdit.text()
        db.close()

    def openMain(self):
        self.window = main_window.MainWindow()
        self.window.show()
        self.close()

if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    window = SettingsWindow()
    application.exec_()