import machine

class TEMPO:
    def __init__(self):
        self.rtc = machine.RTC()
        
    def getDateTime(self):
        return self.rtc.datetime()
    
    def getTempoString(self):
        timestamp= self.rtc.datetime()
        return "%04d-%02d-%02d %02d:%02d:%02d"%(timestamp[0:3] + timestamp[4:7])