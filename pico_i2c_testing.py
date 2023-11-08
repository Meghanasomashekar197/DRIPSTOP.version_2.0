from machine import Pin, I2C
from sh1106 import SH1106_I2C

# Initialize the I2C pins (SCL and SDA) on the Raspberry Pi Pico
sclPin = Pin(15, mode=Pin.OUT, pull=None)
sdaPin = Pin(14, mode=Pin.OUT, pull=None)

# Initialize the I2C interface
i2c = I2C(1, scl=sclPin, sda=sdaPin, freq=25000)
       
# Initialize the SH1106 OLED display
oled = SH1106_I2C(128, 64, i2c)

# Clear the display
oled.fill(0)

# Initialize a text string to display the I2C addresses
addresses_text = ""

# Scan for I2C devices and list their addresses
devices = i2c.scan()

if devices:
    for device in devices:
        addresses_text += "\n0x{:02X}".format(device)
else:
    addresses_text += "\nNo devices found"

# Display the I2C addresses on the OLED display
oled.text(addresses_text, 5, 10)
oled.show()
