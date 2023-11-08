from machine import Pin, I2C
from sh1106 import SH1106_I2C
import time
from PCF8574 import PCF8574

input_pin = Pin(2, Pin.IN)

oled_address=0x3c
pcf8574_address = 0x20

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=250000)

oled = SH1106_I2C(128, 64, i2c,None, oled_address)

pcf = PCF8574(i2c, pcf8574_address)

def input_interrupt_handler(pin):
    
    data = []
    
    for i in range(8):
        data.append(pcf.pin(i))
        
           
    oled.fill(0)
    oled.text(str(data), 5, 10)
    
    oled.show()
    
input_pin.irq(trigger=Pin.IRQ_RISING, handler=input_interrupt_handler)

while True:
    pass
  