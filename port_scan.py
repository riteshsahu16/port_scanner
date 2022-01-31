#! /bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 4: 
	target = socket.gethostbyname(sys.argv[1])
	start = int(sys.argv[2])
	end = int(sys.argv[3])
else:
	print("Usage : <script name> <target> <starting_port> <ending_port>")

print("*" * 80)
print("scanning target :", target)
print(" Time started : ", str(datetime.now))

try:
	for port in range(start, end+1):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		status = sock.connect_ex((target, port))
		if status == 0:
			print("Port {} is open".format(port))
		sock.close()
except KeyboardInterrupt:
	print("\n Exiting Program");
	sys.exit()

except socket.gaierror:
	print("Host name could not be resolved")
	sys.exit()

except socket.error:
	print("Couldn't connect to server")
	sys.exit()

