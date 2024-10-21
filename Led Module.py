import machine
import neopixel
import time

# Configuration
NUM_LEDS = 8
PIN = 16
DELAY = 0.05  # Shorter delay for smoother animation

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

def run_pattern(color, repetitions=1, pattern='full_circle'):
    """
    Runs an LED pattern.
    :param color: The color for the LEDs.
    :param repetitions: Number of times to repeat the pattern.
    :param pattern: The pattern type ('full_circle', 'half_circle', 'back_and_forth').
    """
    for _ in range(repetitions):
        if pattern == 'full_circle':
            for i in range(NUM_LEDS):
                set_leds(i, color)
            for i in range(NUM_LEDS - 1, -1, -1):
                set_leds(i, color)

        elif pattern == 'half_circle':
            for i in range(NUM_LEDS // 2):
                set_leds(i, color)
            for i in range(NUM_LEDS // 2 - 1, -1, -1):
                set_leds(i, color)

        elif pattern == 'back_and_forth':
            for i in range(NUM_LEDS):
                set_leds(i, color)
            for i in range(NUM_LEDS - 2, 0, -1):
                set_leds(i, color)

        else:
            print("Error: Unsupported pattern type.")
            return

def turn_off_leds():
    """Turns off all LEDs."""
    for n in range(NUM_LEDS):
        np[n] = OFF
    np.write()

# Example usage:
while True:
    # Full circle twice for each color
    run_pattern(RED, repetitions=2, pattern='full_circle')
    run_pattern(GREEN, repetitions=2, pattern='full_circle')
    run_pattern(BLUE, repetitions=2, pattern='full_circle')

    # Half circle four times for each color
    run_pattern(RED, repetitions=4, pattern='half_circle')
    run_pattern(GREEN, repetitions=4, pattern='half_circle')
    run_pattern(BLUE, repetitions=4, pattern='half_circle')

    # Back and forth twice for each color
    run_pattern(RED, repetitions=2, pattern='back_and_forth')
    run_pattern(GREEN, repetitions=2, pattern='back_and_forth')
    run_pattern(BLUE, repetitions=2, pattern='back_and_forth')

    # Optional pause after completing the full sequence
    time.sleep(2)

    # Turn off all LEDs before repeating the sequence
    turn_off_leds()
    time.sleep(1)
