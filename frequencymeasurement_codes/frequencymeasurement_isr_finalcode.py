from machine import Pin
import time

input_pin = Pin(14, Pin.IN)

elapsed_time = 0
edge_detected = 0
time_count = 0
time_list = []
interrupt_enabled = True


def handle_falling_edge(pin):
    global edge_detected, previous_time, elapsed_time , time_count ,time_list
    
    edge_detected += 1
    time_count += 1
    
    if edge_detected == 1:
        previous_time = time.ticks_ms()

    if edge_detected == 2:
        current_time = time.ticks_ms()
        elapsed_time = current_time - previous_time
        
        previous_time = current_time
        edge_detected = 0
        
    if time_count <= 5:
        time_list.append(elapsed_time)
while True:    
    if interrupt_enabled == True:
        input_pin.irq(trigger=Pin.IRQ_FALLING, handler=handle_falling_edge)       
        
    else:
        input_pin.irq(handler=None)
    
    if time_count == 5:
        time_list.sort()
        print(time_list[2])
        time_list.clear()
        time_count = 0