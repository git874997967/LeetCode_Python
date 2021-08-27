#1133. Largest Unique Number
def largestUniqueNumber(nums):
    numMap = {}
    for num in nums:
        numMap[num] = numMap.get(num,0) + 1
    maxNum  = -1
    for k,v in numMap.items():
        if v == 1:
            maxNum = max(maxNum, k)
    return maxNum