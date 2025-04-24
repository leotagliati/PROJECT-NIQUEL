
from machine import Pin
import time

botao = Pin(16, Pin.IN, Pin.PULL_UP)
led = Pin(25, Pin.OUT)

while True:
    if botao.value() == 0:  
        led.value(1)        
    else:
        led.value(0)        
    time.sleep(0.05)        