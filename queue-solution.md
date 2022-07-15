```python
# function to reverse the first n
# elements of the queue

queue = []
def reverseElements(n, queue):
    swapQueue = []
    
    # checks for valid input
    if (len(queue) == 0 or n > len(queue)):
        print("Error. Please check the length of your queue or value of n")
        return
    
    if (n <= 0):
        print("Please enter a new value for n")
        return

    # storing the values we are
    # going to reverse into
    # an array called swapQueue
    for i in range(n):
        swapQueue.append(queue[i])
    
    # popping (or removing) the
    # the elements we are going to
    # reverse from the orignal queue
    for i in range(n):
        queue.pop(0)
    
    # now we are going to add those
    # elements back to the original
    # queue but backwards using index -1
    while (len(swapQueue) != 0):
        queue.append(swapQueue[-1])
        swapQueue.pop()
    
    # now we are going to append the
    # elements from the queue that
    # we don't want to reverse 
    # into the swapQueue
    for i in range(len(queue) - n):
        swapQueue.append(queue[i])
    
    # we must delete those elements from
    # from the queue after we append
    for i in range(len(queue) - n):
        queue.pop(0)
        
    # lastly we will readd those elements
    # from the swapQueue back onto the end
    # of our original queue
    for i in range(len(swapQueue)):
        queue.append(swapQueue[i])
        
# Test 1 
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)
queue.append(60)
queue.append(70)
queue.append(80)
queue.append(90)
queue.append(100)


reverseElements(5, queue)
print(queue)
del queue[:]

# Test 2
queue.append(10)
queue.append(9)
queue.append(8)
queue.append(7)
queue.append(6)
queue.append(5)
queue.append(4)
queue.append(3)
queue.append(2)
queue.append(1)

reverseElements(7, queue)
print(queue)
del queue[:]

# Test 3
# check if our size of queue is valid
reverseElements(7, queue)
print(queue)

# Test 4
# check if our n value is valid
queue.append(5)
queue.append(10)
queue.append(15)
queue.append(20)
reverseElements(-1, queue)
print(queue)
```