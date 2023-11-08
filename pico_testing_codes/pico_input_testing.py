import machine
import time

#pin=0
def pin_test(pin_number):
    global pin
    pin = machine.Pin(pin_number, machine.Pin.OUT)
    
while True:
    
    pin_test(0)
    pin.value(1)
    time.sleep(1)
    pin.value(0)
    time.sleep(1)