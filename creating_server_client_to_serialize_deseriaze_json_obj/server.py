import socket #importing the socket module 
import threading #importing the threading module
import json #importing the json data in order to deserialize
import sys #importing the sys module

PORT=5056
HOST=socket.gethostbyname(socket.gethostname())
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))

class Employee(object):
    
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    
    def __str__(self):
        return self.ename
    
    def display(self):
        print(f"EMPNO is {self.eno}")
        print(f"ENAME is {self.ename}")
        print(f"ESAL is {self.esal}")
        print(f"EADDR is {self.eaddr}")


def handle_pickle_desirialization(conn,addr):
    print(f"[CONNECTION ESTABLISHED] on host {addr[0]} and port {addr[1]}")
    Connected=True
    while Connected:
        cmd=conn.recv(1024).decode('utf-8')
        if cmd:
            if cmd=="quit":
                Connected=False
                break
            else:
                p_dict=json.loads(cmd)
                emp_obj=Employee(eno=p_dict['eno'],ename=p_dict['ename'],esal=p_dict['esal'],eaddr=p_dict['eaddr'])
                print(f"Provided value is \n {emp_obj.display()}")    
    conn.close()
    sock.close()
    sys.exit()

def start():
    sock.listen()
    print(f"[Server Started] on {HOST} and {PORT}")
    while True:
        conn,addr=sock.accept()
        thread=threading.Thread(target=handle_pickle_desirialization,args=(conn,addr))
        thread.start()
        print(f"[Active Connection] is {threading.active_count()-1}")

print("[Server] starting ......")

#if called directly calling the start method to listen and accept connections
if __name__ == "__main__":
    start()