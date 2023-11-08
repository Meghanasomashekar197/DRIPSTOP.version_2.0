import machine
from machine import Pin,time


input_pin = Pin(1, Pin.IN)

def input_interrupt_handler(pin):
    print(pin.value())
    
input_pin.irq(trigger=Pin.IRQ_FALLING, handler=input_interrupt_handler)
time.sleep(1)
while True:
    pass
