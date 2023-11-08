from machine import Pin
import time

input_pin = Pin(14, Pin.IN)


def handle_falling_edge(pin):
    global edge_detected
    edge_detected += 1
    previous_time = time.ticks_ms()
    
    if edge_detected == 2:
        current_time = time.ticks_ms()
        elapsed_time = current_time - previous_time
        print("Elapsed Time (ms):", elapsed_time)
        previous_time = current_time  
        edge_detected = 0
input_pin.irq(trigger=Pin.IRQ_FALLING, handler=handle_falling_edge)

while True:
    pass