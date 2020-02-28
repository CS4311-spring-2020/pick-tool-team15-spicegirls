import sys
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import os

class FileDirectory(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Directory'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.openFileNameDialog()
        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Directory", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileDirectory()
<<<<<<< HEAD
    sys.exit(app.exec_())
=======
    sys.exit(app.exec_())
>>>>>>> 9e2d70b7685dd058071c50a0c837b02923230508
