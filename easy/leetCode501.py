# 501. Find Mode in Binary Search Tree
def findMode(self, root):
   result = que = val = []
   if root:
       que.append(root)
       while len(que) > 0:
           node = que.pop(0)
           val.append(node.val)
           if node.left is not None:
               val.append(node.left)
           if node.right is not None:
               val.append(node.right)
       c = Container(val)
       maxVal = max(c.values())
       result = [key for key, val in c.items() if val == maxVal]