from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QToolButton, QComboBox, QTableWidget, QTableWidgetItem, QLabel
from PyQt5.uic import loadUi
from fileDirectory import FileDirectory

class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        loadUi('../ui/SettingView.ui', self)

        self.mainStackedView = self.findChild(QStackedWidget, 'StackView')
        
        self.OV_TeamConfigButton = self.findChild(QPushButton, 'OV_TeamConfigButton')
        self.OV_EventConfigButton = self.findChild(QPushButton, 'OV_EventConfigButton')
        self.OV_DirectoryConfigButton = self.findChild(QPushButton, 'OV_DirectoryConfigButton')
        self.OV_VectorConfigButton = self.findChild(QPushButton, 'OV_VectorConfigButton')
        self.OV_ChangeConfigButton = self.findChild(QPushButton, 'OV_ChangeConfigButton')
        self.OV_IconConfigButton = self.findChild(QPushButton, 'OV_IconConfigButton')

        self.BlueTeamToolButton = self.findChild(QToolButton, 'BlueTeamToolButton')
        self.RootDirectoryToolButton = self.findChild(QToolButton, 'RootDirectoryToolButton')
        self.RedTeamToolButton = self.findChild(QToolButton, 'RedTeamToolButton')
        self.WhiteTeamToolButton = self.findChild(QToolButton, 'WhiteTeamToolButton')

        self.OV_TeamConfigButton.clicked.connect(lambda: self.btn(0))
        self.OV_EventConfigButton.clicked.connect(lambda: self.btn(1))
        self.OV_DirectoryConfigButton.clicked.connect(lambda: self.btn(2))
        self.OV_VectorConfigButton.clicked.connect(lambda: self.btn(3))
        self.OV_ChangeConfigButton.clicked.connect(lambda: self.btn(4))
        self.OV_IconConfigButton.clicked.connect(lambda: self.btn(5))
        
        self.BlueTeamToolButton.clicked.connect(lambda: self.btn(6))
        self.RootDirectoryToolButton.clicked.connect(lambda: self.btn())
        self.RedTeamToolButton.clicked.connect(lambda: self.btn(6))
        self.WhiteTeamToolButton.clicked.connect(lambda: self.btn(6))

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
        if index < 6:
            self.StackView.setCurrentIndex(index)
        elif index == 6:
            self.window = FileDirectory()
            self.window.show()

if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    window = Ui()
    application.exec_()