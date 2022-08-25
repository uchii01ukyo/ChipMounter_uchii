#include <M5Stack.h>
#include "GrblControl.h"

#define I2C_ADDR0 0x70 // default address (1st)
#define I2C_ADDR1 0x71 // alternative address (2nd)

#define SOL_A 26
#define SOL_B 12
#define SOL_C 13
#define SOL_D 5

uint8_t fGRBL = 1;
int pos = 0, count;
char buf[1024];
String fileName, totalParts, partNum;

GRBL _GRBL0 = GRBL(I2C_ADDR0);
GRBL _GRBL1 = GRBL(I2C_ADDR1);

void setup() {
  M5.begin();
  M5.Power.begin();
  Serial.begin(115200);
  while (Serial.available()) Serial.read(); // force serial buffer empty
  
  // GRBL0 Setting
  //_GRBL0.Init();
  //_GRBL0.Gcode("$0=160");   //X[step/mm]
  //_GRBL0.Gcode("$1=160");   //Y[step/mm]
  //_GRBL0.Gcode("$2=160");   //Z[step/mm]
  //_GRBL0.Gcode("$3=30");    //step pulse
  //_GRBL0.Gcode("$4=160");   // default feed rate[mm/min] (for G1)
  //_GRBL0.Gcode("$5=160");   // default seek rate[mm/min] (for G0)
  //_GRBL0.Gcode("$6=96");     // step port invert mask (invert X&Y axis, 32(X)+64(Y)=96)
  //_GRBL0.Gcode("$8=50");   // acc[mm/sec^2]
  //_GRBL0.Gcode("$15=0");    // invert ST
  //_GRBL0.Gcode("$16=0");    // enable hard limit[bool](1=enable)
  //_GRBL0.Gcode("$17=1");    // enable homing[bool](1=have to homing first)
  //_GRBL0.Gcode("$18=224");    // homing direction(32(X)+64(Y)+128(Z)=224)
  //_GRBL0.Gcode("$19=160");  // homing feed rate[mm/min]
  //_GRBL0.Gcode("$20=160");  // homing seek rate[mm/min]
  //_GRBL0.Gcode("$21=1");
  //_GRBL0.Gcode("$22=0");    // disable homing pulloff[mm]

  // GRBL1 Setting
  _GRBL1.Init();
  _GRBL1.Gcode("$0=64");    //X[step/mm]
  _GRBL1.Gcode("$3=30");    //step pulse
  _GRBL1.Gcode("$4=800");   // default feed rate[mm/min] (for G1)
  _GRBL1.Gcode("$5=800");   // default seek rate[mm/min] (for G0)
  //_GRBL1.Gcode("$17=0");    // enable homing[bool](1=have to homing first)
  _GRBL1.Gcode("G91");      // relative mode for GRBL1
  
  // Solenoid Setting
  pinMode(SOL_B, OUTPUT); digitalWrite(SOL_B, 0);
  pinMode(SOL_D, OUTPUT); digitalWrite(SOL_D, 0);
  
  ReadGRBLstatus(0);
  ReadGRBLstatus(1);
  initial_LCD();
}

void ReadGRBLstatus(int ch) {
  String s;
  if (ch == 0) s = _GRBL0.ReadLine();
  //if (ch == 1) s = _GRBL1.ReadLine();
  Serial.print(s);
}

void loop() {
  char c;
  int ch, i;
  
  M5.update();
  
  if (M5.BtnA.wasPressed()) {
    _GRBL0.Gcode("G1X-6F200");
  }
  if (M5.BtnB.wasPressed()) {
    _GRBL0.Gcode("G1X0");
  }

  while (Serial.available()) {
    c = Serial.read();
    if (c == '\r' || c == '\n') {
      fGRBL = 1;
      buf[pos] = '\0';
      if (pos > 0 && (buf[pos - 1] == '\r' || buf[pos - 1] == '\n')) buf[pos - 1] = '\0';
      if (pos != 0) {Serial.print('['); Serial.print(buf); Serial.println(']');}
      
      if (buf[0] == 'S') {
        fGRBL = 0;
        if(buf[1]=='1'){
          fileName = buf;
          fileName.replace("S1:", "");
          M5.Lcd.setTextSize(3);
          M5.Lcd.setCursor(20, 20);
          // if(fileName.length>16){fileName=fileName.substring(0,16);}
          M5.Lcd.println(fileName);
        }
        if(buf[1]=='2'){
          totalParts = buf;
          totalParts.replace("S2:", "");
          m5.Lcd.setTextSize(2);
          M5.Lcd.setCursor(100, 150);
          M5.Lcd.println(totalParts);
        }
        if(buf[1]=='3'){
          partNum = buf;
          partNum.replace("S3:", "");
          float percent=partNum.toInt()/totalParts.toInt();
          progress(percent);
        }
      }
      if (buf[0] == 'M') {
        fGRBL = 1;
        if (buf[1] == '3') digitalWrite(SOL_B, 1);      // M3:Solnenoid B on
        else if (buf[1] == '5') digitalWrite(SOL_B, 0); // M5:Solnenoid B off
        else if (buf[1] == '7') digitalWrite(SOL_D, 1); // M7:Solnenoid D on
        else if (buf[1] == '9') digitalWrite(SOL_D, 0); // M9:Solnenoid D off
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


void progress(float percent){
  M5.Lcd.progressBar(20,60,280,20,percent); // posX, posY, width, height 
  m5.Lcd.setTextSize(2);
  M5.Lcd.setCursor(130, 90);
  M5.Lcd.println(int(count));
  M5.Lcd.setCursor(170, 90);
  M5.Lcd.println("%");
}

void initial_LCD(){
  m5.Lcd.setTextColor(WHITE, BLACK);
  m5.Lcd.setBrightness(100);
  //m5.Lcd.setTextSize(3);
  //M5.Lcd.setCursor(20, 20);
  //M5.Lcd.println("FileName.csv");
  m5.Lcd.setTextSize(2);
  M5.Lcd.setCursor(45, 220);
  M5.Lcd.println("Tune");
  M5.Lcd.setCursor(135, 220);
  M5.Lcd.println("Pause");
  M5.Lcd.setCursor(235, 220);
  M5.Lcd.println("Stop");
  m5.Lcd.setTextSize(2);
  M5.Lcd.setCursor(20, 150);
  M5.Lcd.println("Parts:");
  progress(0);
}
