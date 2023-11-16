import machine
import utime
from pico_i2c_lcd import I2cLcd

class YourDevice:
    def __init__(self):
        # Initialize your LCD instance
        i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
        lcd = I2cLcd(i2c, 0x27, 4, 20)  # Adjust the number of rows and columns according to your LCD

        self.lcd = lcd

        # Initialize device parameters
        self.device_id = "001"

    def screen_setup(self):
        self.screen_blank()
        self.lcd.move_to(0, 0)
        self.lcd.putstr(f"devID:{self.device_id}")
        self.lcd.move_to(2, 1)
        self.lcd.putstr(f"do you want to         continue")
        self.lcd.move_to(1, 3)
        self.lcd.putstr("Yes")
        self.lcd.move_to(17, 3)
        self.lcd.putstr("No")
        self.lcd.move_to(1, 3)
        

    def screen_blank(self):
        self.lcd.clear()

if __name__ == "__main__":
    your_device = YourDevice()
    your_device.screen_setup()
