from machine import Pin, I2C, ADC
from sh1106 import SH1106_I2C
import time

# Initialize I2C for the OLED display
sclPin = Pin(1, mode=Pin.OUT, pull=None)
sdaPin = Pin(0, mode=Pin.OUT, pull=None)
i2c = I2C(0, scl=sclPin, sda=sdaPin, freq=25000)
oled = SH1106_I2C(128, 64, i2c)
oled.fill(0)

# Initialize ADC (Analog-to-Digital Converter)
adc = ADC(Pin(28))  # GP26 corresponds to ADC0

# Set the attenuation to 11dB for a 3.3V input range
#adc.atten(ADC.ATTN_11DB)

while True:
    # Read the analog voltage
    voltage = adc.read_u16() * (3.3 / 65535.0)  # Convert ADC reading to voltage

    # Convert the voltage to a string and display it on the OLED
    voltage_str = "{:.2f} V".format(voltage)
    oled.fill(0)
    oled.text(voltage_str, 5, 30)
    oled.show()

    # Print the voltage value to the serial console
    #print("Voltage:", voltage, "V")

    # Wait for a short delay
    time.sleep(1)
