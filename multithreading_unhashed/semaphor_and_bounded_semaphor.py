# from threading import * #importing all the property from the threading module

# import time #importing the time module

# #creating the Semaphore class Object 
# s=Semaphore(2) #creating the semaphor of counter as 2

# def wish(name:str)->None:
    
#     with s: #aquiring the Semaphor Lock
        
#         print(f"Current thread aquired by {current_thread().getName()}")
    
#         for i in range(10): 
        
#             time.sleep(1)
        
#             print("Good Morning", end=" ")
        
#             print(name)


# #creating the thread object with target as wish method
# th1:Thread=Thread(target=wish,name="Abi Thread",args=("abi",))
# th2:Thread=Thread(target=wish,name="Pratik Thread",args=("pratik",))
# th3:Thread=Thread(target=wish,name="Rika Thread",args=("rika",))

# #starting the thread 
# th1.start()
# th2.start()
# th3.start()

#we can also replicate the same thing using the bounded semaphor as below 

from threading import * #importing all the property from the threading module

import time #importing the time module

#creating the Semaphore class Object 
s=BoundedSemaphore(2) #creating the semaphor of counter as 2

def wish(name:str)->None:
    
    with s: #aquiring the Semaphor Lock
        
        print(f"Current thread aquired by {current_thread().getName()}")
    
        for i in range(10): 
        
            time.sleep(1)
        
            print("Good Morning", end=" ")
        
            print(name)


#creating the thread object with target as wish method
th1:Thread=Thread(target=wish,name="Abi Thread",args=("abi",))
th2:Thread=Thread(target=wish,name="Pratik Thread",args=("pratik",))
th3:Thread=Thread(target=wish,name="Rika Thread",args=("rika",))

#starting the thread 
th1.start()
th2.start()
th3.start()
    