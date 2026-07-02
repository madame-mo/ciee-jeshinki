from mpu6050 import mpu6050
import time

# Create a new Mpu6050 object
mpu6050 = mpu6050(0x68)

# Define a function to read the sensor data
def read_sensor_data():
    # Read the accelerometer values
    accelerometer_data = mpu6050.get_accel_data()

    # Read the gyroscope values
    gyroscope_data = mpu6050.get_gyro_data()

    # Read temp
#    temperature = mpu6050.get_temp()

    return accelerometer_data, gyroscope_data 
#, temperature

# Start a while loop to continuously read the sensor data
