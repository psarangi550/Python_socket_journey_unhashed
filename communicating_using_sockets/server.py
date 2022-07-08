import socket
import threading
import sys
port=5050
host=socket.gethostbyname(socket.gethostname())

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

def handle_connection(conn,addr):
    print(f"New connection established on ip {addr[0]} and port {addr[1]}")
    Connection=True
    while Connection :
        msg=conn.recv(1024).decode('utf-8')
        if msg:
            if msg == "quit":
                Connection=False
                break
            else:
                print(f"{addr[0]} sends {msg}")
    conn.close()
    sock.close()
    sys.exit()


def start():
    print(f"Server running on {host} and port {port}")
    sock.listen()
    while True:
        conn,addr=sock.accept()
        threads=threading.Thread(target=handle_connection,args=(conn,addr))
        threads.start()
        print(f"Active connectrion is {threading.active_count()-1}")

if __name__ == "__main__":
    start()