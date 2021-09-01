#1480. Running Sum of 1d Array
def runningSum(nums):
    result = []
    curSum = 0
    for num in nums:
        curSum += num
        result.append(curSum)
    return result