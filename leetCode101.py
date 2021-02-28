# 101. Symmetric Tree
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import *
def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
  # base case of the tree
  if root == None or ( root.left == None and root.right == None):
      return True
  return self.helper(root.left, root.right)

def helper(self,node1,node2):
    # base 
    if node1 == None and node2 == None:
        return True
    if node1 == None or node2 == None:
        return False
    if node1.val != node2.val :
        return False
    return self.helper(node1.left,node2.right) and self.helper(node1.right,node2.left)

def isSymmetric2(self, root):
    from collections import 
    deq = deque[(root,root)]
    while(deq):
        p,q = deq.popleft()
        if not self.check(p,q):
            return False
        if p:
            
            deq.append((p.left,q.right))
            deq.append((p.right,q.left))
        return True
def check(self, node1, node2):
    # base case 
    if node1 == None and node2 == None:
        return True
    if node1 == None or node2 == None:
        return False
    if node1.val != node2.val:
        return False
    return True

