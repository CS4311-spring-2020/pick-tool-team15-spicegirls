from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QToolButton, QComboBox, \
    QTableWidget, QTableWidgetItem, QLabel
from PyQt5.uic import loadUi
from src.fileDirectory import FileDirectory


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        loadUi('../ui/PICK.ui', self)

        self.mainStackedView = self.findChild(QStackedWidget, 'StackView')

        self.OV_TeamConfigButton = self.findChild(QPushButton, 'OV_TeamConfigButton')
        self.OV_EventConfigButton = self.findChild(QPushButton, 'OV_EventConfigButton')
        self.OV_DirectoryConfigButton = self.findChild(QPushButton, 'OV_DirectoryConfigButton')
        self.OV_VectorConfigButton = self.findChild(QPushButton, 'OV_VectorConfigButton')
        self.OV_LogFileConfigButton = self.findChild(QPushButton, 'OV_LogFileConfigButton')
        self.OV_FilterConfigButton = self.findChild(QPushButton, 'OV_FilterConfigButton')
        self.OV_LogEntryConfigButton = self.findChild(QPushButton, 'OV_LogEntryConfigButton')
        self.OV_ExportConfigButton = self.findChild(QPushButton, 'OV_ExportConfigButton')
        self.OV_ChangeConfigButton = self.findChild(QPushButton, 'OV_ChangeConfigButton')
        self.OV_VectorDBConfigButton = self.findChild(QPushButton, 'OV_VectorDBConfigButton')
        self.OV_IconConfigButton = self.findChild(QPushButton, 'OV_IconConfigButton')
        self.OV_GraphBuilderConfigButton = self.findChild(QPushButton, 'OV_GraphBuilderConfigButton')
        self.OV_NodesConfigInTableButton = self.findChild(QPushButton, 'OV_NodesConfigInTableButton')
        self.OV_NodesConfigInGraphButton = self.findChild(QPushButton, 'OV_NodesConfigInGraphButton')
        self.OV_RelationshipConfigButton = self.findChild(QPushButton, 'OV_RelationshipConfigButton')

        self.BlueTeamToolButton = self.findChild(QToolButton, 'BlueTeamToolButton')
        self.RootDirectoryToolButton = self.findChild(QToolButton, 'RootDirectoryToolButton')
        self.RedTeamToolButton = self.findChild(QToolButton, 'RedTeamToolButton')
        self.WhiteTeamToolButton = self.findChild(QToolButton, 'WhiteTeamToolButton')

        self.OV_TeamConfigButton.clicked.connect(lambda: self.btn(0))
        self.OV_EventConfigButton.clicked.connect(lambda: self.btn(1))
        self.OV_DirectoryConfigButton.clicked.connect(lambda: self.btn(2))
        self.OV_VectorConfigButton.clicked.connect(lambda: self.btn(3))
        self.OV_LogFileConfigButton.clicked.connect(lambda: self.btn(4))
        self.OV_FilterConfigButton.clicked.connect(lambda: self.btn(5))
        self.OV_LogEntryConfigButton.clicked.connect(lambda: self.btn(6))
        self.OV_ExportConfigButton.clicked.connect(lambda: self.btn(7))
        self.OV_ChangeConfigButton.clicked.connect(lambda: self.btn(8))
        self.OV_VectorDBConfigButton.clicked.connect(lambda: self.btn(9))
        self.OV_IconConfigButton.clicked.connect(lambda: self.btn(10))
        self.OV_GraphBuilderConfigButton.clicked.connect(lambda: self.btn(11))
        self.OV_NodesConfigInTableButton.clicked.connect(lambda: self.btn(12))
        self.OV_NodesConfigInGraphButton.clicked.connect(lambda: self.btn(13))
        self.OV_RelationshipConfigButton.clicked.connect(lambda: self.btn(14))

        self.BlueTeamToolButton.clicked.connect(lambda: self.btn(15))
        self.RootDirectoryToolButton.clicked.connect(lambda: self.btn(15))
        self.RedTeamToolButton.clicked.connect(lambda: self.btn(15))
        self.WhiteTeamToolButton.clicked.connect(lambda: self.btn(15))

        # Log entry configuration page
        self.LECtable = self.findChild(QTableWidget, 'LEC_LET_TtableWidget')
        i = 0
        while i < 50:
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            self.LECtable.setItem(i, 0, checkbox)
            combo = QComboBox()
            combo.addItems([' ', '1', '2', '3'])
            self.LECtable.setCellWidget(i, 4, combo)
            i += 1

        # log file configuration table checkboxes
        self.LFGtable = self.findChild(QTableWidget, 'LFT_tableWidget')
        i = 0
        while i < 50:
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            self.LFGtable.setItem(i, 5, checkbox)
            i += 1

        # Vector configuration table checkboxes
        self.VCtable = self.findChild(QTableWidget, 'VC_TableView')
        i = 0
        while i < 50:
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            self.VCtable.setItem(i, 0, checkbox)
            i += 1

        # Relationship config table checkboxes
        self.RCtable = self.findChild(QTableWidget, 'RelationshipConfigTableWidget')
        i = 0
        while i < 50:
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            self.RCtable.setItem(i, 0, checkbox)
            i += 1

        # Pulled vector database table checkboxes
        self.PullVDBtable = self.findChild(QTableWidget, 'VDBC_PulledTableWidget')
        i = 0
        while i < 50:
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            self.PullVDBtable.setItem(i, 0, checkbox)
            i += 1

        # pushed vector database table check boxes
        self.PushVDBtable = self.findChild(QTableWidget, 'VDBC_PushedTableWidget')
        i = 0
        while i < 50:
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            self.PushVDBtable.setItem(i, 0, checkbox)
            i += 1

        # approval database table check boxes and drop down
        self.ADBtable = self.findChild(QTableWidget, 'VDBC_AS_TableWidget')
        i = 0
        while i < 50:
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            self.ADBtable.setItem(i, 0, checkbox)
            combo = QComboBox()
            combo.addItems([' ', '1', '2', '3'])
            self.ADBtable.setCellWidget(i, 7, combo)
            i += 1

        # Node configuration table check boxes and drop down
        self.NCtable = self.findChild(QTableWidget, 'NCITF_NT_tableWidget')
        i = 1
        while i < 50:
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            self.NCtable.setItem(i, 0, checkbox)
            i += 1

        i = 1
        while i < 10:
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            self.NCtable.setItem(0, i, checkbox)
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            self.NCtable.setItem(10, i, checkbox)
            i += 1

        i = 1
        while i < 10:
            j = 6
            while j < 9:
                combo = QComboBox()
                combo.addItems([' ', '1', '2', '3'])
                self.NCtable.setCellWidget(j, i, combo)
                j += 1
            i += 1

        # Node configuration in graphical view checkbox and combobox
        self.NCVtable = self.findChild(QTableWidget, 'NCIGF_TV_tableWidget')
        i = 1
        while i < 10:
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            self.NCVtable.setItem(i, 0, checkbox)
            i += 1

        i = 6
        while i < 9:
            combo = QComboBox()
            combo.addItems([' ', '1', '2', '3'])
            self.NCVtable.setCellWidget(i, 1, combo)
            i += 1

        checkbox = QTableWidgetItem()
        checkbox.setCheckState(Qt.Unchecked)
        self.NCVtable.setItem(0, 1, checkbox)
        self.NCVtable.setItem(10, 1, checkbox)

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
        if index < 15:
            self.StackView.setCurrentIndex(index)
        elif index == 15:
            self.window = FileDirectory()
            self.window.show()


if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    window = Ui()
    application.exec_()
