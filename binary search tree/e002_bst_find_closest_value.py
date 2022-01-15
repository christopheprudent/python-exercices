# web solution
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def closest_value(node, target):
    a = node.val
    kid = node.left if target < a else node.right
    if not kid:
        return a
    print(f"(a)=({a})")
    b = closest_value(kid, target)
    print(f"(a,b)=({a},{b})")
    return min((a,b), key=lambda x: abs(target-x))

def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)

"""
FIXME ne contrôle que la partie gauche!
"""
def checkValidity(node): 
    print(node.val)
    if node.left:
        if node.left.val > node.val:
            return False
        else:
            return checkValidity(node.left)

    if node.right:
        if node.right.val < node.val:
            return False
        else:
            return checkValidity(node.right)

    return True

def is_BST(root):
    stack = []
    prev = None
    
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.val)
        if prev and root.val <= prev.val:
            return False
        prev = root
        root = root.right
    return True

def delete_Node(root, key):
    # if root doesn't exist, just return it
    if not root: 
        return root
    # Find the node in the left subtree    if key value is less than root value
    if root.val > key: 
        root.left = delete_Node(root.left, key)
    # Find the node in right subtree if key value is greater than root value, 
    elif root.val < key: 
        root.right= delete_Node(root.right, key)
    # Delete the node if root.value == key
    else: 
    # If there is no right children delete the node and new root would be root.left
        if not root.right:
            return root.left
    # If there is no left children delete the node and new root would be root.right    
        if not root.left:
            return root.right
        # If both left and right children exist in the node replace its value with 
        # the minmimum value in the right subtree. Now delete that minimum node
        # in the right subtree
        temp_val = root.right
        mini_val = temp_val.val
        while temp_val.left:
            temp_val = temp_val.left
            mini_val = temp_val.val
        # Delete the minimum node in right subtree
        root.right = delete_Node(root.right,root.val)
    return root

print('init arbre binaire')
root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(14)
root.left.left = TreeNode(4)
root.left.right = TreeNode(7)
root.left.right.left = TreeNode(6)
#root.left.right.right = TreeNode(8)
root.right.left = TreeNode(9)
root.right.right = TreeNode(24)
root.right.right.left = TreeNode(22)

"""
     8
   /   \
  5     14
 / \    / \
4   7  9  24
   /      /
  6      22
"""
print('affichage arbre binaire')
preOrder(root)

"""
(a)=(8)
(a)=(14)
(a)=(24)
(a,b)=(24,22)
(a,b)=(14,22)
(a,b)=(8,22)
"""
print('recherche élémént le plus proche de :', 19)
result = closest_value(root, 19)

"""
22
"""
print('->', result)

print('contôle validité de l\'arbre :', is_BST(root))

# test is_BST() avec arbres simples
root = TreeNode(2)  
root.left = TreeNode(1)  
root.right = TreeNode(3) 
result = is_BST(root)
print(result)

root = TreeNode(1)  
root.left = TreeNode(2)  
root.right = TreeNode(3) 
result = is_BST(root)
print(result)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
result = is_BST(root)
print(result)

print('arbre BST')
preOrder(root)
print('arbre BST : effacement élément', 3)
print('nodes: <3>', root.left, root.left.val)
node = delete_Node(root, 3)
print('nodes: delete', node, node.val)
preOrder(root)
