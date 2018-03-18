from socket import *
import time

serverName = '192.168.1.74'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
RTTList = []
numPings = 10

for x in range (1, numPings +1):
    try:
        timeSent = time.time()
        pingMessage = "Ping "+ str(x)+ " "+  str(timeSent)
        clientSocket.sendto(pingMessage.encode(), (serverName,serverPort))
        clientSocket.settimeout(1)
        serverMessage, serverAddress = clientSocket.recvfrom(2048)
        timeElapsed = time.time() - timeSent
        RTT = "RTT: " + str(timeElapsed)
        if serverMessage:
            print(serverMessage.decode())
        print(RTT)
        RTTList.append(timeElapsed)
    except timeout:
        print("Request timed out")

numLost = numPings - (len(RTTList))
if numLost != numPings:
    print("\nMax RTT: " + str(max(RTTList)))
    print("Min RTT: " + str(min(RTTList)))
    print("Average RTT: " + str(sum(RTTList)/(numPings-numLost)))
else:
    print("\nMax RTT: undefined")
    print("Min RTT: undefined")
    print("Average RTT: undefined")


print("Packet loss rate: " + str(numLost * numPings) + "%")
clientSocket.close()
