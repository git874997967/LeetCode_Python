#1800. Maximum Ascending Subarray Sum
def maxAscendingSum(nums):
    curMax,result = nums[0],nums[0]
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            curMax += nums[i]
            result = max(curMax,result)
        else:
            curMax = nums[i]


    return result