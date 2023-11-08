from machine import Pin, Timer

input_pin = Pin(4, Pin.IN)
elapsed_times = []

def record_time(timer):
    elapsed_time = timer.read_us()
    elapsed_times.append(elapsed_time)
    if len(elapsed_times) == 5:
        elapsed_times.sort()
        print("Middle Time:", elapsed_times[2])
        elapsed_times.clear()

def interruption_handler(pin):
    global count, timerState
    count += 1
    print(count)

    if count == 3:
        timerState = 0
        soft_timer.deinit()

timerState = 1
count = 0

while True:
    if timerState == 1:
        soft_timer = Timer(mode=Timer.PERIODIC, freq=1, callback=interruption_handler)
        timerState = 2
    if timerState == 2:
        if input_pin.value() == 0:
            soft_timer.init(freq=1, mode=Timer.PERIODIC)
            timerState = 3
    if timerState == 3:
        if input_pin.value() == 1:
            timerState = 1
