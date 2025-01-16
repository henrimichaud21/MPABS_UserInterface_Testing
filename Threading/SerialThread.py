import serial
from PyQt5.QtCore import *

class SerialThread(QObject):
    data_received = pyqtSignal(str)

    def __init__(self, port, baudrate):
        super().__init__()
        self.serial_port = serial.Serial(port, baudrate, timeout = 1)
        self.running = True

    def run(self):
        while self.running:
            if self.serial_port.in_waiting:
                data = self.serial_port.readline().decode('utf-8').strip()
                self.data_received.emit(data)

    def stop(self):
        self.running = False
        self.serial_port.close()