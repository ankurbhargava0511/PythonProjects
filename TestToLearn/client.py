# client side program
import socket
# Create a socket object
s = socket.socket()
# port where server side program is listening
port = 4042
# connect to the server on local computer
s.connect(('127.0.0.1', port))
# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.close()