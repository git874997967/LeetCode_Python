#18. 4Sum
def fourSum(nums,target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]: continue
        for k in range(i + 1,n):
            if k > i + 1 and nums[k] == nums[k -1]:continue
            left = k + 1 
            right = n - 1 
            while left < right:
                if nums[i] + nums[k] + nums[left] + nums[right] > target : right -= 1
                elif nums[i] + nums[k] + nums[left] + nums[right] < target : left += 1
                else:
                    result.append([nums[i],nums[k],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
    print(result)
    return result 


nums = [1,0,-1,0,-2,2]
target = 0
fourSum(nums,target)