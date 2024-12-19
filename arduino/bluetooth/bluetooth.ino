// Basic bluetooth test sketch. HC-06_01_9600
// HC-06 ZS-040 
// 
// 
//  Uses hardware serial to talk to the host computer and software serial for communication with the bluetooth module
//
//  Pins
//  BT VCC to Arduino 5V out. 
//  BT GND to GND
//  BT RX to Arduino pin 3 (through a voltage divider)
//  BT TX to Arduino pin 2 (no need voltage divider)
//
//  When a command is entered in the serial monitor on the computer 
//  the Arduino will relay it to the bluetooth module and display the result.
//
//  These HC-06 modules require capital letters and no line ending
//
 
// #include <SoftwareSerial.h>

int ledPin = 13;
int microphonePin = A1;

int baseline = 337;

void setup() 
{
  int baudRate = 9600;
  Serial.begin(baudRate);
  Serial.write("Arduino with HC-06 is ready");
  pinMode(ledPin, OUTPUT);
  pinMode(microphonePin, INPUT);
  digitalWrite(ledPin, LOW);
}
 
void loop()
{
  // if (Serial.available()) {
  //   int result = Serial.read();
  // }
  int val = analogRead(microphonePin);
  Serial.println(val);
  // int amplitude = abs(val - baseline);
  // Serial.println(amplitude);
  // Serial.write(amplitude);
  // when the sensor detects a signal above the threshold value, LED flashes
  // if (val > 40) {
  //   digitalWrite(ledPin, HIGH);
  // }
  // } else {
  //   digitalWrite(ledPin, LOW);
  // }
}