# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pickStartPage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PickMainWindow(object):
    def setupUi(self, PickMainWindow):
        PickMainWindow.setObjectName("PickMainWindow")
        PickMainWindow.resize(1025, 711)
        PickMainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(PickMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(320, 280, 391, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MiddlegridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MiddlegridLayout.setContentsMargins(0, 0, 0, 0)
        self.MiddlegridLayout.setObjectName("MiddlegridLayout")
        self.CreateNew_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CreateNew_pushButton.setObjectName("CreateNew_pushButton")
        self.MiddlegridLayout.addWidget(self.CreateNew_pushButton, 0, 0, 1, 1)
        self.CurrentProject_PushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CurrentProject_PushButton.setObjectName("CurrentProject_PushButton")
        self.MiddlegridLayout.addWidget(self.CurrentProject_PushButton, 1, 0, 1, 1)
        self.ServerOption_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ServerOption_pushButton.setObjectName("ServerOption_pushButton")
        self.MiddlegridLayout.addWidget(self.ServerOption_pushButton, 2, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 1011, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Top_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Top_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_verticalLayout.setObjectName("Top_verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Top_verticalLayout.addItem(spacerItem)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 410, 1011, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.Bottom_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Bottom_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Bottom_verticalLayout.setObjectName("Bottom_verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Bottom_verticalLayout.addItem(spacerItem1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 279, 301, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.Left_horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.Left_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Left_horizontalLayout.setObjectName("Left_horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Left_horizontalLayout.addItem(spacerItem2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(720, 280, 301, 121))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.Right_horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.Right_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Right_horizontalLayout.setObjectName("Right_horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Right_horizontalLayout.addItem(spacerItem3)
        PickMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PickMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1025, 22))
        self.menubar.setObjectName("menubar")
        PickMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PickMainWindow)
        self.statusbar.setObjectName("statusbar")
        PickMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PickMainWindow)
        QtCore.QMetaObject.connectSlotsByName(PickMainWindow)

    def retranslateUi(self, PickMainWindow):
        _translate = QtCore.QCoreApplication.translate
        PickMainWindow.setWindowTitle(_translate("PickMainWindow", "PICK"))
        self.CreateNew_pushButton.setText(_translate("PickMainWindow", "Create New Project"))
        self.CurrentProject_PushButton.setText(_translate("PickMainWindow", "Go To Current Project"))
        self.ServerOption_pushButton.setText(_translate("PickMainWindow", "Server Options"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PickMainWindow = QtWidgets.QMainWindow()
    ui = Ui_PickMainWindow()
    ui.setupUi(PickMainWindow)
    PickMainWindow.show()
    sys.exit(app.exec_())
