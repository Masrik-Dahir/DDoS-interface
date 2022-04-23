import os

def layer_4(name, ip, port, thread, second, socket):
    result = os.system('python attacker.py %s %s:%s %s %s - %s' %(name,ip, port, thread, second, socket))


# layer_4("TCP", "127.0.0.1", "12001", "100", "10")