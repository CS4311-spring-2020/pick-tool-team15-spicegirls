import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUi


class LogFileConfig(QMainWindow):
    def __init__(self):
        super(LogFileConfig, self).__init__()
        loadUi('../ui/LogFileConfig.ui', self)

        # log file configuration table checkboxes
        self.LFGtable = self.findChild(QTableWidget, 'LFT_tableWidget')
        i = 0
        while i < 50:
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            self.LFGtable.setItem(i, 5, checkbox)
            i += 1

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = LogFileConfig()
    app.exec_()
