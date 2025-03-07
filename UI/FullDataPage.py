import sys
import csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir
from UI.ReferencePointPage import ReferencePointPage
from datetime import datetime

class FullDataPage(QWidget):
    def __init__(self, reference_point):
        super().__init__()
        self.setGeometry(1000, 100, 600, 700)
        self.setWindowTitle("Microstrip Patch Antenna Full Data Page")

        self.table = QTableWidget(self)
        self.table.setRowCount(0)
        self.table.setColumnCount(2)
        self.table.setFixedSize(500, 600)
        self.table.move(50,75)
        self.table.setHorizontalHeaderLabels(["Time", "Difference From Reference Point (cm)"])
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 400)

        # Add Export to CSV Button
        self.exportData_btn = QPushButton("Export Data", self)
        self.exportData_btn.setFixedSize(125, 50)
        self.exportData_btn.move(425, 10)
        self.exportData_btn.clicked.connect(self.export_Table)

        # Reference Point Label
        self.currentReferenceLabel = QLabel(f"Current Reference Point: {reference_point} cm", self)
        self.currentReferenceLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.currentReferenceLabel.setFixedSize(275,30)
        self.currentReferenceLabel.move(50,20)

        # self.serial_thread = serial_thread
        # self.serial_thread.data_received.connect(self.update_table)

    def update_table(self, water_level):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count) #Add new row
        self.table.setItem(row_count, 0, QTableWidgetItem(datetime.now().strftime("%H:%M:%S")))
        self.table.setItem(row_count, 1, QTableWidgetItem(str(water_level)))
        self.table.scrollToBottom()

    def open_reference_page(self):
        self.referencepoint_btn = ReferencePointPage()
        self.referencepoint_btn.show()

    # def add_data(self):
    #     mock_data = [
    #         ("12:00", "0"),
    #         ("13:00", "1"),
    #         ("14:00", "0"),
    #         ("15:00", "-1"),
    #         ("16:00", "-2"),
    #     ]

    #     if self.table.rowCount() < len(mock_data):
    #         self.table.setRowCount(len(mock_data))

    #     for row, (time, difference) in enumerate(mock_data):
    #         self.table.setItem(row, 0, QTableWidgetItem(time))
    #         self.table.setItem(row, 1, QTableWidgetItem(difference))

    def export_Table(self):
        path, _= QFileDialog.getSaveFileName(self, 'Save File', QDir.homePath() + "/export.csv", "CSV Files(*.csv *.txt)")
        if path:
            with open(path, 'w') as stream:
                print("saving", path)
                writer = csv.writer(stream, dialect='excel', delimiter= ',')
                headers = []

                for column in range(self.table.columnCount()):
                    header = self.table.horizontalHeaderItem(column)
                    if header:
                        headers.append(header.text())
                    else:
                        headers.append(f"Column {column}")
                writer.writerow(headers)

                for row in range(self.table.rowCount()):
                    rowData = []
                    for column in range(self.table.columnCount()):
                        item = self.table.item(row, column)
                        if item is not None:
                            rowData.append(item.text())
                        else:
                            rowData.append('')
                    writer.writerow(rowData)