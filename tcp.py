#!/bin/python3


import socket 
import sys
from datetime import datetime

# define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of syntax")
	print("Syntax: ./scanner.py <hostname>")

# add a pretty banner
print('-' * 50)
print("Scanning target {}".format(target))
print('-' * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		# returns an error indicator - if port is open it throws a 0 otherwise 1
		result = s.connect_ex((target,port))
		
		if result == 0:
			print("Port {} is opem".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()

except socket.error:
	print("Could not connect to server")
	sys.exit()
