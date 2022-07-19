# Trees
In this module, you will be introduced to the basic concepts of trees and will be followed with a quick coding challenge.

## What is a tree?
A tree in essence is a linked list. Unlike a linked list, the data is connected in a hierarchical way. Every tree contains a root node, parent nodes and leaf nodes. The tree starts at the top with a root node from which we can access every element of the tree. The parents nodes are those which contain child nodes. Leaf nodes contain no children. The node to the left or right of any parent form a subtree.

## What are the different types of trees?
We are going to cover three different types of trees: binary trees, binary search trees and balanced binary search trees.

### Binary Trees
Binary Trees have a structure in which each node can only have a maximum of two children. We name its children the left and right child. The left child is usually

![Figure 1 - Binary Tree](/assets/Binary_tree_(oriented_digraph).png)

### Binary Search Trees
To insert into a binary search tree we have to follow some rules. We must compare the data being inserted with the parent node. If the value being added is less than its parent then it is put into the left subtree. If the value is greater than its parent then it is added into the right subtree.

![Figure 2 - Binary Search Tree](/assets/Binary_search_tree.jpeg)

Using a search tree can be an effective way to search for data because we can eliminate a certain subtree depending on the value we are looking for. However, this can only be achieved if the tree is balanced. An example of an unbalanced search tree would be a linked list.

![Figure 3 - Unbalanced tree made balanced](/assets/unbalanced_tree_made_balanced.jpeg)

### Balanced Binary Search Tree
A balanced binary search tree (BST) isn't much different from a binary search tree except for the height. The height of any two subtrees must be equal and can never differ by more than 1. If the difference is greater than 1 at any node, we must declare the tree unbalanced.

## How to insert into a tree
In order to insert a node into a tree we must know that this is a recursive operation.

Recursion is the process of a function calling itself. This allows us to loop through data to reach a certian result. Recursion must be handled with care because it is very easy to write a function in which it never terminates.

Here's a brief example of recursion:
```python
def try_recursion(k):
  if(k>0):
    result = k + tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
```

Now that we understand how to use recursion let me demonstrate how to insert into a BST.

```python
# Python implementation to delete a
# linked list node at
# the given position

class BST:
    
    class Node:
        # initialize our data. the left and right nodes are
        # unknown so we will initialize as None.
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    # set the root to None because
    # value is unknown
    def __init__(self):
        self.root = None
    

    def insert(self, data):
        # if the root is None
        # set it to the given data
        if self.root is None:
            self.root = BST.Node(data)
        else:
            # otherwise, use recursion to
            # find the location to insert
            self._insert(data, self.root)

    # with this function we will compare
    # the node data with previous nodes
    # to find where to insert the new node
    def _insert(self, data, node):
        # check if the node already exits
        if data == node.data:
            print("Node already exists")

        # if the new data is less than the
        # node we are currently comparing to
        # then it belongs on the left subtree
        elif data < node.data:
            # now we must check if we
            # have found an empty space
            if node.left is None:
                node.left = BST.Node(data)
            else:
                # if the space is not available
                # we must loop through
                # the left subtree recursively
                self._insert(data, node.left)
        
        else:
            # if the new node data is greater than the
            # node data we are comparing to it belongs
            # to the right sub tree
            if node.right is None:
                # we may insert here since we found
                # an empty spot
                node.right = BST.Node(data)

            else:
                # we must keep looping through the right
                # subtree recursively to find a space
                # to insert
                self._insert(data, node.right)
```

## How to traverse a tree
Traversing a tree is also a rescursive process. Let's look at how we would traverse a tree in order from smallest to biggest.

We must begin at the root
```python
def __iter_(self):
    # starting at the root we
    # will traverse through the tree
    yield from self.traverseInOrder(self.root)

    # The keyword yield is similar to the
    # return statement for returning values or objects
    # It is used to get a value, stop the function call,
    # and will start back up where it left off

def traverseInOrder(self, node):
    if node is not None:
        # we will first traverse through the
        # left subtree in order
        yield from self.traverseInOrder(node.left)
        yield node.data
        # then we will traverse the right
        # subtree in order
        yield from self.traverseInOrder(node.right)
```

## Common tree operations
Common BST Operation | Description | Performance
-------------------- | ----------- | -----------
insert(value) | Inserts a value into the tree | O(log n)
remove(value) | Removes a value from the tree | O(log n)
search(value) | Searches for an element within the tree | O(log n)
traverseForward | Loops through all elements from biggest to smallest | O(n)
traverseBackwards | Loops through all elements from smallest to biggest | O(n)
height(node) | Determines the height of a tree using node | O(n)

## Problem to solve
In this module your coding challenge is to create a tree and return its height.

To find the height of a binary tree, keep these points in mind:
- If the root of the tree is empty, return 0.
- If the root isn't empty, the the height will be equal to the maximum height of left and right subtrees plus 1.

## Examples of Expected Output
- The height of the tree is 3

Remember to check if the data/inputs are valid...

Once you've attempted to solve the problem, check your solution here: [Solution](trees-solution.py)

[Back to Welcome Page](0-welcome.md)