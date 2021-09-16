#207. Course Schedule
def canFinish(numCourses, prerequisites):
     graph = [[] for _ in range(numCourses)]
     inDegree = [0] * numCourses
     courseCount, dq = 0, []

     # init the graph
     # Indegress store all the course which we cannnot take directly  else 0
     #  graph store the pre couse and its dependancy course
     # (4,3) will be store as graph 4---> 3  and Indeed [3] = 1 [4] = 0  

     for pair in prerequisites:
         preCour,curCour = pair[1],pair[0]
         graph[preCour].append(curCour)
         inDegree[curCour] += 1
    # the sum the course which we can take directly
     for i in range(numCourses):
            if inDegree[i] == 0:
                dq.append(i)
                courseCount += 1
                
     while dq:
         curCourse = dq.pop(0)
         for nei in graph[curCourse]:
             inDegree[nei] -= 1
             if inDegree[nei] == 0:
                 courseCount += 1
    
     return courseCount == numCourses
     
    # 
