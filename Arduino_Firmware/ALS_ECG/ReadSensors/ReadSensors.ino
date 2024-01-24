/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/AnalogReadSerial
*/
#define hlLED 14

#define SENSOR_RA A3  // PA04
#define SENSOR_LL A1  // PB08
#define SENSOR_LA A2  // PB09


// the setup routine runs once when you press reset:
void setup() {
  pinMode(hlLED, OUTPUT);

  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  delay(1000);
}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(hlLED, HIGH);

  // read the input on analog pin 0:
  int sensorValue = analogRead(SENSOR_RA);
  // print out the value you read:
  Serial.print(sensorValue);
  Serial.print(" ");

  sensorValue = analogRead(SENSOR_LA);
  // print out the value you read:
  Serial.print(sensorValue);
  Serial.print(" ");

  sensorValue = analogRead(SENSOR_LL);
  // print out the value you read:
  Serial.print(sensorValue);
  Serial.println(" ");
  digitalWrite(hlLED, LOW);
  delay(100);  // delay in between reads for stability
}
