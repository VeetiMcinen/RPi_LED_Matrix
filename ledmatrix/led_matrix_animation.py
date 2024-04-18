from rpi_ws281x import Color #type: ignore
import time
import random
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

def draw(character, strip=strip, set_color=False, shuffle_animation=False, reverse_animation=False, wait_time=0):
    clearstrip()  # Ensure the strip is cleared before setting new pixels
    colors = set_color if set_color else randomcolor()

    if reverse_animation and shuffle_animation:
        print("Cannot reverse and shuffle at the same time")
        return

    if reverse_animation:
        character.reverse()
    
    if shuffle_animation:
        random.shuffle(character)
    
    for row, col in character:
        led_index = row * 8 + col
        strip.setPixelColor(led_index, Color(colors[0], colors[1], colors[2]))
        if wait_time != 0:
            strip.show()
            time.sleep(wait_time)
    if wait_time == 0:
        strip.show()

def graph_function(equation, strip=strip):
    default_coordinates = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),
                           (6,7),(7,7),(7,0),(7,1),(7,2),(7,3),
                           (7,4),(7,5),(7,6),(7,7)]

strip.begin()
