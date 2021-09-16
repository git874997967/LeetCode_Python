#47. Permutations II
def permuteUnique(nums):
    resultSet = set()
    def backTracking(block, used):
        if len(block) == len(nums):
            return resultSet.add(tuple(block[:]))
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                block.append(nums[i])
                backTracking(block, used)
                block.pop(-1)
                used[i] = False

    backTracking([],[False] * len(nums))
    
    result = [list(i) for i in resultSet]
    return result 


def permuteUnique2(nums):
    if not nums: return[]
    nums.sort()
    result,used = [],[0] * len(nums)
    def backTracking(block,used):
        if len(block) == len(nums):
            return result.append(block[:])

        for i in range(len(nums)):
            if not used[i]:
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = 1
                block.append(nums[i])
                backTracking(block,used)
                block.pop(-1)
                used[i] = 0
    backTracking([],used)
    print(result)
permuteUnique2([1,1,2])