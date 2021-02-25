# 14. Longest Common Prefix
def longestCommonPrefix(strs):
    # take care the basecase
    if len(strs) == 0: return ""
    if lens(strs) == 1: return strs[0]
    myList = sorted(strs,lambda x: len(x), reverse = True)
    result = ""
    first = myList[0]
    while i < len(first):
        char = first[i]
        for j in range(1,len(myList)):
            if myList[j][i] != char:
                return result
        result += char
        i += 1
    return result
     