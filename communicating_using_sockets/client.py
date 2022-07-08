import socket #importing the socket module 
#fetching the hostname as a string
host=socket.gethostbyname(socket.gethostname())
port=5050 #connecting to the server port

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

def send_message(msg):
    message=msg.encode()
    sock.send(message)
    
def called_msg():
    while True:
        msg=input("Enter the Message")
        send_message(msg)
        option=input("Do you want to type one more message[Y/N]")
        if option.lower()=="n":
            send_message("quit")
            break

if __name__=="__main__":
    called_msg()
