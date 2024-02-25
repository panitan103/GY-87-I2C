import smbus
import time

class BMP085:
    def __init__(self,address=0x77,bus=1):
        # BMP085 address
        self.address = 0x77

        # Register addresses
        self.calibration_data = [0xAA, 0xAC, 0xAE, 0xB0, 0xB2, 0xB4, 0xB6, 0xB8, 0xBA, 0xBC, 0xBE, 0xC0, 0xC2, 0xC4, 0xC6, 0xC8, 0xCA, 0xCC, 0xCE, 0xD0, 0xD2, 0xD4, 0xD6, 0xD8, 0xDA, 0xDC, 0xDE, 0xE0, 0xE2, 0xE4, 0xE6, 0xE8, 0xEA, 0xEC, 0xEE, 0xF0, 0xF2, 0xF4, 0xF6, 0xF8, 0xFA, 0xFC, 0xFE]

        # Open I2C bus
        self.bus = smbus.SMBus(1)

    # Read calibration data
    def read_calibration_data(self):
        data = []
        for i in range(0, len(self.calibration_data)):
            data.append(self.bus.read_byte_data(self.address, self.calibration_data[i]))
        return data

    # Read temperature
    def read_temperature(self):
        self.bus.write_byte_data(self.address, 0xF4, 0x2E)
        time.sleep(0.005)
        msb = self.bus.read_byte_data(self.address, 0xF6)
        lsb = self.bus.read_byte_data(self.address, 0xF7)
        temperature = ((msb << 8) + lsb) / 10.0
        return temperature/100

    # Read pressure
    def read_pressure(self):
        self.bus.write_byte_data(self.address, 0xF4, 0x34 + (3 << 6))
        time.sleep(0.026)
        msb = self.bus.read_byte_data(self.address, 0xF6)
        lsb = self.bus.read_byte_data(self.address, 0xF7)
        xlsb = self.bus.read_byte_data(self.address, 0xF8)
        pressure = ((msb << 16) + (lsb << 8) + xlsb) / 100.0
        return pressure

    # Main function
    def main(self):
        # Read calibration data
        calibration_data = self.read_calibration_data()

        # Read temperature
        temperature = self.read_temperature()
        print("Temperature: {:.2f} C".format(temperature))

        # Read pressure
        pressure = self.read_pressure()
        print("Pressure: {} hPa".format(pressure))

if __name__ == "__main__":
    bmp085 = BMP085()
    bmp085.main()
