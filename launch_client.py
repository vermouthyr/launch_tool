import socket
import operator as op

# HOST = '169.229.192.179'
HOST = '127.0.0.1'
PORT = 1360
ADDR = (HOST, PORT)
BUFF_SIZE = 1024

client = socket.socket()
client.connect(ADDR)

while True:
    msg = input('>>').strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode())
    data = client.recv(BUFF_SIZE)
    print(data.decode())
    if op.eq(data.decode(), 'exit'):
        break
