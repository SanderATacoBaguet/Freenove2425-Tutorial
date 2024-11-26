from machine import Pin, PWM
import time

# Sett opp PWM på en GPIO-pin
servo_pin = PWM(Pin(16))  # Bruk GPIO 16 for servoen
servo_pin.freq(50)        # Standard frekvens for servoer (50 Hz)

def set_servo_angle(servo, angle):
    # Konverter vinkel (0-180) til duty cycle (min 1ms, maks 2ms)
    min_duty = 1000  # 1ms
    max_duty = 9000  # 2ms
    duty = min_duty + (angle / 180) * (max_duty - min_duty)
    servo.duty_u16(int(duty))  # Sett duty cycle (16-bit)

try:
    while True:
        # Sveip fra 0 til 180 grader
        for angle in range(0, 181, 1):
            set_servo_angle(servo_pin, angle)
            time.sleep(0.015)  # 15ms for jevn bevegelse
        
        # Sveip fra 180 til 0 grader
        for angle in range(180, -1, -1):
            set_servo_angle(servo_pin, angle)
            time.sleep(0.015)
except KeyboardInterrupt:
    # Deaktiver PWM på pinnen når programmet avsluttes
    servo_pin.deinit()
