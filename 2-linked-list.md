# Linked Lists

In this module, you will be introduced to the basic concepts of linked lists and will be followed with a quick coding challenge.

FYI: This is one of my favorite data structure topics so let's jump right in! >.<

## What is a Linked List?
A linked list is a sequence of elements, more often referred to as nodes, that are connected via links. Each node has a value and a bi-directional connection which acts as a pointer to previous and next node. The link points to a location in memory that contains the previous or next element/node. The firrst node in a linked list is know as the head and the last node is called the tail. If there is only one node in a list, it is both the head and tail.


## Inserting into a Linked List
What I enjoy most about linked lists is how you can access and insert data within them. With dynamic arrays, we had to be concerned with moving all of the elements if inserting at a specific place in memory. Another benefit to using a linked list as opposed to using a dynamic array, we don't have to worry about capacity or growing the list.

A node can be added four different ways:
1. At the front (aka the head) of the list
2. After a given node
3. At the end (aka the tail) of the list
4. Before a given node

To insert at the head:
1. Create a new node (new_node)
2. Set the next of the new node to the current head (new_node.next = self.head)
3. Set the previous of the current head to the new node (self.head.prev = new_node)
4. Set the head equal to the new node (self.head = new_node)

If there is no head then we set both the head and tail to the new node created

To insert at the tail:
1. Create a new node (new_node)
2. Set the previous of the new node to current tail (new_node.prev = self.tail)
3. Set the next of the current tail to the new node (self.tail.next = new_node)
4. Set the tail to the new node (self.tail = new_node)

To insert after a given node:
1. Create a new node (new_node)
2. Set the prev of the new node to current node (new_node.prev = current)
3. Set the next of the new node to the node after the current (new_node.next = current.next)
4. Set the previous of the next node after current to the new node (current.next.prev = new_node)
5. Set the next of the current node to the new node (current.next = new_node)

## Removing from a Linked List
To remove from the head of a list:
1. Set the previous of the next node to be None (self.head.next.prev = None)
2. Set the head to the node after the one we just removed (self.head = self.head.next)

To remove from the tail of a list:
1. Set the next of the previous node to be null (self.tail.prev.next = none)
2. Set the new tail equal to the old tails previous node (self.tail = self.tail.prev)

To remove after a given node:
1. Set the previous of the current nodes next equal to current nodes previous (current.next.prev = current.prev)
2. Set the next of the node before current to the node after current (current.prev.next = current.next)

In the case that there is only one node in the list, set both the head and tail equal to None.

## Traversing and Accessing from a Linked List
When traversing a linked list to find a certain value we must loop through as we would any other list. We can loop through in a forward direction or backwards as long as we know the head or tail value. To traverse we simply have to print whatever the value may be of the current node followed by updating the pointer to the next node of the current data element.

### Example
```python
class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None
      
class LinkedList:
   def __init__(self):
      self.head = None

   def listprint(self):
      printList = self.head
      while printList is not None:
         print (printList.data)
         printList = printList.next

list = LinkedList()
list.head = Node("Mon")
el2 = Node("Tue")
el3 = Node("Wed")

# Link first Node to second node
list.head.next = el2

# Link second Node to third node
el2.next = el3

list.listprint()
```

## Common Linked List Operations
Python Code  | What it does     | Performance
-----------  | ---------------- | -----------
my_queue.appendleft(value) | Adds "value" before the head | O(1)
my_queue.append(value) | Adds "value" after tail | O(1)
my_queue.insert(i, value) | Adds "value" after index i | O(n)
value = my_queue.popleft() | Removes the first item (the head) | O(1)
value = my_queue.pop() | Removes the last item (the tail) | O(1)
del my_deque[i] | Removes node i | O(n)
length = len(my_queue) | Returns the size of the list | O(1)
if len(my_queue) == 0: | Checks if the list is empty | O(1)

## Example
```python
# Python implementation to delete
# a linked list node
# at the given position

# A node of the linked list
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

# Function to delete a node in a linked list.
# head_ref -. pointer to head node pointer.
# del -. pointer to node to be deleted.
def deleteNode(head_, del_):

	# base case
	if (head_ == None or del_ == None):
		return

	# If node to be deleted is head node
	if (head_ == del_):
		head_ = del_.next

	# Change next only if node to be deleted is NOT
	# the last node
	if (del_.next != None):
		del_.next.prev = del_.prev

	# Change prev only if node to be deleted is NOT
	# the first node
	if (del_.prev != None):
		del_.prev.next = del_.next
		
	return head_

# Function to delete the node at the given position
# in the linked list
def deleteNodeAtGivenPos(head_,n):

	# if list in None or invalid position is given
	if (head_ == None or n <= 0):
		return

	current = head_
	i = 1

	# traverse up to the node at position 'n' from
	# the beginning
	while ( current != None and i < n ):
		current = current.next
		i = i + 1

	# if 'n' is greater than the number of nodes
	# in the linked list
	if (current == None):
		return

	# delete the node pointed to by 'current'
	deleteNode(head_, current)
	
	return head_

# Function to insert a node at the beginning
# of the linked list
def push(head_, new_data):

	# allocate node
	new_node = Node(0)

	# put in the data
	new_node.data = new_data

	# since we are adding at the beginning,
	#prev is always None
	new_node.prev = None

	# link the old list off the new node
	new_node.next = (head_)

	# change prev of head node to new node
	if ((head_) != None):
		(head_).prev = new_node

	# move the head to point to the new node
	(head_) = new_node
	
	return head_

# Function to print nodes in a given
# linked list
def printList(head):

	while (head != None) :
		print( head.data ,end= " ")
		head = head.next
	
# Driver program to test above functions

# Start with the empty list
head = None

# Create the linked list 10<.8<.4<.2<.5
head = push(head, 5)
head = push(head, 2)
head = push(head, 4)
head = push(head, 8)
head = push(head, 10)

print("Linked list before deletion:")
printList(head)

n = 2

# delete node at the given position 'n'
head = deleteNodeAtGivenPos(head, n)

print("\nLinked list after deletion:")

printList(head)
```
## Problem to solve
In this module your coding challenge is to write a program that takes an unsorted list and deletes any duplicate nodes. The program should print out a new list without repeated elements.

Only the common linked list operations in this module are allowed to solve this problem.

# Examples of Expected Output:
- Linked list before: [10 10 20 20 30 30 40 50]
    - Linked list after: [10 20 30 40 50]

You may test your program with the following scenarios:
- linkedList = [5, 10, 15, 20, 25, 25]
    - Expected Output: Linked list after: [5, 10, 15, 20, 25]

- linkedList = []
    - Expected Output: List is empty. Please insert into the list.

Remember to check if the data/inputs are valid...

Once you've attempted to solve the problem, check your solution here: [Solution](linked-list-solution.md)

