# import machine
# import utime

# led = machine.Pin(25, machine.Pin.OUT)
# buz = machine.Pin(15, machine.Pin.OUT)
# sensor_temp = machine.ADC(4)
# conversion_factor = 3.3 / (65535)
# 
# 
# led.value(0)
# buz.value(0)
# 
# while True:
#     reading = sensor_temp.read_u16() * conversion_factor
#     
#     temperature = 27 - (reading - 0.706)/0.001721
#     
#     print(temperature)
#     
#     led.toggle()
#     utime.sleep(1)


# 
# 
# sensorInfra = machine.Pin(16, machine.Pin.IN)
# 
# 
# while True:
#     print(sensorInfra.value())
#     utime.sleep(1)

# import machine
# from acelerometro import Acelerometro
# import time
# 
# while True:
#     ac = Acelerometro(0,1)
#     ax= ac.getAx()
#     ay= ac.getAy()
#     az= ac.getAz()
#     gx= ac.getGx() 
#     gy= ac.getGy()
#     gz= ac.getGz()
#     tem= ac.getTemp()
#     
#     print(ax,"\t",ay,"\t",az,"\t",gx,"\t",gy,"\t",gz,"\t",tem," ",end="\r")
#     time.sleep(1)

# import machine
# 
# rtc=machine.RTC()
# 
# while True:
#     timestamp=rtc.datetime()
#     timestring="%04d-%02d-%02d %02d:%02d:%02d"%(timestamp[0:3] + timestamp[4:7])
#     print(timestring)
# 
# 
# import machine
# import utime
# 
# sensorLuz = machine.Pin(15, machine.Pin.IN)
# 
# while True:
#     print(sensorLuz.value())
#     utime.sleep(1)
#     

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
TH = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\xff\xff\x00\x00\x00\x00\x00\x03\xfc\xff\xc0\x00\x00\x00\x00\x1f\x00\x00\xf8\x00\x00\x00\x00x\x00\x00.\x00\x00\x00\x00|\x00\x00:\x00\x00\x00\x01\xe0\x00\x00\x07\x80\x00\x00\x03\x80\x00\x00\x01\xc0\x00\x00\x04\x00\x00\x00\x00`\x00\x00\x0c\x00\x00\x00\x000\x00\x00\x04\x00\x00\x00\x000\x00\x008\x00\x00\x00\x00\x1c\x00\x00\x18\x00\x00\x00\x00\x0c\x00\x00p\x00\x00\x00\x00\x0c\x00\x00p\x00\x00\x00\x00\x0e\x00\x000\x00\x00\x00\x00\x0e\x00\x00\x80\x03\xc0\x02\xc0\x03\x00\x00\xc0\x0f`\x05\xb0\x03\x00\x03\x80\x0f\xe0\x07\xf0\x01\xc0\x03\x80\t\xe0\x07\xf0\x01\xc0\x03\x80\x0f\xc0\x07\xf0\x01\x80\x03\x80\x03\xc0\x03\xc0\x01\xc0\x03\x80\x00\x00\x00\x00\x01\xc0\x03\x80\x00\x00\x00\x00\x01\xc0\x03\x80\x00\x00\x00\x00\x01\x80\x03\x80\x00\x00\x00\x00\x01@\x03\x80\x00\x00\x00\x00\x01\xc0\x03\x80\x00\x04\x00\x00\x01\xc0\x03\x80\x08\x00\x04\x00\x01\xc0\x03\x80\x00\x00\x00\x00\x01\x00\x03\x000\x00\x00\x0c\x00\xc0\x03\x800\x00\x00\x0c\x01@\x03\x80<\x00\x004\x01@\x02\x80<\x00\x00<\x01\xc0\x00\xc0\x16\x00\x00x\x02\x00\x00\xc0\x0f\x00\x00\xd0\x03\x00\x00P\x03\xc0\x03\xc0\x0e\x00\x00p\x03\xc0\x03\x00\x0e\x00\x00p\x01\xe0\x07\x00\x0e\x00\x00\x18\x00\xff\xef\x00\x14\x00\x00\x18\x00\x178\x00\x1c\x00\x00\x0c\x00\x00\x00\x000\x00\x00\x0c\x00\x00\x00\x000\x00\x00\x02\x00\x00\x00\x00`\x00\x00\x03\x00\x00\x00\x01\x80\x00\x00\x01\xe0\x00\x00\x04\x80\x00\x00\x00|\x00\x00>\x00\x00\x00\x00l\x00\x006\x00\x00\x00\x00\x17\x00\x00\xf8\x00\x00\x00\x00\x03\xfc\xff\xc0\x00\x00\x00\x00\x00\xb3\xfd\x00\x00\x00\x00\x00\x00\xbb\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

fb = framebuf.FrameBuffer(TH,64,64, framebuf.MONO_HLSB)
oled.fill(0)
oled.blit(fb,32,0)
oled.show()