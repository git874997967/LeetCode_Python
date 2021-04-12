# 242. Valid Anagram
def isAnagram(s, t):
    if not s or not t or len(s) != len(t):
        return False 
    tDict , sDict = {},{}
    for tChar in t:
        if tChar not in tDict:
            tDict[tChar] = 1
        else:
            tDict[tChar] += 1
    for sChar in s:
        if sChar not in sDict:
            sDict[sChar] = 1
        else:
            sDict[sChar] += 1
    return True if sDict == tDict else False
print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))
    
    