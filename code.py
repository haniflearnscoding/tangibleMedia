"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel
import analogio



#pin mapping
pixel_pin = board.GP0
sensor = analogio.AnalogIn(board.GP26)

num_pixels = 8
# RGBW
ORDER = neopixel.GRB

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

#create led object
num_pixels = 8
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER)

def get_voltage():
    voltage = sensor.value // 655  # Scale the analog value (0-65535) into a smaller range
    print(f"DEBUG:Voltage: {voltage}")

    intensity = int(voltage * 255 / 100) # Scale voltage to from 0-100 to 0-255
    print(f"DEBUG: Intensity: {intensity}")

    base_color = (intensity, 0, 0)  # Dynamic RED intensity
    for i in range(num_pixels):
        pixels[i] = base_color # For each pixel on trip set base color

    pixels.show()
while True:
    get_voltage()
    time.sleep(0.1)

