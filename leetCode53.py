# 53. Maximum Subarray
import time
def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        currentVal = finalVal = nums[0]
        for i in range( len(nums)):
                currentVal = 0
                for j in range( i,len(nums)):
                        currentVal +=nums[j] 
                        finalVal  = max(currentVal, finalVal)
        return finalVal  
# O(n)
def maxSubArray2(nums):
        currMax = finalMax = nums[0]
        for i in range(1, len(nums)):
                currMax = max(nums[i], currMax + nums[i])
                finalMax = max(currMax , finalMax)
        return finalMax

array = [-2,1,-3,4,-1,2,1,-5,4]
sol1_start = time.time()
result = maxSubArray(array)
sol1_end = time.time() - sol1_start
sol2_start = time.time()
result2 = maxSubArray2(array)
sol2_end = time.time() - sol2_start
print(sol1_end,sol2_end)