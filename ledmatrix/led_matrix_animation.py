from rpi_ws281x import Color #type: ignore
import time
import random
from Drawings import * #Maybe remove?
from strip_definition import strip, led_matrix

# LED module configuration:

def randomcolor():
    colors = [255, random.randrange(0, 255, 15), random.randrange(0, 255, 15)]
    random.shuffle(colors)
    return colors

def clearstrip():
    for counter in range(64):
        strip.setPixelColor(counter, Color(0, 0, 0))
    strip.show()

def draw(coordinates, strip=strip, set_color=False, shuffle_animation=False, reverse_animation=False, wait_time=0):
    clearstrip()  # Ensure the strip is cleared before setting new pixels

    colors = set_color if set_color else randomcolor()

    if reverse_animation and shuffle_animation:
        print("Cannot reverse and shuffle at the same time")
        return

    if reverse_animation:
        coordinates.reverse()
    
    if shuffle_animation:
        random.shuffle(coordinates)
    
    for row, col in coordinates:
        led_index = row * 8 + col
        strip.setPixelColor(led_index, Color(colors[0], colors[1], colors[2]))
        if wait_time != 0:
            strip.show()
            time.sleep(wait_time)
    if wait_time == 0:
        strip.show()

strip.begin()
