import machine
import utime

potentiometer = machine.ADC(26)

while True:
    reading = potentiometer.read_u16()
    conversion_factor = 3.3 / 65536  # Calculate the conversion factor
    voltage = reading * conversion_factor  # Convert the reading to voltage
    print("ADC Reading:", reading)
    print("Voltage:", voltage)
    utime.sleep(2)
     #CONNECT GND TO GROUND VCC TO 3V3 AND MIDDLE TERMINAL OF THE POT TO 26TH TERMINAL OF THE POT