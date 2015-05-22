import picamera
import time

camera = picamera.PiCamera()

i = 0
while True:
	camera.capture('foto' + str(i) + '.jpg')
	i = i + 1
	time.sleep(10)
