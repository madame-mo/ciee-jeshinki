from code/motor/car.py import *
from code/mpu/mpu_checking.py import *
import time

while True:

    # Read the sensor data
    accelerometer_data, gyroscope_data = read_sensor_data()

    # Print the sensor data
    print("Accelerometer data:", accelerometer_data)
    print("Gyroscope data:", gyroscope_data)
 #   print("Temp:", temperature)

    # Wait for 1 second
    time.sleep(1)

left_turn()
time.sleep(1)
forward_move()
time.sleep(1)
right_turn()
time.sleep(1)
backward_move()
time.sleep(1)
stop()

#drive.close()

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




