#1984. Minimum Difference Between Highest and Lowest of K Scores
def minimumDifference(nums, k):
    nums.sort()
    minDiff = float('inf')
    print(nums)
    for i in range(0,len(nums) - k + 1):
        minNum = nums[i]
        maxNum = nums[i+k-1]
        
        minDiff = min(minDiff, maxNum - minNum)
    return minDiff

minimumDifference([9,4,1,7],2)


minimumDifference([9,4,1,7],2)