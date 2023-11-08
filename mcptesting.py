from machine import I2C, Pin
from mcp4725 import MCP4725
import time

scl_pin = Pin(15, mode=Pin.OUT, pull=None)
sda_pin = Pin(14, mode=Pin.OUT, pull=None)

i2c = I2C(1, scl=scl_pin, sda=sda_pin, freq=100000)
dac = MCP4725(i2c)
while True:
    
    for i in range(0,101,1):
        dac_value = int(((i*0.05) / 5) * 4095)
        dac.write(dac_value)
        print(dac_value)
        time.sleep(2)
        
    
 





