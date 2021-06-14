 # 559. Maximum Depth of N-ary Tree
def maxDepth(self, root):
  def dfs(root,d):
      # leaf  
      if not root.children:
          return d 
      d, currentMax = d + 1, 0
      for child in root.children:
          cur = dfs(child, d)
          currentMax = max(cur, currentMax)
      return currentMax
  if not root:
      return 0
  return dfs(root,1)
      