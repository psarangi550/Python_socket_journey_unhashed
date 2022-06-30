from threading import * #importing all the property from the threading module 
from typing import List,Any
import time #importing the time module 

items:List[str]=["item1","item2","item3","item4","item5"]

queue:List[str]=[]

e=Event() #creating the event object

def producer():
    
    time.sleep(5)

    print(f"{current_thread().getName()} Thread Producing the item")

    global queue

    global items
    
    for ele in items:

        queue.append(ele)

    print(f"{current_thread().getName()} Thread Produced the item {queue} and notifying the waiting threads")

    time.sleep(5)
    e.set()#now this will notify all the waiting threads that the item been produced
    
    

def consumer():
    
    while True:

        global queue

        print(f"{current_thread().getName()} consuming the item")

        e.wait() #waiting for the queue to update

        if len(queue)==0:

            print("all item been consumed")
            break
        else:
            print("consuming elements as",queue.pop()) #removing all the element from the queue
    

#creating the threads with target
th1:Thread = Thread(target=producer,name="producer thread")
th2:Thread = Thread(target=consumer,name="consumer thread")    


#starting the threads
th1.start()
th2.start()



