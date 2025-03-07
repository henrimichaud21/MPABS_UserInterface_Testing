import serial
from PyQt5.QtCore import *

class SerialThread(QObject):
    data_received = pyqtSignal(int)

    def __init__(self, baudrate=9600):
        super().__init__()
        self.port = "COM4"
        self.baudrate = baudrate
        self.running = True
        self.serial_connection = None

    def run(self):
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout = 1)
            while self.running:
                value = None  # Ensure `value` is initialized first
                if self.serial_connection.in_waiting > 0:
                    data = self.serial_connection.read(1) # read 1 byte
                    value = int.from_bytes(data, "big") # convert to integer
                
                if value is not None and value % 2 == 0:
                    self.data_received.emit(value // 2) #Send processed data to UI
        except serial.SerialException as e:
            print(f"Serial error: {e}")
        finally:
            if self.serial_connection and self.serial_connection.is_open:
                self.serial_connection.close()

    def stop(self):
        self.running = False