import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

# Initialize I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize LCD with MCP23017 I2C expander.
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, address=0x27)

# Clear the LCD display.
lcd.clear()

# Print the message.
message = "My name is\nYagna Sai Kalyan Rebba"
lcd.message = message
