# coding: UTF-8
import csv
import serial
import time
import os
import udp_server

# ---- Serial Setting ---------
port_name = "/dev/cu.SLAB_USBtoUART"
speed = 115200
filePath = '/Users/uchiiukyo/ChipMounter_uchii/data/sample.csv'
# ---- Fabrication Setting [mm] ----
trayPosX=[10.000, 30.000]
trayPosY=1.000
shiftX=3.800; shiftY=2.000
feed=-4.000
# --------------------------------
down=6.00
pulse=[31.900, 31.400, 15.000] # [mm/G1X1], [mm/G1Y1], [mm/G1Z1]
home=[0.200 ,6.200, 6.000] # X,Y,Z
# --------------------------------

def main():
    send_serial('S1:' + str(get_fileName(filePath)))
    send_serial('S2:' + str(get_totalLine(filePath)))
    print('----------------')

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
            send_serial('S3:' + str(count))
    finish_gcode()


def mm_gcode(mm,axis):
    if(axis=='X'):
        gcode = float(mm)/pulse[0]
    elif(axis=='Y'):
        gcode = float(mm)/pulse[1]
    elif(axis=='Z'):
        gcode = float(mm)/pulse[2]
    gcode_str=str(round(gcode, 3))
    return gcode_str

def generation_gcode(posX, posY, rot, trayNum):
    send_serial("G1Z0F200")  # up
    send_serial("G1X" + mm_gcode(trayPosX[int(trayNum)]-shiftX,'X') + "Y" + mm_gcode(trayPosY-shiftY,'Y') + "F200") # trayhole
    send_serial("G1Z" + str(down) + "F200") # down
    send_serial("G1Y" + mm_gcode(feed,'Y') + "F200") # feeder
    send_serial("G1Z0F200")  # up
    send_serial("G1X" + mm_gcode(trayPosX[int(trayNum)],'X') + "Y" + mm_gcode(trayPosY,'Y') + "F200") # tray
    send_serial("G1Z" + str(down) + "F200") # down
    send_serial("M3")               # pump ON
    send_serial("G1Z0F200")  # up
    send_serial("G1X" + mm_gcode(posX,'X') + "Y" + mm_gcode(posY,'Y') + "F200") # set
    send_serial("G1A" + str(rot))   # rotation
    send_serial("G1Z" + str(down) + "F200") # down
    send_serial("M5")               # pump OFF
    send_serial("M7")               # pump ON
    time.sleep(0.2) # waiting
    send_serial("M9")               # pump OFF
    send_serial("G1Z0F200")  # up

def start_gcode():
    send_serial("$X") # unlock
    send_serial("$H") # homing
    send_serial("G1X" + str(home[0]) + "Y" + str(home[1]) + "Z" + str(home[2]) + "F200") # origin
    send_serial("G92X0Y0Z0") # origin setting

def finish_gcode():
    send_serial("G1Z0F200")  # up
    send_serial("G1X0.2Y6.2Z6F200") # home
    send_serial("finish") # finish

def send_serial(send_command):
    print(send_command)
    udp_server.send_cmd(send_command)
    # ser = serial.Serial(port_name, speed, timeout = 0.1)
    # time.sleep(2) # waiting
    # ser.write(send_command + '\r')
    # ser.close()

def get_totalLine(filePath):
    with open(filePath) as myfile:
        totalLines = sum(1 for line in myfile) - 1
    return totalLines

def get_fileName(filePath):
    fileName = os.path.basename(filePath)
    return fileName

if __name__ == '__main__':
    main()