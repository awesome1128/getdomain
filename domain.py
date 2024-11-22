import socket

domain = socket.gethostbyaddr('IP_ADDRESS')
print(domain[0])