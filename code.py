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

def get_voltage():
    voltage = sensor.value  # Scale the analog value (0-65535) into a smaller range
    print(f"DEBUG: voltage_note_keyboard() - Voltage: {voltage}")

    # Map voltage to one of 5 notes
    if voltage > 6500:
        return color_chase(RED, 0.1)
    elif voltage > 4000:
        return color_chase(YELLOW, 0.1)
        # return audible_notes["NOTE_D4"]
    elif voltage > 3500:
        return color_chase(GREEN, 0.1)
        # return audible_notes["NOTE_E4"]
    elif voltage > 2500:
        return color_chase(CYAN, 0.1)
        # return audible_notes["NOTE_G4"]
    else:
        return color_chase(BLUE, 0.1)
        # return audible_notes["NOTE_A4"]

#create led object
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER)


def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)




while True:
    get_voltage()
    #shows red green blue
    # pixels.fill(RED)
    # pixels.show()
    # # Increase or decrease to change the speed of the solid color change.
    # time.sleep(1)
    # pixels.fill(GREEN)
    # pixels.show()
    # time.sleep(1)
    # pixels.fill(BLUE)
    # pixels.show()
    # time.sleep(1)



    #color chase, requires color and time
    # color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    # color_chase(YELLOW, 0.1)
    # color_chase(GREEN, 0.1)
    # color_chase(CYAN, 0.1)
    # color_chase(BLUE, 0.1)
    # color_chase(PURPLE, 0.1)

    # #rainbow, requires time - 0 meaning as fast as possible
    # rainbow_cycle(0)
