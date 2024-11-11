import time
from machine import Pin

# Initialize relay and button pins
relay = Pin(14, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_UP)

# Function to toggle the relay state
def reverseRelay():
    if relay.value():
        relay.value(0)  # Turn relay off
    else:
        relay.value(1)  # Turn relay on

# Main loop
while True:
    if not button.value():  # Check if button is pressed
        time.sleep_ms(20)  # Debounce delay
        if not button.value():  # Confirm button is still pressed
            reverseRelay()  # Toggle relay state
            while not button.value():  # Wait until button is released
                time.sleep_ms(20)
