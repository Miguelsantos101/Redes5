# Este servidor web suporta UM pedido de arquivo.
# Usar num navegador web "localhost:6789/index.html"

# O navegador vai pedir também "Favicon.ico". Criei uma exceção, 
# Tem que rodar muito comportadamente para funcionar

#Completar o programa nos pontos indicados com   ## /* XXXX */

# Import socket module
from socket import * 
import sys # In order to terminate the program

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
## /* 1. PRIMITIVA BIND DE SOCKETS */
serverSocket.bind(('', serverPort))

# Listen to at most 1 connection at a time
## /* 2. PRIMITIVA LISTEN DE SOCKETS */
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections

while True:
	print('The server is ready to receive')

	# Set up a new connection from the client
 	## /* 3. PRIMITIVA ACCEPT DE SOCKETS */
	connectionSocket, addr =  serverSocket.accept()

	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
	try:
		# Receives the request message from the client
		
		print ("** Passou o ACCEPT **")
		
		## /* 4. PRIMITIVA RECEIVE DE SOCKETS */
		message = connectionSocket.recv(1024)

		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filename = message.split()[1]
  
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character
		
		print ("** Arquivo: ", filename)
		if filename == "/favicon.ico": continue
		
		f = open(filename[1:])
  
		# Store the entire content of the requested file in a temporary buffer
		outputdata = f.read()
  
		# Send the HTTP response header line to the connection socket
		## /* 5. PRIMITIVA SEND DE SOCKETS */
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) 
 
		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode()) 
		
		# Close the client connection socket
		
		print ("** Fecha Socket de conexão **")
		
		connectionSocket.close()

	except IOError:				
			print("** IO Error **")
			
			# Send HTTP response header line for file not found (404)			
			## /* 6. PRIMITIVA SEND DE SOCKETS */			
			connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

			# Close the client connection socket
			## /* 7. PRIMITIVA CLOSE DE SOCKETS */
			connectionSocket.close()



serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data