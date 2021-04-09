# 217. Contains Duplicate
def containsDuplicate(nums):
    numSet = set()
    for num in nums:
        numSet.add(num)
    return False if len(nums) == len(numSet) else True

print(containsDuplicate([1,2,3,1]))