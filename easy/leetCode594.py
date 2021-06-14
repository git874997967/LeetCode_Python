# 594. Longest Harmonious Subsequence
def findLHS(nums):
    numMap, maxVal = {},{}, 0
    for num in nums:
        if num in numMap:
            numMap[num] += 1
        else:
            numMap[num] = 1
    
    for i in numMap:
        if i + 1 in numMap:
            maxVal = max((numMap[i] + numMap[i + 1]), maxVal)
    
    return maxVal

print(findLHS([1,2,2,2,2,5,5,5,6,6,6]))


print(findLHS([1,2,3,4]))


print(findLHS([1,3,2,2,2,5,3,7]))


print(findLHS([1,1,1,1]))