#210. Course Schedule II
def findOrder(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    inDegree = [0] * numCourses
    dq , result = [],[]
    for pair in prerequisites:
        curCourse = pair[0]
        preCourse = pair[1]
        graph[preCourse].append(curCourse)
        inDegree[curCourse] += 1

    for i in range(inDegree):
        if inDegree[i] == 0:
            dq.append(i)
            result.append(i)
    
    while dq:
        curCourse = dq.pop(0)
        for course in graph[curCourse]:
            inDegree[course] -= 1
            if inDegree[course] == 0:
                dq.append(course)
                result.append(course)
    #check the inDegree to see if we can take all courses
    for i in inDegree:
        if i != 0:
            return []

    return result  





