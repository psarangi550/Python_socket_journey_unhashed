import socket
import sys

print("Name of the host is",socket.gethostname())
host=socket.gethostbyname(socket.gethostname())
print(host)
port=9999
sock=None

def socket_conn():
    global sock
    sock=socket.socket()

def bind_socket():
    global host 
    global port
    sock.bind((host, port))
    print("binding on port",port)

def listen_sock():
    global sock
    try:
        sock.listen(5)
    except socket.error as e:
        listen_sock()

def accept_conn():
    global sock
    conn,address_list=sock.accept()
    print(f"connected to host {address_list[0]} and {address_list[1]}")
    send_command(conn)
    conn.close()

def send_command(conn):
    global sock
    while True:
        cmd=input("Enter a command")
        if len(str.encode(cmd)) == 0:
            print("Enter a valid command")
        elif cmd=="quit":
            conn.close()
            sock.close()
            sys.exit()
        else:
            conn.send(str.encode(cmd))
            conn_recv=conn.recv(1024).decode("utf-8")
            print(conn_recv)


    

if __name__ == "__main__":
    socket_conn() #calling the socket connection
    bind_socket()
    listen_sock()
    accept_conn()


