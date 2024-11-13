import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

def setup_toggle_button(button, phrase1, phrase2):
    button.setCheckable(True)

    def toggle_button():
        if button.isChecked():
            button.setStyleSheet("background-color: green")
            button.setText(phrase1)

        else:
            button.setChecked(False)
            button.setStyleSheet("")
            button.setText(phrase2)

    button.clicked.connect(toggle_button)

class HomePage(QMainWindow):
    def __init__(self):
        # Create Window
        super().__init__()
        self.setGeometry(1200, 300, 750, 750)
        self.setWindowTitle("Microstrip Patch Antenna Home Screen")

        # Create grid layout, row position, column position
        grid_layout = QGridLayout()
        central_widget = QWidget(self)

        # Add TextFields
        self.antennaLabel = QLabel("Antenna 1 Status: ", self)
        self.antennaLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.antennaLabel.setFixedSize(200, 30)

        self.solutionLabel = QLabel("Select Solution Type:", self)
        self.solutionLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.solutionLabel.setFixedSize(200,30)
        self.solutionLabel.move(0,30)

        self.connectionLabel = QLabel("Not Connected", self)
        self.connectionLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.connectionLabel.setFixedSize(200,30)
        self.connectionLabel.move(250,0)


        # Add checkbox
        self.connectionCheckbox = QCheckBox("", self)
        self.connectionCheckbox.setFixedSize(30,30)
        self.connectionCheckbox.move(200,0)

        # Check connection
        self.connectionCheckbox.stateChanged.connect(self.check_connection)


        # Add Push Buttons
        self.record_btn = QPushButton("Start Recording Data", self)
        self.record_btn.setFixedSize(200, 50)
        self.record_btn.move(210, 60)
        setup_toggle_button(self.record_btn, "Stop Recording Data", "Start Recording Data")

        self.solutionDropdown = QComboBox(self)
        self.solutionDropdown.addItems(["Saline Solution", "Distilled Solution", "Tap Solution"])
        self.solutionDropdown.setFixedSize(200, 30)
        self.solutionDropdown.move(0, 60)
        # grid_layout.addWidget((self.dropdown), 1, 0)

        # central_widget.setLayout(grid_layout)
        # self.setCentralWidget(central_widget)

    def check_connection(self):
        if self.connectionCheckbox.isChecked():
            self.connectionLabel.setText("Connected")
        else:
            self.connectionLabel.setText("Not Connected")