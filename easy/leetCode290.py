# 290. Word Pattern
def wordPattern( pattern, s):
    if pattern is None or s is None:
        return False 
    sArr = s.split(' ')
    if len(pattern) != len(sArr):
        return False 
    mapping = {}
    for i in range(len(pattern)):
        if  pattern[i]not in mapping:
            if sArr[i] in mapping.values():
                return False
            mapping[pattern[i]] = sArr[i]
        else:
            if mapping[pattern[i]] != sArr[i]:
                return False 
    return True
pattern,s = "abba", "dog dog dog dog"
print(wordPattern(pattern,s))
