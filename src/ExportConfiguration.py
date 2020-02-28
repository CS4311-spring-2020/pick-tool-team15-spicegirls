from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExportConfiguration(object):
    def setupUi(self, ExportConfiguration):
        ExportConfiguration.setObjectName("ExportConfiguration")
        ExportConfiguration.setWindowModality(QtCore.Qt.NonModal)
        ExportConfiguration.resize(400, 220)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ExportConfiguration.sizePolicy().hasHeightForWidth())
        ExportConfiguration.setSizePolicy(sizePolicy)
        ExportConfiguration.setMinimumSize(QtCore.QSize(400, 220))
        ExportConfiguration.setMouseTracking(False)
        self.gridLayout_2 = QtWidgets.QGridLayout(ExportConfiguration)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.EC_ExportPushButton = QtWidgets.QPushButton(ExportConfiguration)
        self.EC_ExportPushButton.setObjectName("EC_ExportPushButton")
        self.gridLayout_2.addWidget(self.EC_ExportPushButton, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.ExportFormatLabel = QtWidgets.QLabel(ExportConfiguration)
        self.ExportFormatLabel.setObjectName("ExportFormatLabel")
        self.gridLayout.addWidget(self.ExportFormatLabel, 1, 0, 1, 1)
        self.EC_ExportFormatDropDown = QtWidgets.QFontComboBox(ExportConfiguration)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EC_ExportFormatDropDown.sizePolicy().hasHeightForWidth())
        self.EC_ExportFormatDropDown.setSizePolicy(sizePolicy)
        self.EC_ExportFormatDropDown.setFocusPolicy(QtCore.Qt.TabFocus)
        self.EC_ExportFormatDropDown.setCurrentText("")
        self.EC_ExportFormatDropDown.setObjectName("EC_ExportFormatDropDown")
        self.gridLayout.addWidget(self.EC_ExportFormatDropDown, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 1, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 2, 0, 1, 1)

        self.retranslateUi(ExportConfiguration)
        QtCore.QMetaObject.connectSlotsByName(ExportConfiguration)

    def retranslateUi(self, ExportConfiguration):
        _translate = QtCore.QCoreApplication.translate
        ExportConfiguration.setWindowTitle(_translate("ExportConfiguration", "Export Configuration"))
        self.EC_ExportPushButton.setText(_translate("ExportConfiguration", "Export"))
        self.ExportFormatLabel.setText(_translate("ExportConfiguration", "Export format:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExportConfiguration = QtWidgets.QWidget()
    ui = Ui_ExportConfiguration()
    ui.setupUi(ExportConfiguration)
    ExportConfiguration.show()
    sys.exit(app.exec_())
