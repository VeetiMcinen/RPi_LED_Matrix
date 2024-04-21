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

GRAPHING_LED_COUNT = 49  # Total number of LEDs in a 7x7 matrix
GRAPHING_LED_PIN = 12  # GPIO pin connected to the pixels (must support PWM)
GRAPHING_LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800kHz)
GRAPHING_LED_DMA = 10  # DMA channel to use for generating signal (try 10)
GRAPHING_LED_BRIGHTNESS = 15  # Set to 0 for darkest and 255 for brightest
GRAPHING_LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
GRAPHING_LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53, otherwise '0'
# Define borders based on a 0-indexed system for a 7x7 matrix
GRAPHING_RIGHT_BORDER = [6, 13, 20, 27, 34, 41, 48]  # Last column of each row in 7x7
GRAPHING_LEFT_BORDER = [0, 7, 14, 21, 28, 35, 42]
character_matrix = [[False for _ in range(8)] for _ in range(8)]
strip = PixelStrip(LED_COUNT, 
                   LED_PIN, 
                   LED_FREQ_HZ, 
                   LED_DMA, 
                   LED_INVERT, 
                   LED_BRIGHTNESS, 
                   LED_CHANNEL)

graphing_strip = PixelStrip(GRAPHING_LED_COUNT, 
                            GRAPHING_LED_PIN, 
                            GRAPHING_LED_FREQ_HZ, 
                            GRAPHING_LED_DMA, 
                            GRAPHING_LED_BRIGHTNESS, 
                            GRAPHING_LED_INVERT, 
                            GRAPHING_LED_CHANNEL, 
                            GRAPHING_RIGHT_BORDER, 
                            GRAPHING_LEFT_BORDER)
