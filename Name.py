from gpiozero import Device, MCP23017
from RPLCD.i2c import CharLCD

# Set up MCP23017 as a backend for gpiozero
Device.pin_factory = MCP23017

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

# Initialize MCP23017
mcp = MCP23017()

# Initialize LCD.
lcd = CharLCD(i2c_expander=mcp, address=0x27, port=1, cols=lcd_columns, rows=lcd_rows)

# Clear the LCD display.
lcd.clear()

# Print the message.
message = "My name is\nYagna Sai Kalyan Rebba"
lcd.write_string(message)

# Wait for 5 seconds
lcd.cursor_pos = (0, 0)
lcd.blink = True
lcd.cursor_mode = 'hide'
lcd.autoscroll = True
lcd.write_string(' ' * (lcd_columns * lcd_rows))

# Clear the LCD display.
lcd.close(clear=True)
