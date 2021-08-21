# 965. Univalued Binary Tree
def isUnivalTree(self, root):
    queue = []
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        if node.left is not None:
            val = node.left.val 
            if node.val != val:
                return False 
            else:
                queue.append(node.left)
        if node.right is not None:
            val = node.right.val
            if node.val != val: 
                return False  
            else:
                queue.append(node.right)
    return True 
