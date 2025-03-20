import serial
from PyQt5.QtCore import *

# Define port that is being used
Port_Name = "COM4"
Baud_Rate = 115200

class SerialThread(QObject):
    data_received = pyqtSignal(float)

    def __init__(self):
        super().__init__()
        self.port = Port_Name
        self.baudrate = Baud_Rate
        self.running = True
        self.serial_connection = None

    def run(self):
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=1)
            while self.running:
                data = self.serial_connection.read(4)  # Read 4 bytes (32 bits)
                phase_value = int.from_bytes(data[:2], "big")  # First 16 bits
                gain_value = int.from_bytes(data[2:], "big")  # Last 16 bits

                # Convert to voltage
                phase_voltage = round((phase_value * 3.3) / 4096, 2)
                gain_voltage = round((gain_value * 3.3) / 4096, 2)

                # Emit both values
                self.data_received.emit(phase_voltage)
        except serial.SerialException as e:
            print(f"Serial error: {e}")
        finally:
            if self.serial_connection and self.serial_connection.is_open:
                self.serial_connection.close()

    def map_phase_voltage(self, phase_voltage):
        if 0 <= phase_voltage < 0.5:
            return 0
        elif 0.5 <= phase_voltage < 1.0:
            return 1
        elif 1.0 <= phase_voltage < 1.5:
            return 2
        elif 1.5 <= phase_voltage < 2.0:
            return 3
        elif 2.0 <= phase_voltage < 2.5:
            return 4
        elif 2.5 <= phase_voltage < 3.0:
            return 5
        else:
            return 6
    
    def stop(self):
        self.running = False