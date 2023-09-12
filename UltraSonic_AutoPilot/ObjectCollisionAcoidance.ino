const int motor1pin1 = 2;
const int motor1pin2 = 3;
const int motor2pin1 = 4;
const int motor2pin2 = 5;

const int trigPin = 9;
const int echoPin = 10;
const long maxDistance = 30; 


void setup() {
  pinMode(motor1pin1, OUTPUT);
  pinMode(motor1pin2, OUTPUT);
  pinMode(motor2pin1, OUTPUT);
  pinMode(motor2pin2, OUTPUT);
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  Serial.begin(9600);
}

void loop() {
    if(checkForObstacle() == false) {
    moveForward();
  } else {
    stopMoving();
    turnLeft90();
    //nested checks
    if(checkForObstacle() == true) {
      turnRight180();
      if(checkForObstacle() == true) {
        turnLeft360();  // Spin 360 degrees
        if(checkForObstacle() == true){
          moveBackward();
        }
      }
      
    }
  }
  delay(50); // Add a minor delay to prevent overloading the processor with rapid state changes
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
  delay(250); // A small delay to ensure the car stops before turning
  digitalWrite(motor1pin1, HIGH);
  digitalWrite(motor1pin2, LOW);
  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, HIGH);
  delay(1000);
  stopMoving();
}

void turnRight180() {
  stopMoving();
  delay(250);
  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, HIGH);
  digitalWrite(motor2pin1, HIGH);
  digitalWrite(motor2pin2, LOW);
  delay(2000);
  stopMoving();
}

void turnLeft360() {
  stopMoving();
  delay(250);
  digitalWrite(motor1pin1, HIGH);
  digitalWrite(motor1pin2, LOW);
  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, HIGH);
  delay(4000);
  stopMoving();
}

void moveBackward() {
  digitalWrite(motor1pin1, HIGH);
  digitalWrite(motor1pin2, LOW);
  digitalWrite(motor2pin1, HIGH);
  digitalWrite(motor2pin2, LOW);
  delay(2000);
  stopMoving();
}

