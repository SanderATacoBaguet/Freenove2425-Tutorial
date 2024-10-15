#Hei dette er bare en test
from machine import Pin
import time

led = Pin('LED', Pin.OUT)
try:
    while True:
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
except:
    pass
    