from threading import * #importing all the property from the threading module 
import time #importing the time module 



#here we ar using the Lock synchronization concept

lock=Lock()
#creating the lock object 

def wish(name:str)->None:
    
    with lock: #using the lock with the context manager
        
        for i in range(10):
            
            time.sleep(2) #sleeping for 2 seconds
            
            print("Good Morning", end=" ") #executing with end args inside the print 
            
            print(name) #printing the name to the console
            
            #here auto relese wil happen
        
        # lock.release() # relesing the lock object 
    

#now here main thread will create the child thread as below 

th1:Thread=Thread(target=wish,name="Abi Thread",args=("abi",))
th2:Thread=Thread(target=wish,name="Pratik Thread",args=("pratik",))

#now starting the threads created
th1.start() 
th2.start()
        
        
        
        