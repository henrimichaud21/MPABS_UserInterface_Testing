import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

def setup_toggle_button(button, *other_buttons):
    button.setCheckable(True)

    def toggle_button():
        if button.isChecked():
            button.setStyleSheet("background-color: green")

            for b in other_buttons:
                if b != button:
                    b.setChecked(False)  # Uncheck other buttons
                    b.setStyleSheet("")

    button.clicked.connect(toggle_button)

class MainActivity(QMainWindow):
    def __init__(self):
        # Create Window
        super().__init__()
        self.setGeometry(1200, 300, 750, 750)
        self.setWindowTitle("Microstrip Patch Antenna Home Screen")

        # Add Push Buttons
        self.saline_btn = QPushButton("Saline Solution", self)
        self.saline_btn.setGeometry(100, 100, 150, 50)

        self.distilled_btn = QPushButton("Distilled Solution", self)
        self.distilled_btn.setGeometry(300, 100, 150, 50)

        self.tap_btn = QPushButton("Tap Solution", self)
        self.tap_btn.setGeometry(500, 100, 150, 50)

        # Set up toggle functionality
        setup_toggle_button(self.saline_btn, self.distilled_btn, self.tap_btn)
        setup_toggle_button(self.distilled_btn, self.tap_btn, self.saline_btn)
        setup_toggle_button(self.tap_btn, self.distilled_btn, self.saline_btn)

app = QApplication(sys.argv)
win = MainActivity()
win.show()
sys.exit(app.exec_())