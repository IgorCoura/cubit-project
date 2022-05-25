from imu import MPU6050
from utime import sleep
from machine import Pin, I2C

class Acelerometro:
    def __init__(self, pinSda, pinScl):
        i2c = I2C(1, sda=Pin(pinSda), scl=Pin(pinScl), freq=400000)
        self.imu = MPU6050(i2c)
    def diff(self):
        init = self.imu.accel.x
        sleep(0.05)
        out = self.imu.accel.x
        return round(out-init, 2)
        
    def getAx(self):
        return round(self.imu.accel.x,2)
    
    def getAy(self):
        return round(self.imu.accel.y,2)
    
    def getAz(self):
        return round(self.imu.accel.z,2)
    
    def getGx(self):
        return round(self.imu.gyro.x)
    
    def getGy(self):    
        return round(self.imu.gyro.y)
    
    def getGz(self):
        return round(self.imu.gyro.z)
    
    def getTemp(self):
        return round(self.imu.temperature,2)
    
        