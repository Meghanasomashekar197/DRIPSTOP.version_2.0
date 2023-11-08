from machine import Pin, I2C
from sh1106 import SH1106_I2C

sclPin = Pin(15, mode=Pin.OUT, pull=None)
sdaPin = Pin(14, mode=Pin.OUT, pull=None)

i2c = I2C(1, scl=sclPin, sda=sdaPin, freq=25000)

oled = SH1106_I2C(128, 64, i2c)

oled.fill(0)

oled.text("i want chicken", 5, 10)

oled.show()
