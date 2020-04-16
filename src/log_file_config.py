import os
import shelve
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit
from PyQt5.uic import loadUi


class LogFileConfig(QMainWindow):
    def __init__(self):
        super(LogFileConfig, self).__init__()
        loadUi('../ui/LogFileConfig.ui', self)

        db = shelve.open('../Resouces/ConfigDB/TestConfig')  # Shelve will create data.db
        self.report = db['EAReport']
        db.close()

        self.ValidateButton = self.findChild(QPushButton, 'ValidatePushButton')
        self.ValidateButton.hide()

        self.EARTable = self.findChild(QTableWidget, 'LFC_EAR_tableWidget')
        self.LFGtable = self.findChild(QTableWidget, 'LFT_tableWidget')

        self.EARLineEdit = self.findChild(QLineEdit, 'FileNameLineEdit')

        self.LFGtable.cellClicked.connect(self.showEAReport)

        self.populateLogFileTable()
        self.show()

    def populateLogFileTable(self):
        for i in range(len(self.report)):
            cur = self.report[i]
            self.LFGtable.setItem(i, 0, QTableWidgetItem(os.path.basename(cur['filePath'])))
            self.LFGtable.setItem(i, 1, QTableWidgetItem(os.path.dirname(cur['filePath'])))
            self.LFGtable.setItem(i, 2, QTableWidgetItem("Done"))
            if cur['invalid_timeStamp'] or cur['missing_timeStamp']:
                self.LFGtable.setItem(i, 3, QTableWidgetItem("Action Needed"))
            else:
                self.LFGtable.setItem(i, 3, QTableWidgetItem("Done"))
            #ingestion column
            self.LFGtable.setItem(i, 4, QTableWidgetItem("Pending"))

    def showEAReport(self, row, _):
        self.ValidateButton.show()
        self.EARTable.clearContents()
        if row < len(self.report):
            selected = self.report[row]
            self.EARLineEdit.setText(os.path.basename(selected['filePath']))
            i = 0
            for each in selected['invalid_timeStamp']:
                self.EARTable.setItem(i, 2, QTableWidgetItem(''))

                self.EARTable.setItem(i, 1, QTableWidgetItem("Invalid Timestamp"))
                self.EARTable.setItem(i, 0, QTableWidgetItem(str(each)))
                i += 1
            for each in selected['missing_timeStamp']:
                self.EARTable.setItem(i, 1, QTableWidgetItem("Missing Timestamp"))
                self.EARTable.setItem(i, 0, QTableWidgetItem(str(each)))
                i += 1
        else:
            self.ValidateButton.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = LogFileConfig()
    app.exec_()
