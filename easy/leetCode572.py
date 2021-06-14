# 572. Subtree of Another Tree
def isSubtree(self, root, subRoot):
    if root is None and subRoot is None:
        return True 
    if (root is None and subRoot is not None) or (root is not None and subRoot is None):
        return False
    if isSameTree(root,subRoot):
        return True 
    else :
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

def isSameTree(self,root,subRoot):
     if root is None and subRoot is None:
        return True 
     if (root is None and subRoot is not None) or (root is not None and subRoot is None):
        return False
     return root.val == subRoot.val and self.isSameTree(root.left,subRoot.left) and self.isSameTree(root.right,subRoot.right)




def  isSubTree2(self,root,subRoot):
    def helper(node):
        return  "x" if not node else "#" + str(node.val) + helper(node.left) + helper(node.right)
    return True if helper(subRoot) in help(root) else False 