#include <SoftwareSerial.h>
#include <VoiceRecognitionV3.h>

VR myVR(10, 11); // RX, TX for voice recognition module

const int motor1pin1 = 2;
const int motor1pin2 = 3;
const int motor2pin1 = 4;
const int motor2pin2 = 5;

const int trigPin = 9;
const int echoPin = 10;
const long maxDistance = 20; 

enum State {
  MANUAL,
  FORWARD,
  BACKWARD,
  STOP,
  AUTOPILOT
};

State currentState = MANUAL;

void setup() {
  pinMode(motor1pin1, OUTPUT);
  pinMode(motor1pin2, OUTPUT);
  pinMode(motor2pin1, OUTPUT);
  pinMode(motor2pin2, OUTPUT);
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  Serial.begin(9600);
  myVR.begin(9600);

  uint8_t records[7]; // Assuming you've trained 4 commands
  uint8_t ret = myVR.getRecognize(records);
  if (ret == myVR.isOk()) {
    switch (records[2]) {
      case 0:
        currentState = FORWARD;
        break;
      case 1:
        currentState = BACKWARD;
        break;
      case 2:
        currentState = STOP;
        break;
      case 3:
        currentState = AUTOPILOT;
        break;
    }
  }
}

void loop() {
  switch(currentState) {
    case FORWARD:
      moveForward();
      break;
    case BACKWARD:
      moveBackward();
      break;
    case STOP:
      stopMoving();
      break;
    case AUTOPILOT:
      if (checkForObstacle()) {
        stopMoving();
        turnLeft90();
        if (checkForObstacle()) {
          turnRight180();
          if (checkForObstacle()) {
            turn360();
          }
        }
      } else {
        moveForward();
      }
      break;
  }
  delay(50); 
}

bool checkForObstacle() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  long distance = (duration / 2) / 29.1;
  return (distance < maxDistance && distance > 0);
}

void moveForward() {
  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, HIGH);
  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, HIGH);
}

void stopMoving() {
  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, LOW);
  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, LOW);
}

void turnLeft90() {
  stopMoving();
  delay(250); 
  digitalWrite(motor1pin1, HIGH);
  digitalWrite(motor1pin2, LOW);
  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, HIGH);
  delay(2000);
  stopMoving();
}

void turnRight180() {
  stopMoving();
  delay(250);
  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, HIGH);
  digitalWrite(motor2pin1, HIGH);
  digitalWrite(motor2pin2, LOW);
  delay(4000);
  stopMoving();
}

void turn360() {
  stopMoving();
  delay(250);
  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, HIGH);
  digitalWrite(motor2pin1, HIGH);
  digitalWrite(motor2pin2, LOW);
  delay(8000);
  stopMoving();
}

void moveBackward() {
  digitalWrite(motor1pin1, HIGH);
  digitalWrite(motor1pin2, LOW);
  digitalWrite(motor2pin1, HIGH);
  digitalWrite(motor2pin2, LOW);
}
