<<<<<<< HEAD
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FilterConfiguration.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


=======
>>>>>>> fcd20638fc56508546d4085dee92f9cab645d810
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FilterConfiguration(object):
    def setupUi(self, FilterConfiguration):
        FilterConfiguration.setObjectName("FilterConfiguration")
        FilterConfiguration.setWindowModality(QtCore.Qt.NonModal)
        FilterConfiguration.resize(400, 220)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FilterConfiguration.sizePolicy().hasHeightForWidth())
        FilterConfiguration.setSizePolicy(sizePolicy)
        FilterConfiguration.setMinimumSize(QtCore.QSize(400, 220))
        FilterConfiguration.setMouseTracking(False)
        self.gridLayout_2 = QtWidgets.QGridLayout(FilterConfiguration)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(FilterConfiguration)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(FilterConfiguration)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(FilterConfiguration)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_4 = QtWidgets.QCheckBox(FilterConfiguration)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(FilterConfiguration)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(FilterConfiguration)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout.addWidget(self.checkBox_6)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(FilterConfiguration)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(FilterConfiguration)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(FilterConfiguration)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(FilterConfiguration)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 3, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(FilterConfiguration)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(FilterConfiguration)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(FilterConfiguration)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout.addWidget(self.dateTimeEdit_2, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(FilterConfiguration)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.applyButton = QtWidgets.QPushButton(FilterConfiguration)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applyButton.sizePolicy().hasHeightForWidth())
        self.applyButton.setSizePolicy(sizePolicy)
        self.applyButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.applyButton.setObjectName("applyButton")
        self.gridLayout.addWidget(self.applyButton, 6, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 7)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(FilterConfiguration)
        QtCore.QMetaObject.connectSlotsByName(FilterConfiguration)

    def retranslateUi(self, FilterConfiguration):
        _translate = QtCore.QCoreApplication.translate
        FilterConfiguration.setWindowTitle(_translate("FilterConfiguration", "Form"))
        self.checkBox.setText(_translate("FilterConfiguration", "Red"))
        self.checkBox_2.setText(_translate("FilterConfiguration", "Blue"))
        self.checkBox_3.setText(_translate("FilterConfiguration", "White"))
        self.checkBox_4.setText(_translate("FilterConfiguration", "Red"))
        self.checkBox_5.setText(_translate("FilterConfiguration", "Blue"))
        self.checkBox_6.setText(_translate("FilterConfiguration", "White"))
        self.label_2.setText(_translate("FilterConfiguration", "Event type:"))
        self.label_5.setText(_translate("FilterConfiguration", "End timestamp:"))
        self.label.setText(_translate("FilterConfiguration", "Creator:"))
        self.label_3.setText(_translate("FilterConfiguration", "Start timestamp:"))
        self.label_4.setText(_translate("FilterConfiguration", "Keyword search:"))
        self.applyButton.setText(_translate("FilterConfiguration", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FilterConfiguration = QtWidgets.QWidget()
    ui = Ui_FilterConfiguration()
    ui.setupUi(FilterConfiguration)
    FilterConfiguration.show()
    sys.exit(app.exec_())
