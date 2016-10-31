import socket
sock = socket.socket()
sock.connect(("localhost", 8000))

sock.send("?message=test")

print sock.recv(1000)
sock.close()
