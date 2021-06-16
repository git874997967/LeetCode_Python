# 645. Set Mismatch
def findErrorNums(nums):
    numMap, result ={},[]
    for num in nums:
        if num in numMap:
            result.append(num)
        else:
            maxMap[num] = 1
    for num in range(1,len(nums) +1):
        if num not in numMap: 
            result.append(num)
    return result 

print(findErrorNums([1,2,2,4]))



