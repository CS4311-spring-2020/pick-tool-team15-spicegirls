import sys
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


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
        fileName = str(QFileDialog.getExistingDirectory(self,"Directory"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = app()
    sys.exit(app.exec_())