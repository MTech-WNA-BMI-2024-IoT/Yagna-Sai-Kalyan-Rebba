import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
import time

lcd = CharLCD('PCF8574', 0x27)

try:
    lcd.clear()
    lcd.write_string("LCD is working!")
    time.sleep(5)
    lcd.clear()
finally:
    GPIO.cleanup()
