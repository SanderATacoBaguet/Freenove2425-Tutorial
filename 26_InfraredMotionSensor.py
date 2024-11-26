from machine import Pin
import time

sensorPin = Pin(18, Pin.IN)  # Sensor connected to GPIO18
ledPin = Pin(15, Pin.OUT)     # LED connected to GPIO15

try:
    while True:
        if not sensorPin.value():  # If sensor input is LOW (button pressed or sensor triggered)
            ledPin.value(1)  # Turn LED ON
        else:
            ledPin.value(0)  # Turn LED OFF
        time.sleep(0.1)  # Small delay to avoid excessive processing
except KeyboardInterrupt:
    pass  # Graceful exit when manually interrupted
