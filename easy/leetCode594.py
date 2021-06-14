# 594. Longest Harmonious Subsequence
def findLHS(nums):
    numMap,countMap, maxVal = {},{}, 0
    for num in nums:
        if num in numMap:
            numMap[num] += 1
        else:
            numMap[num] = 1

    if len(numMap) == 1:return 0

    for key in numMap.keys():
        if (key - 1) in numMap and (key + 1) in numMap:
            countMap[key]  = numMap[key] + max(numMap[key -1], numMap[key + 1])
        elif (key - 1) in numMap:
            countMap[key]  = numMap[key] + numMap[key - 1]
        elif (key + 1) in numMap:
            countMap[key]  = numMap[key] + numMap[key + 1]
       
    for key in countMap.keys():
        maxVal = max(maxVal, countMap[key])

    return maxVal

print(findLHS([1,2,2,2,2,5,5,5,6,6,6]))


print(findLHS([1,2,3,4]))


print(findLHS([1,3,2,2,2,5,3,7]))


print(findLHS([1,1,1,1]))