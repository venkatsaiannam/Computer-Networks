import time, socket, sys

def decimalToBinary(n):  
    return n.replace("0b", "")

def binarycode(s):
    a_byte_array = bytearray(s, "utf8")

    byte_list = []

    for byte in a_byte_array:
        binary_representation = bin(byte)
        byte_list.append(decimalToBinary(binary_representation))

    print(byte_list)
    a=""
    for i in byte_list:
        a=a+i
    return a

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

#creating a socket
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
#binding socket with port number (0 --> 65535)
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))
#Accepting one connection
s.listen(1)
print("\nWaiting for incoming connections...\n")
#Accepting client request 
conn, addr = s.accept() #conn client socket,and address
print("Received connection from ", addr[0], "(", addr[1], ")\n")
#receiver with buffer 1024
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter 'bye' to exit chat room\n")

#sending server name

conn.send(name.encode())

#accepting messages to send 
while True:
    message = input(str("Enter Data : "))
    
    conn.send(message.encode())
    #accepts input until user enter '[e]'
    if message == "bye":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break
    #converting message to binary format
    message=binarycode(message)
    f=str(len(message))
    conn.send(f.encode())
    i=0
    j=int(input("Enter the window size -> ")) #window size
    b=""
    j=j-1
    f=int(f)
    k=j
    count=0
    while i!=f:
        for cnt in range(i,k+1):
            print("sending....",cnt)
        while(i!=(f-j)):
            conn.send(message[i].encode())
            if(count>j):
                print("sending....",count)
            #receiving ACK
            b=conn.recv(1024)
            b=b.decode()
            print(b)
            #validating ACK
            if(b!="ACK Lost"):
                time.sleep(1)
                print("Acknowledgement "+str(count)+"  Received! The sliding window is in the range "+(str(i+1))+" to "+str(k+1)+" Now sending the next packet")
                #sliding the window
                i=i+1
                k=k+1
                count+=1
                time.sleep(1)
            #if NACK received
            else:
                time.sleep(1)
                print("Acknowledgement of the data bit is LOST! The sliding window remains in the range "+(str(i+1))+" to "+str(k+1)+" Now Resending the packets of  "+(str(i+1))+" to "+str(k))
                time.sleep(1)
        #resending Packets
        while(i!=f):
            conn.send(message[i].encode())
            print("sending....",count)
            b=conn.recv(1024)
            b=b.decode()
            print(b)
            if(b!="ACK Lost"):
                time.sleep(1)
                print("Acknowledgement "+str(count)+"  Received! The sliding window is in the range "+(str(i+1))+" to "+str(k)+" Now sending the next packet")
                count+=1
                i=i+1
                time.sleep(1)
            else:
                time.sleep(1)
                print("Acknowledgement of the data bit is LOST! The sliding window remains in the range "+(str(i+1))+" to "+str(k)+" Now Resending the packets of  "+(str(i+1))+" to "+str(k))
                time.sleep(1)


