# Python program to find the
# height of a binary tree

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def insert(root, value):
    # if the tree is empty, make the
    # new node the root of the tree
    if root is None:
        root = BinaryTree(value)
        return root
    # if the tree is not empty, check if
    # it is less than or greater than the
    # root and insert where applicable
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def height(root):
    # remember if there is no root
    # the height is 0
    if root == None:
        return 0

    # find the height of the left subtree
    leftHeight = height(root.left)
    
    # find the height of the right subtree
    rightHeight = height(root.right)
    
    #find the max of leftHeight and rightHeight,
    # and add 1 to it
    if leftHeight > rightHeight:
        return leftHeight + 1
    else:
        return rightHeight + 1

    
root = insert(None, 10)
insert(root, 5)
insert(root, 15)
insert(root, 2)
insert(root, 8)
insert(root, 13)
insert(root, 20)
print("The height of the tree is:")
print(height(root))