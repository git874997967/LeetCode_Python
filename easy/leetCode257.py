# 257. Binary Tree Paths
def binaryTreePaths(self, root):
    # recurision
    # base case 
    result = []
    if not root:
        return result
    # leaf 
    if not root.left and not root.right:
        return [str(root.val)]
    # rule
    leftPath = self.binaryTreePaths(root.left)
    rightPath = self.binaryTreePaths(root.right)
    for char in leftPath:
        result.append(str(root.val) + '->' + char)
    for char in rightPath:
        result.append(str(root.val) + '->' + char)
    return result

def binaryTreePaths2(self,root):
    #base case
    if not root:
        return root  
    if not root.left  and not root.right:
        return [root.val]
    # recurison rule
    leftPath = binaryTreePaths2(root.left)
    rightPath = binaryTreePaths2(root.right)
    result = []
    for node in leftPath:
        result.append(str(root.val) + '->' + node)
    for node in rightPath:
        result.append(str(root.val) +'->' + node)
    eixt 
    return result 
