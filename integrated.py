from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class DeadlockGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Deadlock Detection and Removal")
        self.setGeometry(100, 100, 900, 700)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.label = QLabel("Process-Resource Allocation Table")
        self.label.setFont(QFont("Arial", 14))
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
        
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Process", "Resource", "Allocated"])
        self.table.itemChanged.connect(self.update_system)  # Real-time update
        self.layout.addWidget(self.table)
        
        self.add_row_button = QPushButton("Add Row")
        self.add_row_button.clicked.connect(self.add_row)
        self.layout.addWidget(self.add_row_button)
        
        self.detect_button = QPushButton("Detect Deadlock")
        self.detect_button.clicked.connect(self.detect_deadlock)
        self.layout.addWidget(self.detect_button)
        
        self.remove_button = QPushButton("Remove Deadlock")
        self.remove_button.clicked.connect(self.remove_deadlock)
        self.layout.addWidget(self.remove_button)
        self.remove_button.setEnabled(False)
        
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        
        self.graph = nx.DiGraph()
        self.wait_for_graph = nx.DiGraph()
        self.deadlock_cycles = []
    
    def add_row(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
    
    def update_system(self):
        self.detect_deadlock()
    
    def detect_deadlock(self):
        self.graph.clear()
        self.wait_for_graph.clear()
        
        allocation_map = {}
        
        for row in range(self.table.rowCount()):
            process_item = self.table.item(row, 0)
            resource_item = self.table.item(row, 1)
            allocated_item = self.table.item(row, 2)
            
            if process_item and resource_item and allocated_item:
                process = process_item.text().strip()
                resource = resource_item.text().strip()
                allocated = allocated_item.text().strip()
                
                if allocated.lower() == "yes":
                    self.graph.add_edge(resource, process)
                    allocation_map[resource] = process  
                else:
                    self.graph.add_edge(process, resource)
        
        for process, resource in self.graph.edges():
            if resource in allocation_map:
                allocated_process = allocation_map[resource]
                self.wait_for_graph.add_edge(process, allocated_process)
        
        self.deadlock_cycles = list(nx.simple_cycles(self.wait_for_graph))
        self.update_graph_visualization()
        
        if self.deadlock_cycles:
            self.remove_button.setEnabled(True)
        else:
            self.remove_button.setEnabled(False)
    
    def remove_deadlock(self):
        if self.deadlock_cycles:
            for cycle in self.deadlock_cycles:
                process_to_remove = cycle[0]
                self.remove_process_from_table(process_to_remove)
                self.wait_for_graph.remove_node(process_to_remove)
            
            self.deadlock_cycles = []
            self.update_graph_visualization()
            self.remove_button.setEnabled(False)
    
    def remove_process_from_table(self, process):
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 0)
            if item and item.text().strip() == process:
                self.table.removeRow(row)
                break
    
    def update_graph_visualization(self):
        self.ax.clear()
        pos = nx.spring_layout(self.wait_for_graph)
        nx.draw(self.wait_for_graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', ax=self.ax)
        
        if self.deadlock_cycles:
            deadlocked_nodes = set(node for cycle in self.deadlock_cycles for node in cycle)
            nx.draw_networkx_nodes(self.wait_for_graph, pos, nodelist=deadlocked_nodes, node_color='red', ax=self.ax)
        
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DeadlockGUI()
    window.show()
    sys.exit(app.exec_())
