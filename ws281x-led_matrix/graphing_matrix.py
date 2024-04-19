from rpi_ws281x import PixelStrip, Color
import random

# LED matrix and strip configuration
LED_COUNT = 64  # Total number of LEDs in an 8x8 matrix
LED_PIN = 12  # GPIO pin connected to the pixels (must support PWM)
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800kHz)
LED_DMA = 10  # DMA channel to use for generating signal
LED_BRIGHTNESS = 15  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # Set to '1' for GPIOs 13, 19, 41, 45 or 53, otherwise '0'

# Initialize the LED strip
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# Matrix dimensions for the physical LED matrix
full_matrix_size = 8  # 8x8 physical matrix
adjusted_matrix_size = 7  # Logical operation within 7x7 matrix

# Create a list to represent the matrix, initializing all to False
led_matrix = [False] * (full_matrix_size * full_matrix_size)

# Generate coordinates and corresponding indices
coordinates = []
for y in range(-3, 4):  # Logical y-coordinates
    for x in range(-3, 4):  # Logical x-coordinates
        index = (y + 3) * full_matrix_size + (x + 3)
        coordinates.append([x, y, index, False])  # Include x, y, index, and initial state (False)

def calculate(equation, strip):
    pixels_to_render = []

    def evaluate_equation(x):
        # Evaluate the equation safely with error handling
        try:
            result = eval(equation)
            if -3 <= result <= 3:
                return result
        except Exception:
            return None

    for x in range(-3, 4):
        y = evaluate_equation(x)
        if y is not None:
            index = (3 - y) * full_matrix_size + (x + 3)
            if 0 <= index < len(led_matrix):
                led_matrix[index] = True
                strip.setPixelColor(index, Color(255, 255, 255))  # Setting color to white for demonstration
                for coord in coordinates:
                    if coord[2] == index:
                        coord[3] = True  # Update the state

    strip.show()
    return [(c[0], c[1], c[2]) for c in coordinates if c[3]]  # Collect all turned on LED coordinates

# Example usage
print(calculate("(x**2)", strip))

def random_color():
    return Color(random.randrange(0, 255, 15), random.randrange(0, 255, 15), random.randrange(0, 255, 15))
