#976. Largest Perimeter Triangle
def largestPerimeter(nums):
    nums = sorted(nums)
    for i in range( len(nums) ,2 ,-1):
        if nums[i] > nums[i-1] + nums[i -2]:
            return nums[i] + nums[i - 1],nums[i - 2]
    return 0