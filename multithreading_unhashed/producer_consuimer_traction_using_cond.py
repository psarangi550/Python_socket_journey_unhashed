from threading import * #importing all the property from the threading module
from random import * #importing all the property from the random module
import time #importing the time module
from typing import List #importing the List class from typing module

queue:List[int]=[]
cond:Condition=Condition() #creating the condition object in here

def procuder()->None:

    while True: #making an infinity loop

        with cond:#aquiring the condition object

            items=randint(1, 100) #fetching the random item

            queue.append(items)# adding a random item to the List

            print(f"{current_thread().getName()} added the item{queue} to the queue")

            cond.notify()#notify to the waiting queue

        time.sleep(10)


def consumer()->None:

    while True: #making an infinity loop

        with cond:#aquiring the condition object

            print(f"{current_thread().getName()} waiting for the queue to be filled with item ")

            cond.wait()#waiting for the queue

            print(f"removing the item from the queue as {queue.pop()}")

        time.sleep(10)


#now creating the thread object and starting the thread as below 

th1:Thread=Thread(target=consumer,name="cosumer thread")
th2:Thread=Thread(target=procuder,name="producer thread")

#now starting the threads`
th1.start()
th2.start()

