import machine
import time

led = machine.Pin("LED", machine.Pin.OUT)  # Assuming the LED is connected to GPIO pin 25

input_pin = machine.Pin(28, machine.Pin.IN)  # Assuming the input pin is connected to GPIO pin 1

blinking = True  # Flag to control LED blinking

def input_interrupt_handler(pin):
    global blinking
    print("Input Pin Value:", pin.value())
    blinking = not blinking  # Toggle the blinking flag

input_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=input_interrupt_handler)

while True:
    if blinking:
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)
    else:
        led.value(0)  # LED is turned off
        time.sleep(0.1)  # Optional delay to avoid CPU load
