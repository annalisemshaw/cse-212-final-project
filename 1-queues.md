# Queues

In this module, you will be introduced to the basic concepts of queues and will be followed with a quick coding challenge.

## What is a queue?
A queue is a linear data structure that represents a list. A queue follows the First in, First Out (FIFO) principle. Deletion (or dequeue) of an element can only take place at the front. Addition of an item will be enqueued at the end of the list. A real life example of a queue would be much like the line to purchase movie tickets at a cinema. The first person in line is the first to be served. We can use queues to process a collection of requests in an orderly fashion. 

## Queue Operations
Queue Operation | What it does  | Code     | Performance
--------------- | ------------- | -------- | -----------
enqueue(value)  | Adds value to the back of queue| new_queue.append(value) | O(1) - Performance of adding value to end of a dynamic array
dequeue()       | Remove or pop off the value from the front of queue | value = new_queue[0] del new_queue[value] or value = new_queue.pop(0) | O(n) - Performance of getting and removing the beginning element of the dynamic array
size()          | Returns the size of the queue | length = len(new_queue) | O(1) - Performance of returning the size of the dynamic array
empty()         | Returns if the length of the queue is equal to zero | if len(new_queue) == 0: | O(1) - Performance of checking if the size of the queue is 0

## Example
In this example, I will demonstrate how to create a queue and add and remove elements from it using a list

```python
#initializing the queue
new_queue = []

#adding elements to the queue
new_queue.append('p')
new_queue.append('y')
new_queue.append('t')
new_queue.append('h')
new_queue.append('o')
new_queue.append('n')

#print your queue
print("Initial Queue")
print(new_queue)

#dequeue 
print("\nElements dequeued from queue")
print(new_queue.pop(0))
print(new_queue.pop(0))
print(new_queue.pop(0))
print(new_queue.pop(0))
print(new_queue.pop(0))
print(new_queue.pop(0))


print("\nQueue after removing elements")
print(queue)

Expected Output: 
Initial Queue
['p', 'y', 't', 'h', 'o', 'n']

Elements dequeued from queue
p
y
t
h
o
n

Queue after removing elements
[]

```

## Problem to Solve:
Given an integer n and a queue of integers, reverse the first n elements and leave the remaining elements in the same order they were already in.

Only the following standard queue operations are allowed:
- enqueue(x)
- dequeue()
- size()
- empty()

### Examples of Expected Output:
Input: Q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], n = 5
Output: Q = [50, 40, 30, 20, 10, 60, 70, 80, 90, 100]

Input: Q = [25, 50, 75, 100], n = 2
Output: Q = [50, 25, 75, 100]

You can test your program with the following scenarios:
- Q = [7, 43, 10, 21, 50, 35, 8, 19], n = 3
    - Expected output: q = [10, 43, 7, 21, 50, 35, 8, 19]
- Q = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], n = 7
    - expected output: [4, 5, 6, 7, 8, 9, 10, 3, 2, 1]