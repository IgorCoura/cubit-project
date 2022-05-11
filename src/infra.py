import machine

class INFRA:
    def __init__(self, pinOut):
        self.sensor = machine.Pin(pinOut, machine.Pin.IN)

    def getValue(self):
        return self.sensor.value()