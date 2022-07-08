import socket #importing the socket module 
import threading #importing the threading module
import json 
import sys #importing the sys module


PORT=5056
HOST=socket.gethostbyname(socket.gethostname())
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))

# emp_info={
#     "eno":101,
#     "ename":"Abi",
#     "esal":50000.00,
#     "eaddr":"Banglore"
# }

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

emp=Employee(eno=102,ename="Rika",esal=60000,eaddr="Banglore")
e_dict=emp.__dict__

def send_json_object(obj):
    if isinstance(obj,dict):
        json_str=json.dumps(obj)
        json_byte=json_str.encode('utf-8')
        sock.send(json_byte)
    else:
        byte_str=obj.encode('utf-8')
        sock.send(byte_str)

if __name__ == "__main__":
    send_json_object(e_dict)