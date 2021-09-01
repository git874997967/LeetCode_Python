#1403. Minimum Subsequence in Non-Increasing Order
def minSubsequence(nums):
    if len(nums) == 1:
        return nums
    
    nums.sort(reversed = True)
    numSum, curSum = sum(nums),0
    index, result = 0,[]
    while index < len(nums):
        curSum += nums[index]
        result.append(nums[index])
        if curSum > numSum - curSum:
            return result 
        index += 1
    return result

        
    
