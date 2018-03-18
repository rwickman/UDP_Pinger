from socket import *
import time

serverName = '192.168.1.74'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

for x in range (1, 11):
    try:
        timeSent = time.time()
        pingMessage = "Ping "+ str(x)+ " "+  str(timeSent)
        clientSocket.sendto(pingMessage.encode(), (serverName,serverPort))
        clientSocket.settimeout(1)
        serverMessage, serverAddress = clientSocket.recvfrom(2048)
        RTT = "RTT: " + str(time.time() - timeSent)
        if serverMessage:
            print(serverMessage.decode())
        print(RTT)
    except timeout:
        print("Request timed out")

clientSocket.close()
