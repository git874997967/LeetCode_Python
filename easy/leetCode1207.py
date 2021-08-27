#1207. Unique Number of Occurrences
def uniqueOccurrences(arr):
    numMap = {}
    for num in arr:
        numMap[num] = numMap.get(num,0 ) + 1

    valSet = set([i for i in numMap.values()])
    return len(valSet) == len(numMap)