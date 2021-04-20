# 268. Missing Number
def missingNumber(nums):
    total, sum = 0,0
    for i in range(len(nums)):
        total += i
        sum += nums[i]
    total += len(nums)
    print(total,sum)

missingNumber([9,6,4,2,3,5,7,0,1])
missingNumber([0])