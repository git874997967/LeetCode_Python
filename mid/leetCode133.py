# 133. Clone Graph
from collections import deque
class solution():
    def __init__(self):
        self.dict = {}
    def cloneGraph_DFS(self, node):
        # base case  
        if not node:
            return None
        # if found 
        if node in self.dict:
            return self.dict[node]
        # if not found  init a new one
        clone_node = Node[node.val,[]]
        # update the dict
        dict[node] = clone_node
        # update the neighbors
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph_DFS(n) for n in node.neighbors]
        #return the node(headNode)
        return clone_node
    def cloneGraph_BFS(self,node):
        # base case  
        if not node:
            return None
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val,[])
        while queue:
            n = queue.popleft()
            for neighbor in n.neighbor:
                if neighbor not in visited:
                    visited[neighbor] = Node[neighbor.val,[]]
                    queue.append(neighbor)
            visited[n].neighbors = visited[neighbor]   
        return visited[node]