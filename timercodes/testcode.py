from machine import Pin
import time

input_pin = Pin(1, Pin.IN)

rising_edges = 0
falling_edges = 0

previous_state = 1
previous_time = time.ticks_ms()
current_state = input_pin.value()

while(True):

    while (current_state == 1):
        pass
    
    previous_time = time.ticks_ms()
    falling_edges += 1
        
    while current_state == 0:
        pass
    
    rising_edges += 1
    
    while (current_state == 1):
        pass
    
    falling_edges += 1
    
    if (falling_edge == 2):    
        
        current_time = time.ticks_ms()
        
        elapsed_time = current_time - previous_time
        
        current_time = previous_time
        
        print(elapsed_time)
        
        
        