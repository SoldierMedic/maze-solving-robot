#robot_move.py
from time import sleep
from adafruit_crickit import crickit
motor_1 = crickit.dc_motor_1
motor_2 = crickit.dc_motor_2

motor_1.throttle = 0.5
motor_2.throttle = 0.5
sleep(1)

motor_1.throttle = 0
motor_2.throttle = 0
sleep(1)

motor_1.throttle = -0.5
motor_2.throttle = -0.5
sleep(1)

motor_1.throttle = 0
motor_2.throttle = 0
sleep(1)