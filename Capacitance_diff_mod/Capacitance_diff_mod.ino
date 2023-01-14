#include <Wire.h>

// Defnitions of AD7746
#define I2C_adress 0x48
double capa=0;
volatile int cnt=0;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  Serial.println("Serial initalized");
  delay(100);
  Wire.begin();
  delay(100);
  Wire.beginTransmission(I2C_adress); // The adress for writing is 0x90 but in the wire library the write bit is automatically wiriteen so : 0x48 B100 1000
  Wire.write(0x07);   // sets register pointer to the given adress 0x07
  Wire.write(0xA0);   // gives instructions to the device at adress 0x07 single conversion enabled
  Wire.write(0x00);   // gives instructions to the device at adress 0x08 voltage and temp sensordisconected
  Wire.write(0x0B);   // gives instructions to the device at adress 0x09 EXCA and EXCB pin configured EXCA enable EXCB inverted enabled
  Wire.write(0x01);   // gives instructions to the device at adress 0x0A cnersion time 20 ms 50Hz, contineous conversion mode -> important for the reading
  Wire.write(0x9A);   // gives instructions to the device at adress 0x0B connects capacitive DAC to the positive capa input and allows the full range on chanel A (0-8pf)
                      // this shit must be calibrated they have +-20% error on the device 9D 9E for channel A
  Wire.write(0x9F);   // gives instructions to the device at adress 0x0C connects capacitive DAC to the positive capa input and allows the full range on chanel B (0-8pf)
  Wire.write(0xF4);   // gives instructions to the device at adress 0x0D Offset calibration high bite
  Wire.write(0x88);   // gives instructions to the device at adress 0x0E Offset calibration low bite
  Wire.endTransmission();
  delay(100);
  Serial.println("transmitted data");
  attachInterrupt(1,reading,FALLING);
}


void loop()
{
  if(cnt==1){
    capa=readCFemtof();
    cnt=0;
    Serial.println(capa);
  }
  
}

void reading(){
    cnt=1;
}


uint32_t readCFemtof()
{
  unsigned char buffer[3];
  Wire.beginTransmission(I2C_adress);
  Wire.write(0x01);  // register to read
  Wire.endTransmission(false);
  //Serial.println("Set pointer to 0x1");
  Wire.requestFrom(I2C_adress, 3); // read a byte
  char i = 0;
  while (i<3) {
    while(!Wire.available()) {
      // waiting
    }
    buffer[i] = Wire.read();
    i++;
  }
  uint32_t C=0;
  C = ((uint32_t)buffer[0]<<16)|((uint32_t)buffer[1]<<8)|((uint32_t)buffer[2]); // No fixpoint aritmeritc is done yet
  /*Serial.print("Buffer 0: ");Serial.println(buffer[0]);
  Serial.print("Buffer 1: ");Serial.println(buffer[1]);
  Serial.print("Buffer 2: ");Serial.println(buffer[2]);
  Serial.println(C);*/
  //return 99200*(double)C/16777215; // 8192*C/(2^24-1) ensures value between 0 and 8.192pf. Is the capacitance in femto farad.
  return (8192*((double)C/16777215))    ; // 8192*C/(2^24-1) ensures value between 0 and 8.192pf. Is the capacitance in femto farad.

}
