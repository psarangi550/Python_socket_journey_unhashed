from threading import *
#importing all the functionality from the threading module 
import time #importing the time module

def display(): #defining the display method 
    time.sleep(1) #sleeping for 1 sec
    print(f"Thread executed by {current_thread().getName()}")
    #displaying the which thread executing the display method

t1=Thread(target=display,name="Abi Thread")
t2=Thread(target=display,name="Pratik Thread")

#starting the thread
t1.start()#stating the t1 thread
t2.start()#stating the t2 thread

#fetching all the thread thats been executing the display method
list_of_threads=enumerate()

print(list_of_threads)

#now fetching the name and identity number of all the threads
for thread in list_of_threads:
    print(thread)
    print(f"{thread.name} and {thread.ident}")


#fetching the total_count of active thread is determind by active_count()
print("The number of active thread is",active_count())

#checking which threads are active which are not active by the is_alive()
#checking which threads are active and which are not
print(current_thread().is_alive()) 

