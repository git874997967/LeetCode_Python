#46. Permutations
def permute(nums):
    if len(nums) == 1:
        return [nums]
    result, used = [], [False] * len(nums)

    def backTracking(block, used):
        if len(block) == len(nums):
            return result.append(block[:])
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True 
                block.append(nums[i])
                backTracking(block, used)
                block.pop(-1)
                used[i] = False
    backTracking([],used)
    print(result )


permute([1,2,3])