import csv
import serial
import time

# ---- Serial Setting ---------
port_name = "/dev/ttyACM0"
speed = 115200
filePath = 'C:/Users/xxx/Desktop/test/テスト.csv'
fileName = 'テスト.csv'
# ---- Fabrication Setting ----
down=5
trayPosX=[1,2,3,4,5,6,7]
trayPosY=1
# -----------------------------

# memo
# Ref, Val, Package, PosX, PosY, Rot, Side, Tray

def main():
    # 
    max_rows=count_rows(filePath)
    send_serial(fileName)
    send_serial(max_rows)
    send_serial("EOF")

    # 
    start_gcode()
    with open(filePath, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # skip header
        for line in reader:
            if(line[5]=="top"):
                generation_gcode(line[4], line[5], line[6], line[7])
    finish_gcode()


def generation_gcode(posX, posY, rot, trayNum):
    send_serial("G1Z" + down)  # Up
    send_serial("G1X-" + trayPosX[trayNum] + "Y-" + trayPosX)
    send_serial("G1Z-" + down) # down
    send_serial("M3")
    send_serial("G1Z" + down)  # Up
    send_serial("G1X-" + posX + "Y-" + posY)
    send_serial("G1A" + rot) # rotation
    send_serial("G1Z-" + down) # down
    send_serial("M5")

def start_gcode():
    send_serial("$X")
    send_serial("$H")
    send_serial("G1X0Y0") # home

def finish_gcode():
    send_serial("G1Z" + down*2)  # Up
    send_serial("G1X0Y0")

def count_rows(filePath):
    max_rows = sum([1 for _ in open(filePath)])
    return max_rows

def send_serial(send_command):
    ser = serial.Serial(port_name, speed, timeout = 0.1)
    time.sleep(2) # waiting
    ser.write(chr(send_command)) # PC:char -> M5:byte
    ser.close()