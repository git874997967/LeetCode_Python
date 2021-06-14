# 563. Binary Tree Tilt
def findTilt(self, root):
    sumArr,sum = [],0
    def inOrder(root):
        if root:
            inOrder(root.left)
            if root.left is None and root.right is None:
                root.val = 0
            elif root.left is None:
                root.val = root.right.val 
            elif root.right is None:
                root.val = root.left.val 
            else:
                root.val = abs(root.left.val - root.right.val)
            
            inOrder(root.right)
            print()
   

