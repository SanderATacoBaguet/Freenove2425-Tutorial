import machine
import neopixel
import time

# Configuration
NUM_LEDS = 8               # Number of LEDs in the NeoPixel ring
PIN_NEOPIXEL = 16          # GPIO pin connected to the NeoPixel ring
PIN_POT_BRIGHTNESS = 26    # GPIO pin connected to the brightness potentiometer
PIN_POT_COLOR = 27         # GPIO pin connected to the color potentiometer
PIN_POT_SPEED = 28         # GPIO pin connected to the speed potentiometer
PIN_BUTTON_DIRECTION = 14  # GPIO pin connected to the button for direction
PIN_BUTTON_DIMMER = 15     # GPIO pin connected to the button for dimmer

# Initialize NeoPixel
np = neopixel.NeoPixel(machine.Pin(PIN_NEOPIXEL), NUM_LEDS)

# Colors (RGB with full intensity)
COLORS = [
    (127, 0, 0),    # RED
    (0, 127, 0),    # GREEN
    (0, 0, 127),    # BLUE
    (0, 127, 127),  # CYAN
    (127, 127, 0),  # YELLOW
    (127, 0, 127),  # MAGENTA
    (127, 127, 127) # WHITE
]

# Initialize potentiometers and buttons
pot_brightness = machine.ADC(machine.Pin(PIN_POT_BRIGHTNESS))
pot_color = machine.ADC(machine.Pin(PIN_POT_COLOR))
pot_speed = machine.ADC(machine.Pin(PIN_POT_SPEED))
button_direction = machine.Pin(PIN_BUTTON_DIRECTION, machine.Pin.IN, machine.Pin.PULL_UP)
button_dimmer = machine.Pin(PIN_BUTTON_DIMMER, machine.Pin.IN, machine.Pin.PULL_UP)

# State variables
current_color_index = 0
current_position = 0  # Current LED position
direction = 1  # Direction: 1 for forward, -1 for backward
dimmer_enabled = False  # Dimmer enabled by default

def write_leds():
    """Writes the current LED colors to the NeoPixel strip."""
    for i in range(NUM_LEDS):
        np[i] = leds[i]
    np.write()  # Update the LED strip

# LED colors array
leds = [[0, 0, 0] for _ in range(NUM_LEDS)]

def get_brightness():
    """Reads the value from the potentiometer to adjust brightness between 0% and 100%."""
    pot_value = pot_brightness.read_u16()  # Read the value (0-65535)
    
    # Scale brightness from 0% to 100%
    brightness = (pot_value * 255) // 65535
    return brightness

def set_led_brightness():
    """Sets the brightness based on the current mode: dimmer or normal."""
    brightness = get_brightness()  # Get brightness from potentiometer

    for i in range(NUM_LEDS):
        if dimmer_enabled:
            # When dimmer is enabled, only one LED is fully lit based on the current position
            if i == current_position:
                led_brightness = brightness  # Use potentiometer brightness for the active LED
            else:
                led_brightness = 0  # All other LEDs are off
        else:
            # When dimmer is off, set a gradient of brightness
            distance = (i - current_position) % NUM_LEDS
            led_brightness = max(0, brightness - (distance * 30))  # Decrease brightness by 30 for each distance
            
        # Set LED color with the calculated brightness
        leds[i] = tuple(int(c * (led_brightness / 255)) for c in COLORS[current_color_index])

def update_direction():
    """Updates the direction based on button press."""
    global direction
    if not button_direction.value():  # Button pressed (active low)
        direction *= -1  # Toggle direction
        time.sleep(0.2)  # Debounce delay

def update_dimmer():
    """Toggles the dimmer on or off based on button press."""
    global dimmer_enabled
    if not button_dimmer.value():  # Button pressed (active low)
        dimmer_enabled = not dimmer_enabled  # Toggle state
        time.sleep(0.2)  # Debounce delay

def update_color():
    """Updates the color based on the color potentiometer."""
    global current_color_index
    pot_value = pot_color.read_u16()
    num_colors = len(COLORS)
    
    # Divide the potentiometer value to select colors
    color_index = int((pot_value / 65535) * num_colors)
    if color_index != current_color_index:
        current_color_index = color_index % num_colors

# Main loop
try:
    while True:
        # Update LED brightness based on current mode
        set_led_brightness()

        # Check potentiometers to update color
        update_color()
        
        # Update direction
        update_direction()
        
        # Update dimmer status
        update_dimmer()

        # Write LED values to NeoPixel
        write_leds()

        # Update position based on direction
        current_position += direction

        # Handle direction change
        if direction == 1:  # If direction is forward (0 to 7)
            if current_position >= NUM_LEDS:  # If we go past 7, go back to 0
                current_position = 0
        elif direction == -1:  # If direction is backward (7 to 0)
            if current_position < 0:  # If we go past 0
                current_position = NUM_LEDS - 1  # Go to 7 instead of going to -1

        # Wait before next update
        pot_speed_value = pot_speed.read_u16()
        delay = max(0.01, (pot_speed_value / 65535) * 0.1)  # Scale delay
        time.sleep(delay)  # Adjust this for speed
except Exception as e:
    print("An error occurred:", e)
