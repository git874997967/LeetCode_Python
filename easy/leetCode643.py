# 643. Maximum Average Subarray I
def findMaxAverage(nums, k):
    currSum  = sum(nums[0:k])
    for i in range(1,len(nums)- k + 1):
         
        newSum = currSum - nums[i-1] + nums[i+k-1]
        
        currSum = max(newSum,currSum)
    return currSum * 1.0 / k 

findMaxAverage([1,2,3,4,5,6,7,8,9,10],4)
