// #include <fix_fft.h>
int digitalPin = 12;   // KY-037 digital interface
int analogPin = A5;   // KY-037 analog interface
int ledPin = 13;      // Arduino LED pin

char im[128], data[128];
int val, i = 0;

void setup()
{
  pinMode(digitalPin,INPUT); 
  pinMode(analogPin, INPUT);
  pinMode(ledPin,OUTPUT);      
  Serial.begin(9600);
}

void loop()
{

  for (int i = 0; i < 128; i++) {
      val = analogRead(0);
      data[i] = val / 4 - 128; // Center and scale
      im[i] = 0; // Initialize imaginary part
  }



  // Perform FFT
  fix_fft(data, im, 7, 0);
  for (i = 0; i < 64; i++) {
    Serial.write(data[i]); // Send real part as raw byte
    Serial.write(im[i]);   // Send imaginary part as raw byte
  }
}