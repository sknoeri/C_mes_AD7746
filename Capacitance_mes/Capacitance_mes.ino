#include <Wire.h>

// Defnitions of AD7746
#define I2C_adress 0x48
double capa=0;
double volt=0;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  Serial.println("Serial initalized");
  delay(100);
  Wire.begin();
  Wire.beginTransmission(I2C_adress); // The adress for writing is 0x90 but in the wire library the write bit is automatically wiriteen so : 0x48 B100 1000
  Wire.write(0x07);   // sets register pointer to the given adress 0x07
  Wire.write(0x80);   // gives instructions to the device at adress 0x07 single conversion enabled
  Wire.write(0xC1);   // gives instructions to the device at adress 0x08 voltage and temp sensor disconected 0xE1
  Wire.write(0x2B);   // gives instructions to the device at adress 0x09 EXCA and EXCB pin configured
  Wire.write(0xC1);   // gives instructions to the device at adress 0x0A cnersion time 20 ms 50Hz, contineous conversion mode -> important for the reading single conversion
  Wire.write(0xFF);   // gives instructions to the device at adress 0x0B connects capacitive DAC to the positive capa input and allows the full range on chanel A (0-8pf)
                      // this shit must be calibrated they have +-20% error on the device 9D 9E for channel A
  Wire.write(0x80);   // gives instructions to the device at adress 0x0C connects capacitive DAC to the positive capa input and allows the full range on chanel B (0-8pf)
  // Atention if second  last comand is 0x00 then it doesnt work if 0xFF then we can measure full range on cahnel B for channel A this doesnt matter
  Wire.endTransmission();
  delay(100);
  Serial.println("transmitted data");
  pinMode(13,1);
  digitalWrite(13,1);
  pinMode(12,1);
}

volatile unsigned char stat;
volatile unsigned char statOld=100;
volatile unsigned char p=2;

void loop()
{
  /*if((p&0x02)!=2){
    Serial.println(p&0x02);
    Serial.println(0x02,HEX);
    Serial.println(p,HEX);
  }*/
  /*stat=readStatus();
  if(statOld!=100){
    if(((stat&0x01) != 1)&&((statOld&0x01) == 1)){
      //capa = readCFemtof();
      //digitalWrite(13,1);
    }else{}//digitalWrite(13,0);
    if(((stat&0x02) != 2)&&((statOld&0x02) == 2)){
      volt = readVolt();
      Serial.println(volt);
      digitalWrite(12,1);
    }else{digitalWrite(12,0);}
  }
  statOld=stat;*/
  volt = readVolt();
  Serial.println(volt);
  delay(1000);
 
}
uint8_t readStatus(){
  unsigned char buff;
  Wire.requestFrom(I2C_adress, 1); // read a byte
  while(!Wire.available()) {
     // waiting
  }
  buff = Wire.read();
  //Serial.println(buff,BIN);
  return buff;
}

uint32_t readCFemtof()
{
  unsigned char buff[3];
  Wire.beginTransmission(I2C_adress);
  Wire.write(0x01);  // register to read stes adresspointer to the correct register
  Wire.endTransmission(false);
  //Serial.println("Set pointer to 0x1");
  Wire.requestFrom(I2C_adress, 3); // read a byte
  char i = 0;
  while (i<3) {
    while(!Wire.available()) {
      // waiting
    }
    buff[i] = Wire.read();
    i++;
  }
  uint32_t C=0;
  C = ((uint32_t)buff[0]<<16)|((uint32_t)buff[1]<<8)|((uint32_t)buff[2]); // No fixpoint aritmeritc is done yet
  /*Serial.print("Buffer 0: ");Serial.println(buff[0]);
  Serial.print("Buffer 1: ");Serial.println(buff[1]);
  Serial.print("Buffer 2: ");Serial.println(buff[2]);
  Serial.println(C);*/
  return 8192*(double)C/16777215; // 8192*C/(2^24-1) ensures value between 0 and 8.192pf. Is the capacitance in femto farad.
}
uint32_t readVolt()
{
  unsigned char buff[3];
  Wire.beginTransmission(I2C_adress);
  Wire.write(0x04);  // register to read
  Wire.endTransmission(false);//false
  //Serial.println("Set pointer to 0x1");
  Wire.requestFrom(I2C_adress, 3); // read a byte
  char i = 0;
  while (i<3) {
    while(!Wire.available()) {
      // waiting
    }
    buff[i] = Wire.read();
    i++;
  }
  uint32_t C=0;
  C = ((uint32_t)buff[0]<<16)|((uint32_t)buff[1]<<8)|((uint32_t)buff[2]); // No fixpoint aritmeritc is done yet
  Serial.print("Buffer 0: ");Serial.println(buff[0]);
  Serial.print("Buffer 1: ");Serial.println(buff[1]);
  Serial.print("Buffer 2: ");Serial.println(buff[2]);
  Serial.println(C);
  return 5000*(double)C/16777215; // 8192*C/(2^24-1) ensures value between 0 and 8.192pf. Is the capacitance in femto farad.
}

uint32_t readChanAorB(char chanel)
{
  if(chanel=='A'){
    Wire.beginTransmission(I2C_adress); // The adress for writing is 0x90 but in the wire library the write bit is automatically wiriteen so : 0x48 B100 1000
    Wire.write(0x07);   // sets register pointer to the given adress 0x07 Cap setup register bit 6 chooses Chaenl Aor B
    Wire.write(0x80);   // gives instructions to the device at adress 0x07 single conversion enabled sets multiplexer to A
    //Wire.write(0x00);   // gives instructions to the device at adress 0x08 voltage and temp sensordisconected
    //Wire.write(0x2B);   // gives instructions to the device at adress 0x09 EXCA and EXCB pin configured
    //Wire.write(0x11);   // gives instructions to the device at adress 0x0A cnersion time 20 ms 50Hz, contineous conversion mode -> important for the reading
    //Wire.write(0xFF);   // gives instructions to the device at adress 0x0B connects capacitive DAC to the positive capa input and allows the full range on chanel A (0-8pf)
    //Wire.write(0x00);   // gives instructions to the device at adress 0x0C connects capacitive DAC to the positive capa input and allows the full range on chanel B (0-8pf)
    Wire.endTransmission();
    delay(15);
    unsigned char buff[4];
    Wire.requestFrom(I2C_adress, 4); // read a byte
    char i = 0;
    while (i<4) {
      while(!Wire.available()) {
        // waiting
      }
      buff[i] = Wire.read();
      i++;
    }
    uint32_t C=0;
    C = ((uint32_t)buff[1]<<16)|((uint32_t)buff[2]<<8)|((uint32_t)buff[3]); // No fixpoint aritmeritc is done yet
    return 8192*(double)C/16777215; // 8192*C/(2^24-1) ensures value between 0 and 8.192pf. Is the capacitance in femto farad.
  }
  else if(chanel=='B'){
    Wire.beginTransmission(I2C_adress); // The adress for writing is 0x90 but in the wire library the write bit is automatically wiriteen so : 0x48 B100 1000
    Wire.write(0x07);   // sets register pointer to the given adress 0x07 Cap setup register bit 6 chooses Chaenl A or B
    Wire.write(0xC0);   // gives instructions to the device at adress 0x07 single conversion enabled sets multiplexer to B
    Wire.endTransmission();
    delay(15);
    unsigned char buff[4];
    Wire.requestFrom(I2C_adress, 4); // read a byte
    char i = 0;
    while (i<4) {
      while(!Wire.available()) {
        // waiting
      }
      buff[i] = Wire.read();
      i++;
    }
    uint32_t C=0;
    C = ((uint32_t)buff[1]<<16)|((uint32_t)buff[2]<<8)|((uint32_t)buff[3]); // No fixpoint aritmeritc is done yet
    return 8192*(double)C/16777215; // 8192*C/(2^24-1) ensures value between 0 and 8.192pf. Is the capacitance in femto farad.
  }
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
