#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait

# Initialize EV3 brick
ev3 = EV3Brick()

# Initialize motors and sensor
motorA = Motor(Port.A)
motorB = Motor(Port.B)
#ultrasonic = UltrasonicSensor(Port.C)
# Change the sensor port reference from C to S3
ultrasonic = UltrasonicSensor(Port.S3)

MAX_DISTANCE = 300  # in millimeters (30 cm)

def checkForObstacle():
    return ultrasonic.distance() < MAX_DISTANCE


def moveForward():
    motorA.run(200)  # 200 deg/sec is an example speed; adjust as necessary
    motorB.run(200)

def stopMoving():
    motorA.stop(Stop.BRAKE)
    motorB.stop(Stop.BRAKE)

def turnLeft90():
    stopMoving()
    wait(250)
    motorA.run(-200)
    motorB.run(200)
    wait(1000)  # adjust time if needed
    stopMoving()

def turnRight180():
    stopMoving()
    wait(250)
    motorA.run(200)
    motorB.run(-200)
    wait(2000)  # adjust time if needed
    stopMoving()

def turnLeft360():
    stopMoving()
    wait(250)
    motorA.run(-200)
    motorB.run(200)
    wait(4000)  # adjust time if needed
    stopMoving()

def moveBackward():
    motorA.run(-200)
    motorB.run(-200)
    wait(2000)  # adjust time if needed
    stopMoving()

# Main loop
while True:
    if not checkForObstacle():
        moveForward()
    else:
        stopMoving()
        moveBackward()
        turnLeft90()
        if checkForObstacle():
            turnRight180()
            if checkForObstacle():
                turnLeft360()
                    
    wait(50)
