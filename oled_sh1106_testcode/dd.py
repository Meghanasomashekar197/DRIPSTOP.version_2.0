import machine
import sdcard
import uos

# Initialize the SD card
CS = machine.Pin(9, machine.Pin.OUT)
spi = machine.SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=machine.SPI.MSB, sck=machine.Pin(10), mosi=machine.Pin(11), miso=machine.Pin(8))
sd = sdcard.SDCard(spi, CS)
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

# File path for data.txt
file_path = "/sd/data.txt"

# Check if the file exists, and create it if it doesn't
if not "data.txt" in uos.listdir("/sd"):
    with open(file_path, "w") as file:
        print("Created data.txt on the SD card")

# Open the file for reading
with open(file_path, "r") as file:
    line_count = 0

    # Read the file line by line and count the lines
    for line in file:
        line_count += 1

    # Print the number of lines
    print("Number of lines in the file:", line_count)

# Open the file for appending (writing)
with open(file_path, "a") as file:
    # Data to write to the file
    new_data = ["This is a new line.", "Another new line.", "One more new line."]

    # Write the new data to the file and count the lines
    for line in new_data:
        file.write(line + "\n")
        line_count += 1

    # Print the updated number of lines
    print("Updated number of lines in the file:", line_count)

# Open the file for reading
with open(file_path, "r") as file:
    data = file.read()
    print("Data in the file:")
    print(data)
