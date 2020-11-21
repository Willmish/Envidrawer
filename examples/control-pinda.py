#!/usr/bin/env python3

import sys
import time
from concurrent.futures import ThreadPoolExecutor

import automationhat
time.sleep(0.1) # Short pause after ads1015 class creation recommended

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("""This example requires PIL.
Install with: sudo apt install python{v}-pil
""".format(v="" if sys.version_info.major == 2 else sys.version_info.major))
    sys.exit(1)

try:
    from fonts.ttf import RobotoBlackItalic as UserFont
except ImportError:
    print("""This example requires the Roboto font.
Install with: sudo pip{v} install fonts font-roboto
""".format(v="" if sys.version_info.major == 2 else sys.version_info.major))
    sys.exit(1)
import ST7735 as ST7735

print("""output.py

This Automation HAT Mini example toggles and displays the
status of the three 24V-tolerant digital outputs.

Press CTRL+C to exit.
""")

def draw_states(channels):
    # Open our background image.
    image = Image.open("images/outputs-blank.jpg")
    draw = ImageDraw.Draw(image)
    offset = 0

    # Draw the on/off state of each channel.
    for channel in range(len(channels)):
        if channels[channel].is_on():
            draw.ellipse((on_x, on_y + offset, on_x + dia, on_y + dia + offset), on_colour)

        else:
            draw.ellipse((off_x, off_y + offset, off_x + dia, off_y + dia + offset), off_colour)
        offset += 14

    reading = automationhat.analog[0].read()
    draw.text((text_x, text_y + 10), "{reading:.2f}".format(reading=reading), font=font, fill=colour)

    disp.display(image)


# Create ST7735 LCD display class.
disp = ST7735.ST7735(
    port=0,
    cs=ST7735.BG_SPI_CS_FRONT,
    dc=9,
    backlight=25,
    rotation=270,
    spi_speed_hz=4000000
)

# Initialize display.
disp.begin()

on_colour = (99, 225, 162)
off_colour = (235, 102, 121)
bg_colour = (25, 16, 45)
colour = (255, 181, 86)
font = ImageFont.truetype(UserFont, 22)

# Values to keep everything aligned nicely.
on_x = 115
on_y = 35

off_x = 46
off_y = on_y

dia = 10
# Values to keep everything aligned nicely.
text_x = 110
text_y = 34

def wait_for_input() -> str:
    return input("Write 'on' to turn PINDA on, 'off' to turn it off\n")

## Main Loop
offset = 0

on = True
timebefore = time.time()
# Turn capacitance sensor on and off every 5 s
while True:
    draw_states(automationhat.output())
    if (time.time() - timebefore >= 5):
        on = not on
        automationhat.output[0].write(on)
        timebefore = time.time()


