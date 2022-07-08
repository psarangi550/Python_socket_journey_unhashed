import socket #importing the socket module 
import threading #importing the threading module
import pickle #importing the pickle module which will deserialize the recevied data
import sys #importing the sys module

PORT=5055
HOST=socket.gethostbyname(socket.gethostname())
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))

emp_info={
    "eno":101,
    "ename":"Abi",
    "esal":50000.00,
    "eaddr":"Banglore"
}

def send_pickle_object(dict_obj):
    pickle_obj=pickle.dumps(emp_info)
    sock.send(pickle_obj)

# if __name__ == "__main__":
#     send_pickle_object(emp_info)