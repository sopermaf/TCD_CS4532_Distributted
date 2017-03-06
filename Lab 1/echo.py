import socket

s = socket.socket()         # Create a socket object
host = "localhost"	    # On local host this time
port = 8000                 # Correct Port Number Required

aim_message = "ferdia"
message = "GET /echo-server.php?message=" + aim_message + " HTTP/1.1\r\n\r\n"

s.connect((host, port))
s.send(message)

print message
print s.recv(256)
s.close
