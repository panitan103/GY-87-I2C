import smbus
class HMC5883L:
    def __init__(self, address=0x1E,bus=1):
        self.bus = smbus.SMBus(bus)
        self.address = address
    def set_continuous_mode(self):
        self.bus.write_byte_data(self.address, 0x02, 0x00)
    def read_i2c_word(self, register):
        """Read two i2c registers and combine them.

        register -- the first register to read from.
        Returns the combined read results.
        """
        # Read the data from the registers
        high = self.bus.read_byte_data(self.address, register)
        low = self.bus.read_byte_data(self.address, register + 1)

        value = (high << 8) + low

        if (value >= 0x8000):
            return -((65535 - value) + 1)
        else:
            return value

    def read_magnetometer(self):
        x = self.read_i2c_word(0x03)
        y = self.read_i2c_word(0x07)
        z = self.read_i2c_word(0x05)
        return {'x': x, 'y': y, 'z': z}
    def main(self):
        hmc = HMC5883L(0x1E)
        hmc.set_continuous_mode()
        while True:
            print(hmc.read_magnetometer())

if __name__ == "__main__":
    hmc = HMC5883L(0x1E)
    hmc.main()