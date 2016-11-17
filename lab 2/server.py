import socket
import thread

#create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8003))
sock.listen(1)

def newClient(connection, client_address):
	print 'connection from: ' + str(client_address)

	inData = connection.recv(256)
	print 'received: ' + str(inData)

	connection.sendall(inData)
	print 'sending back: ' + str(inData)

	print 'closing connection\n'
	connection.close()

while True:
    # Wait for a connection
    print 'waiting for a connection'
    
    connection, client_address = sock.accept()
    thread.start_new_thread(newClient, (connection, client_address))  
    
