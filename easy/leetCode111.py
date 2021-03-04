# 111. Minimum Depth of Binary Tree

def minDepth(self,root):
    if not root:
         return 0
    elif not root.left:
        return self.min(root.right) + 1
    elif not root.right:
        return self.min(root.left) + 1 
    return min(self.min(root.left),self.minDepth(root.right)) + 1
# dfs   
def minDepth_stack(self,root):
    if not root:
        return 0
    minDepth,stack = float('inf'), [(1,root),]
    while stack:
        depth ,root = stack.pop()
        children = [root.left,root.right]
        if not any children:
            minDepth = min(minDepth,depth)
        for c in children:
            if c:
                stack.append((depth+1,c))
    return minDepth
# bfs 
def minDepth_queue(self,root):
    if not root:
        return 0
    queue = deque[(1,root)]
    while queue:
        depth ,root = queue.pop()
        children = [root.left,root.right]
        if not any children:
            return depth
        for c in children:
            if c:
                queue.append((depth +1, c))