# 455. Assign Cookies
def findContentChildren(g,s):
    g.sort()
    s.sort()
    #  min s > max g content all kids
    if len(s) == 0 or len(g) == 0 or max(s) < min(g):
        return 0
    if min(s) >= max(g) and len(s) >= len(g):
        return len(g)
    # content 0 kids 
    
    count = 0
    i,j = 0,0
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1

    return count 

def findCountentChildren(g,s):
   
    s.sort()
    g.sort()
    count, l_g , l_s =0, len(g) , len(s)
    for i in range(l_s):
        if i < l_g and s[i] >= g[count]:
            count += 1



g = [1,2,3]
s = [3]

print(findContentChildren(g,s))

g1,s1 = [1,2] ,[1,2,3]
print(findContentChildren(g1,s1))


 
