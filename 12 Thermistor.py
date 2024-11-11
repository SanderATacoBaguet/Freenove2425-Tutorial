from machine import Pin, ADC
import time
import math

# Set ADC
adc = ADC(27)

try:
    while True:
        adcValue = adc.read_u16()
        voltage = adcValue / 65535.0 * 3.3
        if voltage >= 3.3:
            print("Voltage too high, skipping calculation to avoid division by zero.")
            continue
        
        Rt = 10 * voltage / (3.3 - voltage)
        tempK = (1 / (1 / (273.15 + 25) + (math.log(Rt / 10)) / 3950))
        tempC = int(tempK - 273.15)
        print("ADC value:", adcValue, " Voltage: %0.2f" % voltage,
              " Temperature: " + str(tempC) + "C")
        time.sleep(1)

except Exception as e:
    print("Error:", e)
