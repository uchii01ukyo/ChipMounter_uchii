import socket
import time

global udpSock, UDP_SERIAL_Addr
# local client
Client_IP = "127.0.0.1"
Client_Port = 10031
Client_Addr = (Client_IP, Client_Port)
# UDP-Serial server
UDP_SERIAL_IP = "127.0.0.1"
UDP_SERIAL_Port = 10030
UDP_SERIAL_Addr = (UDP_SERIAL_IP, UDP_SERIAL_Port)

udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSock.bind(Client_Addr)
udpSock.settimeout(1)

def send_cmd(cmd):
    global udpSock, UDP_SERIAL_Addr
    udpSock.sendto(cmd.encode('utf-8'), UDP_SERIAL_Addr)
    UDP_BUFSIZE = 1024
    #data, addr = udpSock.recvfrom(UDP_BUFSIZE)
    #print(data)

    while True:
        try:
            data, addr = udpSock.recvfrom(UDP_BUFSIZE)
        except:
            print("miss")
            pass
        else:
            if data.decode() == "ok":
                break