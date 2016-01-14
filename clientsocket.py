#!/usr/bin/env python

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("www.google.com", 80))

request = "GET / HTTP/1.0\n\n"

clientSocket.sendall(request)

response = bytearray()

while True:
	part = clientSocket.recv(1024)
	if (part):
		response.extend(part)
	else:
		break

print(response)