def leftRightDifference(nums):
    total_sum = sum(nums)        
    result = [total_sum - nums[0]]
    sum_till_now = 0
    for i in range(1, len(nums)):
        sum_till_now += nums[i -1]   
        result.append(abs(sum_till_now * 2 - total_sum + nums[i]))

    print(result)
    
    
print(leftRightDifference([10,4,8,3]))