import time
import machine

# Define the GPIO pins connected to the stepper motor
step_pin1 = machine.Pin(21, machine.Pin.OUT)  # Pin 1 (A)
step_pin2 = machine.Pin(20, machine.Pin.OUT)  # Pin 2 (B)
step_pin3 = machine.Pin(19, machine.Pin.OUT)  # Pin 3 (C)
step_pin4 = machine.Pin(18, machine.Pin.OUT)  # Pin 4 (D)

# Define the step sequence for a 4-wire stepper motor (full-step mode)
# This sequence controls the coils of the motor in the correct order
sequence = [
    [1, 0, 0, 1],  # Step 1
    [1, 0, 1, 0],  # Step 2
    [0, 1, 1, 0],  # Step 3
    [0, 1, 0, 1],  # Step 4
]

# Function to rotate the motor
def rotate_motor(steps, direction, delay=0.01):
    # Set direction (1 for one direction, 0 for the other)
    # If direction = 1, motor moves in forward; if direction = 0, motor moves backward
    if direction == 1:
        step_sequence = sequence  # Forward direction
    else:
        step_sequence = sequence[::-1]  # Reverse the sequence for backward direction

    for _ in range(steps):
        for step in step_sequence:
            # Apply the step to the motor pins
            step_pin1.value(step[0])
            step_pin2.value(step[1])
            step_pin3.value(step[2])
            step_pin4.value(step[3])
            time.sleep(delay)  # Delay to control speed of rotation

# Main loop to control the stepper motor
try:
    while True:
        # Rotate the motor in forward direction (32*64 steps)
        rotate_motor(32*64, direction=1, delay=0.005)  # Adjust delay for speed control
        time.sleep(1)
        
        # Rotate the motor in backward direction (32*64 steps)
        rotate_motor(32*64, direction=0, delay=0.005)  # Adjust delay for speed control
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped")
