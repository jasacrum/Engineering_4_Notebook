from picamera import PiCamera
import time
from time import sleep

myCamera = PiCamera()

myCamera.start_preview(fullscreen=False,window=(100,200,300,400))

myeffect = ['cartoon', 'watercolor', 'washedout', 'denoise', 'solarize']

for effect in myCamera.IMAGE_EFFECTS:
    myCamera.image_effect = effect
    myCamera.annotate_text = "Effect: %s" % effect
    time.sleep(5)

    if effect in myeffect:
        myCamera.capture("filename" + str(myeffect.index(effect)) + ".jpg")
        
myCamera.stop_preview()
