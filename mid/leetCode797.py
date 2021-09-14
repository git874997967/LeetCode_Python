#797. All Paths From Source to Target
from typing import NewType


def allPathsSourceTarget(graph):
    result,n = [], len(graph) - 1
    nodeQueue = [[0]]

    def backTrack(currNode,path):
        if currNode == n- 1:
            result.append(list(path))
            return 
        for nextNode in graph[currNode]:
            path.append(nextNode)
            backTrack(nextNode,path)
            path.pop()

    backTrack(0,nodeQueue)
     
    return result

def allPathsSourceTarget2(graph):
    result = []
    dq = [(0, [0])]
    target = len(graph) - 1
    while dq:
        cur,route = dq.pop(0)
        if cur == target:
            result.append(route)
        else:
            for node in graph[cur]:
                print(type(route))
                dq.append((node, route + [node]))
    print(result)
    return result

graph = [[1,2],[3],[3],[]]
allPathsSourceTarget(graph)

