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

### General CLI Commands
```
version: Displays the Betaflight firmware version on the flight controller.
dump: Outputs the entire current configuration of the flight controller. Useful for backup.
diff: Shows only the settings that differ from the defaults. Useful for sharing settings.
diff all: Shows the differences, including disabled features, from the defaults.
save: Saves the current configuration and reboots the flight controller.
exit: Exits the CLI mode and reboots the flight controller (without saving if changes were made).
```
Backup and Restore Commands
```
dump or diff: Use these commands to create a backup of your settings before making changes.
```
```# ```(Paste the backup script here): To restore, you simply paste the backup script into the CLI after the ```#``` prompt and then type save.

Configuration Commands
```
get [parameter_name]: Retrieves the current value of a specific configuration parameter.
set [parameter_name] = [value]: Sets the specified parameter to a new value.
defaults: Resets all settings to the firmware defaults (it's important to save after this command if you want to apply the default settings).
```
Feature Commands
```
feature: Lists all available features and their ON/OFF status.
feature [FEATURE_NAME]: Shows the ON/OFF status of a single feature.
feature -[FEATURE_NAME]: Disables a feature.
feature [FEATURE_NAME]: Enables a feature.
```
PID Tuning Commands
```
get pid: Displays the current PID values.
set p_pitch = [value]: Sets the P value for the pitch axis.
set i_pitch = [value]: Sets the I value for the pitch axis.
set d_pitch = [value]: Sets the D value for the pitch axis.
```
Receiver Commands
```
rxrange: Sets the range for each channel from the receiver.
rxfail: Sets up the fail-safe behavior for each channel.
```
Motor and ESC Commands
```
mixer: Displays or sets the current mixer configuration.
mmix: Custom motor mix for setting up custom motor outputs (for non-standard frames).
smix: Custom servo mix for complex airplanes or VTOL aircraft.
motor: Tests individual motor outputs (be cautious with propellers removed).
```
Calibration Commands
```
acc calibration: Calibrates the accelerometer.
mag calibration: Calibrates the magnetometer (if available).
```
Blackbox Commands
```
blackbox: Provides blackbox commands.
blackbox_device: Sets or shows the blackbox recording device.
```
GPS Commands
```
gpspassthrough: Enables passthrough mode for direct communication with the GPS module.
```

---

## ArduPilot Setup Guide

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
