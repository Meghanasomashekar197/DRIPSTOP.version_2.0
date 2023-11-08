import machine
import time

# Define GPIO pins connected to ULN2003 driver board
IN1, IN2, IN3, IN4 = machine.Pin(2), machine.Pin(3), machine.Pin(4), machine.Pin(5)

# Define the sequence for clockwise rotation
clockwise_seq = [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0],
                 [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1]]

# Constants for stepper motor
steps_per_revolution = 512
delay = 0.005

# Function to move the motor to a specific angle
def move_to_angle(angle_degrees):
    steps_needed = int((angle_degrees / 360) * steps_per_revolution)
    direction_seq = clockwise_seq[::-1] if steps_needed < 0 else clockwise_seq
    
    for _ in range(abs(steps_needed)):
        for i in range(8):
            for pin, state in zip([IN1, IN2, IN3, IN4], direction_seq[i]):
                pin.value(state)
            time.sleep(delay)

# Move the motor to a specific angle (e.g., 90 degrees)
target_angle = 180
# Change this to your desired angle
move_to_angle(target_angle)

# Cleanup GPIO
for pin in [IN1, IN2, IN3, IN4]:
    pin.value(0)