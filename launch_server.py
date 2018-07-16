import os
import socket
import operator as op

server = socket.socket()
server.bind(('localhost', 1365))

server.listen(5)
while True:
    conn, addr = server.accept()
    while True:
        data = conn.recv(1024)
        print("data：", data)
        if not data:
            print("client has lost")
            break
        elif op.eq(data, 'git pull origin master') == 0:
            os.system(data)
            conn.send(b'pull success')
        elif op.eq(data, 'python hello.py') == 0:
            os.system(data)
            conn.send(b'launch success')
        elif op.eq(data, 'exit'):
            conn.send(b'exit')
            server.close()
