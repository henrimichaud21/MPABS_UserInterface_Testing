import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class FullDataPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000, 100, 600, 700)
        self.setWindowTitle("Microstrip Patch Antenna Full Data Page")

        self.table = QTableWidget(self)
        self.table.setRowCount(10)
        self.table.setColumnCount(2)
        self.table.setFixedSize(500, 600)
        self.table.move(50,75)
        self.table.setHorizontalHeaderLabels(["Time", "Difference From Reference Point (cm)"])
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 400)