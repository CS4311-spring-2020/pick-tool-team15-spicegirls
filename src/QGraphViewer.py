from PyQt5.QtWidgets import QFileDialog, QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QFormLayout, QComboBox, QPushButton, QInputDialog, QLineEdit, QLabel
import sys
import os
sys.path.insert(1,os.path.dirname(__file__)+"/..")
print(sys.path)
from QGraphViz.QGraphViz import QGraphViz, QGraphVizManipulationMode
from QGraphViz.DotParser import Graph, GraphType
from QGraphViz.Engines import Dot

if __name__ == "__main__":
    # Create QT application
    app = QApplication(sys.argv)
    # Events
    def node_selected(node):
        if(qgv.manipulation_mode==QGraphVizManipulationMode.Node_remove_Mode):
            print("Node {} removed".format(node))
        else:
            print("Node selected {}".format(node))

    def edge_selected(edge):
        if(qgv.manipulation_mode==QGraphVizManipulationMode.Edge_remove_Mode):
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
    show_subgraphs=True
    qgv = QGraphViz(
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
    qgv.setStyleSheet("background-color:white;")
    # Create A new Graph using Dot layout engine
    qgv.new(Dot(Graph("Main_Graph"), show_subgraphs=show_subgraphs))

    # Adding nodes with an image as its shape
    icon_path = os.path.dirname(os.path.abspath(__file__)) + r"\dbicon.png"

    # Build the graph (the layout engine organizes where the nodes and connections are)
    qgv.build()
    # Save it to a file to be loaded by Graphviz if needed
    qgv.save("test.gv")
    # Create a Main window
    w = QMainWindow()
    w.setWindowTitle('Graph')
    # Create a central widget to handle the QGraphViz object
    wi=QWidget()
    wi.setLayout(QVBoxLayout())
    w.setCentralWidget(wi)
    # Add the QGraphViz object to the layout
    wi.layout().addWidget(qgv)
    # Add a horizontal layout (a pannel to select what to do)
    hpanel=QHBoxLayout()
    wi.layout().addLayout(hpanel)
    # Add few buttons to the panel
    def manipulate():
        qgv.manipulation_mode=QGraphVizManipulationMode.Nodes_Move_Mode

    def save():
        fname = QFileDialog.getSaveFileName(qgv, "Save", "", "*.json")
        if(fname[0]!=""):
            qgv.saveAsJson(fname[0])

        
    def new():
        qgv.engine.graph = Graph("MainGraph")
        qgv.build()
        qgv.repaint()

    def load():
        fname = QFileDialog.getOpenFileName(qgv, "Open", "", "*.json")
        if(fname[0]!=""):
            qgv.loadAJson(fname[0])

    def add_node():
        dlg = QDialog()
        dlg.ok=False
        dlg.node_name=""
        dlg.node_label=""
        dlg.node_type="None"
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

        pbOK = QPushButton()
        pbCancel = QPushButton()

        cbxNodeType.addItems(["None","circle","box"])
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

        def ok():
            dlg.OK=True
            dlg.node_name = leNodeName.text()
            dlg.node_label = leNodeLabel.text()
            if(leImagePath.text()): 
                dlg.node_type = leImagePath.text()
            else: 
                dlg.node_type = cbxNodeType.currentText()
            dlg.close()

        def cancel():
            dlg.OK=False
            dlg.close()

        pbOK.clicked.connect(ok)
        pbCancel.clicked.connect(cancel)

        buttons_layout.addWidget(pbOK)
        buttons_layout.addWidget(pbCancel)
        dlg.exec_()

        #node_name, okPressed = QInputDialog.getText(wi, "Node name","Node name:", QLineEdit.Normal, "")
        if dlg.OK and dlg.node_name != '':
                qgv.addNode(qgv.engine.graph, dlg.node_name, label=dlg.node_label, shape=dlg.node_type)
                qgv.build()

    def remove_node():
        qgv.manipulation_mode=QGraphVizManipulationMode.Node_remove_Mode
        for btn in buttons_list:
            btn.setChecked(False)
        btnRemoveNode.setChecked(True)


    def remove_edge():
        qgv.manipulation_mode=QGraphVizManipulationMode.Edge_remove_Mode
        for btn in buttons_list:
            btn.setChecked(False)
        btnRemoveEdge.setChecked(True)

    def add_edge():
        qgv.manipulation_mode=QGraphVizManipulationMode.Edges_Connect_Mode
        for btn in buttons_list:
            btn.setChecked(False)
        btnAddEdge.setChecked(True)

    def add_subgraph():
        dlg = QDialog()
        dlg.ok=False
        dlg.subgraph_name=""
        dlg.subgraph_label=""
        dlg.subgraph_type="None"
        # Layouts
        main_layout = QVBoxLayout()
        l = QFormLayout()
        buttons_layout = QHBoxLayout()

        main_layout.addLayout(l)
        main_layout.addLayout(buttons_layout)
        dlg.setLayout(main_layout)

        leSubgraphName = QLineEdit()
        leSubgraphLabel = QLineEdit()

        pbOK = QPushButton()
        pbCancel = QPushButton()

        pbOK.setText("&OK")
        pbCancel.setText("&Cancel")

        l.setWidget(0, QFormLayout.LabelRole, QLabel("Subgraph Name"))
        l.setWidget(0, QFormLayout.FieldRole, leSubgraphName)
        l.setWidget(1, QFormLayout.LabelRole, QLabel("Subgraph Label"))
        l.setWidget(1, QFormLayout.FieldRole, leSubgraphLabel)
  
        def ok():
            dlg.OK=True
            dlg.subgraph_name = leSubgraphName.text()
            dlg.subgraph_label = leSubgraphLabel.text()
            dlg.close()
    
        def cancel():
            dlg.OK=False
            dlg.close()

        pbOK.clicked.connect(ok)
        pbCancel.clicked.connect(cancel)

        buttons_layout.addWidget(pbOK)
        buttons_layout.addWidget(pbCancel)
        dlg.exec_()

        if dlg.OK and dlg.subgraph_name != '':
                qgv.addSubgraph(qgv.engine.graph, dlg.subgraph_name, subgraph_type= GraphType.SimpleGraph, label=dlg.subgraph_label)
                qgv.build()

    def remove_subgraph():
        qgv.manipulation_mode=QGraphVizManipulationMode.Subgraph_remove_Mode
        for btn in buttons_list:
            btn.setChecked(False)
        btnRemoveSubGraph.setChecked(True)

    # Add buttons                
    btnNew = QPushButton("New")    
    btnNew.clicked.connect(new)
    btnOpen = QPushButton("Open")    
    btnOpen.clicked.connect(load)

    btnSave = QPushButton("Save")    
    btnSave.clicked.connect(save)

    hpanel.addWidget(btnNew)    
    hpanel.addWidget(btnOpen)
    hpanel.addWidget(btnSave)

    buttons_list=[]
    btnManip = QPushButton("Manipulate")    
    btnManip.setCheckable(True)
    btnManip.setChecked(True)
    btnManip.clicked.connect(manipulate)
    hpanel.addWidget(btnManip)
    buttons_list.append(btnManip)

    btnAddNode = QPushButton("Add Node")    
    btnAddNode.clicked.connect(add_node)
    hpanel.addWidget(btnAddNode)
    buttons_list.append(btnManip)

    btnRemoveNode = QPushButton("Remove Node")    
    btnRemoveNode.setCheckable(True)
    btnRemoveNode.clicked.connect(remove_node)
    hpanel.addWidget(btnRemoveNode)
    buttons_list.append(btnRemoveNode)

    btnAddEdge = QPushButton("Add Edge")    
    btnAddEdge.setCheckable(True)
    btnAddEdge.clicked.connect(add_edge)
    hpanel.addWidget(btnAddEdge)
    buttons_list.append(btnAddEdge)

    btnRemoveEdge = QPushButton("Remove Edge")    
    btnRemoveEdge.setCheckable(True)
    btnRemoveEdge.clicked.connect(remove_edge)
    hpanel.addWidget(btnRemoveEdge)
    buttons_list.append(btnRemoveEdge)

    btnAddSubGraph = QPushButton("Add Subgraph")    
    btnAddSubGraph.clicked.connect(add_subgraph)
    hpanel.addWidget(btnAddSubGraph)

    btnRemoveSubGraph = QPushButton("Remove Subgraph")    
    btnRemoveSubGraph.setCheckable(True)
    btnRemoveSubGraph.clicked.connect(remove_subgraph)
    hpanel.addWidget(btnRemoveSubGraph)
    buttons_list.append(btnRemoveSubGraph)

    w.showMaximized()
    
    sys.exit(app.exec_())