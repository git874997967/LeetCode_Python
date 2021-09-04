#1827. Minimum Operations to Make the Array Increasing
def minOperations(nums):
    if len(nums) == 0:
        return 0
    result = 0 
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            pass 
        else:
            result +=  nums[i-1] - nums[i] + 1
            nums[i] += nums[i-1] - nums[i] + 1
    print(result)