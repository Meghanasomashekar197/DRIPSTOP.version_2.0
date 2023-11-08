import machine
import sdcard
import uos

CS = machine.Pin(9, machine.Pin.OUT)
spi = machine.SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=machine.SPI.MSB, sck=machine.Pin(10), mosi=machine.Pin(11), miso=machine.Pin(8))

sd = sdcard.SDCard(spi, CS)

vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

# Replace "/sd/your_file.txt" with the actual path to your file
file_path = "/sd/your_file.txt"

# Open the file for reading
with open(file_path, "r") as file:
    line_count = 0

    # Read the file line by line and count the lines
    for line in file:
        line_count += 1

# Print the number of lines
print("Number of lines in the file:", line_count)