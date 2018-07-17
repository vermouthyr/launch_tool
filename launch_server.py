import os
import socket
from threading import Thread
import operator as op

HOST = '0.0.0.0'
PORT = 1360
ADDR = (HOST, PORT)
BUFF_SIZE = 1024

PULL_COMMAND = 'git pull origin master'
LAUNCH_COMMAND = 'python hello.py'
EXIT_COMMAND = 'exit'

server = socket.socket()
server.bind(ADDR)
server.listen(5)


class RunService(Thread):
    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        os.system(self.command)


EXIT_FLAG = False
while not EXIT_FLAG:
    conn, addr = server.accept()
    print('connected')
    while True:
        data = conn.recv(BUFF_SIZE)
        data = data.decode()
        result = ''
        if not data:
            print('client has lost')
            break
        elif op.eq(data, EXIT_COMMAND):
            conn.send(b'exit')
            EXIT_FLAG = True
            conn.close()
            server.close()
            break
        elif op.eq(data, PULL_COMMAND):
            result = os.popen(PULL_COMMAND).read()
        elif op.eq(data, LAUNCH_COMMAND):
            t = RunService(data)
            t.setDaemon(True)
            t.start()
            # os.system(data)
            # result = os.popen(LAUNCH_COMMAND).read()
            result = 'launch success'
        else:
            result = 'invalid command'
        conn.send(bytes(result, encoding='utf-8'))
