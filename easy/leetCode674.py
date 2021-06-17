# 674. Longest Continuous Increasing Subsequence
def findLengthOfLCIS(nums):
    result = currLength = 1
    for start in range(1, len(nums)):
        if nums[start] > nums[start - 1]:
            currLength += 1
        else:
            currLength = 1
        result = max(result, currLength)

    return result 

print(findLengthOfLCIS([1,3,5,4,7]))

print(findLengthOfLCIS([1,3,5,4,5,7,7,8,9,10,11]))

print(findLengthOfLCIS([1,1,1,1]))