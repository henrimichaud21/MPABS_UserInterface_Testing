import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(1200, 300, 750, 750)
    win.setWindowTitle("Microstrip Patch Atenna Data")
    win.show()
    sys.exit(app.exec_())

window()