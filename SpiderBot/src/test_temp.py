import serial
import serial.tools.list_ports

def find_available_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = [port.device for port in ports]
    return available_ports

def main():
    # Find available ports
    available_ports = find_available_ports()
    if not available_ports:
        print("No serial ports available.")
        return
    
    print("Available serial ports:")
    for port in available_ports:
        print(port)

    # Let the user choose a port
    port_name = input("Enter the name of the port you want to use: ")

    # Open the serial port
    try:
        ser = serial.Serial(port_name, baudrate=9600, timeout=1)
        print(f"Opened port {port_name}")
    except serial.SerialException as e:
        print(f"Failed to open port {port_name}: {e}")
        return

    # Now you can continuously read user input and send it through the serial port
    try:
        while True:
            user_input = input("Enter string to send (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break
            # Append newline character to the user input
            user_input += '\n'
            ser.write(user_input.encode())  # Encode string to bytes before sending
            print(f"Sent: {user_input}")
            
            # Read data from the HC-06 module
            data = ser.readline().strip()  # Read a line of data and remove leading/trailing whitespace
            if data:
                print(f"Received: {data.decode('utf-8')}")

    except KeyboardInterrupt:
        pass
    finally:
        ser.close()  # Close the serial port when done

if __name__ == "__main__":
    main()
