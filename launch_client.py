import socket

client = socket.socket()

client.connect(('localhost', 1365))

while True:
    msg = input('>>').strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode())
    data = client.recv(1024)
    print(data.decode())
