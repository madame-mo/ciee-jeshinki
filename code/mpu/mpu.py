#This is mpu6050 sensor
from mpu6050 import mpu6050
from mpu6050 import mpu6050
import time
import math

#if is over 1.5 the buzzer will beep
SENSITIVITY = 1.5

# Create the MPU6050 object
sensor = mpu6050(0x68)

# Store the previous accelerometer reading
previous_accel = None


def read_sensor_data():
    """
    Reads the accelerometer and gyroscope data.
    Returns:
        accelerometer_data (dict)
        gyroscope_data (dict)
    """
    accelerometer_data = sensor.get_accel_data()
   # gyroscope_data = sensor.get_gyro_data()

    return accelerometer_data, gyroscope_data

#This is definding is shaking or not
def is_shaking(sensitivity):
    """
    0.2 - very sensitive
    0.5 - sensitive
    1.0- moderate
    1.5 and 2 are less sensative
    3.0 -for strong shaking

    
    Lower values = more sensitive.
    Higher values = less sensitive.

    """
    global previous_accel

    accel, _ = read_sensor_data()

    if previous_accel is None:
        previous_accel = accel
        return False

    dx = accel["x"] - previous_accel["x"]
    dy = accel["y"] - previous_accel["y"]
    dz = accel["z"] - previous_accel["z"]

    # change in magnitude of acceleration to detect the shaikng
    change = math.sqrt(dx**2 + dy**2 + dz**2)
    previous_accel = accel

    return change > sensitivity


#we can create a variable in the main method called SHAKING and if it's true then
#  it breaks out of the While True loop and runs the table detection method



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
