import machine
import utime
from pico_i2c_lcd import I2cLcd

class YourDevice:
    def __init__(self):
        # Initialize your LCD instance
        i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
        lcd = I2cLcd(i2c, 0x27, 4, 20)  # Adjust the number of rows and columns according to your LCD

        self.lcd = lcd

    def screen_setup(self):
        self.screen_blank()
        self.lcd.move_to(0, 0)
        self.lcd.putstr("dev:002")
        self.lcd.move_to(0, 1)
        self.lcd.putstr("volume: Loading...")
        self.lcd.move_to(0, 2)
        self.lcd.putstr("sensor: Loading...")

    def screen_blank(self):
        self.lcd.clear()

if __name__ == "__main__":
    your_device = YourDevice()
    your_device.screen_setup()