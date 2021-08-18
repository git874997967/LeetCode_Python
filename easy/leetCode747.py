# 747. Largest Number At Least Twice of Others
def dominantIndex(nums):
     maxIndex , maxNum = 0, float('-inf')
     for i in range(0,len(nums)):
         if maxNum < nums[i]:
             maxNum = nums[i]
             maxIndex = i
     for i in range(0,len(nums)):
         if i != maxIndex and nums[i] != 0:
             if nums[i] * 2 > maxNum:
                 return -1
     return maxIndex 

def domainIndex2(nums):
    temp = list(set(nums))
    if len(nums) == 1:
        return 0
    max, sub = None, None
    for num in temp:
        if max == None and sub == None:
            max = sub = num
        if num > sub and num <= max:
            sub = num
        elif num > sub and num > max:
            max, sub = num, max

    if  (2 * sub) < max:
        return nums.index(max)
    else:
        return -1


print(dominantIndex([1,2,3,4]))


print(dominantIndex([3,6,1,0]))

print(dominantIndex([0,0,2,0]))

print(dominantIndex([0,0,0,1]))