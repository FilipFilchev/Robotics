from flask import Flask, request, jsonify
from flask_cors import CORS
import serial
import time

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests
# CORS(app, origins='192.123.12.123:3000')  # Allow requests from ngrok URL
# CORS(app, origins='http://localhost:3000/')  # Allow requests from ngrok URL

# Configure your serial connection here (adjust the port name and baud rate according to your setup)
SERIAL_PORT = '/dev/cu.HC-06-Port'  # For macOS and Linux, use COMx (e.g., COM3) for Windows
BAUD_RATE = 9600

def setup_serial():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        ser.flush()
        print(f"Connected to device {ser}")
        return ser
        
    except serial.SerialException as e:
        print(f"Serial connection error: {e}")
        return None


ser = setup_serial()  # Initialize serial connection


def send_serial_command(command):
    if not ser or not ser.is_open:
        return {"status": "connection error", "message": "Serial port not connected"}

    try:
        command += '\n'
        #send command to the spider bot
        ser.write(command.encode())
        time.sleep(2)  # Wait for the command to be sent
        ser.flush()  # Clear the serial buffer
        
        # Read data from the HC-06 module
        data = ser.readline().strip()  # Read a line of data and remove leading/trailing whitespace
        if data:
            print(f"Received: {data.decode('utf-8')}")  #Received command: w 0 0
        
        return {"message": f"You are now connected to the bot", "status": "success", "command": command, "received": data}
    except serial.SerialException as e:
        return {"status": "error", "message": str(e)}
    
   
#handle requests
@app.route('/send-command', methods=['POST'])
def send_command():
    # datata = request.get() #here should be the link to the website
    # print(datata)
    data = request.json   #get command FROM the jsonified react body 
    print(data)
    
    command = data.get('command')
    print(f'Received command: {command}')
    
    response = send_serial_command(command)
    return jsonify(response) #return data TO the react app

#INCLUDE
# @app.route('/available-devices', methods=['GET','POST'])
# def check(ser):
#     return jsonify(str(ser))

if __name__ == '__main__':
    app.run(debug=True, port=8080)


"""!!! ngrok http 8080 to forward the port"""