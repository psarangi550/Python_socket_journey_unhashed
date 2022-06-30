from threading import * #importing all the property from the threading module
import time #importing the time module 



def wish(name:str)->None:
    
    if current_thread().getName()=="Pratik Thread":
        
        th1.join()
    
    print(f"Thread been executed by %s" % current_thread().getName())
    
    for i in range(10):
        
        time.sleep(2)
            
        print("Good Morning", end=" ")
        
        print(name)
        
#now here creating thre thread with args and the name and fetching the data

th1:Thread=Thread(target=wish,name="Abi Thread",args=("Abi",))
th2:Thread=Thread(target=wish,name="Pratik Thread",args=("pratik",))

#now here we need to execute the thread start as below

th1.start()
th2.start()