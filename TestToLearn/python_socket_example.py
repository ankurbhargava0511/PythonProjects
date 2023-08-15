import socket
import sys

hostname = "www.bing.com"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created here")
except socket.error as err:
    print ("Socket creation failed here with error %s" %(err))

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname(hostname)
except socket.gaierror:
    print ("Error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip, port))

print (f"Socket successfully connected to {hostname}")