import socket

s = socket.socket()

ipaddress = "localhost"
port = 9999

s.bind(ipaddress, port)
s.listen(3)

while True:
	c, addr = s.accept()
	print("Connection from: " + str(addr))

	message = "sample text"
	c.send(message.encode())
	c.close()