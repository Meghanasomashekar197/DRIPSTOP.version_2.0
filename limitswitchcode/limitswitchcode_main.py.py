import machine
import utime

# Create LED objects to act as driven circuit
Limit_SW_LED = machine.Pin(15, machine.Pin.OUT)
E_Stop_LED = machine.Pin(16, machine.Pin.OUT)

# Turn on LEDs to simulate a running circuit
Limit_SW_LED.on()
E_Stop_LED.on()

# Create Switch objects for physical switches
Limit_SW = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
E_Stop_SW = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)

# Define debounce delay in milliseconds (adjust as needed)
debounce_delay = 50  # 50ms debounce delay

# Create state variables to track switch states and timestamps
limit_sw_state = True
e_stop_sw_state = True
last_limit_sw_time = utime.ticks_ms()
last_e_stop_sw_time = utime.ticks_ms()

# Create Interrupt handler for Limit Switch
def Limit_SW_Handler(pin):
    global limit_sw_state, last_limit_sw_time
    current_time = utime.ticks_ms()

    if current_time - last_limit_sw_time >= debounce_delay:
        last_limit_sw_time = current_time
        limit_sw_state = not limit_sw_state

    if not limit_sw_state:
        Limit_SW_LED.off()
        print("LIMIT REACHED - CORRECT PROBLEM AND RESTART PROGRAM")

# Create Interrupt handler for E-Stop Switch
def EStop_SW_Handler(pin):
    global e_stop_sw_state, last_e_stop_sw_time
    current_time = utime.ticks_ms()

    if current_time - last_e_stop_sw_time >= debounce_delay:
        last_e_stop_sw_time = current_time
        e_stop_sw_state = not e_stop_sw_state

    if not e_stop_sw_state:
        E_Stop_LED.off()
        print("E-Stop Pressed - CORRECT PROBLEM AND RESTART PROGRAM")

# Start the interrupt handler routines
Limit_SW.irq(trigger=machine.Pin.IRQ_FALLING, handler=Limit_SW_Handler)
E_Stop_SW.irq(trigger=machine.Pin.IRQ_FALLING, handler=EStop_SW_Handler)

# A loop just to keep things running, but does nothing constructive
print("Ready, Set, Go!")
x = 0
while True:  # Run an endless loop
    x += 1
    print(x)
    utime.sleep(.5)
