from mpu6050 import MPU6050
import time

G = 9.8  # Acceleration due to gravity in m/s^2

# Initialize the MPU6050 with I2C bus(1), SCL on GP15, SDA on GP14
mpu = MPU6050(1, 15, 14)  # bus(1), SCL(GP15), SDA(GP14)
mpu.MPU_Init()  # Initialize the MPU6050
time.sleep(1)  # Allow time for the MPU6050 to stabilize

try:
    while True:
        # Get accelerometer and gyroscope readings
        accel = mpu.MPU_Get_Accelerometer()  # Get accelerometer data
        gyro = mpu.MPU_Get_Gyroscope()      # Get gyroscope data

        # Print original raw data
        print("Original data: ")
        print("a/g: \tax: %d, ay: %d, az: %d\n\tgx: %d, gy: %d, gz: %d" % 
              (accel[0], accel[1], accel[2], gyro[0], gyro[1], gyro[2]))

        # Calculate and print the data in real-world units
        print("Calculated data (g for accelerometer, deg/s for gyroscope): ")
        print("a/g: \tax: %0.4f, ay: %0.4f, az: %0.4f\n\tgx: %0.4f, gy: %0.4f, gz: %0.4f\n" %
              (accel[0] / 16384.0, accel[1] / 16384.0, accel[2] / 16384.0,  # accelerometer scale
               gyro[0] / 131.0, gyro[1] / 131.0, gyro[2] / 131.0))  # gyroscope scale

        time.sleep(1)  # Wait for 1 second before the next reading

except Exception as e:
    print("Error:", e)  # Print any error that occurs
