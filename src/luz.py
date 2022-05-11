import machine

class LUZ:
    def __init__(self, pin):
        self.sensor = machine.Pin(pin, machine.Pin.IN)
    
    def getValue(self):
        return self.sensor.value()