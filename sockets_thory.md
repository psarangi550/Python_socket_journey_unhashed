---
                                  date: 2022-06-24T20:50
---

### **<u>SOCKETS THEORY</u>**

- **Sockets is the one end point of the two way communication between two programs existing in the same network**
- **Sockets are bind to have a end point from which the TCP Layer discover where to send the data to by the ip addresss and port number of the end point**
- **when 2 computers need to communicate with each other then we need to build a socket between them so that one computer can communicate with another one using the socket end points**
- **end point is nothing but the combination of ip address i.e considered as hostname and port number**

#### **<u>PYTHON COMMAND FOR SOCKET PROGRAMING**
	
```
>> <socket obj>=socket.socket() #create socket in both server and                  client  
#this will create an socket instance

>> <socket obj>.bind((<host>,<port>)) #binding the host and port in                server.py
#bind the host number and port

>> <socket obj>.connect((<host>,<port>)) #binding the host and port number         in the client.py file 
#bind the host number and port

>> <socket obj>.send() #used in the client.py to send info to the server  
#sending the message using the socket object

>> <socket obj>.listen() #used in server.py to listen to the connection
#listening and checking other computer recv or not

>> <socket obj>.recv() #used in the client.py to receive the connection
#receiving the socket message and decoding it 

>> <socket obj>.close() #closing the socket used in client and server 
#closing the socket that been created 
```
##### **DIRECT CONNECTION**





