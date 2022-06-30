# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:58:34 2022

@author: 611903295
"""

from threading import Event,Thread  #importing the Event class from the threading module  
import time #importing the time module

#creating the object of the event class 
e=Event()

num=0 #setting the value as None globally 

def trafic_signal()->None:
    while True:
        time.sleep(5)
        e.set() #making the signal as green
        print("Signal is Green now !! vehicle can go now ")
        time.sleep(10) #sleeping for the 10 seconds
        print("Signal is red again and wait for it to turn green")
        e.clear()
    
def vehicle_passed()->None:
    global num
    while True:
        print("waiting for the signal to turn green")
        e.wait() #waiting for the signal 
        print("Signal Turned Green and vechicle can move now")
        if e.is_set():#checking the signal is True
            num += 1
            time.sleep(1)
            print(f"{num}vechicle moving")
        print("signal is Red Now we have to wait")
        print("Total vehicle moved is",num)
    
th1:Thread=Thread(target=trafic_signal)
th2:Thread=Thread(target=vehicle_passed)

#starting the thread 
th1.start()
th2.start()

   



