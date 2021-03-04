# 110. Balanced Binary Tree
def isBalanced(self, root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    # judge the isBalance before judge the height match
    if self.isBalanced(root.left) and self.isBalanced(root.right):
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        return abs(leftHeight - rightHeight) <= 1
    return False

def height(self,root):
    # base case 
    if root is None:
        return 0
    leftHeight = self.height(root.left)
    rightHeight = self.height(root.right)
    return 1 + max(leftHeight,rightHeight)