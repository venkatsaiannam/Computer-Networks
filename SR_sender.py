import socket
import time
def sender():
	print("Initialising....\n")
	n=int(input("Enter Window Size -->"));
	W_S = 0
	W_E = W_S + n - 1
	s_host = socket.gethostname()  # as both code is running on same pc
	
	ip_addr = socket.gethostbyname(s_host)
	print(s_host, "(", ip_addr, ")\n")
	host_name = input(str("Enter server address: "))
	#Server port Number
	port_no = 12344  
	print("\nConnecting to host: ", host_name, "at port:", port_no, "\n")
	time.sleep(1)
	sender = []
	#Send whole list if 0 else only start window frame
	f = 0 
	#Creating a socket
	c_sock = socket.socket()  
	#Connecting to the Server
	c_sock.connect((host_name, port_no))
	print("Connected\n")
	print ('******** Enter "bye" to close connection ***************')
	message = input("Hit any key to send required frames -> ")  # take input
	while message.lower().strip() != 'bye':
		print ("Sending frames...")
		if (f == 0):
			
			for i in range(n):
				sender.append(W_S + i)
			for i in sender :
				time.sleep(1)
				print ("Frame -> ", i)
		else:
			print ("Frame -> ", W_S)
		msg = str(W_S)
		# sending message to server
		c_sock.send(msg.encode())  
		rec_data = c_sock.recv(1024).decode()  # receive NA
		msg = str(rec_data)
		ack = int(msg)
		if ack not in sender:
			W_S = ack
			W_E = W_S + n - 1
			#sending new frame
			f = 0         		
			print("-------window slided-------")
			for i in range(n):
				sender.pop()
		else:
			W_S = int(msg)
			#sending old frame
			f = 1			
			
		print ("******************************")
		print ('Received ACK server: ' + rec_data) 
		# again taking input
		message = input("Hit any key to send required frames -> ") 
		# closing the connection 
	c_sock.close()  

sender()