import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from UI.HomePage import HomePage

class MainActivity(QMainWindow):
    def __init__(self):
        self.home_page = HomePage()
        self.home_page.show()

app = QApplication(sys.argv)
win = MainActivity()
sys.exit(app.exec_())