 # 219. Contains Duplicate II
def containsNearbyDuplicate(nums, k):
    numDict = {}
    for i in range(len(nums)):
        if nums[i] not in numDict:
            numDict[nums[i]] = i
        else:
            if abs(i - numDict[nums[i]]) <= k:
                return True 
            else:
                numDict[nums[i]] = i
    return False
