#938. Range Sum of BST
def rangeSumBST(root, low, high):
    arr = []
    result = 0
    self.inOrder(root,arr)
    for i in range(len(arr)):
        if arr[i] >= low and arr[i]<= high:
            result += arr[i]
    return result 
def inOrder(self,root,arr):
    if root:
        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right,arr)

def rangeSumBST(root,low,high):
    self.total = 0
    self.BFS(root,low,high)
    return self.total


def BFS(self,root,low,high):
    if root:
        if root.val <= high and root.val >= low:
            self.total += root.val
            self.BFS(root.left,low,high)
            self.BFS(root.righ,low,high) 
        elif root.val > high:
            self.BFS(root.left,low,high)
        elif root.val > low:
            self.BFS(root.right,low,high)
        
