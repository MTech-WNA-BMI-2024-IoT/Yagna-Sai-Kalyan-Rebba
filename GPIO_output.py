import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set GPIO pin 18 as output
GPIO.setup(18, GPIO.OUT)

# Blink the LED 5 times
for _ in range(5):
    GPIO.output(18, GPIO.HIGH)  # Turn on LED
    time.sleep(1)                # Wait for 1 second
    GPIO.output(18, GPIO.LOW)   # Turn off LED
    time.sleep(1)                # Wait for 1 second

# Clean up GPIO
GPIO.cleanup()
