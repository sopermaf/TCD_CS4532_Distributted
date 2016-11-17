import socket

s = socket.socket()         # Create a socket object
host = "localhost"	    # On local host this time
port = 8002                 # Correct Port Number Required

aim_message = "ferdia"
message = "hello"

s.connect((host, port))
s.send(message)

print s.recv(256)
s.close
