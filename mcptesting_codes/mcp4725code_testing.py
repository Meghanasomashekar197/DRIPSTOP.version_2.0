from machine import I2C, Pin
from mcp4725 import MCP4725
import time

scl_pin = Pin(15, mode=Pin.OUT, pull=None)
sda_pin = Pin(14, mode=Pin.OUT, pull=None)

i2c = I2C(1, scl=scl_pin, sda=sda_pin, freq=100000)
dac = MCP4725(i2c)

desired_voltage = 2.4

def set_voltage(desired_voltage):
    dac_value = int((desired_voltage / 5) * 4095)
    dac.write(dac_value)

set_voltage(desired_voltage)
#print("Desired Voltage set to:", desired_voltage, "V")

while True:
    set_voltage(2.4)  
    time.sleep(1)
    
    set_voltage(2.6) 
    time.sleep(1)
