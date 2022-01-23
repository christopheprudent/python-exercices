# web solution
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kth_smallest(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            break
        root = root.right
    return root.val

# https://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-statistics-in-bst
# This code is contributed by mohit kumar 29
# A simple inorder traversal based Python3
# program to find k-th smallest element
# in a BST.

# A BST node
class Node2:
	
	def __init__(self, key):
		
		self.data = key
		self.left = None
		self.right = None

# Recursive function to insert2 an key into BST
def insert2(root, x):
	
	if (root == None):
		return Node2(x)
	if (x < root.data):
		root.left = insert2(root.left, x)
	elif (x > root.data):
		root.right = insert2(root.right, x)
	return root

# Function to find k'th largest element
# in BST. Here count denotes the number
# of nodes processed so far
def kthSmallest2(root):
	
    global k
	
    # Base case
    if (root == None):
        print('None')
        return None

    # Search in left subtree
    print('left')
    left = kthSmallest2(root.left)

    # If k'th smallest is found in
    # left subtree, return it
    if (left != None):
        print('left not None')
        return left
		
    # If current element is k'th
    # smallest, return it
    k -= 1
    if (k == 0):
        print('found it!')
        return root

    # Else search in right subtree
    print('right')
    return kthSmallest2(root.right)

# Function to find k'th largest element in BST
def printKthSmallest2(root):

	# Maintain index to count number
	# of nodes processed so far
    count = 0

    _k = k
    res = kthSmallest2(root)
	
    if (res == None):
        print("There are less than k nodes in the BST")
    else:
        print(f'K-th Smallest Element is (k={_k}) : {res.data}')


# This code is contributed by bgangwar59
# A simple inorder traversal based Python3
# program to find k-th smallest element in a BST.

# A BST node
class Node3:
	
	def __init__(self, x):
		
		self.data = x
		self.left = None
		self.right = None
		self.lCount = 0

# Recursive function to insert3
# an key into BST
def insert3(root, x):
	
	if (root == None):
		return Node3(x)

	# If a node is inserted in left subtree,
	# then lCount of this node is increased.
	# For simplicity, we are assuming that
	# all keys (tried to be inserted) are
	# distinct.
	if (x < root.data):
		root.left = insert3(root.left, x)
		root.lCount += 1

	elif (x > root.data):
		root.right = insert3(root.right, x);
		
	return root

# Function to find k'th largest element
# in BST. Here count denotes the number
# of nodes processed so far
def kthSmallest3(root, k):
	
	# Base case
	if (root == None):
		return None
		
	count = root.lCount + 1
	
	if (count == k):
		return root

	if (count > k):
		return kthSmallest3(root.left, k)

	# Else search in right subtree
	return kthSmallest3(root.right, k - count)



# Driver code
if __name__ == '__main__':
	
    sol = 'sol2'

    if sol == 'sol1':
        root = TreeNode(8)  
        root.left = TreeNode(5)  
        root.right = TreeNode(14) 
        root.left.left = TreeNode(4)  
        root.left.right = TreeNode(6) 
        root.left.right.left = TreeNode(8)  
        root.left.right.right = TreeNode(7)  
        root.right.right = TreeNode(24) 
        root.right.right.left = TreeNode(22)  

        for i in range(1, 10):
            print(f'k={i}', kth_smallest(root, i))

    root = None
    keys = [ 20, 8, 22, 4, 12, 10, 14 ]
    print('éléments', keys)
    if sol == 'sol2':
        for x in keys:
            root = insert2(root, x)

        k = 3
        
        printKthSmallest2(root)

    if sol == 'sol3':
        for x in keys:
            root = insert3(root, x)

        k = 4
        res = kthSmallest3(root, k)
        
        if (res == None):
            print("There are less than k nodes in the BST")
        else:
            print(f'K-th Smallest Element is (k={k}) : {res.data}')

