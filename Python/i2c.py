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

padding = 2
shape_width = 20
top = padding
x = padding


while True:
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    draw.text((x, top),    'ACCEL DATA',  font=font, fill=255)
    draw.text((x, top + 15), 'X:' + str(accel_x/100), font=font, fill=255)
    draw.text((x, top + 30), 'y:' + str(accel_y/100), font=font, fill=255)
    draw.text((x, top + 45), 'z:' + str(accel_z/100), font=font, fill=255)
    disp.clear()
    time.sleep(0.5)

    disp.image(image)
    disp.display()
    time.sleep(0.5)
