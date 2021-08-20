# 897. Increasing Order Search Tree
def increasingBST(root):
    queue = []
    self.inOrder(root,queue)
    newRoot = currentNode = TreeNode(queue[0])
     
    for i in range(1,len(queue)):
         currentNode.right = TreeNode(queue[i])
         currentNode = currentNode.right 

    return newRoot
def inOrder(root, queue):
    if root is None:
        return 
    self.inOrder(root.left, queue)
    queue.append(root.val)
    self.inOrder(root.right,queue)