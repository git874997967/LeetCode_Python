#1971. Find if Path Exists in Graph
from collections import deque
def validPath(n, edges, start, end):
     graph = [[] for _ in range(n)]
     for u, v in edges:
         
            graph[u].append(v)
            graph[v].append(u)
     dq =  [start] 
     print(graph)
     visited = [False] * n
     while dq:
         node = dq.pop(0)
         visited[node] = True
         if node == end:
             return True
         for nei in graph[node]:
             if not visited[nei]:
                 dq.append(nei)

     return False


n = 6
edges = [[0,1],[0,3],[3,5],[5,4],[4,3]]
start = 0
end  = 5
validPath(n,edges, start, end )