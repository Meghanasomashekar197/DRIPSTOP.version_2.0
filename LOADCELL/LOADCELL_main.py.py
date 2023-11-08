from machine import Pin
from hx711 import HX711

# Define the GPIO pins for the HX711 module
dout_pin = 12  # GPIO pin connected to DOUT on HX711
pd_sck_pin = 13  # GPIO pin connected to PD_SCK on HX711


# Initialize the HX711 driver
load_cell = HX711(d_out=dout_pin, pd_sck=pd_sck_pin)

# Set the channel and gain for the load cell
load_cell.channel = HX711.CHANNEL_B_32

# Read and print weight data
while True:
    try:
        # Read weight data from the load cell (in grams)
        weight = load_cell.read()
        
        # Print the weight
        print('Weight:', weight, 'g')
    except KeyboardInterrupt:
        # Exit the loop if Ctrl+C is pressed
        break
    except Exception as e:
        # Handle any exceptions that may occur
        print('Error:', e)

# Power off the HX711 when done (optional)
load_cell.power_off()
