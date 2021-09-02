#1512. Number of Good Pairs
#A pair (i, j) is called good if nums[i] == nums[j] and i < j.
import math
def numIdenticalPairs(nums):
    numMap ,result ,match = {},0,0
    for index in range(len(nums)):
        numMap[nums[index]] = numMap.get(nums[index], 0) + 1
    
    for v in numMap.values():
        if v > 1:
            match = math.factorial(v) // (math.factorial(v-2) * 2)
            result += match

    print(result)
    return result 


    print(result)
    return result 

    
numIdenticalPairs([1,2,3,1,1,3])