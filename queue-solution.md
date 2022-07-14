```python
# function to reverse the first n
# elements of the queue

def reverseElements(n, queue):
    #check if our queue length is valid
    if queue.empty() == True or n > queue.size():
        return;
    
    #check if the value of n is valid
    if (n <= 0):
        return;

    
```