import socket

client = socket.socket()

# client.connect(('169.229.192.179', 1360))
client.connect(('localhost', 1360))

while True:
    msg = input('>>').strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode())
    data = client.recv(1024)
    print(data.decode())
