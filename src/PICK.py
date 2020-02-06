from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QToolButton, QComboBox, \
    QTableWidget, QTableWidgetItem
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



        self.show()

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
