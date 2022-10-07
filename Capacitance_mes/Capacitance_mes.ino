
//#include <Arduino_FreeRTOS.h>
#include <Wire.h>
#define I2C_adress 0x48

// define Task for for control
//void Cpacitance( void *pvParameters );

// the setup function runs once when you press reset or power the board
void setup() {
  pinMode(5,OUTPUT);
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
  /*unsigned char data[2];
  readRegisters(0x01,3,data[2]);
  Serial.print("Cadp data 1:");Serial.println(data[0],BIN);
  Serial.print("Cadp data 2:");Serial.println(data[1],BIN);
  Serial.print("Cadp data 3:");Serial.println(data[2],BIN);*/
  // Now set up two Tasks to run independently.
  /*xTaskCreate(
    Cpacitance
    ,  "Cpacitance"  // A name just for humans
    ,  128  // This stack size can be checked & adjusted by reading the Stack Highwater
    ,  NULL //Parameters for the task
    ,  2  // Priority, with 3 (configMAX_PRIORITIES - 1) being the highest, and 0 being the lowest.
    ,  NULL ); //Task Handle

  // Now the Task scheduler, which takes over control of scheduling individual Tasks, is automatically started.*/
}

void loop()
{
  Serial.println("Hallo");
  delay(1000);
  // Empty. Things are done in Tasks.
  unsigned char buffer[4];
  Wire.beginTransmission(I2C_adress);
  Wire.write(0x01);  // register to read
  Wire.endTransmission();
  Serial.println("Set pointer to 0x1");
  Wire.requestFrom(I2C_adress, 4); // read a byte
  char i = 0;
  while (i<4) {
    while(!Wire.available()) {
      // waiting
      Serial.print("waits on wire");
    }
    buffer[i] = Wire.read();
    i++;
  }
  uint32_t C=0;
  C = ((uint32_t)buffer[1]<<16)|((uint32_t)buffer[2]<<8)|((uint32_t)buffer[3]); // No fixpoint aritmeritc is done yet
  double capa = 8000*(double)C/16777215; // 8*C/(2^24-1)-4 ensures value between -4 and 8. Is the capacitance in 10^3 pico farad
  Serial.print("Buffer 0: ");Serial.println(buffer[0]);
  Serial.print("Buffer 1: ");Serial.println(buffer[1]);
  Serial.print("Buffer 2: ");Serial.println(buffer[2]);
  Serial.print("Buffer 3: ");Serial.println(buffer[3]);
  Serial.println(C);
  Serial.println(capa);
}

/*--------------------------------------------------*/
/*---------------------- Tasks ---------------------*/
/*--------------------------------------------------*/

/*void Cpacitance( void *pvParameters __attribute__((unused)) )  // This is a Task.
{
 
  for (;;) // A Task shall never return or exit.
  {
    vTaskDelay(100 / portTICK_PERIOD_MS);  // one tick delay (10ms) in between reads for stability
  }
}*/


void readRegisters(unsigned char r, unsigned int numberOfBytes, unsigned char buffer[])
{
  unsigned char v;
  Wire.beginTransmission(I2C_adress);
  Wire.write(r);  // register to read
  Wire.endTransmission();

  Wire.requestFrom(I2C_adress, numberOfBytes); // read a byte
  char i = 0;
  while (i<numberOfBytes) {
    while(!Wire.available()) {
      // waiting
      Serial.print("waits on wire");
    }
    buffer[i] = Wire.read();
    i++;
  }
}






































/*#include <Wire.h>

//I/O pin configuration registers
#define DIRD *((volatile unsigned char*) 0x2A) // Data dircetion register of port D
#define PORTB*((volatile unsigned char*) 0x2B) // Pin set register of port B woks according to DIR port
#define PIND *((volatile unsigned char*) 0x29) // Pin toggle register of port D woks independent of DIR port

#define DIRB *((volatile unsigned char*) 0x24) // Data dircetion register of port B
#define PORTB*((volatile unsigned char*) 0x25) // Pin set register of port B woks according to DIR port
#define PINB *((volatile unsigned char*) 0x23) // Pin toggle register of port B woks independent of DIR port

// Timer0 configuration register
#define TCCR2A *((volatile unsigned char*) 0xB0) // Timer register A
#define TCCR2B *((volatile unsigned char*) 0xB1) // Timer register B
#define TIMSK2 *((volatile unsigned char*) 0x70) // Timer interrup enable register


void setup() {
  DIRB=0;
  PORTB=0;
  DIRB|=(1<<5); // Sets direction register for PB5
  PORTD|=(0<<5);
  DIRD=0;
  PORTD=0;
  DIRD|=(1<<5); // Sets direction register for PB5
  PORTD|=(1<<5);
  initTimer2();
  Serial.begin(115200);
}

void loop() { 
  PORTD|=(1<<5);
  Serial.print("Tis is inerrupt ");Serial.println(*TIMER2_OVF_vect);
}

void initTimer2(){
  TCCR2A|=(0<<7)|(0<<6);          // Timer in normal operation, OC0A disconected
  TCCR2A|=(0<<0)|(0<<1);          // Timer in normal opperation counts until 0xFF and sets TOV flag there
  TCCR2B|=(0<<3);          // Timer in normal opperation counts until 0xFF and sets TOV flag there continuation of TCCR0A
  TCCR2B|=(1<<2)|(1<<1)|(1<<0);          // No prescaling takes clock frequenzie
  TIMSK2|=(1<<0);          // Enalbs the overflow interuppt
}
unsigned char b=0;
unsigned char c=0;
ISR(TIMER2_OVF_vect){
  b++;
  if(b==10){
    b=0;
    c=32; 
    PORTB^=32; // Toggels PB5
    Serial.print("Tis is B");Serial.println(PORTB);
    //digitalWrite(13,1);
  }
}*/
