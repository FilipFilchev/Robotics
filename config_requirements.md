# FPV Drone Setup Guide

- ATTENTION: Be careful with the Amps(Current) provided by the battery - ECU - to motors.
- If they are not compatible this will result in burning the motors or the controller.
- Also make sure to plug the board in the PC via data-cable not just charging-cable

## Betaflight Setup

### Preconditions

- Remove all propellers.
- Ensure your flight controller is compatible with Betaflight.
- Have a fully charged battery for the drone and a USB cable (depending on the drone, cause some will connect with just a cable)

### Step 1: Driver Installation

Install the necessary drivers for your flight controller (e.g., CP210x, STM32 VCP).

### Step 2: Betaflight Configurator

Download and install the Betaflight Configurator on your computer.

### Step 3: Flashing Firmware

1. Connect the flight controller to your computer via USB.
2. Open Betaflight Configurator and go to the `Firmware Flasher` tab.
3. Select your board and the latest firmware version.
4. Click `Load Firmware [Online]` and then `Flash Firmware`.
5. Wait for the process to complete, then disconnect the USB.

### Step 4: Initial Configuration

1. Reconnect the flight controller to Betaflight.
2. Calibrate the accelerometer in the `Setup` tab.
3. Configure UARTs in the `Ports` tab.
4. Set up the ESC/Motor protocol and other features in the `Configuration` tab.

### Step 5: Receiver Setup

1. In the `Receiver` tab, select your protocol.
2. Bind your receiver and transmitter.
3. Verify the channel map and stick movements.

### Step 6: Flight Modes Setup

Assign switches on your transmitter to flight modes in the `Modes` tab.

### Step 7: ESC Calibration

1. Go to the `Motors` tab with the battery disconnected.
2. Raise the `Master` slider, connect the battery, then lower the slider after the tones.

### Step 8: PID Tuning

Adjust PIDs for stable flight after an initial test.

### Step 9: Final Checks

Confirm fail-safe settings, motor directions, and prop orientation.

### Step 10: First Flight

Test the drone in a safe and legal area.

---

# ArduPilot Setup Guide

### Prerequisites

- Same as Betaflight setup.

### Step 1: Firmware Installation

1. Install Mission Planner.
2. Connect the flight controller.
3. Flash the firmware for your vehicle type in Mission Planner.

### Step 2: Mandatory Hardware Configuration

Configure the frame, calibrate accelerometers, compass, transmitter, ESCs, and battery monitor.

### Step 3: Optional Hardware Configuration

Set up GPS, OSD, telemetry radios, etc., if applicable.

### Step 4: Initial Parameter Setup

Review and adjust the standard parameters for your hardware.

### Step 5: Pre-Arm Checks

Resolve any pre-arm warnings before attempting to arm the drone.

### Step 6: Arming and Motor Test

Ensure motors spin correctly and the drone arms properly before flight.
