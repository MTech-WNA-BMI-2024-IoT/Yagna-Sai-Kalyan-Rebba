import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
import time

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

# Initialize LCD.
lcd = CharLCD('PCF8574', 0x27)

# Clear the LCD display.
lcd.clear()

# Print the message.
message = "My name is\nYagna Sai Kalyan Rebba"
lcd.write_string(message)

# Wait for 5 seconds
time.sleep(5)

# Clear the LCD display.
lcd.clear()
