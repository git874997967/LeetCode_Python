# 530. Minimum Absolute Difference in BST
# recurive way
def getMinimumDifference(self,root):
        self.ans = float('inf')
        self.prev = float('-inf')
        helper(root)
        return self.ans 

def helper(self,root):
    if root:
        self.helper(root.left)
        self.ans = min(self.ans , root.val- self.prev)
        self.prev = root.val
        self.helper(root.right)
#  inorder- travesal way 

def getMinDifference(self,root):
    arr, result = [], float('inf')
    def prev(root,arr):
        if root:
            prev(root.left,arr)
            arr.append(root.val)
            prev(root.right)
    prev(root,arr)
    for i in range(1,len(arr)):
        result = min(result, arr[i] - arr[i-1])
    return result

