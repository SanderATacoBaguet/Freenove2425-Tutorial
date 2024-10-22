import machine
import neopixel
import time

# Configuration
NUM_LEDS = 8
PIN = 16
DELAY = 0.00416666666666666666666667  # Adjustable delay for smooth animation

# Colors (half brightness values for RGB)
RED = (127, 0, 0)
GREEN = (0, 127, 0)
BLUE = (0, 0, 127)
OFF = (0, 0, 0)

# Initialize the NeoPixel object
np = neopixel.NeoPixel(machine.Pin(PIN), NUM_LEDS)

def set_leds(index, color=OFF):
    """Sets a specific LED to the given color and turns off others."""
    for i in range(NUM_LEDS):
        np[i] = color if i == index else OFF
    np.write()
    time.sleep(DELAY)

def loop_pattern(color, repetitions=1):
    """
    Runs the loop pattern where the light moves sequentially from 0 to 7,
    wraps back to 0, and repeats the pattern.
    :param color: The color for the LEDs.
    :param repetitions: Number of times to repeat the loop.
    """
    for _ in range(repetitions):
        # Move from LED 0 to 7
        for i in range(NUM_LEDS):
            set_leds(i, color)
        
        # Loop back to LED 0
        set_leds(0, color)

        # Move again from LED 1 to 7
        for i in range(1, NUM_LEDS):
            set_leds(i, color)

def turn_off_leds():
    """Turns off all LEDs."""
    for n in range(NUM_LEDS):
        np[n] = OFF
    np.write()

# Example usage:
while True:
    # Loop pattern twice for each color
    loop_pattern(RED, repetitions=10)
    loop_pattern(GREEN, repetitions=10)
    loop_pattern(BLUE, repetitions=10)

    # Optional pause after completing the full sequence
    time.sleep(0.001)

    # Turn off all LEDs before repeating the sequence
    turn_off_leds()
    time.sleep(0.001)