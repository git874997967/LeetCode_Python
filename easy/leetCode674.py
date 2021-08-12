# 674. Longest Continuous Increasing Subsequence
def findLengthOfLCIS(nums):
     result = currentMax = 1
     for i in range(1,len(nums)):
         if nums[i] > nums[i - 1]:
             currentMax += 1
         else:
             currentMax = 1
         result = max(currentMax, result)

     return result 

print(findLengthOfLCIS([1,3,5,4,7]))

print(findLengthOfLCIS([1,3,5,4,5,7,7,8,9,10,11]))

print(findLengthOfLCIS([1,1,1,1]))