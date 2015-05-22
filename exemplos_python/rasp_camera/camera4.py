import picamera

camera = picamera.PiCamera()
camera.brightness = 70
camera.vflip = True
camera.hflip = True
camera.saturation = 60

camera.capture('foto_config.jpg')
