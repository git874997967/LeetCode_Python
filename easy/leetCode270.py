# 270. Closest Binary Search Tree Value
def closestValue(root, target):
   rootVal = root.val
   while root:
       if abs(root.val - target) < abs(rootVal - target):
           rootVal = root.val  
       root = root.right if root.val < target else root.left 
    
   return rootVal 
