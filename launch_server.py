import os
import sys
import socket
import operator as op

HOST = '0.0.0.0'
PORT = 1362
ADDR = (HOST, PORT)
BUFF_SIZE = 1024

PULL_COMMAND = 'git pull origin master'
LAUNCH_COMMAND = 'python hello.py'
EXIT_COMMAND = 'exit'

server = socket.socket()
server.bind(ADDR)
server.listen(5)

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
            break
        elif op.eq(data, PULL_COMMAND):
            result = os.popen(PULL_COMMAND).read()
        elif op.eq(data, LAUNCH_COMMAND):
            result = os.popen(LAUNCH_COMMAND).read()
        else:
            result = 'invalid command'
        conn.send(bytes(result, encoding='utf-8'))
    conn.close()
    server.close()
