import socket

s = socket.socket()         # Create a socket object
host = "localhost"	    # On local host this time
port = 8000                 # Correct Port Number Required

s.connect((host, port))
s.send("echo-server.php?message=test")

print s.recv(10)
s.close
