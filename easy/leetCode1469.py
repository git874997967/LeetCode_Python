#1469. Find All The Lonely Nodes
def getLonelyNodes(root):
    result = []
        if root.left == root.right == None:
            return result
        self.getLongly(root.left,result)
        self.getLongly(root.right,result)
        return result
    
def getLongly(self,root, result):
        if root is None :
            print("heer")
            return 
        
        elif root.left is None and root.right is not None:
            print(root.right.val , "right is not null")
            result.append(root.right.val)
            self.getLongly(root.right,result)
        elif root.right is None and root.left is not None:
            print(root.left.val, "left is not null")
            result.append(root.left.val)
            self.getLongly(root.left,result)
        else:
            print(root.val,"root is not null")
            self.getLongly(root.left,result)
            self.getLongly(root.right,result)

def getLonelyNodes2(root):
    result = []
    nodeQueue = []
    if root:
        nodeQueue.append(root)
    while len(nodeQueue) > 0:
        node = nodeQueue.pop(0)
        if node.left is not None and node.right is not None:
            nodeQueue.append(node.left)
            nodeQueue.append(node.right)
        elif node.left is not None and node.right is None:
            nodeQueue.append(node.left)
            result.append(node.left.val)
        elif node.left is None and node.right is  not None:
            nodeQueue.append(node.right)
            result.append(node.right.val)
    return result
