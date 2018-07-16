import os
import socket

server = socket.socket()
server.bind(('localhost', 1362))

server.listen(5)
while True:
    conn, addr = server.accept()
    while True:
        data = conn.recv(1024)
        print("data：", data)
        if not data:
            print("client has lost")
            break
        elif data == 'git pull origin master':
            os.system(data)
            conn.send('pull success')
        elif data == 'python hello.py':
            os.system(data)
            conn.send('launch success')
        elif data == 'exit':
            server.close()
