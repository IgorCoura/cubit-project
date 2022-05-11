import machine

class BUZZER:
    def __init__(self, pin):
        self.buz = machine.Pin(pin, machine.Pin.OUT)
        self.buz.value(0)
    
    def toggle(self):
        self.buz.toggle()