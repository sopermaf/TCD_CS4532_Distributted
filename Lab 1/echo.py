import socket

s = socket.socket()         # Create a socket object
host = "localhost"	    # On local host this time
port = 8000                 # Correct Port Number Required


message = "GET /echo-server.php?message=hello HTTP/1.1\r\n\r\n"

s.connect((host, port))
s.send(message)

print s.recv(496)
s.close
