# Python program to remove duplicate
# nodes from a sorted linked list

# Node class
class Node:

	# Constructor to initialize
	# the node object
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

# Linked List class
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None
		self.tail = None

	# Function to insert a new node
	# at the beginning
	def insert(self, value):
	   new_node = Node(value)
	   new_node.next = self.head
	   self.head = new_node

	# Given a reference to the head of a
	# list and a key, delete the first
	# occurrence of key in linked list
	def deleteNode(self, key):
		
		# Store head node
		temp = self.head

		# If head node itself holds the
		# key to be deleted
		if (temp is not None):
			if (temp.data == key):
				self.head = temp.next
				temp = None
				return

		# Search for the key to be deleted,
		# keep track of the previous node as
		# we need to change 'prev.next'
		while(temp is not None):
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		# if key was not present in
		# linked list
		if(temp == None):
			return

		# Unlink the node from linked list
		prev.next = temp.next

		temp = None

	# Utility function to print the
	# linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data , end = ' ')
			temp = temp.next
	
	# This function removes duplicates
	# from a sorted list		
	def removeDuplicates(self):
		temp = self.head
		if temp is None:
			print("List is empty. Please insert into the list.")
			return
		while temp.next is not None:
			if temp.data == temp.next.data:
				new = temp.next.next
				temp.next = None
				temp.next = new
			else:
				temp = temp.next
		return self.head

# Driver Code
llist = LinkedList()

llist.insert(10)
llist.insert(40)
llist.insert(30)
llist.insert(30)
llist.insert(20)
llist.insert(20)
llist.insert(10)
llist.insert(10)
print ("Created Linked List: ")
llist.printList()
print()
print("Linked List after removing",
			"duplicate elements:")
llist.removeDuplicates()
llist.printList()

llist = LinkedList()
print ("\n")
print ("Created Linked List: ")
llist.printList()
print()
print("Linked List after removing",
			"duplicate elements:")
llist.removeDuplicates()
llist.printList()