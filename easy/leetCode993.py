#993. Cousins in Binary Tree
from collections import deque
def isCousins(root, x, y):
# same depth but diff parents
    que = deque()
    deque.append(root)
    while que is not None:
        sib, cousin = False, False
        size = len(que)
        for i in range(size):
            node = que.popleft()
            if node is None:
                sib = False 
            else:
                if node.left == x or node.right == y:
                    if not cousin:
                        sib ,cousin = True, True
                    else:
                        return not sib
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
            que.append(None)
        if cousin:
            return False
        return False

        
