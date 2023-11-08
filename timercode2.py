from machine import Pin
import time

input_pin = Pin(14, Pin.IN)

rising_edges = 0
falling_edges = 0


while(True):
    
    current_state = input_pin.value()
      
    
    if (current_state == 1):

        while (current_state == 1):
            
            current_state = input_pin.value()
            
            pass
        
            
        previous_time = time.ticks_ms()
        falling_edges += 1
        
        while current_state == 0:
            current_state = input_pin.value()
            pass
        
        rising_edges += 1
        
        while (current_state == 1):
            current_state = input_pin.value()
            pass
        
        falling_edges += 1
        
        if (falling_edges == 2):    
            
            current_time = time.ticks_ms()
            
            elapsed_time = current_time - previous_time
            
            current_time = previous_time
            
            falling_edges = 0
            
            print(elapsed_time)
