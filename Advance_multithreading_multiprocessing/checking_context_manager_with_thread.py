from threading import * #importing all the property from the threading module 
import time #importing the time module 
from concurrent.futures import ThreadPoolExecutor

start=time.perf_counter()

def do_something(seconds:int)->None:
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    print("Done Sleeping")


with ThreadPoolExecutor() as executor:
    fo=executor.submit(do_something,1)
    fo.result()



end=time.perf_counter()

print(f"script took around {round((end-start),2)} seconds")