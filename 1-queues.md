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
Given an integer n and a queue of integers, we need to reverse the first n elements and leave the remaining elements in the same order they were already in.

Only the following standard queue operations are allowed:
1. enqueue(x)
2. dequeue()
3. size()
4. empty()

### Examples of Expected Output:
Input: q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]&nbsp;
       n = 5&nbsp;
Output: q = [50, 40, 30, 20, 10, 60, 70, 80, 90, 100]&nbsp;

Input: q = 