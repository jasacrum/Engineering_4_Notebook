from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

now = datetime.now()
filename = "{0:%Y}-{0:%m}-{0:%d}".format(now) 
camera = PiCamera()
pir = MotionSensor(23)

while True:
    pir.wait_for_motion()
    camera.start_preview(fullscreen=False,window=(100,200,300,400))
    camera.start_recording('/home/pi/Jackspiriosity.h264')
    pir.wait_for_no_motion()
    camera.stop_recording()
    camera.stop_preview()

