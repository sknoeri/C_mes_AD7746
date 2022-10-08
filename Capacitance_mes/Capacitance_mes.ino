#include <Wire.h>

// Defnitions of AD7746
#define I2C_adress 0x48
double capa=0;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  Serial.println("Serial initalized");
  delay(100);
  Wire.begin();
  Wire.beginTransmission(I2C_adress); // The adress for writing is 0x90 but in the wire library the write bit is automatically wiriteen so : 0x48 B100 1000
  Wire.write(0x07);   // sets register pointer to the given adress 0x07
  Wire.write(0x80);   // gives instructions to the device at adress 0x07 single conversion enabled
  Wire.write(0x00);   // gives instructions to the device at adress 0x08 voltage and temp sensordisconected
  Wire.write(0x2B);   // gives instructions to the device at adress 0x09 EXCA and EXCB pin configured
  Wire.write(0x11);   // gives instructions to the device at adress 0x0A cnersion time 20 ms 50Hz, contineous conversion mode -> important for the reading
  Wire.write(0x00);   // gives instructions to the device at adress 0x0B no calibration offset done for cap mesure chanel A
  Wire.write(0x00);   // gives instructions to the device at adress 0x0B no calibration offset done for cap mesure chanel B
  Wire.endTransmission();
  delay(100);
  Serial.println("transmitted data");
}


void loop()
{
    
  capa=readCNanof();
  delay(30);
  Serial.println(capa);
}


uint32_t readCNanof()
{
  unsigned char buffer[4];
  Wire.beginTransmission(I2C_adress);
  Wire.write(0x01);  // register to read
  Wire.endTransmission();
  //Serial.println("Set pointer to 0x1");
  Wire.requestFrom(I2C_adress, 4); // read a byte
  char i = 0;
  while (i<4) {
    while(!Wire.available()) {
      // waiting
    }
    buffer[i] = Wire.read();
    i++;
  }
  uint32_t C=0;
  C = ((uint32_t)buffer[1]<<16)|((uint32_t)buffer[2]<<8)|((uint32_t)buffer[3]); // No fixpoint aritmeritc is done yet
  /*Serial.print("Buffer 0: ");Serial.println(buffer[0]);
  Serial.print("Buffer 1: ");Serial.println(buffer[1]);
  Serial.print("Buffer 2: ");Serial.println(buffer[2]);
  Serial.print("Buffer 3: ");Serial.println(buffer[3]);
  Serial.println(C);*/
  return 8000*(double)C/16777215; // 8*C/(2^24-1)-4 ensures value between -4 and 8. Is the capacitance in 10^3 pico farad
}

/*
//I/O pin configuration registers
#define DIRD *((volatile unsigned char*) 0x2A) // Data dircetion register of port D
#define PORTB*((volatile unsigned char*) 0x2B) // Pin set register of port B woks according to DIR port
#define PIND *((volatile unsigned char*) 0x29) // Pin toggle register of port D woks independent of DIR port

#define DIRB *((volatile unsigned char*) 0x24) // Data dircetion register of port B
#define PORTB*((volatile unsigned char*) 0x25) // Pin set register of port B woks according to DIR port
#define PINB *((volatile unsigned char*) 0x23) // Pin toggle register of port B woks independent of DIR port

// Timer2 configuration register
#define TCCR1A *((volatile unsigned char*) 0x80) // Timer register A
#define TCCR1B *((volatile unsigned char*) 0x81) // Timer register B
#define TIMSK1 *((volatile unsigned char*) 0x6F) // Timer interrup enable register

unsigned char b=0;
unsigned char c=0;
void initTimer1(){
  TCCR1A|=(0<<7)|(0<<6);          // Timer in normal operation, OC0A disconected
  TCCR1A|=(0<<0)|(0<<1);          // Timer in normal opperation counts until 0xFF and sets TOV flag there
  TCCR1B|=(0<<3)|(0<<4);          // Timer in normal opperation counts until 0xFF and sets TOV flag there continuation of TCCR0A
  TCCR1B|=(0<<2)|(1<<1)|(0<<0);          // No prescaling takes clock frequenzie
  TIMSK1|=(1<<0);          // Enalbs the overflow interuppt
}*/
