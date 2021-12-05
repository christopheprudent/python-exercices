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

root = TreeNode(8)  
root.left = TreeNode(5)  
root.right = TreeNode(14) 
root.left.left = TreeNode(4)  
root.left.right = TreeNode(6) 
root.left.right.left = TreeNode(8)  
root.left.right.right = TreeNode(7)  
root.right.right = TreeNode(24) 
root.right.right.left = TreeNode(22)  

"""
     8
   /   \
  5     14
 / \     \
4   6     24
     \     /
      8  22
     /
    7
"""
preOrder(root)

"""
(a)=(8)
(a)=(14)
(a)=(24)
(a,b)=(24,22)
(a,b)=(14,22)
(a,b)=(8,22)
"""
result = closest_value(root, 19)

"""
22
"""
print(result)
