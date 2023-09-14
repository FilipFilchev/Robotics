# LED Binary Counter with 74HC595

Create a simple binary counter that illuminates LEDs sequentially with every button press using a 74HC595 shift register.

## Components:
- 74HC595 shift register
- 8 LEDs
- 8 x 220Ω resistors (for LED current limiting)
- 1 x 10kΩ resistor (for button debouncing)
- 1 x 10µF capacitor (for button debouncing)
- 1 button
- Jumper cables
- Breadboard
- Power source (like an Arduino or a simple battery setup)

## Steps:

### 1. Setting up the 74HC595:
   - Connect Pin 8 (GND) to Ground
   - Connect Pin 16 (VCC) to +5V
   - Connect Pin 10 (MR - Master Reset) to +5V to disable the reset
   - Connect Pin 13 (OE - Output Enable) to Ground to enable the outputs

### 2. Connecting LEDs:
   - Connect the 8 LEDs to Q0-Q7 output pins (Pins 15, 1, 2, 3, 4, 5, 6, 7) of the 74HC595. Make sure to use the 220Ω resistors in series with each LED.

### 3. Button Setup (For Incrementing the Counter):

   a. Connect one terminal of the button to +5V.
   
   b. From the other terminal of the button:
   
   - Connect it to one leg of the 10kΩ resistor. The other leg of this resistor should connect to Ground.
       
   - Also, connect it to the positive terminal of the 10µF capacitor. The negative terminal of this capacitor should be connected to Pin 14 (DS - Data Input) of the 74HC595.
       
   c. Also, from the same terminal of the button (the one not connected to +5V), connect a jumper wire to Pin 11 (SH_CP - Shift Register Clock Pin) of the 74HC595.

### 4. Power Up:
   - Power up the circuit with your 5V power source.

## Operation:

With each button press, the LEDs will display a binary number that increments. The counter starts from 00000000 (all LEDs off) and progresses up to 11111111 (all LEDs on). After all LEDs are illuminated, the next button press will reset the counter, turning all LEDs off.
