#724. Find Pivot Index
def pivotIndex( nums):
    index = 0
    leftSum ,rightSum = 0,sum(nums[1:])
    if leftSum == rightSum :
        return index
    for index in range(1,len(nums)):
        leftSum = leftSum + nums[index-1]
        rightSum = rightSum - nums[index]
         
        if leftSum == rightSum:
            return index
    return -1

print(pivotIndex([1,2,3]))
print(pivotIndex([2,1,-1]))
print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([-1,-1,-1,0,1,0]))