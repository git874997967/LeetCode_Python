# 404. Sum of Left Leaves
class Solution:
    self.sum = 0 
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        elif root.left is not None:
            if root.left.left is None and root.left.right is None:
                self.sum += root.left.val
        self.sumOfLeftLeaves(root.left)
        self.sumOfLeftLeaves(root.right)
        return self.sum