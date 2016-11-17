import socket
import threading
	
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        print "Starting " + self.name
        #add logic for thread waiting for instructions here
        while True:
        	#lock resource
        	#change needed variable
        	#release resource
        	#deal with client

def newClient(connection, client_address):
	print 'connection from: ' + str(client_address)

	inData = connection.recv(256)
	print 'received: ' + str(inData)

	connection.sendall(inData)
	print 'sending back: ' + str(inData)

	print 'closing connection\n'
	connection.close()

#our threadpool setup
threadpool = [] 

#create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8005))
sock.listen(1)

while True:
    # Wait for a connection
    print 'waiting for a connection'
    
    connection, client_address = sock.accept()
    #thread.start_new_thread(newClient, (connection, client_address))  
    
