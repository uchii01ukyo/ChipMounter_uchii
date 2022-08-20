# coding: UTF-8
import csv
import serial
import time
import os

# ---- Serial Setting ---------
port_name = "/dev/cu.SLAB_USBtoUART"
speed = 115200
filePath = '/Users/uchiiukyo/ChipMounter_uchii/src/sample.csv'
# ---- Fabrication Setting ----
down=3
trayPosX=[1,1]
trayPosY=1
# -----------------------------

def main():
    send_serial('S1' + str(get_fileName(filePath)))
    send_serial('S2' + str(get_totalLine(filePath)))

    # GCODE
    start_gcode()
    count=0
    with open(filePath, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # skip header
        for line in reader:
            count+=1
            print("Parts count: " + str(count))
            print(line)
            generation_gcode(line[3], line[4], line[5], line[7])
            send_serial('S3' + str(count))
    finish_gcode()

def generation_gcode(posX, posY, rot, trayNum):
    send_serial("G1Z" + str(down))  # up
    send_serial("G1X-" + str(trayPosX[int(trayNum)]) + "Y-" + str(trayPosY)) # tray
    send_serial("G1Z-" + str(down)) # down
    send_serial("M3")               # pump ON
    send_serial("G1Z" + str(down))  # up
    send_serial("G1X-" + str(posX) + "Y-" + str(posY)) # set
    send_serial("G1A" + str(rot))   # rotation
    send_serial("G1Z-" + str(down)) # down
    send_serial("M5")               # pump OFF

def start_gcode():
    send_serial("$X") # unlock
    send_serial("$H") # homing
    send_serial("G1X-0.3Y-6Z-15") # home

def finish_gcode():
    send_serial("G1Z" + str(down*2))  # up
    send_serial("G1X-0.3Y-6Z-15")     # home

def send_serial(send_command):
    ser = serial.Serial(port_name, speed, timeout = 0.1)
    time.sleep(1) # waiting
    print(send_command)
    ser.write(send_command + '\r')
    ser.close()

def get_totalLine(filePath):
    with open(filePath) as myfile:
        totalLines = sum(1 for line in myfile)
    return totalLines

def get_fileName(filePath):
    fileName = os.path.basename(filePath)
    return fileName

if __name__ == '__main__':
    main()