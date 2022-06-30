# def func(n:int)->int:
    
#     if n == 0:
#         return 1
#     else:
#         return n*func(n-1)

# print(func(5))


from threading import * #importing all the property from the threading module 
import time #importing the time module 

#creating the R-lock object here
r_lock=RLock()

def func(n:int)->int:
    
    with r_lock: #aquiring the lock which will release the lock automatically
        time.sleep(1) #sleeping for 1 seconds
        print(f"lock aquired by the {current_thread().getName()}")
        
        result=None
        if n == 0:
            result=1
        else:
            result=n*func(n-1)
        return result #returning the result collected 

def result(num:int)->None:
    
    print(f"The value of Result with args {num} is {func(num)}")
    
#creating the Thread object with target function and name and args tuple defined
th1:Thread=Thread(target=result,name="Abi Thread",args=(5,))
th2:Thread=Thread(target=result,name="Pratik Thread",args=(6,))

#starting the thread object as below
th1.start()
th2.start()
    
        