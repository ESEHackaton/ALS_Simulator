/*
  I/O Test for ActuatorHub

  Turns LEDs on for one second, then off for one second, repeatedly.
  Idem for actuators

  Johan Korten Apr. 3, 2023
  Based on Blink example


  Uses https://github.com/wagiminator/SAMD-Development-Boards firmware

  Install this boards file:
  https://raw.githubusercontent.com/wagiminator/SAMD-Development-Boards/main/packages/package_wagiminator_samd_index.json
 
*/

#define numActuators 6
// PA18 .. PA21
#define PA18 10
#define PA19 12
#define PA20 6
#define PA21 7

const int actuatorPins[numActuators] = {PA18, PA19, PA20, PA21, 5, 14};

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pins from actuatorPins as outputs.
  for (int i = 0; i < numActuators; i++) {
    pinMode(actuatorPins[i], OUTPUT);
  }
}

// the loop function runs over and over again forever
void loop() {
  for (int i = 0; i < numActuators; i++) {
    digitalWrite(actuatorPins[i], HIGH);   // turn the pin on (HIGH is the voltage level)
  }
  delay(1000);
  for (int i = 0; i < numActuators; i++) {
    digitalWrite(actuatorPins[i], LOW);   // turn the pin on (HIGH is the voltage level)
  }
  delay(1000);
}
