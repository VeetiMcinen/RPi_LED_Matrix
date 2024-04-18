#from rpi_ws281x import PixelStrip, Color
LED_COUNT = 49  # Total number of LEDs in a 7x7 matrix
LED_PIN = 12  # GPIO pin connected to the pixels (must support PWM)
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800kHz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 15  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53, otherwise '0'
# Define borders based on a 0-indexed system for a 7x7 matrix
RIGHT_BORDER = [6, 13, 20, 27, 34, 41, 48]  # Last column of each row in 7x7
LEFT_BORDER = [0, 7, 14, 21, 28, 35, 42]  # First column of each row in 7x7
#graphing_strip = Pixelstrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)


#TODO LIST: impliment render function into strip, highlight x and y coordinates, clearstrip,


def render(equation:str):
    pixels_to_render = []
    
    def evaluate_equation(x):
        # Evaluate the equation safely with error handling
        try:
            result = eval(equation)
            return result
        except Exception as e:
            print(f"Error evaluating equation: {e}")
            return None  # Return None if there's an error

    for x in range(-3, 4):
        y = evaluate_equation(x)
        if y is not None and -3 <= y <= 3:  # Ensure y is within the valid range
            result_index = (3 - y) * matrix_size + (x + 3)
            if 0 <= result_index < len(led_matrix):  # Check index bounds
                led_matrix[result_index] = True  # Set the LED state to True
                # Update the corresponding entry in the 'coordinates' list
                for coord in coordinates:
                    if coord[2] == result_index:
                        coord[3] = True  # Update the state

    # Collect all turned on LED coordinates
    for coordinate in coordinates:
        if coordinate[3]:
            pixels_to_render.append((coordinate[0], coordinate[1]))  # Append as a tuple

    return pixels_to_render

matrix_size = 7
# Create a list to represent the matrix, each entry starts with False
led_matrix = [False] * (matrix_size * matrix_size)

# Generate coordinates for y from 3 to -3 (inclusive)
coordinates = []
for y in range(3, -4, -1):  # y starts at 3 and decreases to -3
    for x in range(-3, 4):  # x starts at -3 and increases to 3
        # Calculate the index for the 1D list
        index = (3 - y) * matrix_size + (x + 3)
        # Append the coordinate along with its initial state (False) and its index
        coordinates.append([x, y, index, False])  # Include the boolean value as the fourth element


equation = "3*x"
print(render(equation))


