# UDP PING SERVER 
# We will need the following module to generate randomized lost packets
import random
from socket import * 

# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP updates 
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP Address and port no to socket: 
serverSocket.bind(('', 12000))

while True:
	# Generate random number from the range 0 to 10
	rand = random.randint(0, 10)
	# Receive the client packet along with the address it is coming from
	message, address = serverSocket.recvfrom(1024)
	# Capitalise the message from the client
	message = message.upper()
	# If rand is less than 4, we conside the packet lost and do not respond
	if rand < 4:
		continue
	# Otherwise, the server responds
	serverSocket.sendto(message.encode(), address)