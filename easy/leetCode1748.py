#1748. Sum of Unique Elements
def sumOfUnique(nums):
    result = 0
    countMap = {}
    for num in nums:
        countMap[num] = countMap.get(num,0) + 1
    result = sum([k for k,v in countMap.items() if v == 1])
    return result