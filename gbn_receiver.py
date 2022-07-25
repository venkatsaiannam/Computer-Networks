import time, socket
import random

print("\nWelcome....\n")
print("Initialising....\n")
time.sleep(1)

#creating a client socket

s = socket.socket()
shost_name = socket.gethostname()
ip_addr = socket.gethostbyname(shost_name)
print(shost_name, "(", ip_addr, ")\n")
host_name = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port_no = 1234
print("\nConnecting to ", host_name, "(", port_no, ")\n")
time.sleep(1)

#connecting to server using IP address and port number

s.connect((host_name, port_no))
print("Connected...\n")

s.send(name.encode())

#receiving server name

s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, " joined...\n")
print("Enter 'bye' to exit\n")
#Accepting Messages
while True:

    m=s.recv(1024)
    m=m.decode()
    k=s.recv(1024)
    k=k.decode()
    k=int(k)
    i=0
    a=""
    b=""
    count=0
    #Generating random number
    f=random.randint(0,1)
    msg=""
    while i!=k:
       
       
       f=random.randint(0,1)
       if(f==0): #sending NACK 
          b="ACK Lost"
          print("NACK....:(",count)
          msg = s.recv(1024)
          msg = msg.decode()
          s.send(b.encode())
         
       elif(f==1): #Sending ACK
          b="ACK "+str(i)
          msg = s.recv(1024)
          msg = msg.decode()
          print("Received bit:",count)
          s.send(b.encode())
          print("Acknowledged...:)",count)
          a=a+msg
          count+=1
          i=i+1
          
    print("Received message is :", m)