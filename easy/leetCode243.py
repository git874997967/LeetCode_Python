# 243. Shortest Word Distance
def shortestDistance(wordsDict, word1, word2):
    minDist = len(wordsDict)
    i1, i2 = -1,-1
    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            i1 = i 
        elif wordsDict[i] == word2:
            i2 = i
        if i1 != -1 and i2 != -1:
            minDist = min(minDist, i1,i2)
    return minDist
