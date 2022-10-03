#include <Arduino_FreeRTOS.h>
#include <Wire.h>
#include "Adafruit_MPRLS.h"

// You dont *need* a reset and EOC pin for most uses, so we set to -1 and don't connect
#define RESET_PIN  -1  // set to any GPIO pin # to hard-reset on begin()
#define EOC_PIN    -1  // set to any GPIO pin to read end-of-conversion by pin
Adafruit_MPRLS mpr = Adafruit_MPRLS(RESET_PIN, EOC_PIN);

// define Task for for control
void Control_pres( void *pvParameters );

// the setup function runs once when you press reset or power the board
void setup() {
  pinMode(5,OUTPUT);
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  Serial.println("MPRLS Simple Test");
  if (! mpr.begin()) {
    Serial.println("Failed to communicate with MPRLS sensor, check wiring?");
    while (1) {
      delay(10);
    }
  }
  Serial.println("Found MPRLS sensor");

  
  // Now set up two Tasks to run independently.
  xTaskCreate(
    Control_pres
    ,  "Control_pres"  // A name just for humans
    ,  128  // This stack size can be checked & adjusted by reading the Stack Highwater
    ,  NULL //Parameters for the task
    ,  2  // Priority, with 3 (configMAX_PRIORITIES - 1) being the highest, and 0 being the lowest.
    ,  NULL ); //Task Handle

  // Now the Task scheduler, which takes over control of scheduling individual Tasks, is automatically started.
}

void loop()
{
  // Empty. Things are done in Tasks.
}

/*--------------------------------------------------*/
/*---------------------- Tasks ---------------------*/
/*--------------------------------------------------*/
uint8_t duty=0;
void Control_pres( void *pvParameters __attribute__((unused)) )  // This is a Task.
{
 
  for (;;) // A Task shall never return or exit.
  {
    float pressure_hPa = mpr.readPressure();
    Serial.println(pressure_hPa); //Serial.print("Pressure (hPa): "); 
    //Serial.print("Duty: "); Serial.println(duty);
    digitalWrite(5,duty);
    if(duty>256){
      duty=0;
    }
    duty=duty+10;
    //Serial.print(portTICK_PERIOD_MS);
    vTaskDelay(100 / portTICK_PERIOD_MS);  // one tick delay (10ms) in between reads for stability
  }
}
