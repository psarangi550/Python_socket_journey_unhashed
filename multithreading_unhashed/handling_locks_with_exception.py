from threading import *

lock=Lock() #creating the lock object

def wish(name:str)->None:
    try:#risky code
        lock.acquire() #acquire the lock in try block
        print("Good Morning", end=' ')
        print(name)
        if current_thread().getName() =="abi thread":
            print(10/0)
    finally:
        lock.release() #release the lock object in finally block

#creating the thread object with name and args
th1:Thread=Thread(target=wish,name="abi thread",args=("abi",))
th2:Thread=Thread(target=wish,name="pratik thread",args=("pratik",))
th3:Thread=Thread(target=wish,name="rika thread",args=("rika",))

#starting the thread as 
th1.start()
th2.start()
th3.start()

