from machine import Pin, PWM, ADC
import time

# Set up the servo and potentiometer
servo_pin = PWM(Pin(16))  # Servo connected to GPIO 16
servo_pin.freq(50)        # 50Hz is the typical frequency for servo motors

potentiometer_pin = ADC(Pin(26))  # Potentiometer connected to GPIO 26 (ADC pin)

# Function to set servo angle based on potentiometer input
def set_servo_angle(servo, angle):
    # Map the angle (0-180) to a duty cycle (1ms to 2ms)
    min_duty = 1000  # Corresponds to 0° (1ms)
    max_duty = 9000  # Corresponds to 180° (2ms)
    duty = min_duty + (angle / 180) * (max_duty - min_duty)
    servo.duty_u16(int(duty))  # Set the servo duty cycle

try:
    while True:
        # Read the potentiometer value (0 to 65535)
        pot_value = potentiometer_pin.read_u16()
        
        # Map potentiometer value (0-65535) to an angle (0-180 degrees)
        angle = (pot_value / 65535) * 180
        
        # Set the servo angle based on potentiometer input
        set_servo_angle(servo_pin, angle)
        
        time.sleep(0.05)  # Small delay for smooth operation

except KeyboardInterrupt:
    # Deactivate PWM when the program is interrupted
    servo_pin.deinit()
