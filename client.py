#UDP Client 
from socket import *
import sys
import time

# Create a UDP Socket 
# The use of SOCK_DGRAM for UDP packets
serverName = '' 
serverPort = ''
avgrtt = 0
maxrtt = 0
minrtt = 0
packet = 0.0
packetLoss = 0.0

# AF_INET Address Family | SOC_DGRAM = UDP is a Datagram protocol 
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set wait time on server
clientSocket.settimeout(1)

# Declare server's socket address
remoteAddress = (sys.argv[1], int(sys.argv[2]))
#remoteAddress = (serverName, serverPort)

# Ping 10 times
for i in range (10):

	# Countdown to 10 seconds
	sendTime = time.time()
	# Prints PING and the count and time in HH:MM:ss
	message = 'PING ' + str(i + 1) + " " + str(time.strftime("%H:%M:%S"))
	# Print message to the remoteAddress (client)
	clientSocket.sendto(message, remoteAddress)

	# We are trying to catch packets that are being received from our server.
	try: 
		data, server = clientSocket.recvfrom(1024)  # Only reading max 1024 bytes of data 
		recdTime = time.time() 						
		rtt = recdTime - sendTime
		if rtt < minrtt or minrtt == 0:
			minrtt = rtt
		if rtt > maxrtt or maxrtt == 0:
			maxrtt = rtt
		avgrtt = avgrtt + rtt
		packet = packet + 1					
		print "Message received!", data
		print "Round trip time: ", rtt
		print

	except timeout:	
		packetLoss = packetLoss + 1			
		print 'REQUEST TIMED OUT'
		print 
# packet loss is calculated as a moving average of 10 last ICMP echos. 
# Each ICMP request has value SUCCESS/FAILURE. 
# Those results are store into buffer with length 10, and we calculate average on it.
totalPackets = packet + packetLoss
average = avgrtt/10
print "Average Round trip time: ", str(average) + " ms"
print "Max round trip time: ", str(maxrtt) + " ms"
print "Min round trip time: ", str(minrtt) + " ms"
print "Packet loss: ", str(packetLoss/totalPackets * 100) + "%"

