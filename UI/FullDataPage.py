import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from UI.ReferencePointPage import ReferencePointPage

class FullDataPage(QWidget):
    def __init__(self, reference_point):
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

        # Add data
        self.add_data()

        # Add Export to CSV Button
        self.exportData_btn = QPushButton("Export Data", self)
        self.exportData_btn.setFixedSize(125, 50)
        self.exportData_btn.move(425, 10)
        # hbox01.addWidget((self.dataPage_btn))

        # Enter Reference Point Button
        # self.referencepoint_btn = QPushButton("Enter Reference Point", self)
        # self.referencepoint_btn.setFixedSize(175, 50)
        # self.referencepoint_btn.move(135, 10)
        # self.referencepoint_btn.clicked.connect(self.open_reference_page)

        # Reference Point Label
        self.currentReferenceLabel = QLabel(f"Current Reference Point: {reference_point} cm", self)
        self.currentReferenceLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.currentReferenceLabel.setFixedSize(275,30)
        self.currentReferenceLabel.move(50,20)

    def open_reference_page(self):
        self.referencepoint_btn = ReferencePointPage()
        self.referencepoint_btn.show()

    def add_data(self):
        mock_data = [
            ("12:00", "0"),
            ("13:00", "1"),
            ("14:00", "0"),
            ("15:00", "-1"),
            ("16:00", "-2"),
        ]
        for row, (time, difference) in enumerate(mock_data):
            self.table.setItem(row, 0, QTableWidgetItem(time))
            self.table.setItem(row, 1, QTableWidgetItem(difference))
