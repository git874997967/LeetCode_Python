#106 tree Depth
def depth(root):
    result = 0 
    if not root:
        return result
    nodeList = [root]

    while nodeList:
        for _ in range(len(nodeList)):
            node = nodeList.pop(0)
            if node.left:
                nodeList.append(node.left)
            if node.right:
                nodeList.append(node.right)
        result += 1
    return result 