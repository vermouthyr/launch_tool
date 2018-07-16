import os
import sys
import socket
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

while True:
    conn, addr = server.accept()
    print('connected')
    while True:
        data = conn.recv(BUFF_SIZE)
        data_str = str(data, encoding='utf-8')
        result = ''
        if not data:
            print('client has lost')
            break
        elif op.eq(data_str, EXIT_COMMAND):
            conn.send(b'exit')
            break
        elif op.eq(data_str, PULL_COMMAND):
            result = os.popen(PULL_COMMAND).read()
        elif op.eq(data_str, LAUNCH_COMMAND):
            result = os.popen(LAUNCH_COMMAND).read()
        else:
            result = 'invalid command'
        conn.send(bytes(result, encoding='utf-8'))
    server.close()
    break
