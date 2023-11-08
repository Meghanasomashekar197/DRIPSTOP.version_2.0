import time
from machine import Pin

button_pressed_count = 0  # global variable
pin_button = Pin(14, Pin.IN, Pin.PULL_UP)

def button_isr(pin):
    global button_pressed_count
    button_pressed_count += 1

if __name__ == "__main__":
    button_pressed_count_old = 0
    pin_button.irq(trigger=Pin.IRQ_FALLING, handler=button_isr)

    while True:
        if button_pressed_count_old != button_pressed_count:
            print('Button value:', button_pressed_count)
            button_pressed_count_old = button_pressed_count

        if button_pressed_count > 10:  # Perform a heavy task here
            print("Performing a heavy task...")
            # Add your code for the heavy task here
