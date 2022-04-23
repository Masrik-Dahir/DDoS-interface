import socket
server_port = 12001
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', server_port))
server.listen(1)
print ("The server is ready to receive")
while 1:
    print ("Waiting ...")
    connection_socket, addr = server.accept()
    print ("accept")
    sentence = connection_socket.recv(2048).decode(encoding = 'iso-8859-1')
    print ("Message Received: " + sentence)
    modifiedSentence = sentence.upper()
    connection_socket.send(modifiedSentence.encode())
    connection_socket.close()