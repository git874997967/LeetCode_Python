#1133. Largest Unique Number
def largestUniqueNumber(nums):
     numMap = {}
     for num in nums:
         numMap[num] = numMap.get(num,0) + 1
     maxNum = - 1
     for num in numMap.keys():
        if numMap[num] == 1:
            maxNum = max(num, maxNum)
     print(maxNum)
     return maxNum

largestUniqueNumber([9,9,8,8])


largestUniqueNumber([5,7,3,9,4,9,8,3,1])


