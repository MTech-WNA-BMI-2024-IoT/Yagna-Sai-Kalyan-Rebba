import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
import time

lcd = CharLCD('PCF8574', 0x27)
lcd.clear()
lcd.write_string("Hello, LCD!")
time.sleep(5)
lcd.clear()
