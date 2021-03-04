# 104. Maximum Depth of Binary Tree
# iteration solution : use tuple to save node and level(depth) status
def maxDepth(self, root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    return 1 + max(self.maxDepth(root.left) +self.maxDepth(root.right))

def maxDepth2(self,root):
    depth = 0
    stack = []
    if root != None:
        stack.append((1,root))
    # loop the stack
    while stack != []:
        cur_depth, node = stack.pop()
        if node != None:
            # update the depth(result)
            depth = max (depth,cur_depth)
            # update the stack
            stack.append((cur_depth+1, node.left))
            stack.append((cur_depth+1,node.right))
    return depth