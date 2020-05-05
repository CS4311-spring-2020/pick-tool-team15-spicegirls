#!/user/bin/python3
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, qApp, QMenu, QLineEdit, QTableWidget, \
    QTableWidgetItem, QComboBox, QGroupBox, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, QDialog, QFileDialog
from PyQt5.uic import loadUi
import os
from filter_configuration import FilterConfig
import setting_view
from export_configuration import ExportConfig
from QGraphViz.QGraphViz import QGraphViz, QGraphVizManipulationMode
from QGraphViz.DotParser import Graph, GraphType
from QGraphViz.Engines import Dot
from pymongo import MongoClient
from vector_db_config import VectorDBConfig
from db_handler import DBHandler
from graph_operations import GraphOperations

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('../ui/MainWindow.ui', self)
        self.myDb = DBHandler()
        self.FilterConfigButton = self.findChild(QPushButton, 'filterButton')
        self.FilterConfigButton.clicked.connect(self.openFilterConfig)
        self.settingsConfig = self.findChild(QAction, 'actionSettings')
        self.settingsConfig.triggered.connect(self.openSettings)

        #Search button functionality ##need to add keyword search still
        self.searchSearchButton = self.findChild(QPushButton, 'searchSearchButton')
        self.searchSearchButton.clicked.connect(self.openFilterConfig)

        # Enter press on qlineedit search tab triggers the search button
        self.searchLineEdit = self.findChild(QLineEdit, 'lineEdit_2')
        self.searchLineEdit.returnPressed.connect(self.searchSearchButton.click)

        # Enter press on qlineedit graph tab triggers search button
        self.graphSearchEdit = self.findChild(QLineEdit, 'graphLineEdit')

        #Exit menu option functionality
        self.CloseMenuSelect = self.findChild(QAction, 'actionClose_Exit')
        self.CloseMenuSelect.setShortcut('Ctrl+Q')
        self.CloseMenuSelect.triggered.connect(qApp.quit)

        #Export menu option functionality
        self.exportConfig = self.findChild(QAction, 'actionExport')
        self.exportConfig.setShortcut('Ctrl+E')
        self.exportConfig.triggered.connect(self.openExportConfig)

        #VectorDBConfig linked to menu option
        self.versionControl = self.findChild(QAction, 'actionVersion_Control')
        self.versionControl.setShortcut('Ctrl+S')
        self.versionControl.triggered.connect(self.openVectDBConfig)

        self.GraphTable = self.findChild(QTableWidget, 'tableWidget')

        self.graphArea = self.findChild(QWidget, 'graphArea')
        self.graphArea.setLayout(QVBoxLayout())

        self.graphSearchButton = self.findChild(QPushButton, 'graphSearchButton_2')

        self.currentVectorMenu = self.findChild(QComboBox, 'VectorMenu')
        self.currentVectorLabel = self.findChild(QLabel, 'CurrentVector')

        self.currentVectorMenu.addItems(self.myDb.get_vector_names())
        self.currentVectorLabel.setText(self.currentVectorMenu.currentText())
        self.currentVectorMenu.activated.connect(self.vectorSelected)

        self.GraphTable.cellClicked.connect()

        # Events
        def node_selected(node):
            if self.qgv.manipulation_mode == QGraphVizManipulationMode.Node_remove_Mode:
                print("Node {} removed".format(node))
                self.saveGraph()
                # self.updateTableFromGraph()
            else:
                print("Node selected {}".format(node))

        def edge_selected(edge):
            if self.qgv.manipulation_mode == QGraphVizManipulationMode.Edge_remove_Mode:
                print("Edge {} removed".format(edge))
            else:
                print("Edge selected {}".format(edge))

        def node_invoked(node):
            print("Node double clicked")

        def edge_invoked(node):
            print("Edge double clicked")

        def node_removed(node):
            print("Node removed")

        def edge_removed(node):
            print("Edge removed")

        # Create QGraphViz widget
        show_subgraphs = True
        self.qgv = QGraphViz(
            show_subgraphs=show_subgraphs,

            node_selected_callback=node_selected,
            edge_selected_callback=edge_selected,
            node_invoked_callback=node_invoked,
            edge_invoked_callback=edge_invoked,
            node_removed_callback=node_removed,
            edge_removed_callback=edge_removed,

            hilight_Nodes=True,
            hilight_Edges=True
        )
        self.qgv.setStyleSheet("background-color:white;")
        # Create A new Graph using Dot layout engine
        self.qgv.new(Dot(Graph("Main_Graph"), show_subgraphs=show_subgraphs))

        # Adding nodes with an image as its shape
        icon_path = os.path.dirname(os.path.abspath(__file__)) + r"\dbicon.png"
        # Build the graph (the layout engine organizes where the nodes and connections are)
        self.qgv.build()
        # Save it to a file to be loaded by Graphviz if needed
        self.qgv.save("test.gv")

        # Add the QGraphViz object to the layout
        self.graphArea.layout().addWidget(self.qgv)

        # Add a horizontal layout (a pannel to select what to do)
        self.hpanel = QHBoxLayout()
        self.graphArea.layout().addLayout(self.hpanel)

        # Add buttons to the panel
        def save():
            fname = QFileDialog.getSaveFileName(self.qgv, "Save", "", "*.json")
            if (fname[0] != ""):
                self.qgv.saveAsJson(fname[0])

        def new():
            self.qgv.engine.graph = Graph("MainGraph")
            self.qgv.build()
            self.qgv.repaint()

        def load():
            fname = QFileDialog.getOpenFileName(self.qgv, "Open", "", "*.json")
            if (fname[0] != ""):
                self.qgv.loadAJson(fname[0])

        def add_node():
            dlg = QDialog()
            dlg.ok = False
            dlg.node_name = ""
            dlg.node_label = ""
            dlg.node_color = ""
            dlg.node_type = "None"
            # Layouts
            main_layout = QVBoxLayout()
            l = QFormLayout()
            buttons_layout = QHBoxLayout()

            main_layout.addLayout(l)
            main_layout.addLayout(buttons_layout)
            dlg.setLayout(main_layout)

            leNodeName = QLineEdit()
            leNodeLabel = QLineEdit()
            cbxNodeType = QComboBox()
            leImagePath = QLineEdit()
            leNodeColor = QLineEdit()

            pbOK = QPushButton()
            pbCancel = QPushButton()

            cbxNodeType.addItems(["None", "circle", "box"])
            pbOK.setText("&OK")
            pbCancel.setText("&Cancel")

            l.setWidget(0, QFormLayout.LabelRole, QLabel("Node Name"))
            l.setWidget(0, QFormLayout.FieldRole, leNodeName)
            l.setWidget(1, QFormLayout.LabelRole, QLabel("Node Label"))
            l.setWidget(1, QFormLayout.FieldRole, leNodeLabel)
            l.setWidget(2, QFormLayout.LabelRole, QLabel("Node Type"))
            l.setWidget(2, QFormLayout.FieldRole, cbxNodeType)
            l.setWidget(3, QFormLayout.LabelRole, QLabel("Node Image"))
            l.setWidget(3, QFormLayout.FieldRole, leImagePath)
            l.setWidget(4, QFormLayout.LabelRole, QLabel("Node Color"))
            l.setWidget(4, QFormLayout.FieldRole, leNodeColor)

            def ok():
                dlg.OK = True
                dlg.node_name = leNodeName.text()
                dlg.node_label = leNodeLabel.text()
                if (leImagePath.text()):
                    dlg.node_type = leImagePath.text()
                else:
                    dlg.node_type = cbxNodeType.currentText()
                dlg.node_color = leNodeColor.text()
                dlg.close()

            def cancel():
                dlg.OK = False
                dlg.close()

            pbOK.clicked.connect(ok)
            pbCancel.clicked.connect(cancel)

            buttons_layout.addWidget(pbOK)
            buttons_layout.addWidget(pbCancel)
            dlg.exec_()

            # node_name, okPressed = QInputDialog.getText(wi, "Node name","Node name:", QLineEdit.Normal, "")
            if dlg.OK and dlg.node_name != '':
                self.qgv.addNode(self.qgv.engine.graph, dlg.node_name, label=dlg.node_label, shape=dlg.node_type, color=dlg.node_color)
                self.qgv.build()

        def remove_node():
            self.qgv.manipulation_mode = QGraphVizManipulationMode.Node_remove_Mode
            for btn in self.buttons_list:
                btn.setChecked(False)
            self.btnRemoveNode.setChecked(True)

        def remove_edge():
            self.qgv.manipulation_mode = QGraphVizManipulationMode.Edge_remove_Mode
            for btn in self.buttons_list:
                btn.setChecked(False)
            self.btnRemoveEdge.setChecked(True)

        def add_edge():
            self.qgv.manipulation_mode = QGraphVizManipulationMode.Edges_Connect_Mode
            for btn in self.buttons_list:
                btn.setChecked(False)
            self.btnAddEdge.setChecked(True)

        # Add buttons
        self.btnNew = QPushButton("New")
        self.btnNew.clicked.connect(new)
        self.btnOpen = QPushButton("Open")
        self.btnOpen.clicked.connect(load)

        self.btnSave = QPushButton("Save")
        self.btnSave.clicked.connect(save)

        self.hpanel.addWidget(self.btnNew)
        self.hpanel.addWidget(self.btnOpen)
        self.hpanel.addWidget(self.btnSave)

        self.buttons_list = []

        self.btnAddNode = QPushButton("Add Node")
        self.btnAddNode.clicked.connect(add_node)
        self.hpanel.addWidget(self.btnAddNode)
        self.buttons_list.append(self.btnAddNode)

        self.btnRemoveNode = QPushButton("Remove Node")
        self.btnRemoveNode.setCheckable(True)
        self.btnRemoveNode.clicked.connect(remove_node)
        self.hpanel.addWidget(self.btnRemoveNode)
        self.buttons_list.append(self.btnRemoveNode)

        self.btnAddEdge = QPushButton("Add Edge")
        self.btnAddEdge.setCheckable(True)
        self.btnAddEdge.clicked.connect(add_edge)
        self.hpanel.addWidget(self.btnAddEdge)
        self.buttons_list.append(self.btnAddEdge)

        self.btnRemoveEdge = QPushButton("Remove Edge")
        self.btnRemoveEdge.setCheckable(True)
        self.btnRemoveEdge.clicked.connect(remove_edge)
        self.hpanel.addWidget(self.btnRemoveEdge)
        self.buttons_list.append(self.btnRemoveEdge)

        #icon_path = os.path.dirname(os.path.abspath(__file__)) + r"\Resouces\IconDir,100,100"
        # n9 = qgv.addNode(qgv.engine.graph, "Node9", label="N9", shape=icon_path)

        #drop down menus vector collumn search table
        self.searchSearchTableWidget = self.findChild(QTableWidget, 'tableWidget_2')
        i = 0
        while i < 10:
            combo = QComboBox()
            combo.addItems([' ', '1', '2', '3'])
            self.searchSearchTableWidget.setCellWidget(i, 3, combo)
            i += 1

        self.showMaximized()
        # DBHandler.create_vector_entry('../Resources/LocalGraphs/VECTOR_3.json')
        self.updateViews()

    def updateViews(self):
        self.generateModels()
        self.populateTable()
        self.populateGraph()

    def openVectDBConfig(self):
        self.window = VectorDBConfig()
        self.window.show()

    def openExportConfig(self):
        self.window = ExportConfig()
        self.window.show()

    def openFilterConfig(self):
        self.window = FilterConfig()
        self.window.show()

    def openSettings(self):
        self.window = setting_view.SettingsWindow()
        self.window.show()

    def vectorSelected(self, index):
        self.currentVectorLabel.setText(self.currentVectorMenu.currentText())
        self.updateViews()

    def populateTable(self):
        self.GraphTable.setRowCount(0)
        vectorList = self.myDb.get_all_vectors_raw()
        i = 0
        for vector in vectorList:
            if vector['name'] == self.currentVectorMenu.currentText():
                for entry in vector['entries']:
                    self.GraphTable.insertRow(i)

                    self.GraphTable.setItem(i, 0, QTableWidgetItem(str(entry['id'])))
                    self.GraphTable.setItem(i, 1, QTableWidgetItem(str(entry['name'])))
                    self.GraphTable.setItem(i, 2, QTableWidgetItem(str(entry['timestamp'])))
                    self.GraphTable.setItem(i, 3, QTableWidgetItem(entry['description']))
                    self.GraphTable.setItem(i, 4, QTableWidgetItem(str(entry['reference'])))
                    self.GraphTable.setItem(i, 5, QTableWidgetItem(str(entry['source'])))
                    i+=1

    def populateGraph(self):
        vectorList = self.myDb.get_all_vectors_raw()
        for vector in vectorList:
            if vector['name'] == self.currentVectorMenu.currentText():
                self.qgv.loadAJson("../Resouces/LocalGraphs/" + vector['name'] + ".json")

    def generateModels(self):
        vectorList = self.myDb.get_all_vectors_raw()
        for vector in vectorList:
            GraphOperations.graph_from_raw_vector(vector)

    # def refreshView(self):    #     self.populateTable()
    #     self.populateGraph()
    #
    # #compares graph to table elements
    # def updateTableFromGraph(self):
    #     client = MongoClient(port=27017)
    #     db = client.business
    #     cursor = db.Vectors.find({})
    #     for vector in cursor:
    #         if vector['name'] == self.currentVectorMenu.currentText():
    #             f = open("../Resouces/LocalGraphs/" + vector['name'] + ".json", "r")
    #             tempFile = f.read()
    #             tempJson = json.loads(tempFile)
    #             f.close
    #             tempSet1 = []
    #             tempSet2 = []
    #             for each in vector['entries']:
    #                 tempSet1.append(str(each['number']))
    #             for each in tempJson['nodes']:
    #                 tempSet2.append(str(each['name']))
    #             listDifference = [item for item in tempSet1 if item not in tempSet2]
    #
    #             tempVector = vector
    #             self.deleteThis(listDifference)
    #             if '_id' in tempVector:
    #                 del tempVector['_id']
    #             i = 0
    #             for entry in tempVector['entries']:
    #                 if int(listDifference) == entry['number']:
    #                     del tempVector['entries'][i]
    #                 i+=1
    #             db.Vectors.insert_one(tempVector)
    #
    # def deleteThis(self, num):
    #     client = MongoClient(port=27017)
    #     db = client.business
    #     db.Vectors.delete_one({'entries.number': int(num)})
    #
    def saveGraph(self):
        self.qgv.saveAsJson("../Resouces/LocalGraphs/" + self.currentVectorMenu.currentText() + ".json")


if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    window = MainWindow()
    application.exec_()
