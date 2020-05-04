import os
import shutil
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFileDialog, QLabel, QLineEdit
from PyQt5.uic import loadUi


class IconConfig(QWidget):
    def __init__(self):
        super(IconConfig, self).__init__()
        loadUi('../ui/IconWidget.ui', self)

        self.show()
        self.source = ""

        self.sourceLabel = self.findChild(QLabel, 'SourceIconLabel')

        self.nameLineEdit = self.findChild(QLineEdit, 'lineEdit')
        self.nameLineEdit.textChanged.connect(self.syncLineEdit)

        self.AddIconButton = self.findChild(QPushButton, 'IconButton')
        self.AddIconButton.clicked.connect(self.openIconDirectory)

        self.AcceptIconButton = self.findChild(QPushButton, 'acceptButton')
        self.AcceptIconButton.clicked.connect(self.pressedAccept)

        self.CancelIconButton = self.findChild(QPushButton, 'cancelButton')
        self.CancelIconButton.clicked.connect(self.pressedCancel)

        self.AcceptIconButton.hide()

    def setPath(self, msg):
        self.sourceLabel.setText(msg)

    def syncLineEdit(self):
        if self.source:
            self.AcceptIconButton.show()

    def pressedAccept(self):
        if self.source:
            shutil.copy(self.source, '../Resouces/IconDir/' + self.nameLineEdit.text() + os.path.splitext(self.source)[1])
            self.close()

    def pressedCancel(self):
        self.close()

    def openIconDirectory(self):
        temp_dir = QFileDialog.getOpenFileName(self, 'Choose File', "", "Images (*.png *.xpm *.jpg)")
        if temp_dir:
            self.source = temp_dir[0]
            self.sourceLabel.setText(self.source)
            if self.nameLineEdit.text():
                self.AcceptIconButton.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = IconConfig()
    app.exec_()
