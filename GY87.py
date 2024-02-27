import smbus
from HMC5883L import HMC5883L
from MPU6050 import mpu6050
from BMP085 import BMP085

class GY87:
    def __init__(self,mpu_address=0x68,hmc_address=0x1E,bmp_address=0x77 , bus=1):
        self.bus = smbus.SMBus(bus)
        self.mpu = mpu6050(mpu_address)
        self.hmc = HMC5883L(hmc_address)
        self.bmp = BMP085(bmp_address)
    def bypass_i2c(self):
        self.mpu.bypass_i2c()
    def get_all_data(self):
        accel = self.mpu.get_accel_data()
        gyro = self.mpu.get_gyro_data()
        temp = self.mpu.get_temp()
        mag = self.hmc.read_magnetometer()
        pressure = self.bmp.read_pressure()
        return [accel, gyro, temp, mag, pressure]
    def main(self):
        while True:
            [accel, gyro, temp, mag, pressure]=self.get_all_data()
            # print(self.get_all_data())

            print(f"Acceleration: X={accel['x']:.2f}m/s², Y={accel['y']:.2f}m/s², Z={accel['z']:.2f}m/s²")
            print(f"Rotation: X={gyro['x']:.2f}rad/s, Y={gyro['y']:.2f}rad/s, Z={gyro['z']:.2f}rad/s")
            print(f"Temperature ={temp:.2f}°C")
            print(f"Magnetrometer: X={mag['x']:.2f} µT, Y={mag['y']:.2f} µT, Z={mag['z']:.2f} µT")
            print(f"Pressure= {pressure:.2f} hPa")
            print("")

if __name__ == "__main__":
    gy87=GY87()
    gy87.main()