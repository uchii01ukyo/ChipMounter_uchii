import socket
import serial
import time

fNoSerial = False

port_name = "/dev/cu.SLAB_USBtoUART"
speed = 115200
# local client
Client_IP = "127.0.0.1"
Client_Port = 10031
Client_Addr = (Client_IP, Client_Port)
# UDP-Serial server
UDP_SERIAL_IP = "127.0.0.1"
UDP_SERIAL_Port = 10030
UDP_SERIAL_Addr = (UDP_SERIAL_IP, UDP_SERIAL_Port)
BUFSIZE = 1024

udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSock.bind(UDP_SERIAL_Addr)
udpSock.settimeout(1)

if fNoSerial == True:
    print("***Debug mode without serial***")
else:
    ser = serial.Serial(port_name, speed, timeout = 0.1)
    time.sleep(1)


def main():
    print("lock -> unlock")
    send_cmd('$X')
    # send_cmd('$H')

    f = open('waiting.txt', 'w')
    f.write('OK')
    f.close()
    print("Ready... Python csv_gcode.py")

    while True:                                     
        try:
            data, addr = udpSock.recvfrom(BUFSIZE)
        except:
            pass
        else:
            # print("> " + data.decode())
            send_cmd(data.decode())
            udpSock.sendto("ok".encode('utf-8'), addr)
            print("-> OK")
            if data.decode() == "finish":
                break
        
    print("finish")
    if fNoSerial == False:
        ser.close()


def wait_motion():
    if fNoSerial == False:
        finish = False
        count = 0
        while count < 2: # check 2 times of "IDLE" to avoid incorrect motion and detection
            ser.write('@\n')
            line = "init"
            while count < 2 and len(line) != 0:
                line0 = ser.readline()
                try:
                    line = line0.decode()
                    # print("line: " + line)
                except:
                    pass
                else:
                    finish = 'IDLE' in line
                    if finish == True:
                        count = count + 1
                    time.sleep(0.01)
    print("-> done")


def send_cmd(cmd):
    if fNoSerial == False:
        cmd = cmd + '\n'
        s = cmd.encode()
        ser.write(s)
        if s[0] == 77: # 'M'
            time.sleep(0.01)
        else:
            wait_motion()

if __name__ == '__main__':
    main()