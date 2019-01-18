import time

import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lsm303 = Adafruit_LSM303.LSM303()

RST = 24

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw.ellipse((0,0,width,height), outline=0, fill=0)  

padding = 2
shape_width = 20
top = padding
x = padding


font = ImageFont.load_default()

while True:

    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    print(int(accel_x/20))
    draw.ellipse((64-int(accel_x/20)/2,32-int(accel_x/20)/2,64+int(accel_x/20)/2,32+int(accel_x/20)/2), outline=0, fill=100)

    disp.image(image)
    disp.display()
    time.sleep(0.1)
    disp.clear()
