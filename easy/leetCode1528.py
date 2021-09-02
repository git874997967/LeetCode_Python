#1528. Shuffle String
def restoreString(s, indices):
    result ,charMap = "", {}
    for i in range(len(indices)):
        charMap[indices[i]] = s[i]

    charMap = sorted(charMap.items(),key = lambda x:x[0])
    #print(charMap)
    for k,v in charMap:
        result += v 
    print( result)
    return result

s = "codeleet" 
indices = [4,5,6,7,0,2,1,3]
restoreString(s,indices)
s = "aiohn"
indices = [3,1,4,2,0]
restoreString(s,indices)