# 561. Array Partition I
def arrayPairSum( nums):
    sum = 0
    nums.sort()
    for i in range(0,len(nums),2):
        sum += nums[i]
    return sum 