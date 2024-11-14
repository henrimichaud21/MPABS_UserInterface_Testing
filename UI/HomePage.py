import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from UI.FullDataPage import FullDataPage

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
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Grid layout
        grid_layout = QGridLayout(central_widget)

        # Create VBox Layout
        hbox00 = QHBoxLayout()
        hbox01 = QHBoxLayout()

        # Add TextFields
        self.antennaLabel = QLabel("Antenna 1 Status: ", self)
        self.antennaLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.antennaLabel.setFixedSize(200, 30)
        # hbox00.addWidget((self.antennaLabel))

        self.connectionLabel = QLabel("Not Connected", self)
        self.connectionLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.connectionLabel.setFixedSize(200,30)
        self.connectionLabel.move(250,0)
        # grid_layout.addWidget((self.connectionLabel))

        self.solutionLabel = QLabel("Select Solution Type:", self)
        self.solutionLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.solutionLabel.setFixedSize(200,30)
        self.solutionLabel.move(0,30)
        # hbox01.addWidget((self.solutionLabel))

        self.timeLastReadingLabel = QLabel("Time since last reading: xx:xx", self)
        self.timeLastReadingLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.timeLastReadingLabel.setFixedSize(250,30)
        self.timeLastReadingLabel.move(0,120)

        self.valueLastReadingLabel = QLabel("Value of last reading: x cm", self)
        self.valueLastReadingLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.valueLastReadingLabel.setFixedSize(250,30)
        self.valueLastReadingLabel.move(0,150)

        # Add checkbox
        self.connectionCheckbox = QCheckBox("", self)
        self.connectionCheckbox.setFixedSize(30,30)
        self.connectionCheckbox.move(200,0)
        # hbox00.addWidget((self.connectionCheckbox))

        # Check connection
        self.connectionCheckbox.stateChanged.connect(self.check_connection)


        # Add Record Button
        self.record_btn = QPushButton("Start Recording Data", self)
        self.record_btn.setFixedSize(200, 50)
        self.record_btn.move(210, 60)
        # hbox01.addWidget((self.record_btn))
        setup_toggle_button(self.record_btn, "Stop Recording Data", "Start Recording Data")

        # Add View Full Data Button
        self.dataPage_btn = QPushButton("View Full Data", self)
        self.dataPage_btn.setFixedSize(200, 50)
        self.dataPage_btn.move(420, 60)
        # hbox01.addWidget((self.dataPage_btn))
        self.dataPage_btn.clicked.connect(self.open_data_page)


        # Dropdown
        self.solutionDropdown = QComboBox(self)
        self.solutionDropdown.addItems(["Saline Solution", "Distilled Solution", "Tap Solution"])
        self.solutionDropdown.setFixedSize(200, 30)
        self.solutionDropdown.move(0, 60)
        # hbox01.addWidget((self.solutionDropdown))
        # grid_layout.addWidget((self.dropdown), 1, 0)

        # grid_layout.addLayout(hbox00, 0, 0)
        # grid_layout.addLayout(hbox01, 1, 0)

        # central_widget.setLayout(grid_layout)
        # self.setCentralWidget(central_widget)

    def check_connection(self):
        if self.connectionCheckbox.isChecked():
            self.connectionLabel.setText("Connected")
        else:
            self.connectionLabel.setText("Not Connected")
    
    def open_data_page(self):
        self.dataPage_btn = FullDataPage()
        self.dataPage_btn.show()