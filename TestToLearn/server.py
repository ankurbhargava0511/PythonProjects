#server side program
import socket
# create a socket object
s = socket.socket()
print ("Socket successfully created")
# choose any random available port
port = 4042

# Next bind to the port
# empty string makes listen from all computers in the network
s.bind(('', port))
print ("socket binded to %s" %(port))
# start listening
s.listen(5)
print ("socket started listening")

# a forever loop until we interrupt it or
# an error occurs
counter = 0
while counter < 5:
    # Keep establishing connection with clients
    c, addr = s.accept()
    print ('Got a connection from', addr )
    counter+= 1
    # send a message to the client. encoding to send byte type.
    c.send('We listened to you'.encode())
    # Close the connection with the client
    c.close()
    # Breaking once connection closed
    #break