# 100. Same Tree
# check the value and ignore the tree structure
def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
    if p == None and q == None:
        return True
    if p == None or q == None:
        return False
    if p.val == q.val:
        return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    return False


        