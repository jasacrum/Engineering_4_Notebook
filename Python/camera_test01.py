from picamera import PiCamera
import time
from time import sleep

myCamera = PiCamera()

myCamera.start_preview(fullscreen=False,window=(100,200,300,400))
time.sleep(5)
myCamera.stop_preview()
