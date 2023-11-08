import machine
import time

IN1, IN2, IN3, IN4 = machine.Pin(2,machine.Pin.OUT), machine.Pin(3,machine.Pin.OUT), machine.Pin(4,machine.Pin.OUT), machine.Pin(5,machine.Pin.OUT)

state = 1

direction_clockwise = 0
while True:   
    
    for i in range(0,50,1):
        
        if state==1:
            #state is assigned 1 here because while loop is never ending and
            #we need to stop the cam at a particular point so we use it stop at a start and stop the loop
            
            if direction_clockwise == 1:
                #here direction is used to determine the run in specific direction
                #increasing the time of delay to increase torque
                IN1.value(1)
                IN2.value(1)
                IN3.value(0)
                IN4.value(0)
                time.sleep(0.02)
                
                IN1.value(0)
                IN2.value(1)
                IN3.value(1)
                IN4.value(0)
                time.sleep(0.02)
                
                IN1.value(0)
                IN2.value(0)
                IN3.value(1)
                IN4.value(1)
                time.sleep(0.02)
                
                
                IN1.value(1)
                IN2.value(0)
                IN3.value(0)
                IN4.value(1)
                time.sleep(0.02)
                
            if direction_clockwise == 0:
            
                IN4.value(1)
                IN3.value(1)
                IN2.value(0)
                IN1.value(0)
                time.sleep(0.020)
                
                IN4.value(0)
                IN3.value(1)
                IN2.value(1)
                IN1.value(0)
                time.sleep(0.02)
                
                IN4.value(0)
                IN3.value(0)
                IN2.value(1)
                IN1.value(1)
                time.sleep(0.02)
                
                
                IN4.value(1)
                IN3.value(0)
                IN2.value(0)
                IN1.value(1)
                time.sleep(0.02)
                
            
    state=0