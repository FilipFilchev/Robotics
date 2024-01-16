#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick

# Initialize 
#EV3 brick
ev3 = EV3Brick()
# motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
# color sensor.
line_sensor = ColorSensor(Port.S3)
# drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=80, axle_track=96)

# Set the drive speed.
DRIVE_SPEED = 100

# Adjust the proportional gain. - not in use anymore, because of changing from PID of deviation between the light reflection values from the brick to simply adjusting the turning rate between the colors white/black (better performance)
#PROPORTIONAL_GAIN = 2   

# Function to stop the robot's movement.
def stopMoving():
    robot.stop()
    
# Function to turn the robot right by approximately 90 degrees.
def turnRight90():
    stopMoving()
    ev3.speaker.beep(frequency=600, duration=300) 
    wait(100)
    left_motor.run(200)
    right_motor.run(200)
    wait(440)
    left_motor.run(155)
    right_motor.run(-155)
    wait(1000)  # Adjust time as needed. To turn properly 
    stopMoving()
    
def slowDown():
    ev3.speaker.beep(frequency=600, duration=600) 
    # wait(100)
    DRIVE_SPEED = 15 #17
    robot.drive(DRIVE_SPEED, -2)
    wait(12000) #8000 
    ev3.speaker.beep(frequency=100, duration=600) 
    #stopMoving()
    

# Start following the line continuesly.
while True:
    
    # Read the detected color from the sensor in color-based mode.
    detected_color = line_sensor.color()
    
    #stay in line
    if detected_color == Color.WHITE:
        robot.drive(DRIVE_SPEED, -19) #17
    elif detected_color == Color.BLACK:
        robot.drive(DRIVE_SPEED, 19)

    # Check for red color and turn right.
    elif detected_color == Color.RED:
        turnRight90()
        continue
    
    # Check for blue color and slow down.   *CALIBRATE FOR BLUE from parameters
    if detected_color == Color.BLUE:
        ev3.speaker.beep(frequency=600, duration=800) 
        pass
        
    # Check for green color and stop.
    elif detected_color == Color.GREEN:
        slowDown()
        stopMoving()
        break


    wait(10)
    
    
    
    
    """Old method
BLACK = 1
WHITE = 86
threshold = (BLACK + WHITE) / 2

# Start following the line continuesly.
while True:
    # Read the reflection value from the sensor for line following.
    current_reflection = line_sensor.reflection()

    # Read the detected color from the sensor for color-based actions.
    detected_color = line_sensor.color()

    # Check for blue color and turn right.
    if detected_color == Color.BLUE:
        turnRight90()
        continue

    # Check for green color and stop.
    if detected_color == Color.GREEN:
        stopMoving()
        break

    # Calculate the deviation from the threshold for line following.
    error = current_reflection - threshold
    integral += error
    derivative = error - last_error
    turn_rate = PROPORTIONAL_GAIN * error + INTEGRAL_GAIN * integral + DERIVATIVE_GAIN * derivative
    last_error = error

    # Adjust robot movement based on the line following logic.
    robot.drive(DRIVE_SPEED, turn_rate)

    # Short wait or other actions.
    wait(10)"""