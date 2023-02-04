#include <Wire.h>
// Defnitions of AD7746
#define I2C_adress 0x48 // I2C adress of the CN-0552 eval bord. actually 0x90 for read and 0x91 for write but 
                        // the last bit is taken by he wire library so only the last seven bits counts --> 0x48

double capa=0;
volatile int cnt=0; // global defined valiable

// the setup function runs once when you press reset or power the board
// configures the CN-0552 and the Arduino
void setup() {
  // initialize serial communication at 115200 bits per second:
  Serial.begin(115200);
  Serial.println("Serial initalized");
  delay(100);
  Wire.begin();
  delay(100);
  Wire.beginTransmission(I2C_adress); // The adress for writing is 0x90 but in the wire library 0x48
  Wire.write(0x07);   // sets register pointer to the given adress 0x07
  Wire.write(0x80);   // writes regsiter 0x07 single conversion enabled
  Wire.write(0x00);   // writes regsiter 0x08 voltage and temp sensordisconected
  Wire.write(0x1B);   // writes regsiter 0x09 EXCA and EXCB pin configured EXCA enable EXCB inverted enabled
  Wire.write(0x01);   // writes regsiter 0x0A sets sample time, puts contineous conversion mode -> important for the reading
  Wire.write(0x9F);   // writes regsiter 0x0B offset calibration on the device for channel A
  Wire.write(0x80);   // writes regsiter 0x0C offset calibration on the device for channel B
  Wire.write(0xF4);   // writes regsiter 0x0D Offset calibration high bite
  Wire.write(0x88);   // writes regsiter 0x0E Offset calibration low bite
  Wire.endTransmission();
  delay(100);
  Serial.println("transmitted data");
  attachInterrupt(1,reading,FALLING); // Attaches an input interrupt on falling edge on pin 4
}


void loop()
{
  if(cnt==1){
    //delay(1);
    readChanAorB('A');
    capa=readCFemtof();
    cnt=0;
    Serial.println(capa);
  }
}

void reading(){ // executed interrupt routine
    cnt=1;
    return cnt;
}


uint32_t readCFemtof() // reads the 24 bit capacitance register
{
  unsigned char buffer[3];
  Wire.beginTransmission(I2C_adress);
  Wire.write(0x01);  // register to read
  Wire.endTransmission(false); // need such that the adress pointer is not reset back to 0x00
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
  C = ((uint32_t)buffer[0]<<16)|((uint32_t)buffer[1]<<8)|((uint32_t)buffer[2]); // No fixpoint aritmetritc is done yet
  return 99200*(double)C/16777215; // 8192*C/(2^24-1) ensures value between 0 and 8.192pF/99.2pF. In femto farad.

}

void readChanAorB(char chanel) // Function which allows to seclect the imputchannel to read
{
  if(chanel=='A'){
    Wire.beginTransmission(I2C_adress); 
    Wire.write(0x07);   // sets register pointer to 0x07 Cap setup register bit 6 chooses Chaenl Aor B
    Wire.write(0x80);   // writes regsiter 0x07 single conversion enabled sets multiplexer to A
    Wire.endTransmission();
  }
  else if(chanel=='B'){
    Wire.beginTransmission(I2C_adress); 
    Wire.write(0x07);   // sets register pointer to 0x07 Cap setup register bit 6 chooses Chaenl A or B
    Wire.write(0xC0);   // writes regsiter 0x07 single conversion enabled sets multiplexer to B
    Wire.endTransmission();
  }
}
