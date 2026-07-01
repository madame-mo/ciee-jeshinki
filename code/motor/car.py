from motor import MotorController
import time

drive = MotorController()

def left_turn():
        drive.set_motor_direction(front_left=0,rear_left=0,front_right=-1,rear_right=-1)

        drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)

def stop():
        drive.set_motors(front_left=0,rear_left=0,front_right=0,rear_right=0)

def right_turn():
        drive.set_motor_direction(front_left=-1,rear_left=-1,front_right=0,rear_right=0)

        drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)

def forward():
        drive.set_motor_direction(front_left=-1,rear_left=-1,front_right=-1,rear_right=-1)

        drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)

def backward():
        drive.set_motor_direction(front_left=1,rear_left=1,front_right=1,rear_right=1)

        drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)

def diagonal_L():
        drive.set_motor_direction(front_left=-1,rear_left=0,front_right=0,rear_right=-1)

        drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)

<<<<<<< HEAD:motor/car.py
def diagonal_R():
        drive.set_motor_direction(front_left=0,rear_left=-1,front_right=-1,rear_right=0)

        drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)

def diagonal_BL():
        drive.set_motor_direction(front_left=1,rear_left=0,front_right=0,rear_right=1)

        drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)

def diagonal_BR():
        drive.set_motor_direction(front_left=0,rear_left=1,front_right=1,rear_right=0)

        drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)

def sideway_R():
        drive.set_motor_direction(front_left=-1,rear_left=1,front_right=1,rear_right=-1)

        drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)

def sideway_L():
        drive.set_motor_direction(front_left=1,rear_left=-1,front_right=-1,rear_right=1)

        drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)

left_turn()
time.sleep(1)
forward()
time.sleep(1)
right_turn()
time.sleep(1)
backward()
time.sleep(1)
diagonal_L()
time.sleep(1)
diagonal_R()
time.sleep(1)
diagonal_BL()
time.sleep(1)
diagonal_BR()
time.sleep(1)
sideway_R()
time.sleep(1)
sideway_L()
time.sleep(1)
stop()
drive.close()
=======
>>>>>>> 4dea2e7 (organizing and making main directory):code/motor/car.py
