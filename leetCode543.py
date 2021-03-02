# 543. Diameter of Binary Tree
# why we need the global ans which is diff as other recurision?
# because the diameter may or may not pass the root
def diameterOfBinaryTree(self, root):
    self.ans = 1
    if not root:
        return 0
    def height(root):
        if not root:
            return 0
        L = height(root.left)
        R = height(root.right)
        self.ans = max(L+R+1,self.ans)
        return 1 + max( L,R)
    height(root)
    return self.ans - 1

def diameterOfBinaryTree2(self,root):
    self.ans = 1
    def height(root):
        # base case 
        if not root:
            return 0
        L = height(root.left)
        R = height(root.right)
        self.ans = max(self.ans, L + R - 1) # update the global var  height contains itself twice means - 1
        return max(L, R) + 1 #   because not root return 0  means leaf with hight 0 + 0  + 1(itself)
    height(root)
    return self.ans - 1