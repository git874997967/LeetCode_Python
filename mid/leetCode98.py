# 98. Validate Binary Search Tree
# use the range to test each node, root in range(root.left, root.right) and root.left in range( - math.inf, root.va)
# and root.right(root.val, math.inf)
def isValidBST(self, root):
    def vaild(root, low = -math.inf, high = math.inf):
        # base case 
        if not root:
            return True
        if root.val >= high or root.val <= low:
            return False
        # RECURION 
        return valid(root.left,low, root.val) and valid(root.right, root.val, high)
    return vaild(root)

def isValidBST2(self,root):
    stack, prev = [], - math.inf
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= prev:
            return False
        prev = root.val  
        root = root.right 
    return True