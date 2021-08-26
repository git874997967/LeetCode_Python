#1099. Two Sum Less Than K
import bisect
from typing import Counter
def twoSumLessThanK(nums, k):
    nums.sort()
    currentMax, start, end = -1, 0, len(nums) - 1
    while start < end:
        numSum = nums[start] + nums[end]
        if numSum < k:
            currentMax = max(currentMax,numSum)
            start += 1
        else:
            end -= 1
    return currentMax
 
def twoSumLessThanK2(nums,k):
     nums.sort()
     currentMax = -1
     for i in range(len(nums)):
         j = bisect.bisect_left(a = nums,x = k - nums[i], lo = i + 1, hi = len(nums)) - 1
         if j > i :
             currentMax = max(currentMax,nums[i] + nums[j])
     print(currentMax)
nums = [34,23,1,24,75,33,54,8]
k = 60
twoSumLessThanK2(nums,k)