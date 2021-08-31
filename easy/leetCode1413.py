#1413. Minimum Value to Get Positive Step by Step Sum
def minStartValue(nums):
    pefixSum = 0
    curMin = float('inf')
    for num in nums:
        pefixSum += num
        curMin = min(pefixSum,curMin)
         
    
    return 1 - curMin if curMin< 0 else 1

print(minStartValue([1,-2,-3]))


print(minStartValue([-3,2,-3,4,2]))

print(minStartValue([2,3,5,-5,-1]))