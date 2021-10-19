# UDPServer.py
import sys
from socket import *
from random import randrange
# Set print destination for later log file
sys.stdout = open('server_log', 'w')
# Set server name and port
serverName = 'tux-59.cae.wisc.edu'
serverPort = 12000
# Create server socket and bind
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
# Wait for packet to arrive
while 1:
	# Receive data packets
	name,clientAddress = serverSocket.recvfrom(2048)
	movie,clientAddress = serverSocket.recvfrom(2048)
	time,clientAddress = serverSocket.recvfrom(2048)
	cost = '$5.00'
	password = str(randrange(0,256))
	# Create response and send
	message = 'Server name: ' + serverName + ' Movie Name: ' + movie + ' Movie Time: ' + time + ' Cost: ' + cost + ' Password: ' + password
	serverSocket.sendto(message,clientAddress)
	# Print response to server_log
	print message