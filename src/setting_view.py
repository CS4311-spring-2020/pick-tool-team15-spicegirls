from os import listdir
from os.path import isdir

from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QToolButton, QTableWidget, \
    QTableWidgetItem, QLabel, QLineEdit, QFileDialog, QWidget, QMessageBox
from PyQt5.uic import loadUi
import os
import main_window
import shelve
from os.path import isfile, join
import shutil
from Validate import Validator
from cleansing import Cleanser
from audio_transcription import AudioTranscription
from image_transcribe import ImageTranscription
import socket

class SettingsWindow(QMainWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        loadUi('../ui/SettingView.ui', self)

        self.root_dir, self.red_dir, self.blue_dir, self.white_dir = '','','',''

        self.myValidator = Validator('s', 'q')
        # self.configDB = shelve.open('../Resouces/ConfigDB/TestConfig')  # Initialize values to avoid e
        # self.configDB.close()

        self.mainStackedView = self.findChild(QStackedWidget, 'StackView')
        
        self.OV_TeamConfigButton = self.findChild(QPushButton, 'OV_TeamConfigButton')
        self.OV_EventConfigButton = self.findChild(QPushButton, 'OV_EventConfigButton')
        self.OV_DirectoryConfigButton = self.findChild(QPushButton, 'OV_DirectoryConfigButton')
        self.OV_VectorConfigButton = self.findChild(QPushButton, 'OV_VectorConfigButton')
        self.OV_IconConfigButton = self.findChild(QPushButton, 'OV_IconConfigButton')

        self.SaveEventConfig = self.findChild(QPushButton, 'SaveEventPushButton')

        self.LeadCheckBox = self.findChild(QCheckBox, 'LeadCheckBox')
        self.LeadCheckBox.toggle()
        self.LeadCheckBox.stateChanged.connect(self.LeadCheckBoxClicked)
        self.NoConnections = self.findChild(QLineEdit, 'NoOfConnectionslineEdit')
        self.IPAddress = self.findChild(QLineEdit, "IPAddressLineEdit")
        hostname = socket.gethostname()
        self.IPAddress.setText(socket.gethostbyname(hostname))

        self.ENLineEdit = self.findChild(QLineEdit, 'EventNameLineEdit')  # This goes to test persistence db
        self.EDLineEdit = self.findChild(QLineEdit, 'EventDescriptionLineEdit')
        self.ESLineEdit = self.findChild(QLineEdit, 'EventStartLineEdit')
        self.EELineEdit = self.findChild(QLineEdit, 'EventEndLineEdit')

        self.rootLE = self.findChild(QLineEdit, 'RootDirectoryLineEdit')
        self.redLE = self.findChild(QLineEdit, 'RedTeamLineEdit')
        self.blueLE = self.findChild(QLineEdit, 'BlueTeamLineEdit')
        self.whiteLE = self.findChild(QLineEdit, 'WhiteTeamLineEdit')

        self.configDB = shelve.open('../Resouces/ConfigDB/TestConfig')
        # Internal project settings display for line edits
        self.ENLineEdit.setText(self.configDB['EventName'])
        self.EDLineEdit.setText(self.configDB['EventDescription'])
        self.ESLineEdit.setText(self.configDB['EventStartTime'])
        self.EELineEdit.setText(self.configDB['EventEndTime'])
        self.rootLE.setText(self.configDB['root_dir'])
        self.redLE.setText(self.configDB['red_dir'])
        self.blueLE.setText(self.configDB['blue_dir'])
        self.whiteLE.setText(self.configDB['white_dir'])
        self.configDB.close()

        self.rootLE.textChanged.connect(self.updateDirLE)
        self.redLE.textChanged.connect(self.updateDirLE)
        self.blueLE.textChanged.connect(self.updateDirLE)
        self.whiteLE.textChanged.connect(self.updateDirLE)

        self.rootLE.editingFinished.connect(lambda: self.finishedEditingDirLE('root_dir'))
        self.redLE.editingFinished.connect(lambda: self.finishedEditingDirLE('red_dir'))
        self.blueLE.editingFinished.connect(lambda: self.finishedEditingDirLE('blue_dir'))
        self.whiteLE.editingFinished.connect(lambda: self.finishedEditingDirLE('white_dir'))

        self.ENLineEdit.textChanged.connect(self.updateED)
        self.EDLineEdit.textChanged.connect(self.updateED)
        self.ESLineEdit.textChanged.connect(self.updateED)
        self.EELineEdit.textChanged.connect(self.updateED)

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

        self.StartIngestionB = self.findChild(QPushButton, 'StartIngestionPushButton')
        self.StartIngestionB.clicked.connect(self.startIngestion)

        self.completeSettings = self.findChild(QPushButton, 'completeSetupButton_pushButton')
        self.completeSettings.clicked.connect(self.openMain)

        self.pBar = self.findChild(QWidget, 'progressBar')


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

    def validateIP(self):
        try:
            socket.inet_aton(self.IPAddress.text())
            # legal
        except socket.error:
            error_dialog = QErrorMessage()
            error_dialog.showMessage('Not A Valid IP Address')

            #error_dialog.exec_()

    def LeadCheckBoxClicked(self):
        if self.IPAddress.isVisible:
            self.IPAddress.setEnabled(1)
        else:
            self.IPAddress.setDisabled(1)

    def connectButtonClicked(self):
        if self.connectButton.text() == 'Disconnect':
            self.validateIP
            self.connectButton.setText('Connect')
            self.NoConnections.setText('0')
            self.connectStatus.setText('Not Connected')
        else:
            self.NoConnections.setText('1')
            self.connectStatus.setText('Connected')
            self.connectButton.setText('Disconnect')

    def btn(self, index):
        if index < 5:
            self.StackView.setCurrentIndex(index)

    def setDir(self, index):
        flag = True
        while flag:
            temp_dir = QFileDialog.getExistingDirectory(self, 'Choose Directory', "", QFileDialog.ShowDirsOnly)
            if temp_dir == self.root_dir or temp_dir == self.red_dir or temp_dir == self.blue_dir or temp_dir == self.white_dir:
                if temp_dir == '':
                    break
                retry = QMessageBox.question(self, 'Error - Invalid directory',
                                           "The directory: {} has already been used".format(temp_dir),
                                           QMessageBox.Retry | QMessageBox.Cancel, QMessageBox.Cancel)
                if retry == QMessageBox.Cancel:
                    flag = False
            else:
                self.configDB = shelve.open('../Resouces/ConfigDB/TestConfig')
                if index == 0:
                    self.RootLineEdit.setText(str(temp_dir))
                    self.configDB['root_dir'] = temp_dir
                    self.root_dir = temp_dir
                elif index == 1:
                    self.RedTeamLineEdit.setText(str(temp_dir))
                    self.red_dir = temp_dir
                elif index == 2:
                    self.BlueTeamLineEdit.setText(str(temp_dir))
                    self.blue_dir = temp_dir
                elif index == 3:
                    self.WhiteTeamLineEdit.setText(str(temp_dir))
                    self.white_dir = temp_dir
                self.configDB.close()
                flag = False

    def updateED(self):
        db = shelve.open('../Resouces/ConfigDB/TestConfig')  # Shelve will create data.db
        db['EventName'] = self.ENLineEdit.text()
        db['EventDescription'] = self.EDLineEdit.text()
        db['EventStartTime'] = self.ESLineEdit.text()
        db['EventEndTime'] = self.EELineEdit.text()
        db.close()

    def updateDirLE(self):
        db = shelve.open('../Resouces/ConfigDB/TestConfig')  # Shelve will create data.db
        db['root_dir'] = self.rootLE.text()
        db['red_dir'] = self.redLE.text()
        db['blue_dir'] = self.blueLE.text()
        db['white_dir'] = self.whiteLE.text()
        db.close()

    def finishedEditingDirLE(self, dir):
        self.configDB = shelve.open('../Resouces/ConfigDB/TestConfig')
        # if not isdir(self.configDB[dir]):
        # QMessageBox.question(self, 'Error - Invalid directory', "The directory: {} is not valid.".format(dir), QMessageBox.Ok)
        self.configDB.close()

    def startCleanse(self):
        db = shelve.open('../Resouces/ConfigDB/TestConfig')  # Shelve will create data.db
        dirList = [db['red_dir'], db['blue_dir'], db['white_dir']]
        db.close()
        myCleanser = Cleanser
        for dir in dirList:
            if isdir(dir):
                allCurDirFiles = [f for f in listdir(dir) if isfile(join(dir, f))]
                for eachFile in allCurDirFiles:
                    extension = os.path.splitext(eachFile)[1]
                    if extension == '.txt' or extension == '.log':
                        eachFile = dir + "/" + eachFile
                        myCleanser.cleanse(eachFile)

    def startAudioTranscription(self):
        db = shelve.open('../Resouces/ConfigDB/TestConfig')  # Shelve will create data.db
        dirList = [db['red_dir'], db['blue_dir'], db['white_dir']]
        db.close()
        myTranscriber = AudioTranscription
        for dir in dirList:
            if isdir(dir):
                allCurDirFiles = [f for f in listdir(dir) if isfile(join(dir, f))]
                for fileName in allCurDirFiles:
                    extension = os.path.splitext(fileName)[1]
                    if extension == '.wav' or extension == '.mp3':
                        myTranscriber.transcribeAudio(fileName, dir)

    def startImageTranscription(self):
        db = shelve.open('../Resouces/ConfigDB/TestConfig')  # Shelve will create data.db
        dirList = [db['red_dir'], db['blue_dir'], db['white_dir']]
        db.close()
        myImageTranscriber = ImageTranscription
        for dir in dirList:
            if isdir(dir):
                allCurDirFiles = [f for f in listdir(dir) if isfile(join(dir, f))]
                for fileName in allCurDirFiles:
                    extension = os.path.splitext(fileName)[1]
                    if extension == '.png' or extension == '.jpeg':
                        myImageTranscriber.transcribeAudio(fileName, dir)

    def startValidation(self):
        db = shelve.open('../Resouces/ConfigDB/TestConfig')  # Shelve will create data.db
        dirList = [db['red_dir'], db['blue_dir'], db['white_dir']]
        db.close()
        for dir in dirList:
            if isdir(dir):
                allCurDirFiles = [f for f in listdir(dir) if isfile(join(dir, f))]
                for fileName in allCurDirFiles:
                    fileName = dir + "/" + fileName
                    self.myValidator.validate(fileName)

    def organizeDirectories(self):
        db = shelve.open('../Resouces/ConfigDB/TestConfig')  # Shelve will create data.db
        dirList = [db['red_dir'], db['blue_dir'], db['white_dir']]
        db.close()
        for dir in dirList:
            if isdir(dir):
                allCurDirFiles = [f for f in listdir(dir) if isfile(join(dir, f))]
                for fileName in allCurDirFiles:
                    dest = dir + '/' + 'raw_files'
                    if not os.path.exists(dest):
                        os.makedirs(dest)
                    extension = os.path.splitext(fileName)[1]
                    if extension == '.png' or extension == '.jpeg' or extension == '.wav' or extension == '.mp3':
                    # fileName = dir + "/" + fileName
                        shutil.move(dir + '/' + fileName, dest)

    def startIngestion(self):
        self.startAudioTranscription()
        # self.startImageTranscription()
        self.organizeDirectories()
        self.startCleanse()
        self.startValidation()
        db = shelve.open('../Resouces/ConfigDB/TestConfig')  # Shelve will create data.db
        db['EAReport'] = self.myValidator.getEnforcementReport()
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