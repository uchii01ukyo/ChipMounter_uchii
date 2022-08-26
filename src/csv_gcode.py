# coding: UTF-8
import csv
import time
import os
import socket

# ---- Serial Setting ---------
port_name = "/dev/cu.SLAB_USBtoUART"
speed = 115200
filePath = '/Users/uchiiukyo/ChipMounter_uchii/data/sample.csv'
# ---- Fabrication Setting [mm] ----
trayPosX=[10.000, 30.000]
trayPosY=1.000
shiftX=3.800; shiftY=2.000
feed=-4.000
# 
down=6.00
pulse=[31.900, 31.400, 6.440] # [mm/G1X1], [mm/G1Y1], [mm/G1Z1]
home=[0.200 , -6.200, -6.000] # X,Y,Z
# --------- UDP Setting ----------
# global udpSock, Client_Addr, UDP_SERIAL_Addr
Client_IP = "127.0.0.1"
Client_Port = 10031
Client_Addr = (Client_IP, Client_Port)
UDP_SERIAL_IP = "127.0.0.1"
UDP_SERIAL_Port = 10030
UDP_SERIAL_Addr = (UDP_SERIAL_IP, UDP_SERIAL_Port)
UDP_BUFSIZE = 1024
# 
udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSock.bind(Client_Addr)
udpSock.settimeout(1)
# --------------------------------
code_count=0

def main():
    send_serial('S1:' + str(get_fileName(filePath)))
    send_serial('S2:' + str(get_totalLine(filePath)))
    send_serial('S3:0')

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
    send_serial("G1Z-" + str(down) + "F200") # down
    send_serial("G1Y" + mm_gcode(feed,'Y') + "F200") # feeder
    send_serial("G1Z0F200")  # up
    send_serial("G1X" + mm_gcode(trayPosX[int(trayNum)],'X') + "Y" + mm_gcode(trayPosY,'Y') + "F200") # tray
    send_serial("G1Z-" + str(down) + "F200") # down
    send_serial("M3")               # pump ON
    send_serial("G1Z0F200")  # up
    send_serial("G1X" + mm_gcode(posX,'X') + "Y" + mm_gcode(posY,'Y') + "F200") # set position
    send_serial("G1A" + str(rot))   # rotation
    send_serial("G1Z-" + str(down) + "F200") # down
    send_serial("M5")               # pump OFF
    send_serial("M7")               # pump ON
    time.sleep(0.2) # waiting
    send_serial("M9")               # pump OFF
    send_serial("G1Z0F200")  # up

def start_gcode():
    send_serial("$X") # unlock
    send_serial("$H") # homing
    send_serial("G1X" + str(home[0]) + "Y" + str(home[1]) + "Z" + str(home[2]) + "F200") # origin
    send_serial("G92X0Y0Z0F200") # origin setting

def finish_gcode():
    send_serial("G1Z0F200")  # up
    send_serial("G1X0Y0F200") # home
    send_serial("finish") # finish

def get_totalLine(filePath):
    with open(filePath) as myfile:
        totalLines = sum(1 for line in myfile) - 1
    return totalLines

def get_fileName(filePath):
    fileName = os.path.basename(filePath)
    return fileName

def send_serial(cmd):
    # global udpSock, UDP_SERIAL_Addr
    global code_count
    code_count=code_count+1
    command = cmd + ',' + str(code_count)
    print(command)
    udpSock.sendto(command.encode('utf-8'), UDP_SERIAL_Addr)

    while True:
        try:
            data, addr = udpSock.recvfrom(UDP_BUFSIZE)
        except:
            pass
        else:
            if data.decode() == "ok":
                print("-> OK")
                break


if __name__ == '__main__':
    main()