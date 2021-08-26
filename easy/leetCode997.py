#997. Find the Town Judge
def findJudge(n, trust):
    # use two arr to maintain the relationship
    outArr,inArr = [0] *(n + 1) , [0] * (n + 1)
    if len(trust) < n - 1:
        return -1 
    for a, b in trust:
        outArr[a] += 1
        inArr[b] += 1
    for i in range(1,n + 1):
        if inArr[i] == n - 1 and outArr[i] == 0:
            return i 
    return - 1

def findJudge2(n, trust):
    if n == 1:
        return n 
    if len(trust) < n - 1:
        return -1 
    trustScore = [0] * n - 1
    candidate = 0
    for a,b in trust :
        if candidate == a :
            return -1
        trustScore[a]  = -1
        if trustScore[b] >= 0:
            trustScore[b] += 1
            if trustScore[b] == n -1:
                candidate = b
    return candidate or -1

def findJudge3(n,trust):
    if n == 1:
        return 1
    if len(trust)< n :
        return - 1 
    trustMap, candidate = {}, 0
    for a,b in trust:
        if candidate == a:
            return -1
        trustMap[a] = -1
        if trustMap[b] >= 0:
            trustMap[b] += 1
        if trustMap[b] == n -1:
            candidate = b 
    return candidate or - 1



n = 2
trust = [[1,2]]

print(findJudge(n,trust))

n = 3 
trust =  [[1,3],[2,3],[3,1]]

print(findJudge(n,trust))


n0 = 4 
trust0 =  [[1,3],[1,4],[2,3],[2,4],[4,3]]

print(findJudge(n0,trust0))

n1 = 3 
trust1 =  [[1,2],[2,3]]

print(findJudge(n1,trust1))