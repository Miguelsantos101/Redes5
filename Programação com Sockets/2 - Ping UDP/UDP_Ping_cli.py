import sys, time
from socket import socket, AF_INET, SOCK_DGRAM

totalPacPerdidos = 0
minRTT = 0
medRTT = 0
maxRTT = 0
RTTtotal = 0

# Get the server hostname and port as command line arguments
argv = sys.argv                      
host = argv[1]
port = argv[2]
timeout = 1 # in second

# Create UDP client socket
# Note the use of SOCK_DGRAM for UDP datagram packet
#/**/ /* 1. Cria o socket UDP */
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set socket timeout as 1 second
#/**/ /* Seta o timeout de 1s para o socket */
clientSocket.settimeout(timeout)

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
		clientSocket.sendto(data.encode(), (host, port))

	# Receive the server response
	#/**/ /* 3. Recebe o reply do servidor */
		message, address = clientSocket.recvfrom(1024)
	# Received time
		RTTr = time.time()
	# Display the server response as an output
		print("Reply from " + address[0] + ": " + message.decode())       
	# Round trip time is the difference between sent and received time
	#/**/ /* 4. Apresenta o RTT na tela */
		RTTtotal = RTTr - RTTs
		if (RTTtotal > maxRTT):
			maxRTT = RTTtotal
		elif (RTTtotal < minRTT):
			minRTT = RTTtotal
		medRTT += RTTtotal

		print(f"{RTTtotal:.4f}")
	except:
		# Server does not respond
	        # Assume the packet is lost
		print ("Request", seqNum,"timed out.")
		totalPacPerdidos += 1
		continue

print(f"Taxa de perda: {(totalPacPerdidos / 10) * 100}%")
print(f"RTT: \n\tMínimo = {minRTT:.4f}, Máximo = {maxRTT:.4f}, Média = {medRTT / 10:.4f}")

# Close the client socket
#/**/ /* 5. Fecha o socket */
clientSocket.close()
 




