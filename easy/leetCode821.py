# 821. Shortest Distance to a Character
def shortestToChar(s, c):
    charLoc = []
    result = [0] * len(s)
    for i in range(len(s)):
        if s[i] == c:
            charLoc.append(i) #[3,5,6,11]
            
    for i in range(len(s)):
        distance = float('inf')
        if i in charLoc:
            result[i] = 0
        else:
            for j in charLoc:
                distance = min(abs(i - j), distance)

            result[i] = distance
    print(result)
    return result

def shortestToChar2(s,c):
    prev = float('-inf')
    ans = []
    for i,x in enumerate(s):
        if x == c: 
            prev = i
        ans.append(i - prev)
    print(ans)
    prev = float('-inf')
    for i in range(len(s) - 1, -1, -1):
        if s[i] == c:
            prev = i
        ans[i] = min(ans[i], prev - 1)

    return ans 

def shortestToChar3(s,c):
    n = len(s)
    ans = [0 if char == c else n for char in s]

    for i in range(1,n):
        ans[i] = min(ans[i] , ans[i - 1] + 1)

    for i in range(n-2,-1,-1):
        ans[i] = min(ans[i], ans[i + 1] + 1)
    return ans 

shortestToChar2("loveleetcode","e")

shortestToChar2("aaab","b")


