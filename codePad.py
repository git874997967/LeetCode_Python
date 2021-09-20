# per  the length is aways len(num) we do need to care the start of loop
def per(nums):
    nums.sort()
    result  = []
    used = [False] * len(nums)
    def backTrack(block,used):
        if len(block) == len(nums):
            return result.append(block[:])
        for idx in range(len(nums)):
            if used[idx]:
                continue
            used[idx] = True
            block.append(nums[idx])
            backTrack(block,used )
            block.pop(-1)
            used[idx] = False
        
    backTrack([],used)
    print(result)
    
per([1,2,3])
# def subSet
def subSet(nums):
    nums.sort()
    result = []
    used = [False] * len(nums)
    def backTrack(block,index):
        result.append(block[:])
        for idx in range(index,len(nums)):
            if len(block) >= len(nums):
                return 
            
            block.append(nums[idx])
            backTrack(block,idx+1)
            
            block.pop(-1)
    backTrack([],0)
    print(result)


subSet([1,2,3])