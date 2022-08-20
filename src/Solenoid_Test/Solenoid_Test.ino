/* By Akita*/

#include <M5Stack.h>
// #include "GrblControl.h"

#define SOL_A 26
#define SOL_B 12
#define SOL_C 13
#define SOL_D 5

#define LEDC_CHANNEL_0 0
#define LEDC_TIMER_BIT 8
#define LEDC_BASE_FREQ 2400.0
#define TDS_CLK_PIN SOL_C
#define SOLC_ON_DUTY  0x80 // 50%
#define SOLC_OFF_DUTY 0x00 // 0%

void setup() {
  M5.begin();
  M5.Power.begin();
  Serial.begin(115200);
  
  pinMode(SOL_A, OUTPUT); digitalWrite(SOL_A, 0);
  pinMode(SOL_B, OUTPUT); digitalWrite(SOL_B, 0);
//  pinMode(SOL_C, OUTPUT); digitalWrite(SOL_C, 0);
  pinMode(SOL_D, OUTPUT); digitalWrite(SOL_D, 0);
  
  ledcSetup(LEDC_CHANNEL_0, LEDC_BASE_FREQ, LEDC_TIMER_BIT);
  ledcAttachPin(TDS_CLK_PIN, LEDC_CHANNEL_0);
  ledcWrite(LEDC_CHANNEL_0, 0x00);

  Serial.println("ready");
}


void loop() {
  M5.update();
  if (M5.BtnA.wasPressed()) {
    Serial.println("A Pressed");
    digitalWrite(SOL_A, 1); // ON
  }
  if (M5.BtnB.wasPressed()) {
    Serial.println("B Pressed");
    digitalWrite(SOL_A, 0); // OFF
  }
}
