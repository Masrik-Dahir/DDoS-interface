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
    option = connection_socket.recv(2048).decode(encoding = 'iso-8859-1')

    print ("Message Received: " + sentence)
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    modifiedOption = option.split(" ")
    result = ""
    modifiedSentence = ""
    for i in modifiedOption:
        if i == "1":
            result += str(sentence.upper()) + "\n"
        if i == "2":
            result += str(sentence.lower()) + "\n"
        if i == "3":
            result += str(len(sentence)) + "\n"
        if i == "4":
            for i in sentence:
                if i.lower() in vowel:
                    count += 1
            result += str(count) + "\n"
        if i == "5":
            words = sentence.split(" ")
            result += str(len(words)) + "\n"
    # print(result)
    connection_socket.send(modifiedSentence.encode())
    connection_socket.send(result.encode())
    connection_socket.close()