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
for item in coordinates:
    print(f"Coordinate ({item[0]}, {item[1]}) maps to index {item[2]} in the LED matrix, initial state: {item[3]}.")

# Example of how to update a specific LED state
# If you want to turn on the LED at coordinate (0, 0) which corresponds to the center of the matrix
center_index = (3 - 0) * matrix_size + (0 + 3)
led_matrix[center_index] = True  # Set the LED state to True in the 1D representation

# Update the corresponding entry in the 'coordinates' list
for coord in coordinates:
    if coord[2] == center_index:
        coord[3] = True  # Update the state in the structured list

print(f"Updated state of index {center_index}: {led_matrix[center_index]}")
