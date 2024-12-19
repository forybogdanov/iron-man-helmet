/*
  ESP8266 Blink
  Blink the LED on the ESP8266 module
  This example code is in the public domain

  The external LED on the ESP8266 module is connected to GPIO12
 
*/

void setup() {
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  Serial.print("Hello World!");
  delay(1000);
}