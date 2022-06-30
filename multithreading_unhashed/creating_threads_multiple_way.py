from threading import * #importing all the member from the threading module

#1st approach without any class using the Thread class and creating the object of that 

# def display(name:str)->None: #creating a display function which will be executed by the threads 
    
#     print(f"executing the display method with args {name} and thread name {current_thread().getName()}")

# #now here we need to create a thread obj and execute that thread obj as below 

# #creating the thread object using the thread class and taget and args as tuple
# th1:Thread=Thread(target=display,name="abi thread ",args=("abi",))

# #staring the thread 
# th1.start()#stating the thread 

# #now this will be executed by the main thread as below 
# print(f"{current_thread().getName()} is executing")

#using the 2nd approach by extending the thread class and overiding the run method inside it 

# class AbiThread(Thread):
    
#     def run(self,name:str)->None: #overiding the run() which is in AbiThread class
        
#         print(f"Thread been executed by the {current_thread().getName()} and args is {name}")
        

# #now we need to create the object of the Thread class a below

# #as we are passing the args here 

# #1st approach:-

# th2:AbiThread=AbiThread() #creating the object of subclass of thread class  

# #now starting the thread as below 

# th3:Thread=Thread(target=th2.run,name="Abi Thread",args=("abi",))

# th3.start() #starting the thread here 

# print(f"{current_thread().getName()} is executing")

#2nd approach alternative :-

# class AbiThread(Thread):
    
#     def run(self)->None: #overiding the run() which is in AbiThread class
        
#         print(f"Thread been executed by the {current_thread().getName()} and args is {self._kwargs['name']}")

# th4:AbiThread=AbiThread(kwargs={"name":"pratik"})
# #creating the threading object 

# #starting the threading object
# th4.start() #starting the thread here 

#3rd way without extending  the thread class object as below 

class ThdClass():
    
    def display(self,name:str)->None:
        
        current_thread().setName("AbiThread")
        print(f"Thread been executed by the {current_thread().getName()} with arsg as {name}")
              
    
#now here we need to use the class object display method executed bu the threads then

th5:Thread=Thread(target=ThdClass().display,args=("Abi",))

#starting the thread 

th5.start()

print(f"{current_thread().getName()} is executing")

