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
#graphing_strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)


#TODO LIST: Graph function, highlight x and y coordinates

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

# Optional: Print to check the mapping and initial states

# Example of how to update a specific LED state
# If you want to turn on the LED at coordinate (0, 0) which corresponds to the center of the matrix
x_coordinate = 0
y_coordinate = 0
center_index = (3 - x_coordinate) * matrix_size + (y_coordinate + 3)
led_matrix[center_index] = True  # Set the LED state to True in the 1D representation

# Update the corresponding entry in the 'coordinates' list
print(center_index)
for coord in coordinates:
    if coord[2] == center_index:
        coord[3] = True  # Update the state in the structured list


for coordinate in coordinates:
    if coordinate[3]:
        print(f"({coordinate[0]}, {coordinate[1]})")