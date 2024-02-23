from gpiozero import CharacterLCD
from gpiozero.tools import text

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

# Initialize LCD.
lcd = CharacterLCD(rs=26, e=19, d4=13, d5=6, d6=5, d7=11, cols=lcd_columns, rows=lcd_rows)

# Clear the LCD display.
lcd.clear()

# Print the message.
message = "My name is\nYagna Sai Kalyan Rebba"
lcd.text = message

# Wait for 5 seconds
lcd.wait_for_text()

# Clear the LCD display.
lcd.clear()
