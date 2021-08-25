#1022. Sum of Root To Leaf Binary Numbers
def sumRootToLeaf(root,val = 0):
      if root:
          val = val * 2 + root.val 
          return self.sumRootToLeaf(root.left,val) + self.sumRootToLeaf(root.right, val)
      else:
          return 0