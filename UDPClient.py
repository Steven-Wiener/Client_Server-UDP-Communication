# UDPClient.py
import sys
from socket import *
# Set print destination for later log file
sys.stdout = open('client_log', 'w')
# Set server name and port
serverName = 'tux-59.cae.wisc.edu'
serverPort = 12000
# Create server socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set variables
name = 'Steven'
movie = 'Troll 2'
time = '18:00'
# Send as three messages so server doesn't have to sort through
clientSocket.sendto(name,(serverName, serverPort))
clientSocket.sendto(movie,(serverName, serverPort))
clientSocket.sendto(time,(serverName, serverPort))
# Receive response from server
response = clientSocket.recvfrom(2048)
# Print response to client_log
print response
# Close client socket
clientSocket.close()