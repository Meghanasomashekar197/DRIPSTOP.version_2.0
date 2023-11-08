from machine import I2C, Pin, ADC
import time
from mcp4725 import MCP4725, BUS_ADDRESS

sclPin = Pin(15, mode=Pin.OUT, pull=None)
sdaPin = Pin(14, mode=Pin.OUT, pull=None)


i2c = I2C(1, scl=sclPin, sda=sdaPin, freq=25000)

dac = MCP4725(i2c, BUS_ADDRESS[0])

desired_voltage = 2.5

dac_value = int((desired_voltage / 3.3) * 4095)

dac.write(dac_value)

# Initialize the ADC
adc = ADC(Pin(27))  # Replace with the correct pin for your setup

# Function to scale voltage
def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Function to read and scale voltage
def read_scaled_voltage():
    raw_value = adc.read_u16()  # Read raw ADC value
    voltage = (raw_value / 65535.0) * 3.3  # Calculate voltage from ADC reading
    scaled_voltage = map_value(voltage, 0, 3.3, 0, 3.3)  # Scale voltage from 0-3.3V to 1-3.3V
    return scaled_voltage

# Read and print the scaled voltage
while True:
    scaled_voltage = read_scaled_voltage()
    print("Voltage:", scaled_voltage, "V")
    time.sleep(1)
