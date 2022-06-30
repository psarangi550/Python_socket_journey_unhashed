import queue #importing the queue module

#fetching the queue which is FIFO queue which stands for First in First Out
# fq=queue.Queue()

#fetching the queue which is LIFO queue which stands as below
lq=queue.LifoQueue()

#fetching the queue as Priority Queue as below 
pq=queue.PriorityQueue()

#puttung the element to the queue
# lq.put(10)
# lq.put(15)
# lq.put(20)

#puttung the element to the queue on the basis of Priority
#here we need to put the priority and their corresponding value as tuple
pq.put((1,"AAA"))
pq.put((3,"BBB"))
pq.put((2,"CCC"))

#now we need to get the element from the queue hence we need to use as 
while True:
    if not pq.empty():
        print(f"elements are {pq.get()[1]}")
    else:
        break
