import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

message = input("->")

while message.lower().strip() != 'end':
    s.send(message.encode())
    data = s.recv(1024).decode()
    print("Client:"+ data)
    message = input("->")

s.close()
msg = s.recv(1024)
print(msg.decode("utf-8"))