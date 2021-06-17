# 671. Second Minimum Node In a Binary Tree
def findSecondMinimumValue(root):
    if root.left is None and root.right is None:
         return -1
    queue ,numSet = [root] , set()

    while len(queue) > 0:
        node = queue.pop(0)
        numSet.add(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        
    return -1 if len(numSet) == 1 else sorted(numSet)[1]
    