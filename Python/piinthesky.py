import RPi.GPIO as gpio
import time 
import datetime
import Adafruit_LSM303, math
#from datetime import date
#from datetime import time
#from datetime import datetime
# Import the LSM303 module.
lsm303 = Adafruit_LSM303.LSM303()
# These import all of the Pi components we need for the code
#GPIO.setmode(GPIO.BCM)

#GPIO.setwarnings(False)

#alarmpin = 27

filename = "acceldata"+str(datetime.datetime.now())+".txt"
#This is the file data will go to
file = open(filename,"w+")
for i in range (0,250):
#while True: 

    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    #Accelerometer to start reading the data
    
    file.write('Accel X={0}, Accel Y={1}, Accel Z={2}\n'.format(round(accel_x/105.0,2), round(accel_y/105.0, 2), round(accel_z/105.0, 2)))
    print('Accel X={0}, Accel Y={1}, Accel Z={2}'.format(accel_x, accel_y, accel_z))
    file.write('Total Acceleration =' .format( + math.sqrt(math.pow(round(accel_x/105.0,2),2) + math.pow(round(accel_y/105.0, 2),2) + math.pow(round(accel_z/105.0, 2),2))))
    print('Total Acceleration =' .format( + math.sqrt(math.pow(round(accel_x/105.0,2),2) + math.pow(round(accel_y/105.0, 2),2) + math.pow(round(accel_z/105.0, 2),2))))
    #  Take all of the X, Y, and Z data and print them out
    time.sleep(0.1)
    # Repeat after .1 seconds
file.close()
#Stops the code after 
