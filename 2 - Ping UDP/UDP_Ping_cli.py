import sys, time
from socket import *

# Get the server hostname and port as command line arguments
argv = sys.argv                      
host = argv[1]
port = argv[2]
timeout = 1 # in second

# Create UDP client socket
# Note the use of SOCK_DGRAM for UDP datagram packet
#/**/ /* 1. Cria o socket UDP */

# Set socket timeout as 1 second
#/**/ /* Seta o timeout de 1s para o socket */


# Command line argument is a string, change the port into integer
port = int(port)  
# Sequence number of the ping message
seqNum = 0  

# Ping for 10 times
while seqNum < 10: 
	seqNum += 1
	# Format the message to be sent
	data = "Ping " + str(seqNum) + " " + time.asctime()
    
	try:
	# Sent time
		RTTs = time.time()  #time in seconds
	# Send the UDP packet with the ping message
	#/**/ /* 2. Envia os dados para o servidor */

	# Receive the server response
	#/**/ /* 3. Recebe o reply do servidor */

	# Received time
		RTTr = time.time()
	# Display the server response as an output
		print("Reply from " + address[0] + ": " + message.decode())       
	# Round trip time is the difference between sent and received time
	#/**/ /* 4. Apresenta o RTT na tela */

	except:
		# Server does not respond
	        # Assume the packet is lost
		print ("Request", seqNum,"timed out.")
		continue

# Close the client socket
#/**/ /* 5. Fecha o socket */

 




