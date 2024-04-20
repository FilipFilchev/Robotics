import React, { useState, useEffect } from 'react';
import './App.css';
import firebase from 'firebase/compat/app';
import 'firebase/compat/analytics';
import { ReactComponent as Logo } from './logo.svg'; 

// Firebase configuration (replace placeholders with your actual Firebase config)
firebase.initializeApp({
  apiKey: "...",
  authDomain: "...",
  projectId: "spider-bot-70184",
  storageBucket: "...",
  messagingSenderId: "...",
  appId: "...",
  measurementId: ",,,"
});

function App() {
  const [connected, setConnected] = useState(false);
  const [availableDevices, setAvailableDevices] = useState([]);
  const [customCommand, setCustomCommand] = useState('');

  useEffect(() => {
    // Fetch available Bluetooth devices from the forwarded server port
    fetch('https://123-456-789.ngrok-free.app/available-devices')
      .then(response => response.json())
      .then(data => {
        setAvailableDevices(data.devices);
        alert(`Available Bluetooth Devices:\n${data.devices.map(device => `${device.name}: ${device.address}`).join('\n')}`);
        console.log(`Available Bluetooth Devices:\n${data.devices.map(device => `${device.name}: ${device.address}`).join('\n')}`);
      })
      .catch(error => console.error('Error fetching available devices:', error));
    
    // connection status check
    setConnected(true); // Assume always connected for simplicity
    alert("Connected to device")
  }, []);

  //Send custom commands to the flask app via Post requests
  const sendCommand = (command) => {
    console.log('Sending command:', command);
    fetch('https://123-456-789.ngrok-free.app/send-command', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ command }), //return json TO the flask server
    })
    .then(response => response.json())  // get the jsonified response FROM the flask app
    .then(data => console.log(data))
    .catch((error) => {
      console.error('Error sending commands:', error);
    });
  };

  const handleCustomCommandChange = (event) => {
    setCustomCommand(event.target.value);
  };

  const handleCustomCommandSubmit = () => {
    if (customCommand.trim() !== '') {
      sendCommand(customCommand);
      setCustomCommand('');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <Logo /> 
        <p>Spider Robot Controller</p>
        {connected ? (
          <>
            <button onClick={() => sendCommand('w 1 1')}>Step Forward</button>
            <button onClick={() => sendCommand('w 2 1')}>Step Backward</button>
            <button className='leftButton' onClick={() => sendCommand('w 4 1')}>Step Left</button>
            <button className='rightButton' onClick={() => sendCommand('w 3 1')}>Step Right</button>
            <button onClick={() => sendCommand('w 5 4')}>Wave!</button>
            <button className='startPos' onClick={() => sendCommand('w 0 0')}>Start Position</button>
          </>
        ) : (
          <p>Connecting to server...</p>
        )}
        <div className="custom-command-input">
          <input 
            type="text" 
            value={customCommand} 
            onChange={handleCustomCommandChange} 
            placeholder="Enter custom command" 
          />
          <button onClick={handleCustomCommandSubmit}>Submit</button>
        </div>
      </header>
    </div>
  );
}

export default App;
