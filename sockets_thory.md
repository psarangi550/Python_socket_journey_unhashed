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
<socket obj>=socket.socket() 
#this will create an socket instance
<socket obj>.bind((<host>,<port>)) 
#bind the host number and port
<socket obj>.send() 
#sending the message using the socket object
<socket obj>.listen() 
#listening and checking other computer recv or not
<socket obj>.receive() 
#receiving the socket message and decoding it 
<socket obj>.close()
#closing the socket that been created 
```
##### **DIRECT CONNECTION**





