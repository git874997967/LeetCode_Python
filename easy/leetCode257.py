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
    