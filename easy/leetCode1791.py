#1791. Find Center of Star Graph
def findCenter(edges):
    edgeLength = len(edges)
    edgeMap = {}
    for edge in edges:
        edgeMap[edge[0]] = edgeMap.get(edge[0],0) + 1
        edgeMap[edge[1]] = edgeMap.get(edge[1],0) + 1
    print(edgeMap,edgeLength)
    for k ,v in edgeMap.items():
        if v == edgeLength:
            return k 
    return -1

print(findCenter( [[1,2],[2,3],[4,2]]))