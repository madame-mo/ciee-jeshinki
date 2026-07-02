from code/motor/car.py import *
from code/mpu/mpu_checking.py import *
import time

while True:

    accelerometer_data = read_sensor_data()

    print("Accelerometer:", accelerometer_data)
    #we dont gotta use the gyroscope data
    #print("Gyroscope:", gyroscope_data)

    if is_shaking(SENSITIVITY):
        print(" SHAKING DETECTED! ")
        #RUN THE METHOD TO DETECT THE TABLE!!
    else:
        print("Not shaking.")
        #nothing

    print()

    time.sleep(0.1)

right_turn();

time.sleep(1)

forward();

time.sleep(1)

drive.close()

#if movement detected
#buzzer beep on
#activate voice line

#while no table detected
#turn in circle until table found
#if computer vision detects table, (move towards table, how?)
#if under table buzzer off, voice line change ("please hide under the nearest table")
#flashing lights? 

#check for movement stopped
#if movement stopped, voice line "proceed safely"




