#!/usr/bin/env python

# Import required libraries
import time
import RPi.GPIO as GPIO

# Disable GPIO warnings
GPIO.setwarnings(False)

# Use BOARd GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BOARD)

# Setup pins
RPIO.setup(40, RPIO.OUT)

while True:
  RPIO.output(40, True)
  time.sleep(0.0015)
  RPIO.output(40, False)
  time.sleep(2)

# Clear all pins
GPIO.cleanup();
