//  // Define the pins
//  const int motorSpeedPin = 9;  // E1 connected to PWM-capable pin D9
//  const int motorDirectionPin = 7;  // M1 connected to digital pin D7

//  void setup() {
//    pinMode(motorSpeedPin, OUTPUT);
//    pinMode(motorDirectionPin, OUTPUT);
//  }

//  void loop() {
//    driveForward();
//    delay(5000);  // Drive forward for 5 seconds

//    turnAround();
//    delay(5000);  // Turn for 5 seconds
//  }

//  void driveForward() {
//    analogWrite(motorSpeedPin, 255);  // Set motor speed to maximum
//    digitalWrite(motorDirectionPin, HIGH);  // Forward direction
//  }

//  void turnAround() {
//    analogWrite(motorSpeedPin, 150);  // Set motor speed to a lower value for turning
//    digitalWrite(motorDirectionPin, LOW);  // Reverse direction
//  }


// Define the pins
const int motorSpeedPin = 8;  // E1 connected to PWM-capable pin D8 for motor speed
const int motorDirectionPin = 7;  // M1 connected to digital pin D7 for motor direction

void setup() {
  pinMode(motorSpeedPin, OUTPUT);
  pinMode(motorDirectionPin, OUTPUT);
}

void loop() {
  driveForward();
  delay(5000);  // Drive forward for 5 seconds
  
  driveBackward();
  delay(5000);  // Drive backward for 5 seconds
}

void driveForward() {
  analogWrite(motorSpeedPin, 255);  // Set motor speed to maximum
  digitalWrite(motorDirectionPin, HIGH);  // Forward direction
}

void driveBackward() {
  analogWrite(motorSpeedPin, 255);  // Set motor speed to maximum
  digitalWrite(motorDirectionPin, LOW);  // Reverse direction
}

