from threading import * #importing all the property from the threading module
import queue #importing the queue module
import time #importing the time module 
from random import randint #importing the randint() from random module

def producer():#creating a producer function

    while True:

        item=randint(1, 100) #fetching the random number between 1 and 100

        q.put(item) #adding item to the queue and notifying all the waiting threads internally

        print(f"{current_thread().getName()} producing item {item} to the queue")

        time.sleep(2) #giving a sleep for 10 seconds

def consumer():#creating a consumer function

    while True:

        print(f"{current_thread().getName()} fetching the item as {q.get()}")

        time.sleep(2) 


q=queue.Queue()#creating the queue object


#creating the thread object for the same 
th1:Thread=Thread(target=producer,name="producer Thread")
th2:Thread=Thread(target=consumer,name="consumer Thread")

#starting the thread as below 
th1.start()
th2.start()
