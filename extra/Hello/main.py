import machine
import utime

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
# sensor = machine.Pin(16, machine.Pin.IN)
# 
# 
# while True:
#     print(sensor.value())
#     utime.sleep(1)



scl = machine.Pin(15, machine.Pin.IN)
sda = machine.Pin(14, machine.Pin.IN)


