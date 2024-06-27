import socket

s = socket.socket()
s.connect(("localhost", 9999))

print(s.recv(1024))