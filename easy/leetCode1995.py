#1995. Count Special Quadruplets (mid)
from collections import defaultdict
def countQuadruplets(nums):
    end = len(nums) - 1
    result = 0
    seenDict = defaultdict(int)
    for i in range(end , - 1,-1):
        for j in range(i-1,-1,-1):
            result += seenDict[nums[i] + nums[j]]
        for d in range(end , i,-1):
            seenDict[nums[d]- nums[i]] += 1
    return result