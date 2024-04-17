
import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD
import spidev
import os
# Define columns and rows of the display
lcd_columns = 16
lcd_rows = 2
# Initialize the display
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)
# Configure the SPI bus
spi = spidev.SpiDev()
spi.open(0,1)
spi.max_speed_hz = 1000000
class ButtonMatrix():
    def __init__(self):
        self.calculated = ""
        GPIO.setmode(GPIO.BCM)
        self.key_channel = 4
        self.delay = 0.1
        self.adc_key_val = [30,90,160,230,280,330,400,470,530,590,650,720,780,840,890,960]
        self.key = -1
        self.oldkey = -1
        self.num_keys = 16
        self.indexes = {
            12:1,
            13:2,
            14:3,
            15:4,
            10:7,
            9:6,
            8:5,
            11:8,
            4:9,
            5:10,
            6:11,
            7:12,
            0:13,
            1:14,
            2:15,
            3:16
        }
    def ReadChannel(self,channel):
        # Read data from the MCP3008 chip over SPI
        adc = spi.xfer2([1, (8+channel)<<4, 0])
        data = ((adc[1]&3) << 8) + adc[2]
        return data
    def GetAdcValue(self):
        adc_key_value = self.ReadChannel(self.key_channel)
        return adc_key_value
    def GetKeyNum(self, adc_key_value):
        for num in range(0,16):
            if adc_key_value < self.adc_key_val[num]:
                return num
        if adc_key_value >= self.num_keys:
            num = -1
            return num
    def activateButton(self, btnIndex):
        # Retrieve index over SPI
        btnIndex = int(btnIndex)
        # Correct index to a better format
        btnIndex = self.indexes[btnIndex]
        # Execute calculation function
        self.calculate(btnIndex)
        print("Button %s pressed" % btnIndex)
        # Suppress key presses that are too quick in succession
        time.sleep(0.3)
        return self.calculated
    def calculate(self, btnIndex):
        # Retrieve index over SPI
        btnIndex = int(btnIndex)
        # Numbers
        if(btnIndex == 1):
            self.calculated += "7"
        elif(btnIndex == 2):
            self.calculated += "8"
        elif(btnIndex == 3):
            self.calculated += "9"
        elif(btnIndex == 5):
            self.calculated += "4"
        elif(btnIndex == 6):
            self.calculated += "5"
        elif(btnIndex == 7):
            self.calculated += "6"
        elif(btnIndex == 9):
            self.calculated += "1"
        elif(btnIndex == 10):
            self.calculated += "2"
        elif(btnIndex == 11):
            self.calculated += "3"
        elif(btnIndex == 13):
            self.calculated += "0"
        # Reset
        elif(btnIndex == 14):
            self.calculated = ""
        # Functions
        elif(btnIndex == 12):
            self.calculated += "+"
        elif(btnIndex == 16):
            self.calculated += "-"
        elif(btnIndex == 4):
            self.calculated += "*"
        elif(btnIndex == 8):
            self.calculated += "/"
        elif(btnIndex == 15):
            # calculate
            self.calculated = str(eval(self.calculated))
            return self.calculated
# Initialize button matrix
buttons = ButtonMatrix()
# Turn on backlight
lcd.set_backlight(0)
while True:
    # Retrieve key press over SPI
    adc_key_value = buttons.GetAdcValue()
    key = buttons.GetKeyNum(adc_key_value)
    if key != buttons.oldkey:
        time.sleep(0.05)
        adc_key_value = buttons.GetAdcValue()
        key = buttons.GetKeyNum(adc_key_value)
        if key != buttons.oldkey:
            oldkey = key
            if key >= 0:
                calculated = buttons.activateButton(key)
                print(calculated)
                # Clear LCD before displaying new value
                lcd.clear()
                # Display calculated value on LCD
                lcd.message(calculated)
