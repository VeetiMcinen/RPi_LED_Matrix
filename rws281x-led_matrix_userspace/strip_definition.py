from rpi_ws281x import PixelStrip, Color # type: ignore
LED_COUNT = 64 # Number of LEDs.
LED_PIN = 12 # GPIO pin used
LED_FREQ_HZ = 800000 # Signal frequency
LED_DMA = 10 # DMA channel
LED_BRIGHTNESS = 15 # Set LED brightness from 0-255
LED_INVERT = False
LED_CHANNEL = 0
RIGHT_BORDER = [7,15,23,31,39,47,55,63]
LEFT_BORDER = [0,8,16,24,32,40,48,56]
character_matrix = [[False for _ in range(8)] for _ in range(8)]
graphing_matrix = []
# Generate coordinates for y from 3 to -3 (inclusive)
for y in range(4, -5, -1):  # Start from 3, stop at -3, step by -1
    for x in range(-4, 5):  # x ranges from -3 to 3
        graphing_matrix.append([x, y, False])

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
