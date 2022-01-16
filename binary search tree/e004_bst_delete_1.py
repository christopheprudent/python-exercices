# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
# Python program to demonstrate delete operation
# in binary search tree

# A Binary Tree Node


class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# A utility function to do inorder traversal of BST

def inorder(root, reverse=False):
    if root is not None:
        inorder(root.left, reverse) if not reverse else inorder(root.right, reverse)
        print(root.key)
        inorder(root.right, reverse) if not reverse else inorder(root.left, reverse)

# A utility function to print BST

def bst_print(root, addr = False):
    if not root:
        return
    if addr:
        print(f'{root} ', end='')
    print(f'value={root.key}')
    bst_print(root.left, addr)
    bst_print(root.right, addr)

# A utility function to insert a
# new node with given key in BST

def insert(node, key):

    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # return the (unchanged) node pointer
    return node

# Given a non-empty binary 
# search tree, return the node
# with minimum key value 
# found in that tree. Note that the
# entire tree does not need to be searched


def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left

    return current

# Given a binary search tree and a key, this function
# delete the key and returns the new root


def deleteNode(root, key):

    # Base Case
    if root is None:
        return root

    # If the key to be deleted 
    # is smaller than the root's key
    # then it lies in  left subtree
    if key < root.key:
        print(f'on left: {root.left} {key}<{root.key}')
        root.left = deleteNode(root.left, key)

    # If the key to be deleted
    # is greater than the root's key
    # then it lies in right subtree
    elif(key > root.key):
        print(f'on right: {root.right} {key}>{root.key}')
        root.right = deleteNode(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:
        print(f'found!: {root} {key}={root.key}')

        # Node with only one child or no child
        if root.left is None:
            print(f'case 1: less than 1 child {root.right} on right')
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            print(f'case 1: less than 1 child {root.left} on left')
            temp = root.left
            root = None
            return temp

        print('case 2: more than 1 child')
        # Node with two children: 
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)
        print(f'smallest key in right subtree {temp.key}')

        # Copy the inorder successor's 
        # content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
        print(f'after delete: node={root} key={root.key} left={root.left} right={root.right}')

    return root


# Driver code
""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80
           /  \
          35  45
             /  \
            42  46
"""

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 35)
root = insert(root, 45)
root = insert(root, 42)
root = insert(root, 46)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree")
inorder(root)
print("Reverse inorder traversal of the given tree")
inorder(root, True)
print("in-place traversal of the given tree")
bst_print(root, True)

#print("\nDelete 20")
#root = deleteNode(root, 20)
#print("Inorder traversal of the modified tree")
#inorder(root)

"""
in-place traversal of the given tree
<__main__.Node object at 0x7efd212810d0> value=50
<__main__.Node object at 0x7efd212537c0> value=30
<__main__.Node object at 0x7efd21253eb0> value=20
<__main__.Node object at 0x7efd21253f10> value=40
<__main__.Node object at 0x7efd21253f70> value=35
<__main__.Node object at 0x7efd21253d60> value=45
<__main__.Node object at 0x7efd21253880> value=70
<__main__.Node object at 0x7efd2126adf0> value=60
<__main__.Node object at 0x7efd211cc070> value=80

Delete 40
on left: <__main__.Node object at 0x7efd212537c0> 40<50
on right: <__main__.Node object at 0x7efd21253f10> 40>30
found!: <__main__.Node object at 0x7efd21253f10> 40=40
found!: <__main__.Node object at 0x7efd21253d60> 45=45

in-place traversal of the given tree
<__main__.Node object at 0x7efd212810d0> value=50
<__main__.Node object at 0x7efd212537c0> value=30
<__main__.Node object at 0x7efd21253eb0> value=20
<__main__.Node object at 0x7efd21253f10> value=45
<__main__.Node object at 0x7efd21253f70> value=35
<__main__.Node object at 0x7efd21253880> value=70
<__main__.Node object at 0x7efd2126adf0> value=60
<__main__.Node object at 0x7efd211cc070> value=80
"""

print("\nDelete 40")
root = deleteNode(root, 40)
print("in-place traversal of the given tree")
bst_print(root, True)

#print("\nDelete 50")
#root = deleteNode(root, 50)
#print("Inorder traversal of the modified tree")
#inorder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(7)

print('arbre BST')
bst_print(root, True)
#inorder(root)
print('effacement élément', 3)
root = deleteNode(root, 3)
bst_print(root, True)
#inorder(root)
