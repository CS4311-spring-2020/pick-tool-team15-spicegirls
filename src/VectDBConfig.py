from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VectorDBConfig(object):
    def setupUi(self, VectorDBConfig):
        VectorDBConfig.setObjectName("VectorDBConfig")
        VectorDBConfig.setWindowModality(QtCore.Qt.NonModal)
        VectorDBConfig.resize(1198, 777)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VectorDBConfig.sizePolicy().hasHeightForWidth())
        VectorDBConfig.setSizePolicy(sizePolicy)
        VectorDBConfig.setMinimumSize(QtCore.QSize(400, 220))
        VectorDBConfig.setMouseTracking(False)
        self.gridLayout_2 = QtWidgets.QGridLayout(VectorDBConfig)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.VectorDBConfigGroupBox = QtWidgets.QGroupBox(VectorDBConfig)
        self.VectorDBConfigGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.VectorDBConfigGroupBox.setObjectName("VectorDBConfigGroupBox")
        self.VDBC_ConnectionStatusLabel = QtWidgets.QLabel(self.VectorDBConfigGroupBox)
        self.VDBC_ConnectionStatusLabel.setGeometry(QtCore.QRect(40, 40, 171, 16))
        self.VDBC_ConnectionStatusLabel.setObjectName("VDBC_ConnectionStatusLabel")
        self.VDBC_ConnectionStatusLineEdit = QtWidgets.QLineEdit(self.VectorDBConfigGroupBox)
        self.VDBC_ConnectionStatusLineEdit.setGeometry(QtCore.QRect(230, 40, 891, 21))
        self.VDBC_ConnectionStatusLineEdit.setObjectName("VDBC_ConnectionStatusLineEdit")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.VectorDBConfigGroupBox)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(30, 80, 531, 211))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.VDBC_PulledVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.VDBC_PulledVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.VDBC_PulledVerticalLayout.setObjectName("VDBC_PulledVerticalLayout")
        self.VDBC_PulledGroupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_5)
        self.VDBC_PulledGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.VDBC_PulledGroupBox.setObjectName("VDBC_PulledGroupBox")
        self.VDBC_PulledTableWidget = QtWidgets.QTableWidget(self.VDBC_PulledGroupBox)
        self.VDBC_PulledTableWidget.setGeometry(QtCore.QRect(0, 20, 531, 191))
        self.VDBC_PulledTableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.VDBC_PulledTableWidget.setRowCount(50)
        self.VDBC_PulledTableWidget.setObjectName("VDBC_PulledTableWidget")
        self.VDBC_PulledTableWidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.VDBC_PulledTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_PulledTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_PulledTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_PulledTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(14, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(15, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(16, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(17, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(18, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(19, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(20, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(21, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(22, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(23, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(24, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(25, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(26, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(27, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(28, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(29, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(30, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(31, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(32, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(33, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(34, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(35, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(36, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_PulledTableWidget.setItem(37, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(38, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(39, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(40, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(41, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(42, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(43, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(44, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(45, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(46, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(47, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(48, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PulledTableWidget.setItem(49, 0, item)
        self.VDBC_PulledTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.VDBC_PulledTableWidget.horizontalHeader().setDefaultSectionSize(91)
        self.VDBC_PulledTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.VDBC_PulledTableWidget.horizontalHeader().setStretchLastSection(False)
        self.VDBC_PulledTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.VDBC_PulledTableWidget.verticalHeader().setSortIndicatorShown(False)
        self.VDBC_PulledTableWidget.verticalHeader().setStretchLastSection(False)
        self.VDBC_PulledVerticalLayout.addWidget(self.VDBC_PulledGroupBox)
        self.VDBC_PullButton = QtWidgets.QPushButton(self.VectorDBConfigGroupBox)
        self.VDBC_PullButton.setGeometry(QtCore.QRect(20, 300, 551, 32))
        self.VDBC_PullButton.setObjectName("VDBC_PullButton")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.VectorDBConfigGroupBox)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(590, 80, 531, 211))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.VDBC_PushedVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.VDBC_PushedVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.VDBC_PushedVerticalLayout.setObjectName("VDBC_PushedVerticalLayout")
        self.VDBC_PushedGroupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_6)
        self.VDBC_PushedGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.VDBC_PushedGroupBox.setObjectName("VDBC_PushedGroupBox")
        self.VDBC_PushedTableWidget = QtWidgets.QTableWidget(self.VDBC_PushedGroupBox)
        self.VDBC_PushedTableWidget.setGeometry(QtCore.QRect(0, 20, 531, 191))
        self.VDBC_PushedTableWidget.setRowCount(50)
        self.VDBC_PushedTableWidget.setObjectName("VDBC_PushedTableWidget")
        self.VDBC_PushedTableWidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_PushedTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_PushedTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_PushedTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_PushedTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(14, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(15, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(16, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(17, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(18, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(19, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(20, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(21, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(22, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(23, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(24, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(25, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(26, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(27, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(28, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(29, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(30, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(31, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(32, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(33, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(34, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(35, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(36, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(37, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(38, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(39, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(40, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(41, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(42, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(43, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(44, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(45, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(46, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(47, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(48, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_PushedTableWidget.setItem(49, 0, item)
        self.VDBC_PushedTableWidget.horizontalHeader().setDefaultSectionSize(96)
        self.VDBC_PushedVerticalLayout.addWidget(self.VDBC_PushedGroupBox)
        self.VDBC_PushButton = QtWidgets.QPushButton(self.VectorDBConfigGroupBox)
        self.VDBC_PushButton.setGeometry(QtCore.QRect(580, 300, 551, 32))
        self.VDBC_PushButton.setObjectName("VDBC_PushButton")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.VectorDBConfigGroupBox)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 340, 1101, 331))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.VDBC_ApprovalSyncVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.VDBC_ApprovalSyncVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.VDBC_ApprovalSyncVerticalLayout.setObjectName("VDBC_ApprovalSyncVerticalLayout")
        self.VDBC_ApprovalSyncGroupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_7)
        self.VDBC_ApprovalSyncGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.VDBC_ApprovalSyncGroupBox.setObjectName("VDBC_ApprovalSyncGroupBox")
        self.VDBC_AS_TableWidget_2 = QtWidgets.QTableWidget(self.VDBC_ApprovalSyncGroupBox)
        self.VDBC_AS_TableWidget_2.setGeometry(QtCore.QRect(0, 20, 1101, 311))
        self.VDBC_AS_TableWidget_2.setRowCount(50)
        self.VDBC_AS_TableWidget_2.setObjectName("VDBC_AS_TableWidget_2")
        self.VDBC_AS_TableWidget_2.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_AS_TableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_AS_TableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_AS_TableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_AS_TableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_AS_TableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_AS_TableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_AS_TableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.VDBC_AS_TableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_AS_TableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_AS_TableWidget_2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.VDBC_AS_TableWidget_2.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(14, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(15, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(16, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(17, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(18, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(19, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(20, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(21, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(22, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(23, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(24, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(25, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(26, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(27, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(28, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(29, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(30, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(31, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(32, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(33, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(34, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(35, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(36, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(37, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(38, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(39, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(40, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(41, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(42, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(43, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(44, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(45, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(46, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(47, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(48, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.VDBC_AS_TableWidget_2.setItem(49, 0, item)
        self.VDBC_AS_TableWidget_2.horizontalHeader().setDefaultSectionSize(101)
        self.VDBC_ApprovalSyncVerticalLayout.addWidget(self.VDBC_ApprovalSyncGroupBox)
        self.VDBC_CommitButton = QtWidgets.QPushButton(self.VectorDBConfigGroupBox)
        self.VDBC_CommitButton.setGeometry(QtCore.QRect(10, 680, 1121, 32))
        self.VDBC_CommitButton.setObjectName("VDBC_CommitButton")
        self.verticalLayout.addWidget(self.VectorDBConfigGroupBox)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 2, 1, 1)

        self.retranslateUi(VectorDBConfig)
        QtCore.QMetaObject.connectSlotsByName(VectorDBConfig)

    def retranslateUi(self, VectorDBConfig):
        _translate = QtCore.QCoreApplication.translate
        VectorDBConfig.setWindowTitle(_translate("VectorDBConfig", "Vector DB Configuration"))
        self.VectorDBConfigGroupBox.setTitle(_translate("VectorDBConfig", "Vector DB configuration"))
        self.VDBC_ConnectionStatusLabel.setText(_translate("VectorDBConfig", "Connection status to lead:"))
        self.VDBC_PulledGroupBox.setTitle(_translate("VectorDBConfig", "Pulled vector DB table (Analyst)"))
        self.VDBC_PulledTableWidget.setSortingEnabled(True)
        item = self.VDBC_PulledTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("VectorDBConfig", "Vector"))
        item = self.VDBC_PulledTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("VectorDBConfig", "Description"))
        item = self.VDBC_PulledTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("VectorDBConfig", "Graph"))
        __sortingEnabled = self.VDBC_PulledTableWidget.isSortingEnabled()
        self.VDBC_PulledTableWidget.setSortingEnabled(False)
        self.VDBC_PulledTableWidget.setSortingEnabled(__sortingEnabled)
        self.VDBC_PullButton.setText(_translate("VectorDBConfig", "Pull"))
        self.VDBC_PushedGroupBox.setTitle(_translate("VectorDBConfig", "Pushed vector DB table (Analyst)"))
        self.VDBC_PushedTableWidget.setSortingEnabled(True)
        item = self.VDBC_PushedTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("VectorDBConfig", "Vector"))
        item = self.VDBC_PushedTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("VectorDBConfig", "Description"))
        item = self.VDBC_PushedTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("VectorDBConfig", "Graph"))
        __sortingEnabled = self.VDBC_PushedTableWidget.isSortingEnabled()
        self.VDBC_PushedTableWidget.setSortingEnabled(False)
        self.VDBC_PushedTableWidget.setSortingEnabled(__sortingEnabled)
        self.VDBC_PushButton.setText(_translate("VectorDBConfig", "Push"))
        self.VDBC_ApprovalSyncGroupBox.setTitle(_translate("VectorDBConfig", "Approval sync:"))
        self.VDBC_AS_TableWidget_2.setSortingEnabled(True)
        item = self.VDBC_AS_TableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("VectorDBConfig", "Source IP"))
        item = self.VDBC_AS_TableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("VectorDBConfig", "Request timestamp"))
        item = self.VDBC_AS_TableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("VectorDBConfig", "Vector"))
        item = self.VDBC_AS_TableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("VectorDBConfig", "Description"))
        item = self.VDBC_AS_TableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("VectorDBConfig", "Graph"))
        item = self.VDBC_AS_TableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("VectorDBConfig", "Change summary"))
        item = self.VDBC_AS_TableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("VectorDBConfig", "Sync status"))
        __sortingEnabled = self.VDBC_AS_TableWidget_2.isSortingEnabled()
        self.VDBC_AS_TableWidget_2.setSortingEnabled(False)
        self.VDBC_AS_TableWidget_2.setSortingEnabled(__sortingEnabled)
        self.VDBC_CommitButton.setText(_translate("VectorDBConfig", "Commit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VectorDBConfig = QtWidgets.QWidget()
    ui = Ui_VectorDBConfig()
    ui.setupUi(VectorDBConfig)
    VectorDBConfig.show()
    sys.exit(app.exec_())