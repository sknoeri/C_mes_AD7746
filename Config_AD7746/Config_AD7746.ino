//#include <AD7746.h>
#include <Wire.h>

void setup() {
  Wire.begin(); // join i2c bus (address optional for master)
   Wire.beginTransmission(0x48); // The adress for writing is 0x90 but in the wire library the write bit is automatically wiriteen so : 0x48 B1001 0000
  Wire.write(byte(0x07));   // sets register pointer to the given adress 0x07
  Wire.write(byte(0x50));   // gives instructions to the device at adress 0x07
  Wire.write(byte(0x50));   // gives instructions to the device at adress 0x08
  Wire.write(byte(0x50));   // gives instructions to the device at adress 0x09
  Wire.write(byte(0x50));   // gives instructions to the device at adress 0x0A
  Wire.write(byte(0x50));   // gives instructions to the device at adress 0x0B
  Wire.endTransmission();
}

void loop() {
  unsigned char buffer[4];
  Wire.requestFrom(0x48,4);
  if(Wire.available()){
    for (int i=0; i<4; i++){
      buffer[i]=Wire.read();
    }
  }
  uint32_t C=0;
  C = ((uint32_t)buffer[1]<<16)|((uint32_t)buffer[2]<<8)|((uint32_t)buffer[3]); // No fixpoint aritmeritc is done yet
}
