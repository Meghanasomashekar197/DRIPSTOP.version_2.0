from machine import I2C, Pin
from PCF8574 import PCF8574

# Initialize the I2C interface (I2C0)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)
# Define the interrupt pin connected to the PCF8574
interrupt_pin = Pin(2, Pin.IN)
# PCF8574 I2C address (0x20 by default, change if you've configured the address differently)
pcf8574_address = 0x20

# Create an instance of the PCF8574 class
pcf = PCF8574(i2c, pcf8574_address)

def switch_isr(pin):
      # Read the state of all pins at once
    print(pcf.pin(0))

while True:
    interrupt_pin.irq(trigger=Pin.IRQ_HIGH_LEVEL, handler=switch_isr)