import utime
from display import DISPLAY
from ultra import ULTRA
from acelerometro import Acelerometro
from infra import INFRA
from buzzer import BUZZER
from luz import LUZ
from temperatura import TEMPERATURA
from tempo import TEMPO

sensorUltra = ULTRA(trig_pin = 17, echo_pin = 16)
sensorInfra = INFRA(pinOut= 21)
sensorLuz = LUZ(pin=19)
temp= TEMPERATURA()
buz = BUZZER(pin = 20,volumeMax = 30000, music = ["C7"] )
tempo = TEMPO()
ac = Acelerometro(pinSda = 14, pinScl = 15)
tela = DISPLAY(pinSda = 0, pinScl = 1)
tela.show("feliz")

i = 0
while True:
    print("cm: ",sensorUltra.distance_cm())
    print("Infra: ", sensorInfra.getValue())
    print("Luz: ", sensorLuz.getValue())
    print("Temp: ", temp.getValue())
    print("Tempo: ", tempo.getTempoString())
    
    ax= ac.diff()
    if(ax > 1.0):
        buz.playsong("feliz")
    ay= ac.getAy()
    az= ac.getAz()
    print(ax,"\t",ay,"\t",az)
    i += 1
    if (i > 5):
        i = 0
    utime.sleep(0.1)

# 
# 
# 
# buz.playsong("init")
# 
# while True:
#     


