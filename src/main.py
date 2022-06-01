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
buz = BUZZER(pin = 20,volumeMax = 30000)
tempo = TEMPO()
ac = Acelerometro(pinSda = 14, pinScl = 15)
tela = DISPLAY(pinSda = 0, pinScl = 1)

emocoes = ["feliz", "dormindo", "muito_feliz","neutro", "raiva", "triste"]
estadoAtual= "neutro"

quantCarinho = 0
quantCarinhoAtual = 0
carinho = False
quantLoop = 0

buz.playsong("init")
tela.show("neutro")

while True:
    
    if(sensorInfra.getValue() == 0):
        carinho = True
    
    if(sensorInfra.getValue() == 1 and carinho):
        quantCarinho += 1
        carinho = False
        
    if(quantLoop >= 1000):
        quantCarinho = 0
        quantLoop = 0
    
    if(quantCarinho >= 2):
        estadoAtual = "muito_feliz"
        updateEstado(estadoAtual)
        quantCarinho = 0
        quantLoop = 0
    
    if(sensorLuz.getValue() == 1 and estadoAtual != "dormindo"):
        estadoAtual = "dormindo"
        updateEstado(estadoAtual)
        
    if(sensorUltra.distance_cm() <= 10 and estadoAtual != "triste"):
        estadoAtual = "triste"
        updateEstado(estadoAtual)
        
    if(sensorLuz.getValue() == 0 and estadoAtual != "neutro" and sensorUltra.distance_cm() > 10):
        estadoAtual = "neutro"
        updateEstado(estadoAtual)
        
    
    if(ac.diff() > 1.0):
        updateEstado("raiva")
        utime.sleep(1)
        updateEstado(estadoAtual)
    
    quantLoop +=1

        
    
    


