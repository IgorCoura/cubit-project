import machine

class TEMPERATURA:
    def __init__(self):
        self.sensor = machine.ADC(4)
        self.conversion_factor = 3.3 / (65535)
    def getValue(self):
        reading = self.sensor.read_u16() * self.conversion_factor
        return 27 - (reading - 0.706)/0.001721