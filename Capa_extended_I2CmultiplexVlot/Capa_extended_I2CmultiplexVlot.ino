#include <Wire.h>

// Defnitions of AD7746
#define I2C_adress 0x48
#define TCAADDR 0x70
double capa1=0;
double capa0=0;
volatile int cnt1=0;
volatile int cnt0=0;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  Serial.println("Serial initalized");
  delay(100);
  Wire.begin();
  delay(100);
  
  
  for(uint8_t i=0; i<2; i++){
    chanSelect(i);
    delay(5);
    Wire.beginTransmission(I2C_adress); // The adress for writing is 0x90 but in the wire library the write bit is automatically wiriteen so : 0x48 B100 1000
    Wire.write(0x07);   // sets register pointer to the given adress 0x07
    Wire.write(0x80);   // gives instructions to the device at adress 0x07 single conversion enabled
    Wire.write(0x00);   // gives instructions to the device at adress 0x08 voltage and temp sensordisconected
    Wire.write(0x1B);   // gives instructions to the device at adress 0x09 EXCA and EXCB pin configured EXCA enable EXCB inverted enabled
    Wire.write(0x01);   // gives instructions to the device at adress 0x0A cnersion time 20 ms 50Hz, contineous conversion mode -> important for the reading  39
    Wire.write(0x99);   // gives instructions to the device at adress 0x0B connects capacitive DAC to the positive capa input and allows the full range on chanel A (0-8pf)
                        // this shit must be calibrated they have +-20% error on the device 9D 9E for channel A
    Wire.write(0x80);   // gives instructions to the device at adress 0x0C connects capacitive DAC to the positive capa input and allows the full range on chanel B (0-8pf)
                        // Atention if second  last comand is 0x00 then it doesnt work if 0xFF then we can measure full range on cahnel B for channel A this doesnt matter
    Wire.write(0xF4);   // gives instructions to the device at adress 0x0D Offset calibration high bite
    Wire.write(0x88);   // gives instructions to the device at adress 0x0E Offset calibration low bite
    Wire.endTransmission();
    delay(10);
  }31.2
  
  delay(100);
  Serial.println("transmitted data");
  delay(100);
  attachInterrupt(1,reading1,FALLING);
  attachInterrupt(0,reading0,FALLING);
  pinMode(13,1);
  pinMode(12,1);
}


void loop()
{
  if(cnt1==1){
    chanSelect(1);
    capa1=readCFemtof();
    cnt1=0;
    digitalWrite(12,0);
    Serial.print('A');Serial.println(capa1);
    
    
  }
  if(cnt0==1){
    chanSelect(0);
    capa0=readCFemtof();
    cnt0=0;
    digitalWrite(13,0);
    Serial.print('B');Serial.println(capa0);
    int VoltValue=analogRead(A0);
    float V=VoltValue*(5.0/1023.0);
    Serial.print('V');Serial.println(V);
    
    
  }
  
  /*delay(100);
  readChanAorB('A');
  capa=readCFemtof();
  Serial.print('A');Serial.println(capa);
  delay(1);
  readChanAorB('B');
  capa=readCFemtof();
  Serial.print('B');Serial.println(capa);*/
  
}

void chanSelect(uint8_t i){
  if(i>7)return;
  Wire.beginTransmission(TCAADDR);
  Wire.write(1<<i);
  Wire.endTransmission();
}

void reading1(){
  cnt1=1;
  digitalWrite(12,1);
}

void reading0(){
  cnt0=1;
  digitalWrite(13,1);
}


uint32_t readCFemtof()
{
  unsigned char buffer[4];
  Wire.beginTransmission(I2C_adress);
  Wire.write(0x00);  // register to read
  Wire.endTransmission(false); // if false the the adresspointer is not reset to zero!
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

  return 99200*(double)C/16777215; // 8192*C/(2^24-1) ensures value between 0 and 8.192pf. Is the capacitance in femto farad.
}

void readChanAorB(char chanel)
{
  if(chanel=='A'){
    Wire.beginTransmission(I2C_adress); // The adress for writing is 0x90 but in the wire library the write bit is automatically wiriteen so : 0x48 B100 1000
    Wire.write(0x07);   // sets register pointer to the given adress 0x07 Cap setup register bit 6 chooses Chaenl Aor B
    Wire.write(0x80);   // gives instructions to the device at adress 0x07 single conversion enabled sets multiplexer to A
    Wire.endTransmission(false);
  }
  else if(chanel=='B'){
    Wire.beginTransmission(I2C_adress); // The adress for writing is 0x90 but in the wire library the write bit is automatically wiriteen so : 0x48 B100 1000
    Wire.write(0x07);   // sets register pointer to the given adress 0x07 Cap setup register bit 6 chooses Chaenl A or B
    Wire.write(0xC0);   // gives instructions to the device at adress 0x07 single conversion enabled sets multiplexer to B
    Wire.endTransmission(false);
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
