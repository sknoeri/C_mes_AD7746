//I/O pin configuration registers
#define DIRD *((volatile unsigned char*) 0x2A) // Data dircetion register of port D
#define PIND *((volatile unsigned char*) 0x29) // Pin set register of port D
#define DIRB *((volatile unsigned char*) 0x24) // Data dircetion register of port B
#define PINB *((volatile unsigned char*) 0x23) // Pin set register of port B

// Timer0 configuration register
#define TCCR2A *((volatile unsigned char*) 0xB0) // Timer register A
#define TCCR2B *((volatile unsigned char*) 0xB1) // Timer register B
#define TIMSK2 *((volatile unsigned char*) 0x70) // Timer interrup enable register

volatile unsigned char b=0;
void setup() {
  DIRB=0;
  DIRB|=(1<<5); // Sets direction register for PB5 
  initTimer2();
  
  
}

void loop() {
  ///digitalWrite(6,1);
  //analogWrite(6,100); 
  //PINB^=(1<<5);
  //delay(1000);                       // wait for a second
}

void initTimer2(){
  //TCCR1A=0;
  //TCCR1B=0;
  //TIMSK1=0;
  TCCR2A|=(0<<7)|(0<<6);          // Timer in normal operation, OC0A disconected
  TCCR2A|=(0<<0)|(0<<1);          // Timer in normal opperation counts until 0xFF and sets TOV flag there
  TCCR2B|=(0<<3);          // Timer in normal opperation counts until 0xFF and sets TOV flag there continuation of TCCR0A
  TCCR2B|=(1<<2)|(1<<1)|(1<<0);          // No prescaling takes clock frequenzie
  TIMSK2|=(1<<0);          // Enalbs the overflow interuppt
}
ISR(TIMER2_OVF_vect){
  b++;
  if(b==10){
    b=0;
    PINB|=(1<<5); // Toggels PB5 
  }
}
