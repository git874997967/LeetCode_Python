#1462. Course Schedule IV
def checkIfPrerequisite(numCourses, prerequisites, queries):
    result,inDegree = [],[0] * numCourses
    graph = [[] for i in range(numCourses)]
    preList = [set() for _ in range(numCourses)]

    for pre, cur in prerequisites:
        graph[pre].append(cur)
        inDegree[cur] += 1
        preList[cur].add(pre)

    dq = [i for i,v in enumerate(inDegree) if v == 0 ]
    
    while dq:
        node = dq.pop(0)
        for cour in graph[node]:
            preList[cour] = preList[cour].union(preList[node])
            inDegree[cour] -= 1
            if inDegree[cour] == 0:
                dq.append(cour)

    result = [pre in preList[cur] for pre, cur in queries]

    return result
#[true,false,true,false]
numCourses = 5
prerequisites = [[0,1],[1,2],[2,3],[3,4]]
queries = [[0,4],[4,0],[1,3],[3,0]]
checkIfPrerequisite(numCourses, prerequisites, queries)

    

     
        
        
            