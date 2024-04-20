# Spider Robot Controller

This web application allows you to control a spider robot via Web App, using the Master Bluetooth device to communicate with an HC-06 Bluetooth module attached to the Arduino Nano.

![spiderbot](img1.jpeg)

![spiderbot](img2.jpeg)

### Scan QR to access the app
![spiderbot](SpiderBot-QR.jpg)

## Prerequisites

- Your spider robot hw, with the HC-06 Bluetooth module correctly set up and paired with your Arduino.

## Setup

1. Clone the repository to your local machine.
2. npx create-react-app your-name-here
3. Navigate to the project directory.
4. Install the necessary dependencies.
5. Run the app in development mode with npm start.
6. deploy to firebase with npm run build & firebase deploy


## Usage

1. Open the web app in a compatible browser.
2. Click on the **Connect to Robot** button to open the Bluetooth device selection dialog.
3. Select your robot's HC-06 Bluetooth module from the list and confirm to establish a connection.
4. Use the provided buttons to control the robot:
- **Start Position**: Sends the robot to its starting position.
- **Step Forward**: Makes the robot take a step forward.
- **Step Backward**: Makes the robot take a step backward.
- **Custom Command**: Send a string command to the robot


## Contributing

Feel free to fork the repository and submit pull requests with any enhancements or fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


# More Info:

- This is not a master-slave communication its an server-client based project
- The master device is connected to the robot via the flask server script and the ulr is forwarded to the React App via Ngrok
- Post requests are sent to the master that decodes and sends serial data to the HC-06 slave module