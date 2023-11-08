import machine
import sdcard
import uos

CS = machine.Pin(9, machine.Pin.OUT)
spi = machine.SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=machine.SPI.MSB, sck=machine.Pin(10), mosi=machine.Pin(11), miso=machine.Pin(8))

sd = sdcard.SDCard(spi, CS)

vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

file_path = "/sd/your_file.txt"

# Open the file for writing, which effectively clears its contents
with open(file_path, "w") as file:
    pass  # An empty pass statement effectively clears the file

print("File contents have been cleared.")
