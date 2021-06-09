# 448. Find All Numbers Disappeared in an Array
def findDisappearedNumbers(nums):
    result = []
    numSet = set(nums)
    for i in range(1,len(nums) + 1):
        if i not in numSet:
            result.append(i)
    return result