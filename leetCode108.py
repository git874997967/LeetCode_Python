# 108. Convert Sorted Array to Binary Search Tree
# return not only a balance tree but a bst
def sortedArrayToBST(self, nums):
    
    if not nums:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = self.sortedArrayToBST(nums[:mid])
    root.right = self.sortedArrayToBST(nums[mid+1:])
    return root    

def sortedArrayToBST2(self, nums):
    if not nums:
        return None
    root = TreeNode() 
    stack =[(root,0,len(nums))] #   0 always the left child and last must on the right subtree

    while(stack):
        mid = len(nums)//2
        node,lower,upper = stack.pop()
        node.val = nums[mid]
        node.left = TreeNode() if mid > lower else None
        node.right = TreeNode() if mid + 1 < upper else None
        # build subtree  position mapping(  root ,left smaller , right larger)   left < root < right
        if node.left: stack.append(node.left,lower,mid)
        if node.right: stack.append(node.right,mid+1,upper)
    