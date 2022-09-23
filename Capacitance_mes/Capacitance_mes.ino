#include <Wire.h>

//I/O pin configuration registers
#define DIRD *((volatile unsigned char*) 0x2A) // Data dircetion register of port D
#define PORTB*((volatile unsigned char*) 0x2B) // Pin set register of port B woks according to DIR port
#define PIND *((volatile unsigned char*) 0x29) // Pin toggle register of port D woks independent of DIR port

#define DIRB *((volatile unsigned char*) 0x24) // Data dircetion register of port B
#define PORTB*((volatile unsigned char*) 0x25) // Pin set register of port B woks according to DIR port
#define PINB *((volatile unsigned char*) 0x23) // Pin toggle register of port B woks independent of DIR port

// Timer2 configuration register
#define TCCR2A *((volatile unsigned char*) 0xB0) // Timer register A
#define TCCR2B *((volatile unsigned char*) 0xB1) // Timer register B
#define TIMSK2 *((volatile unsigned char*) 0x70) // Timer interrup enable register

#define TCCR1A *((volatile unsigned char*) 0x80) // Timer register A
#define TCCR1B *((volatile unsigned char*) 0x81) // Timer register B
#define TIMSK1 *((volatile unsigned char*) 0x6F) // Timer interrup enable register

#include "Adafruit_MPRLS.h"

// You dont *need* a reset and EOC pin for most uses, so we set to -1 and don't connect
#define RESET_PIN  -1  // set to any GPIO pin # to hard-reset on begin()
#define EOC_PIN    -1  // set to any GPIO pin to read end-of-conversion by pin
Adafruit_MPRLS mpr = Adafruit_MPRLS(RESET_PIN, EOC_PIN);


void setup() {
  // IO pin configuration
  DIRB=0;
  PORTB=0;
  DIRB|=(1<<5); // Sets direction register for PB5
  PORTD|=(0<<5);
  DIRD=0;
  PORTD=0;
  DIRD|=(1<<5); // Sets direction register for PB5
  PORTD|=(1<<5);
  // initialize the timer for measurimg the preasure at constant sample rate
  initTimer1();
  
  Serial.begin(115200);
}

void loop() { 
  PORTD|=(1<<5);
}

void initTimer2(){
  TCCR2A|=(0<<7)|(0<<6);          // Timer in normal operation, OC0A disconected
  TCCR2A|=(0<<0)|(0<<1);          // Timer in normal opperation counts until 0xFF and sets TOV flag there
  TCCR2B|=(0<<3);          // Timer in normal opperation counts until 0xFF and sets TOV flag there continuation of TCCR0A
  TCCR2B|=(1<<2)|(1<<1)|(1<<0);          // No prescaling takes clock frequenzie
  TIMSK2|=(1<<0);          // Enalbs the overflow interuppt
}
void initTimer1(){
  TCCR1A|=(0<<7)|(0<<6);          // Timer in normal operation, OC0A disconected
  TCCR1A|=(0<<0)|(0<<1);          // Timer in normal opperation counts until 0xFF and sets TOV flag there
  TCCR1B|=(0<<4)|(0<<3);          // Timer in normal opperation counts until 0xFF and sets TOV flag there continuation of TCCR0A
  TCCR1B|=(0<<2)|(0<<1)|(1<<0);          // No prescaling takes clock frequenzie
  TIMSK1|=(1<<0);          // Enalbs the overflow interuppt
}
unsigned char b=0;
unsigned char c=0;
ISR(TIMER1_OVF_vect){
  b++;
  if(b==50){
    b=0;
    c=32; 
    PORTB^=32; // Toggels PB
    //digitalWrite(13,1);
  }
}
