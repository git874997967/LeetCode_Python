#1991. Find the Middle Index in Array
def findMiddleIndex(nums):
    totalSum = sum(nums)
    leftSum ,rightSum = 0, 0
    for i in range(len(nums)):
        leftSum += nums[i]
        rightSum = totalSum - leftSum 
        if leftSum - nums[i] == rightSum:
            return i
    return - 1

print(findMiddleIndex([1]))
print(findMiddleIndex([2,5]))
print(findMiddleIndex([1,-1,4]))
print(findMiddleIndex([2,3,-1,8,4]))
