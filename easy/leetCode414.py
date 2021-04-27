# 414. Third Maximum Number
#  find the max and min in the set costs O(n)

def thirdMax(nums):
    nums = set(nums)
    maxium = max(nums)
    if len(nums) < 3:
        return maxium
    nums.remove(maxium)
    second_max = max(nums)
    nums.remove(second_max)
    return max(nums)

print(thirdMax([3,4,5,3,2,1,2,65,332,3245,673]))


def thirdMax2(nums):
    sets = set()
    for num in nums:
        sets.add(num)
        if len(sets) > 3:
            sets.remove(min(sets))
    if len(sets) >= 3:
        return min(sets)
    return max(sets)

