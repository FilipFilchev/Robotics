#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
import time

# Initialize EV3 brick
ev3 = EV3Brick()

# Initialize the motors and sensors.
conveyor_motor = Motor(Port.A)
pusher_motor = Motor(Port.B)
lift_motor = Motor(Port.C)
# Initialize the color sensor.
color_sensor = ColorSensor(Port.S3)
# Init UltraSonic Sensor.
ultra_sensor = UltrasonicSensor(Port.S4)

# Conveyor, pusher, lift, ultrasonic and timer presets.
CONVEYOR_SPEED = -150 # Speed of the conveyor belt
PUSHER_SPEED = 800 #Speed of black cube pusher
PUSHER_RETURN_SPEED = -800 # Speed to return the pusher to starting position
PUSHER_DURATION = 550 # Duration for which the pusher motor runs
ALIGNMENT_DELAY = 920 # Delay for cube alignment
LIFT_DURATION = 3200
LIFT_SPEED = 200
MAX_DISTANCE = 200 #Max distance of carrier from conveyor in mm before it starts the system and count down
carrierCheck = False
timerStarted = False

#lift function after timout (40secs)
def lift():
    ev3.speaker.beep(frequency=800, duration=100) 
    lift_motor.run(LIFT_SPEED)
    wait(LIFT_DURATION)

# Main loop for the conveyor system.
while True:
     #check for carrier nearby (20cm)
    if ultra_sensor.distance() < MAX_DISTANCE:
        carrierCheck = True
       
        #check if timer has started in order to start it initially 
        if not timerStarted:
            start_time = time.time()
            timerStarted = True

    #Start the system when carrier arrives
    if carrierCheck:
        #start conveyor motor
        conveyor_motor.run(CONVEYOR_SPEED)
        #checking colors via light reflection sensor
        current_color = color_sensor.color()
        if current_color in [Color.RED, Color.GREEN, Color.BLUE]:
            ev3.speaker.beep(frequency=800, duration=100) 

        # Activate the pusher to move the cube.
        if current_color == Color.BLACK:    #to calibrate config the parameters
            ev3.speaker.beep(frequency=50, duration=400) 
            wait(ALIGNMENT_DELAY)
            pusher_motor.run_time(PUSHER_SPEED, PUSHER_DURATION)
            pusher_motor.run_time(PUSHER_RETURN_SPEED, PUSHER_DURATION)
            
     # Check if 40 seconds have passed
    if timerStarted and time.time() - start_time > 40:
        ev3.speaker.beep(frequency=200, duration=200) 
        lift()
        break # Break out of the loop after 40 seconds

    wait(10)  # Small delay for the loop


"""Previous version
#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
import time


# Initialize EV3 brick
ev3 = EV3Brick()



# Initialize the motors.
conveyor_motor = Motor(Port.A)  # Motor for the conveyor belt
pusher_motor = Motor(Port.B)    # Motor for pushing the cube

# Initialize the color sensor.
color_sensor = ColorSensor(Port.S3)
# Init UltraSonic Sensor.
ultra_sensor = UltrasonicSensor(Port.S4)

# Initialize lift the motor.
lift_motor = Motor(Port.C)  # Motor for the lift

LIFT_DURATION = 3200
LIFT_SPEED = 200

# Conveyor and pusher settings.
CONVEYOR_SPEED = -150  # Speed of the conveyor belt
PUSHER_SPEED = 800    # Increased speed for a faster push
PUSHER_RETURN_SPEED = -800  # Speed to return the pusher to starting position
PUSHER_DURATION = 550 # Duration for which the pusher motor runs
ALIGNMENT_DELAY = 920 # Delay for cube alignment

#Max distance of carrier from conveyor in mm
MAX_DISTANCE = 200
carrierCheck = False

def lift():
    ev3.speaker.beep(frequency=800, duration=100) 
    lift_motor.run(LIFT_SPEED)
    wait(LIFT_DURATION)
    
# Init the start time
start_time = time.time()

# Main loop for the conveyor system.
while True:
    
    # Check if 40 seconds have passed
    if time.time() - start_time > 40:
        ev3.speaker.beep(frequency=200, duration=200) 
        lift()
        break  # Break out of the loop after 40 seconds
    
    #check for carrier nearby (10cm)
    if ultra_sensor.distance() < MAX_DISTANCE:
        carrierCheck = True
    
    #check for carrier nearby (10cm)
    if carrierCheck == True:
    
        # Start the conveyor motor.
        conveyor_motor.run(CONVEYOR_SPEED)
    
        # Read the reflection value from the sensor.
        current_color = color_sensor.color()
    
        if current_color == Color.RED or current_color == Color.GREEN or current_color==Color.BLUE:
            ev3.speaker.beep(frequency=800, duration=100) 


        # Check if the reflection indicates a black surface.
        if current_color == Color.BLACK:
            ev3.speaker.beep(frequency=50, duration=400) 
            # Wait for the cube to align with the pusher.
            wait(ALIGNMENT_DELAY)

            # Activate the pusher to move the cube.
            pusher_motor.run_time(PUSHER_SPEED, PUSHER_DURATION)
            #wait(PUSHER_DURATION)

            # Return the pusher to its starting position.
            pusher_motor.run_time(PUSHER_RETURN_SPEED, PUSHER_DURATION)
            #wait(PUSHER_DURATION)

        wait(10)  # Small delay for the loop"""
      
  

