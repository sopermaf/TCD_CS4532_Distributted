import socket
import sys

#create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8002))
sock.listen(1)

while True:
    # Wait for a connection
    print 'waiting for a connection'
    
    connection, client_address = sock.accept()   
    print 'connection from: ' + str(client_address)
    
    inData = connection.recv(256)
    print 'received: ' + str(inData)
    
    connection.sendall(inData)
    print 'sending back: ' + str(inData)
    
    print 'closing connection\n'
    connection.close()
