# coding: UTF-8
import csv
import time
import os
import socket

# ---- Fabrication Setting [mm] ----
trayPosX=[29.189, 69.585, 107.982]
trayPosY=-27.24 # 50.21
shiftX=3.800; shiftY=2.000
feed=4.000
down=8.000
pulse=[31.900, 31.400, 6.440, 18.000] # [mm/G1X1], [mm/G1Y1], [mm/G1Z1], [mm/G1A1]
home=[0.000 , -6.800, -3.000] # X,Y,Z
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

#filePath = '../data/sample.csv'

def main(filePath):
    # UDP waiting
    waiting_udp()

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
    elif(axis=='R'):
        gcode = float(mm)/pulse[3]
    gcode_str=str(round(gcode, 3))
    return gcode_str

def generation_gcode(posX, posY, rot, trayNum):
    # send_serial("G90G1X0Y0F800")  # up
    send_serial("G90G1X" + mm_gcode(trayPosX[int(trayNum)]-shiftX,'X') + "Y" + mm_gcode(trayPosY+shiftY,'Y') + "F400") # trayhole
    send_serial("G90G1Z-" + str(down) + "F400") # down
    send_serial("G90G1Y" + mm_gcode(trayPosY+shiftY+feed,'Y') + "F50") # feeder
    send_serial("G90G1Z-5F400")  # up
    send_serial("G90G1X" + mm_gcode(trayPosX[int(trayNum)],'X') + "Y" + mm_gcode(trayPosY,'Y') + "F800") # tray
    send_serial("G90G1Z-" + str(down) + "F800") # down
    send_serial("M3")  # pump ON
    send_serial("G90G1Z0F800")  # up
    send_serial("G90G1X" + mm_gcode(posX,'X') + "Y" + mm_gcode(posY,'Y') + "F800") # set position
    send_serial("G91G1A" + mm_gcode(rot,'R'))   # rotation
    send_serial("G90G1Z-4.6F800") # down
    send_serial("M5")               # pump OFF
    send_serial("M7")               # pump ON
    # time.sleep(0.01) # waiting
    send_serial("M9")               # pump OFF
    send_serial("G90G1Z0F800")  # up

def start_gcode():
    send_serial("$X") # unlock
    send_serial("$H") # homing
    send_serial("G92X0Y0Z0") # origin setting
    send_serial("G90G1X" + str(home[0]) + "Y" + str(home[1]) + "F200") # origin
    send_serial("G90G1Z" + str(home[2]) + "F200") # origin
    send_serial("G92X0Y0Z0") # origin setting

def finish_gcode():
    send_serial("G90G1Z0F200")  # up
    send_serial("G90G1X0Y0F200") # home
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

def waiting_udp():
    print("wait")
    while True: 
        f = open('waiting.txt', 'r')
        data = f.read()
        f.close()
        if(data=='OK'):
            break
        print(".",end=" ")
        time.sleep(0.5) # waiting
    print("OK")

if __name__ == '__main__':
    main()