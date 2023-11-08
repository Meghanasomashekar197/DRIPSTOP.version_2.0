import machine
import sdcard
import uos

CS = machine.Pin(9, machine.Pin.OUT)
spi = machine.SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=machine.SPI.MSB, sck=machine.Pin(10), mosi=machine.Pin(11), miso=machine.Pin(8))

sd = sdcard.SDCard(spi, CS)

vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

# Create a file and write something to it
with open("/sd/data.txt", "w") as file:
    print("Writing to data.txt...")
    #file.write("\n")
    file.write("Welcome to microcontrollerslab!\r\n")
    file.write("This is a test\r\n")
    file.write("work\r\n")
    file.write("life\r\n")
    file.write("balance\r\n")
# Important: Create a filesystem on the SD card if it's not already formatted
if not "data.txt" in uos.listdir("/sd"):
    uos.mkfs("/sd")

with open("/sd/data.txt", "r") as file:
    print("Reading data.txt...")    
    data = file.read()
    print(data)


# Open the file we just created and read from it
with open("/sd/data.txt", "r") as file:
    print("Reading data.txt...")    
    lines = file.readlines()
    print(lines)
    
lines.append('Replaced text\r\n') 

with open("/sd/data.txt", 'w') as file:
    
    for item in lines:
        file.write(item)


with open("/sd/data.txt", "r") as file:
    print("Reading data.txt...")    
    data = file.read()
    print(data)