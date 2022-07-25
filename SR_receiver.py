import socket
import random
import time
def receiver():
	#hostname
	host_addr = socket.gethostname()
	ip = socket.gethostbyname(host_addr)
	#port no initiating
	port_no = 12344  
	exp = 0
	w_size=int(input("Enter Window Size-->"))
	new = 1
	W_S = 0
	W_E   = W_S + w_size - 1
	rec = []
	# server instance
	s_socket = socket.socket()  
    # bind host address and port together
	s_socket.bind((host_addr, port_no))  

    # no of clients listening simultaneously
	s_socket.listen(1)
	print("\nWaiting for incoming connections...\n")

	# accepting the connection
	conn, addr = s_socket.accept()  
	time.sleep(1)
	print ("\nReceived Connection from: ", addr[0],"(",addr[1],")\n")
	while (True):
		rec_data = conn.recv(1024).decode()
		if not rec_data:   # break when data is not received
			break
		temp = 0
		cnt = 0
		recieve = int(rec_data)
		ackn = recieve
		limit = recieve + w_size - 1
	
	
		ran = random.randint(1, 3)

		#received new frame
		if new == 1 : 			
			while(cnt != ran):
				temp = random.randint(recieve, limit)
				time.sleep(1)
				if temp not in rec:
					print ("Received Frame -> ", temp)
					cnt+=1

					temp = 1       
					rec.append(temp)
		else :
			time.sleep(1)

			#received a new frame of an old window  
			print ("Received Frame -> ", recieve)       
			rec.append(recieve)
			temp = 1
		if(temp == 1):
			for i in range(recieve,limit+1):
				if i not in rec:
					ackn = i
					break
				ackn = i+1
		#next expected frame
		print ("Sending ACK    -> ", ackn) 
		time.sleep(1)
		print ('*********************************************')
		rec_data = str(ackn)

		# sending data to the client
		conn.send(rec_data.encode())  

		if ackn > W_E :
			W_S = ackn
			W_E   = W_S + w_size - 1
			print("----window Slided----")
			new = 1			
		else :
			# now received a new frame of an old window
			new = 0 
	# closing the connection		
	conn.close()
receiver()