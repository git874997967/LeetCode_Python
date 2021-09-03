#1624. Largest Substring Between Two Equal Characters
def maxLengthBetweenEqualCharacters(s):
    charMap = {}
    maxDis = 0
    for index in range(len(s)):
        c = s[index]
        if c not in charMap.keys():
            ind_Dis =  (index,0)
            charMap[c] = ind_Dis
        else:
            firstPlace = charMap.get(c)[0] 
            dis = index - firstPlace
            ind_Dis =  (firstPlace,dis)
            maxDis = max(maxDis,dis)
    print(maxDis - 1)
    return maxDis - 1 if maxDis > 0 else -1


maxLengthBetweenEqualCharacters("aa")
maxLengthBetweenEqualCharacters("abca")
maxLengthBetweenEqualCharacters("cbzxy")
maxLengthBetweenEqualCharacters("abbcdedabvcfwea")