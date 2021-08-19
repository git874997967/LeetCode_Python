#872. Leaf-Similar Trees
def leafSimilar(root1, root2):
    queue1 = queue2 = []
    DFS(root1,queue1)
    DFS(root2,queue2)

    return queue1 == queue2


def DFS(root, queue):
  if root is None:
      return 
  elif root.left is None and root.right is None:
      queue.append(root.val)

  DFS(root.left,queue)
  DFS(root.right,queue)