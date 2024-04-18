
# LED Matrix Display Project

## Project Overview
This project controls a 7x7 LED matrix display using a Python script to represent mathematical equations visually. The LEDs can be individually controlled to display the output of an equation graphed across a defined coordinate system ranging from -3 to 3 on both the x and y axes.

## Hardware Requirements
- **Raspberry Pi**: Any model that supports Python and GPIO pin output.
- **7x7 LED Matrix**: WS281x LED strip configured in a 7x7 matrix.
- **Power Supply**: Adequate to power the Raspberry Pi and the LED matrix.
- **Connecting Wires**: For connecting the LED matrix to the Raspberry Pi GPIO pins.

## Software Dependencies
- **Python 3.x**: The main programming language used for the script.
- **rpi_ws281x Library**: A Python library to control Raspberry Pi GPIO pins specifically for driving WS281x LEDs.

## Installation
1. **Set up your Raspberry Pi**: Install the latest version of Raspberry Pi OS and ensure it has network connectivity.
2. **Install Python**: Python 3.x is usually pre-installed on Raspberry Pi OS; verify this by running `python3 --version`.
3. **Install rpi_ws281x Library**:

    ```bash
   sudo pip3 install rpi_ws281x
   ```
   
5. **Connect the LED Matrix**: Connect the data input of your LED matrix to the designated GPIO pin on your Raspberry Pi. Please ensure your ground connections are secure and your power supply is good and connected.

## Configuration
Edit the Python script to match your hardware setup, specifically the `LED_PIN` variable to match the GPIO pin connected to the LED matrix.

## Usage
Run the script with:
Configure the functions you wish to draw in main and then run the file with
```bash
python3 main.py
```

This will start the program, which listens for equation inputs and displays the results dynamically on the LED matrix.

## Contributing
Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.

## License
This project is released under the MIT License. See the `LICENSE` file for more details.

## Authors
- **Veeti Mäkinen** - *Programming* - [Github](https://github.com/VeetiMcinen)
- **Aaro Aleksejev** - *Graphic design*

## Acknowledgments
- Kampf Group
