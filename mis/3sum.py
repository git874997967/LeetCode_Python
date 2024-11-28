def three_sum(nums):
     nums.sort()
     result,n = [],len(nums)
     for i in range(n):
         if i > 0 and nums[i] == nums[i - 1]:
             continue
         left,right = i + 1, n - 1
         target = - nums[i]
         while left < right:
             sum_two = nums[left] + nums[right]
             if sum_two == target:
                 result.append([nums[i],nums[left],nums[right]])
                 left += 1
                 right -= 1
                 while left < right and nums[left] == nums[left - 1]:
                     left += 1
                 while left < right and nums[right] == nums[right + 1]:
                     right -= 1
             elif sum_two < target:
                 left += 1
             else:
                 right -= 1
     return result
result = three_sum([-1,0,1,2,-1,-4])
print(result )

result = three_sum([0,0,0,0])
print(result)