# 🤖  Robotics
Arduino, Raspberry and BreadBoard Projects

## Table of Contents
- [Building FPV Drones](#fpv-drone-build)
- [Arduino Robot Car UltraSonic](#configuring-authentication)
- [AI Drone Build](#Robot-Car-with-Obstacle-Avoidance-and-VA)


#FPV Drone Build

![drone](imgfpv0.png)

![drone](imgfpv1.png)

![drone](imgfpv2.png)

# Robot Car with Obstacle Avoidance and VA

Build an Arduino-powered robot car that can be controlled via voice commands. Additionally, this robot features obstacle avoidance capabilities using an ultrasonic sensor.

![Robot Car Photo](robot1.png)

## Components
1. Arduino UNO board
2. Motor Drive Controller (L298N)
3. 4 DC Motors with wheels
4. HC-SR04 Ultrasonic Sensor
5. Elechouse's Voice Recognition v3 Module
6. Other components: jumper wires, batteries, etc...

![components](img2.png)

![components](img3.jpeg)

## Setup & Connections


![Robot Car Assembly Photo](img4.jpg)

### 2. Arduino Connections
- Connect the motors to the motor driver and then to the respective pins on the Arduino.
- Set up the HC-SR04 Ultrasonic Sensor & the Elechouse Module

![Connections](connections.png)

### 3. Voice Recognition v3 Module Setup
Follow the guide from [Elechouse](https://www.elechouse.com/product/speak-recognition-voice-recognition-module-v3/) to connect and set up the module.

## Software & Coding

1. **Library Setup**: Install the `VoiceRecognitionV3` library via the Arduino IDE Library Manager.
2. **Voice Training**: Train the Voice Recognition module to recognize your commands - 'forward', 'backward', 'stop', and 'autopilot'.
3. **Code Upload**: Upload the provided code to the Arduino in this repo.
4. Connect Bluetooth Controller
![controller](connect_bl_control.png)

## Usage

- Say "forward" to move the robot car forward.
- Say "backward" to move it backward.
- Say "stop" to halt the robot.
- Say "autopilot" to enable obstacle avoidance mode.

## Contribute
Feel free to modify, distribute, and enhance this project! Feedback and improvements are always welcomed.

![video](video1.mov)

# CV Drone Build

## Building a Raspberry Pi computer vision powered drone with autonomous flight assistant mode, flight controller hat, voice assistance, speech to text algorithm, 4G hat for remote control, and a Python-backend:


![drone](img10.png)



### Hardware setup:

- Assemble the drone frame and attach the flight controller (such as Pixhawk or some simpler uC).
Connect the Raspberry Pi to the flight controller hat via the appropriate communication interface (e.g., SPI, I2C, UART).
Attach the Raspberry Pi Camera module for manimupaltion and programming.
Connect a 4G/LTE modem or dongle to provide remote connectivity.

Install the operating system:

- Install the latest version of Raspberry Pi OS (formerly Raspbian) on an SD card.
Set up the Raspberry Pi and connect it to a network (either through Wi-Fi or Ethernet).

Install necessary libraries and dependencies:

-Create your own backend processing or use pretrained models and already built libraries
- Install OpenCV library for computer vision tasks: pip install opencv-python.
Install Dronekit-Python for interfacing with the flight controller: pip install dronekit.
Install HuggingFace/VA/LLM libraries for speech to text and reverted manipulation (for voice assistance) OR build your own with TensorFlow

Computer vision obstacle avoidance:

- Use OpenCV to capture frames from the Raspberry Pi Camera module.
Process the frames using computer vision techniques (e.g., object detection, image segmentation) to identify obstacles.
Implement an algorithm to recognize the obsticles from the training and calculate the drone's movements based on the detected obstacles and send appropriate commands to the flight controller.

Voice assistance and speech-to-text:

- Implement a speech-to-text algorithm (such as using the Google Cloud Speech-to-Text API or Mozilla DeepSpeech) to convert spoken commands to text.
Use a voice assistant library like pyttsx3 to provide voice assistance by converting text to speech.

Remote control via 4G:

- Set up the 4G/LTE modem or dongle to establish an internet connection.
Implement a communication protocol (TCP/IP or MQTT) to transmit commands from a remote device to the drone.
Create a server on the drone to receive and interpret commands from the remote device.
Encode and decode the commands sent between the remote device and the drone using an appropriate protocol.

Python code and implementation:

- Write Python scripts to handle computer vision, flight control, voice assistance, speech-to-text, and remote control functionalities.
Implement multithreading or asynchronous programming to handle concurrent tasks.
Test and iterate on the code to ensure proper integration and functionality.

React GUI for controller:

- Set up a React.js development environment.
Design and develop a user interface (UI) using React components for the remote control application.
Implement communication with the drone using the established communication protocol.
Deploy the React app to a suitable hosting platform like FireBase or AWS; Connect and establish a database for data handling.

Establish Communication:

- Use MAVlink & WebSockets for communication.
- Implement RESTful APIs on the backend & communication protocol with the Raspberry Pi.
Configure the Raspberry Pi to make HTTP requests to these APIs.
- Design a way for the Raspberry Pi to send data back to the cloud platform, such as telemetry data or status updates.
Implement APIs on the backend to receive and store this data.

Security Measures:

- Implement token-based authentication for API endpoints to secure communication between the cloud platform and Raspberry Pi.
Use HTTPS to encrypt data transmission.

Test and Optimize:

- Test communication between the cloud platform and Raspberry Pi.
Optimize the API calls and data transmission for efficiency.
- Simulate the flight first and then test it in the real enviroment ON A STRING to avoid LOSING the drone in the AIR!

Scalability and Iteration:

- Consider scaling up your cloud infrastructure as user demand increases.
Collect user feedback and iterate on both the frontend(interface) and backend(communication & manimulation) components.

- Integrate satellite communication if necessary (this might be complex and requires specific modules).
- Autopilot can be implemented with your own model and reinforcement learning instead of using libraries like DroneKit.
- Object avoidance can be achieved using ultrasonic sensors & Lidar connected to the Pi. The AFAS (Advanced Flight Assistance System) will require additional programming and integration, ensuring that it works in tandem with the flight controller.
