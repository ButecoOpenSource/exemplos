import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_15", GPIO.OUT)
GPIO.output("P9_15", GPIO.HIGH)
time.sleep(2)
GPIO.cleanup()
