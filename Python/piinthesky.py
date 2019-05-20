import RPi.GPIO as gpio
import time
import datetime
import Adafruit_LSM303, math
#import Adafruit_SSD1306

lsm303 = Adafruit_LSM303.LSM303()

#GPIO.setmode(GPIO.BCM)

#GPIO.setwarnings(False)

#alarmpin = 27

filename = "acceldata"+str(datetime.datetime.now())+".txt"
file = open(filename,"w+")
for i in range (0,250):
#while True: 

    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag

    file.write('Accel X={0}, Accel Y={1}, Accel Z={2}\n'.format(round(accel_x/105.0,2), round(accel_y/105.0, 2), round(accel_z/105.0, 2)))
    print('Accel X={0}, Accel Y={1}, Accel Z={2}'.format(accel_x, accel_y, accel_z))
    file.write('Total Acceleration =' .format( + math.sqrt(math.pow(round(accel_x/105.0,2),2) + math.pow(round(accel_y/105.0, 2),2) + math.pow(round(accel_z/105.0, 2),2))))
    print('Total Acceleration =' .format( + math.sqrt(math.pow(round(accel_x/105.0,2),2) + math.pow(round(accel_y/105.0, 2),2) + math.pow(round(accel_z/105.0, 2),2))))
          
    time.sleep(0.1)
          
file.close()

