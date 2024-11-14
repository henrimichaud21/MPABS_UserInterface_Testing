from PyQt5.QtWidgets import QMainWindow, QLabel


class FullDataPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Full Data Page")

        # Example content for the new page
        self.label = QLabel("Welcome to the Full Data Page", self)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.move(150, 180)