# 637. Average of Levels in Binary Tree
def averageOfLevels( root):
   result, queue = [], [root]
   while queue:
       count = len(queue)
       sum = 0
       for i in range(count):
          node = queue.pop(0)
          sum += node.val 
          if node.left:
              queue.append(node.left)
          if node.right:
              queue.append(node.right)
          result.append(sum * 1.0 / count)

   return result