/*
========================================================
SMART HOME IoT - DAY 7

MODE SWITCH GUIDE:

👉 MODE 1 (REAL ARDUINO - USE THIS WHEN UPLOADING TO BOARD)
    #define MODE_ARDUINO 1

👉 MODE 2 (SIMULATION ON PC / VISUAL STUDIO TERMINAL)
    #define MODE_ARDUINO 0

--------------------------------------------------------
WHEN USING ARDUINO:
- KEEP Serial.print LINES ACTIVE

WHEN SIMULATING ON PC:
- USE C++ COMPILER OR PLATFORMIO TERMINAL
- RANDOM VALUES WILL BE PRINTED
========================================================
*/
#include <stdio.h>
#include <stdlib.h> 
#define MODE_ARDUINO 0   // 🔁 CHANGE THIS TO 1 FOR REAL ARDUINO

#if MODE_ARDUINO
  #include <Arduino.h>
#endif

int fanSpeed = 0;
int acTemp = 24;
int lightState = 0;

unsigned long lastUpdate = 0;

void setup() {
#if MODE_ARDUINO
  Serial.begin(9600);
#endif
}

void loop() {

#if MODE_ARDUINO

  // ================= REAL ARDUINO MODE =================

  fanSpeed = (millis() / 1000) % 100;
  acTemp = 22 + (millis() / 5000) % 6;
  lightState = (millis() / 5000) % 2;

  Serial.print("LIGHT:");
  Serial.print(lightState);

  Serial.print(",FAN:");
  Serial.print(fanSpeed);

  Serial.print(",AC:");
  Serial.println(acTemp);

  delay(2000);

#else

  // ================= SIMULATION MODE (PC TESTING) =================

  // random values for testing dashboard logic
  fanSpeed = rand() % 101;      // 0–100
  acTemp = 18 + rand() % 10;    // 18–27
  lightState = rand() % 2;      // 0 or 1

  // print to terminal
  printf("LIGHT:%d,FAN:%d,AC:%d\n", lightState, fanSpeed, acTemp);

  // slow down output like Arduino loop delay
  for (volatile long i = 0; i < 100000000; i++);

#endif
}