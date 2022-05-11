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
buz = BUZZER(pin = 20)
tempo = TEMPO()
ac = Acelerometro(pinSda = 14, pinScl = 15)
tela = DISPLAY(pinSda = 0, pinScl = 1)
tela.show()

while True:
    print("cm: ",sensorUltra.distance_cm())
    print("Infra: ", sensorInfra.getValue())
    print("Luz: ", sensorLuz.getValue())
    print("Temp: ", temp.getValue())
    print("Tempo: ", tempo.getTempoString())
#    buz.toggle();
    ax= ac.getAx()
    ay= ac.getAy()
    az= ac.getAz()
    print(ax,"\t",ay,"\t",az)
    utime.sleep(1)


