# Author: Masrik Dahir
# Date: 2021-05-04

import matplotlib.pyplot as plt
import socket
import time

server_name = '127.0.0.1'
server_port = 12001

# create a socket object
t = [0]
p = [0]
while True:
    start = time.time()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_name, server_port))
    sentence = "None"
    client.send(sentence.encode())
    modifiedSentence = client.recvfrom(2048)
    print (modifiedSentence[0].decode())
    client.close()
    end = time.time()
    print("Eclipsed time: %f" %(end-start))
    time.sleep(1)

    t.append(end-start)
    p.append(p[len(p)-1] + 100)

    plt.plot(t, p)
    plt.xlabel('Time (hr)')
    plt.ylabel('Position (km)')
