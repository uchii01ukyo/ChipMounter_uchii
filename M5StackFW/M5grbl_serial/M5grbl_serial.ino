#include <M5Stack.h>
#include "GrblControl.h"

#define I2C_ADDR0 0x70 // default address (1st)
#define I2C_ADDR1 0x71 // alternative address (2nd)

#define SOL_A 26
#define SOL_B 12
#define SOL_C 13
#define SOL_D 5

GRBL _GRBL0 = GRBL(I2C_ADDR0);
GRBL _GRBL1 = GRBL(I2C_ADDR1);
uint8_t fGRBL = 1;

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

  /*
  #define XY_STEP_PER_MM 160 // 1mm(cmd) -> 2mm(actual), 1/32 microstep
  #define Z_STEP_PER_MM 160 // 1mm(cmd) -> 4mm(actual), 1/32 microstep, 1/5
  #define ACC 500 // acc is converted *(60*60) in M5-GRBL, 1/32 microstep
  */

  // GRBL0 Setting
  _GRBL0.Init();
  _GRBL0.Gcode("$0=160"); //X[step/mm]
  _GRBL0.Gcode("$1=160"); //Y[step/mm]
  _GRBL0.Gcode("$2=80"); //Z[step/mm]
  _GRBL0.Gcode("$3=30");  //step pulse
  _GRBL0.Gcode("$4=800"); // default feed rate[mm/min] (for G1)
  _GRBL0.Gcode("$5=800"); // default seek rate[mm/min] (for G0)
  _GRBL0.Gcode("$6=0"); // step port invert mask (invert X&Y axis, 32(X)+64(Y)=96)
  _GRBL0.Gcode("$8=50"); // acc[mm/sec^2]
  _GRBL0.Gcode("$15=0"); // invert ST
  _GRBL0.Gcode("$16=0"); // enable hard limit[bool](1=enable)
  _GRBL0.Gcode("$17=1"); // enable homing[bool](1=have to homing first)
  _GRBL0.Gcode("$18=0"); // homing direction(128(XYZ)=224)
  _GRBL0.Gcode("$19=800"); // homing feed rate[mm/min]
  _GRBL0.Gcode("$20=800"); // homing seek rate[mm/min]
  _GRBL0.Gcode("$22=0"); // disable homing pulloff[mm]

  // GRBL1 Setting
  _GRBL1.Init();
  _GRBL1.Gcode("$0=64"); //X[step/mm]
  _GRBL1.Gcode("$3=30");  //step pulse
  _GRBL1.Gcode("$4=800"); // default feed rate[mm/min] (for G1)
  _GRBL1.Gcode("$5=800"); // default seek rate[mm/min] (for G0)
  _GRBL1.Gcode("$17=0"); // enable homing[bool](1=have to homing first)
  _GRBL1.Gcode("G91"); // relative mode for GRBL1

  // PinMode
  pinMode(SOL_A, OUTPUT); digitalWrite(SOL_A, 0);
  pinMode(SOL_B, OUTPUT); digitalWrite(SOL_B, 0);
  // pinMode(SOL_C, OUTPUT); digitalWrite(SOL_C, 0);
  pinMode(SOL_D, OUTPUT); digitalWrite(SOL_D, 0);

  // UserInterface
  Serial.begin(115200);
  m5.Lcd.setTextColor(WHITE, BLACK);
  m5.Lcd.setTextSize(3);
  m5.Lcd.setBrightness(100);
  M5.Lcd.setCursor(70, 20);
  M5.Lcd.println("ChipMounter");
  M5.Lcd.setCursor(60, 200);
  M5.Lcd.println("A");
  M5.Lcd.setCursor(155, 200);
  M5.Lcd.println("B");
  M5.Lcd.setCursor(250, 200);
  M5.Lcd.println("C");
  m5.Lcd.setTextSize(2);
  M5.Lcd.setCursor(100, 55);
  M5.Lcd.println("2022.07.21");

  //
  ledcSetup(LEDC_CHANNEL_0, LEDC_BASE_FREQ, LEDC_TIMER_BIT);
  ledcAttachPin(TDS_CLK_PIN, LEDC_CHANNEL_0);
  ledcWrite(LEDC_CHANNEL_0, 0x00);

  // Inicial Solenoid
  SolenoidStatus(0, 0);
  SolenoidStatus(1, 0);
  SolenoidStatus(2, 0);
  SolenoidStatus(3, 0);
  
  while (Serial.available()) Serial.read(); // force serial buffer empty
  ReadGRBLstatus(0);
  ReadGRBLstatus(1);
  Serial.println("ready");
}


void SolenoidStatus(int ch, int status){
  fGRBL = 0;
  if (ch == 0) {
    if (status == 1) digitalWrite(SOL_A, 1);
    else digitalWrite(SOL_A, 0);
  }
  else if (ch == 1) {
    if (status == 1) digitalWrite(SOL_B, 1);
    else digitalWrite(SOL_B, 0);
  }
  else if (ch == 2){
    if (status == 1) ledcWrite(LEDC_CHANNEL_0, SOLC_ON_DUTY);
    else ledcWrite(LEDC_CHANNEL_0, SOLC_OFF_DUTY);
  }
  else if (ch == 3){
    if (status == 1) digitalWrite(SOL_D, 1);
    else digitalWrite(SOL_D, 0);
  }
}

void ReadGRBLstatus(int ch) {
  String s;
  if (ch == 0) s = _GRBL0.ReadLine();
  if (ch == 1) s = _GRBL1.ReadLine();
  Serial.print(s);
}


int pos = 0;
char buf[1024];
int fSolCD = 0;
void loop() {
  char c;
  int ch, i;
  
  M5.update();
  // unlock
  if (M5.BtnA.wasPressed()) {
    _GRBL0.Gcode("$X");
    delay(100);
    _GRBL0.Gcode("$X");
    ReadGRBLstatus(0);
    delay(100);
    _GRBL1.Gcode("$X");
    delay(100);
    _GRBL1.Gcode("$X");
    ReadGRBLstatus(1);
  }

   if (M5.BtnB.wasPressed()) {
    _GRBL0.Gcode("$H");
    delay(100);
    _GRBL0.Gcode("G1X-6");
    delay(100);
    _GRBL0.Gcode("G1X-1");
    delay(100);
    _GRBL0.Gcode("G1X-6");
    delay(100);
    _GRBL0.Gcode("G1X-1");
    delay(100);
    _GRBL0.Gcode("G1X-6");
    delay(100);
    _GRBL0.Gcode("G1X-2.5");
    delay(100);
    ReadGRBLstatus(0);
  }

  while (Serial.available()) {
    c = Serial.read();
    if (c == '\r' || c == '\n') {
      buf[pos] = '\0';
      if (pos > 0 && (buf[pos - 1] == '\r' || buf[pos - 1] == '\n')) buf[pos - 1] = '\0';
      if (pos != 0) {
        Serial.print('['); Serial.print(buf); Serial.println(']');
      }
      fGRBL = 1;
      if (buf[0] == 'M') {
        if (buf[1] == '3') SolenoidStatus(0, 1);      // M3:Solnenoid A on
        else if (buf[1] == '5') SolenoidStatus(0, 0); // M5:Solnenoid A off
        else if (buf[1] == '7') SolenoidStatus(1, 1); // M7:Solnenoid B on
        else if (buf[1] == '9') SolenoidStatus(1, 0); // M9:Solnenoid B off
        else if (buf[1] == '1' && buf[2] == '0') SolenoidStatus(2, 1); // M10: Solnenoid C on
        else if (buf[1] == '1' && buf[2] == '1') SolenoidStatus(2, 0); // M11: Solnenoid C off
        else if (buf[1] == '1' && buf[2] == '2') SolenoidStatus(3, 1); // M12: Solnenoid D on
        else if (buf[1] == '1' && buf[2] == '3') SolenoidStatus(3, 0); // M13: Solnenoid D off
      }
      if (fGRBL == 1) {
        ch = 0;
        // A/B/C axis -> GRBL1's X/Y/Z axis
        for (i = 0; i < pos; i++) {
          if (buf[i] == 'A') {ch = 1; buf[i] = 'X';}
          if (buf[i] == 'B') {ch = 1; buf[i] = 'Y';}
          if (buf[i] == 'C') {ch = 1; buf[i] = 'Z';}
        }
        Serial.print(ch); Serial.print(' '); Serial.println(buf);        
        if (ch == 0) {
          _GRBL0.Gcode(buf);
          ReadGRBLstatus(0);
        }
        else {
          _GRBL1.Gcode(buf);
          ReadGRBLstatus(1);
        }
      }
      pos = 0;
    }
    else buf[pos++] = c;
  }
}
