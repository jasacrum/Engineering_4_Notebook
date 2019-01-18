from picamera import PiCamera
import time
from time import sleep

myCamera = PiCamera()

myCamera.start_preview(fullscreen=False,window=(100,200,300,400))
myCamera.start_recording('/home/pi/video.h264')

time.sleep(10)

myCamera.stop_recording()
myCamera.stop_preview()
