# Author: Qin Siyuan
# Date: 2025-04-02
# Description: This program controls an LED connected to GPIO pin 18 on a Raspberry Pi.
# It turns the LED on for 1 second and then turns it off.

import RPi.GPIO as GPIO   # Import the Raspberry Pi GPIO library
import time               # Import the time module for delays

GPIO.setmode(GPIO.BCM)    # Use Broadcom pin numbering
GPIO.setwarnings(False)   # Disable GPIO warnings
GPIO.setup(18,GPIO.OUT)   # Set GPIO 18 as an output pin

print ("LED on")          # Display message indicating the LED is turned on
GPIO.output(18,GPIO.HIGH) # Set GPIO 18 to high, turning the LED on
time.sleep(1)             # Wait for 1 second
print ("LED off")         # Display message indicating the LED is turned off
GPIO.output(18,GPIO.LOW)  # Set GPIO 18 to low, turning the LED off
