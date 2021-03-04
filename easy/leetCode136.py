# 136. Single Number
def singleNumber(  nums):
    result = 0
    for  i in range(len(nums)):
        result = result ^ nums[i]

    return result

arr = [2,2,1]
res =  singleNumber(arr)
print(res)