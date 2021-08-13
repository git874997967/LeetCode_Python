#945. Minimum Increment to Make Array Unique
def minIncrementForUnique( nums): # time exceed
    numMap = {}
    for num in nums:
        count = numMap.get(num,0) + 1
        numMap[num] = count 
    numSet = set(numMap.keys())
    curSum = sum(nums)
    for k in numMap:
        val = numMap[k]
        while(val) != 1:

             while k in numSet:
                 k += 1
             numSet.add(k)
             val -= 1       
    newSum = sum(numSet)
    return newSum - curSum

def minIncrementForUnique(nums):
    count = 0
    nums.sort()
    for i in range(1,len(nums)):
        diff = nums[i-1]-nums[i]+1
        
        if diff >0:
            count+=diff
            nums[i]+= diff
    return count
print(minIncrementForUnique([3,2,1,2,1,7]))
print(minIncrementForUnique([1,2,2]))
