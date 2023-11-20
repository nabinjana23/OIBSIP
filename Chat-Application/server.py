import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

clientsocket, address = s.accept()
print(f"Connection from {address} has been established")
while True:
    data = clientsocket.recv(1024).decode()
    if not data:
        break
    print("Server: "+ str(data))
    data = input("->")
    clientsocket.send(data.encode())
clientsocket.close()