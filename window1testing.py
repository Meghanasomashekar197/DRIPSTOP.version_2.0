from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
from time import sleep

class ButtonLCDController:
    def __init__(self, lcd, button_up_pin, button_down_pin, button_left_pin, button_right_pin):
        self.lcd = lcd
        self.button_up = Pin(button_up_pin, Pin.IN, Pin.PULL_UP)
        self.button_down = Pin(button_down_pin, Pin.IN, Pin.PULL_UP)
        self.button_left = Pin(button_left_pin, Pin.IN, Pin.PULL_UP)
        self.button_right = Pin(button_right_pin, Pin.IN, Pin.PULL_UP)
        self.cursor = 0 
        self.device_id = "001" 
        self.fluid_options = ["IV", "Blood", "Lipid"]
        self.volume_options = ["100ml", "250ml", "500ml", "1000ml"]
        self.drip_factor_options = ["10", "15", "20", "60"]
        self.update_display()

    def update_display(self):
        self.lcd.clear()
        self.lcd.move_to(0, 0)
        self.lcd.putstr(f"devID: {self.device_id}")

        for i in range(3):
            self.lcd.move_to(0, i + 1)
            if self.cursor == i:
                self.lcd.putstr(f">{self.get_option(i)}")
            else:
                self.lcd.putstr(f" {self.get_option(i)}")

    def get_option(self, index):
        if index == 0:
            return f"Fluid: {self.fluid_options[self.cursor]}"
        elif index == 1:
            return f"Volume: {self.volume_options[self.cursor]}"
        elif index == 2:
            return f"DripFactor:{self.drip_factor_options[self.cursor]}gtt/ml"

    def check_buttons(self):
        if self.button_down.value() == 0:
            self.cursor = (self.cursor + 1) % 3
            self.update_display()
            sleep(0.2)  

        elif self.button_up.value() == 0:
            self.cursor = (self.cursor - 1) % 3
            self.update_display()
            sleep(0.2) 

        elif self.button_left.value() == 0:
            self.update_option(left=True)

        elif self.button_right.value() == 0:
            self.update_option(left=False)

    def update_option(self, left=True):
        if self.cursor == 0:
            options = self.fluid_options
        elif self.cursor == 1:
            options = self.volume_options
        elif self.cursor == 2:
            options = self.drip_factor_options

        if left:
            options.insert(0, options.pop())
        else:
            options.append(options.pop(0))

        self.update_display()

# Instantiate your LCD object
i2c = I2C(0, sda=Pin(0), scl=Pin(1))  # Adjust pins based on your actual connections
lcd = I2cLcd(i2c, 0x27, 4, 20)  # Adjust I2C address and LCD dimensions

# Define button pins
button_up_pin = 12  # Replace with the actual pin number
button_down_pin = 13  # Replace with the actual pin number
button_left_pin = 14  # Replace with the actual pin number
button_right_pin = 15  # Replace with the actual pin number

# Create the ButtonLCDController instance
controller = ButtonLCDController(lcd, button_up_pin, button_down_pin, button_left_pin, button_right_pin)

# Main loop to continuously check buttons
while True:
    controller.check_buttons()
    sleep(0.1)  # Add a short delay to avoid busy-waiting and reduce CPU usage
