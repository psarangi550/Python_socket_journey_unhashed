from threading import *
# importing all the property from the threading module 

import time #importing the time module

def new_display()->None :
    
    print(f"The Thread executing are {current_thread().getName()}")
    
    if current_thread().isDaemon():
        
        print("Daemon Thread")
    
    else:
        
        print("Non Daemon thread")


def display()->None: #defining the display function
    
    print(f"The Thread executing are {current_thread().getName()}")
    
    if current_thread().isDaemon():
        
        print("Daemon Thread")
    
    else:
        
        print("Non Daemon thread")
        
    daemon_th:Thread = Thread(target=new_display,name="daemon_thread")
    
    daemon_th.start()

#creating a thread object for the execution of display()    
th:Thread=Thread(target=display,name="Abi Thread")

#making the thread as daemon
th.setDaemon(True)

#starting the thread
th.start()

#keeping the main thread active for 2 sec
time.sleep(15)


#printing the End of main as the daemon thread
print("End of Main")
