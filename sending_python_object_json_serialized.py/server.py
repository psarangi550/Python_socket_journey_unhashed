import socket #importing the socket module 
import threading #importing the threading module
import pickle #importing the pickle module which will deserialize the recevied data
import sys #importing the sys module

PORT=5055
HOST=socket.gethostbyname(socket.gethostname())
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))

def handle_pickle_desirialization(conn,addr):
    print(f"[CONNECTION ESTABLISHED] on host {addr[0]} and port {addr[1]}")
    Connected=True
    while Connected:
        cmd=conn.recv(1024)
        if cmd:
            p_dict=pickle.loads(cmd)
            print(f"Provided value is {p_dict}")    
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