import serial
from PyQt5.QtCore import *

# Define port that is being used
Port_Name = "COM4"

class SerialThread(QObject):
    data_received = pyqtSignal(float)

    def __init__(self, baudrate=9600):
        super().__init__()
        self.port = Port_Name
        self.baudrate = baudrate
        self.running = True
        self.serial_connection = None

    def run(self):
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=1)
            while self.running:
                value = None  # Ensure `value` is initialized first

                if self.serial_connection.in_waiting > 0:
                    data = self.serial_connection.read(1)  # Read 1 byte
                    value = int.from_bytes(data, "big")  # Convert to integer

                # Ensure value is not None before performing operations on it
                if value is not None and value % 2 == 0:
                    self.data_received.emit(value // 2)  # Send processed data to UI
        except serial.SerialException as e:
            print(f"Serial error: {e}")
        finally:
            if self.serial_connection and self.serial_connection.is_open:
                self.serial_connection.close()
    
    def stop(self):
        self.running = False