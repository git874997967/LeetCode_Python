# 112. Path Sum
def hasPathSum(self, root, targetSum):
    if not root:
        return False
    result = False
    sum =  targetSum - root.val
    stack = [(sum,root)]
    while stack:
        sum,node = stack.pop()
        children = [node.left,node.right]
        if not any children:
            if sum == 0:
                return   True
        else:
            for c in children:
                if c:
                    stack.append(sum - c.val, c)
    return result
def hasPathSum2(root,targetSum):
    if not root:
        return False
    result = False
    stack = [(targetSum - root.val,root)]
    while stack:
        val, node = stack.pop()
        children = [node.left,node.right]
        if not any children:
            if val == 0:
                return True
        for c in children:
            if c:
                stack.push([val- c.val, c])
    return result