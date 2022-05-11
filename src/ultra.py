from machine import Pin
import utime

class ULTRA:
    def __init__(self, trig_pin, echo_pin):
        self.trigger = Pin(trig_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
    def distance_cm(self):
        self.trigger.low()
        utime.sleep_us(2)
        self.trigger.high()
        utime.sleep_us(5)
        self.trigger.low()
        while self.echo.value() == 0:
            signaloff = utime.ticks_us()
        while self.echo.value() == 1:
            signalon = utime.ticks_us()
        timepassed = signalon - signaloff
        return (timepassed * 0.0343) / 2
        
        
