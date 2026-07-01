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

def forward_move():
  drive.set_motor_direction(front_left=-1,rear_left=-1,front_right=-1,rear_right=-1)

  drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)

def backward_move():
  drive.set_motor_direction(front_left=1,rear_left=1,front_right=1,rear_right=1)

  drive.set_motors(front_left=1000,rear_left=1000,front_right=1000,rear_right=1000)


if input("W"):
  forward_move()
  time.sleep(1)
elif input("A"):
  
# print("testing 123")

#left_turn()
#time.sleep(1)
#forward_move()
#time.sleep(1)
#right_turn()
#time.sleep(1)
#backward_move()
#time.sleep(1)
#stop()

#drive.close()
