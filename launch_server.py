import os
import socket
import operator as op

pull_command = 'git pull origin master'
launch_command = 'python hello.py'
exit_command = 'exit'

server = socket.socket()
server.bind(('localhost', 1360))
server.listen(5)

while True:
    conn, addr = server.accept()
    print('connected')
    while True:
        data = conn.recv(1024)
        data_str = str(data, encoding='utf-8')
        result = ''
        if not data:
            print('client has lost')
            break
        elif op.eq(data_str, exit_command):
            conn.send(b'exit')
            server.close()
        elif op.eq(data_str, pull_command):
            result = os.popen(pull_command).read()
        elif op.eq(data_str, launch_command):
            result = os.popen(launch_command).read()
        else:
            result = 'invalid command'
        conn.send(bytes(result, encoding='utf-8'))
