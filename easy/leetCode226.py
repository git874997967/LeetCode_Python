# 226. Invert Binary Tree
def invertTree(self, root):
    if not root or root.left == root.right == none:
        return root
    else:
        root.left , root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root 